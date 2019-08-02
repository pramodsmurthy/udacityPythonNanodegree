from collections import OrderedDict

class Lru:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = OrderedDict()  # OrderedDict remembers the order of the keys at which they were inserted
    
    def get(self, key):        
        if key in self.cache:   # Since cache is a dictionary, lookup will be quick
            value = self.cache[key] 
            self.cache.pop(key) # Key is being accessed, remove the key first, so that its order gets changed
            self.cache[key] = value # Insert back, key will now be added to the end. Dict now knows this was the latest 'item' that was used 
            return value
        else:
            return -1
    
    def set(self, key, value):
        if key in self.cache:
            self.cache.pop(key) # Key is being accessed, remove it first, so that it gets added at the end
        elif len(self.cache) == self.capacity: # In case if capacity is full, pop the least recently used
            self.cache.popitem(last=False)
        self.cache[key] = value # Add the item to the dict
    
    def display(self):
        for k, v in self.cache.items():
            print(f"{k}-->{v}")
    
    def tester(self, input, output):
        #print(f"Input: {input}")
        observed_output = self.get(input)
        return observed_output
"""     print(f"Observed output: {observed_output}")
        print(f"Expected output: {output}")
        if observed_output == output:
            print("Test Result: Pass")
        else:
            print("Test Result: Fail")
        print("- - "*10)
"""            

lruc = Lru(5)
# Test Case 1
# Look for a item in empty cache
print("Look for an item in empty cache")
output = lruc.tester(1, -1)
#print("Expected Output: -1")

lruc.set(1, 10)
lruc.set(2, 30)
lruc.set(3, 40)

# Test Case 2
# Look for item that is present in cache
print("Look for an item that is present in cache")
output = lruc.tester(2, 30)
#print("Expected Output: 30")

lruc.set(9, 50)
lruc.set(7, 90)
lruc.set(10, 50) # Capacity full, LRU item replaced

# Test Case 3
# Search for replaced item in cache, lookup should return -1 (not found)
print("Look for an item that was replaced due to LRU criteria")
output = lruc.tester(1, -1) 
#print("Expected Output: -1")

# Test Case 4
# Search for item that is inserted after replacing the LRU item
print("Look for an item that got inserted after LRU")
output = lruc.tester(10, 50)
#print("Expected Output: 50")

#lruc.display()