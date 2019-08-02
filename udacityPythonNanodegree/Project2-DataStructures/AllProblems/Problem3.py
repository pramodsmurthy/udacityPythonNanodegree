"""
Huffman Algorithm:
Huffman algorithm is used to compress data. It is a lossless compression algorithm. So no data is lost between compression and decompression.
Heart of the algorithm relies on using less bits to represent most frequent letters, and more bits to represent less frequent letters. 
Below is the general guideline followed to implement Huffman Algorithm.

* Find the frequency of all characters in a string.
* Store characters along with their frequencies and sort them based on their frequencies.
* Assign codes for each character. Assign small codes for most frequent characters and longer codes for less frequent characters.
* Decode the compressed data using similar logic. 
"""

codes = dict()
def find_freq(data):
    freq = dict()
    for c in data:
        freq[c] = freq.get(c, 0) + 1
    #print(freq)
    return freq

def sort_on_freq(data_with_freq):
    sorteddata = list()
    for ch in data_with_freq.keys():
        sorteddata.append((data_with_freq[ch], ch))
    sorteddata.sort()
    #print("Sorted data on freq: ", sorteddata)
    return sorteddata

def create_tree(data_tuple):
    while len(data_tuple) > 1:
        firsttwo = data_tuple[:2]
        rest = data_tuple[2:]
        new_freq = firsttwo[0][0] + firsttwo[1][0]
        new_branch = [(new_freq, tuple(firsttwo))]
        data_tuple = rest + new_branch 
        data_tuple.sort()    
    return data_tuple[0]

def remove_freq_from_single_tree(data):
    no_freq = data[1]
    if type(no_freq) == type(""):
        return no_freq
    else:
        return (remove_freq_from_single_tree(no_freq[0]), remove_freq_from_single_tree(no_freq[1]))

def create_codes(node, pat):
    # Base condition
    if type(node) == type(""):
        codes[node] = pat
    else:
        create_codes(node[0], pat+"0")
        create_codes(node[1], pat+"1")

def assign_codes(sorted_data_with_freq):
    
    # Combine the data to form branches and store the frequencies for each branch. Branch Freq = sum of individual frequencies
    single_tree = create_tree(sorted_data_with_freq)
    #print("Single Tree: ", single_tree)

    # Then get data in the form of 'characters-only' format by removing frequencies.
    tree_without_freq = remove_freq_from_single_tree(single_tree)
    #print("Tree without freq: ", tree_without_freq)
    
    # Then proceed with assigning codes for the characters.
    create_codes(tree_without_freq, pat="")
    
    #print("Data with codes: ", codes)
    return tree_without_freq

def encode_data(data):
    encoded = ""
    for c in data:
        encoded = encoded+codes[c]
    #print("Encoded data is ", encoded)
    return encoded

def decode_data(single_tree, encoded):
    decoded = ""
    tr = single_tree
    for bit in encoded:
        if bit == "0":
            tr = tr[0]
        else:
            tr = tr[1]
        if type(tr) == type(""):
            decoded += tr
            tr = single_tree
    #print("Decoded data is ", decoded)
    return decoded

def run_test(input_data):
    if len(input_data):
        fr = find_freq(input_data)
        sortdata = sort_on_freq(fr)
        singletree = assign_codes(sortdata)
        encoded = encode_data(input_data)    
        decoded = decode_data(singletree, encoded)
        if input_data == decoded:
            print("Encoding and Decoding Successful")
        else:
            print("Test Failed")
    else:
        print("Empty data - Nothing to Encode")

run_test("")                                                    # Test1 - No input data
print("Test1: Input is: ''")
#print("Expected Output is 'Empty data - Nothing to Encode'")

run_test("Avngr Movies")                                        # Test2 - No Repetitions
print("Test2: Input is: 'Avngr Movies'")
#print("Expected Output is 'Encoding and Decoding Successful'")

run_test("%I - like, Avenger...movies%")                        # Test3 - Input with special characters
print("Test3: Input is: '%I - like, Avenger...movies%'")
#print("Expected Output is 'Encoding and Decoding Successful'")
