
import os

def find_files(suffix, path, pathslist = [], filelist = []):

    if path is None or path == "" or os.path.exists(path) is False:
        return filelist
    elif os.path.isfile(path):
        if path.endswith(suffix) and path not in filelist:            
            filelist.append(path)
    elif os.path.isdir(path):
        for entry in os.listdir(path):
            pathslist.append(os.path.join(path, entry))
    
    if len(pathslist):
        #display (pathslist)
        find_files(suffix, pathslist.pop(0), pathslist, filelist)
    
    return filelist

#  Test Case 1 - Empty Path
#  When the path is empty
expected_output1 = []
output1 = sorted(find_files(".c", ""))                                                                                        
#print(f"Expected Outout1: {output1}")

# Test Case 2 - Only one file
# When there is only one file in the path
expected_output2 = ['C:\\Users\\pkrishna\\Google Drive\\udacityPython\\Project2-DataStructures\\testdir\\subdir1\\a.c']
output2 = sorted(find_files(".c", r'C:\Users\pkrishna\Google Drive\udacityPython\Project2-DataStructures\testdir\subdir1'))   
#print(f"Expected Outout2: {output2}")

# Test Case 3 - Multiple Files
# When there are multiple files present
expected_output3 = ['C:\\Users\\pkrishna\\Google Drive\\udacityPython\\Project2-DataStructures\\testdir\\subdir1\\a.c', 'C:\\Users\\pkrishna\\Google Drive\\udacityPython\\Project2-DataStructures\\testdir\\t1.c', 'C:\\Users\\pkrishna\\Google Drive\\udacityPython\\Project2-DataStructures\\testdir\\subdir5\\a.c', 'C:\\Users\\pkrishna\\Google Drive\\udacityPython\\Project2-DataStructures\\testdir\\subdir3\\subsubdir1\\b.c']
expected_output3 = sorted(expected_output3)
output3 = sorted(find_files(".c", r'C:\Users\pkrishna\Google Drive\udacityPython\Project2-DataStructures\testdir'))           # Test Case 3 - Multiple Files
#print(f"Expected Outout3: {expected_output3}")

# Test Case 4 - Invalid Path
# When given path is invalid
expected_output4 = []
output4 = sorted(find_files(".c", r'C:\\Users\\pkrishna\\Google Drive\\udacityPython\\Project2-DataStructures\\\testdir\\'))
print(f"Expected Outout4: {expected_output4}")

"""
def display(pathslist):
    for entry in pathslist:
        print(entry)

def result(output, expected_output):
    print("- -"*20)
    if output == expected_output:
        print("Pass")
    else:
        print("Fail")
        print(f"Expected Output: {expected_output}")
        print(f"Output Seen: {output}")
result(output1, expected_output1)
result(output2, expected_output2)
result(output3, expected_output3)
"""