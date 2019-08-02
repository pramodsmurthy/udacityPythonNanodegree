from datetime import datetime
import calendar
import hashlib

class Block(object):
    def __init__(self, next, prev_hash, num):
        self.next = next
        self.timestamp = self.get_time() #Todo
        self.prev_hash = prev_hash
        self.data = "I am block "+str(num)
        self.hash = self.calc_hash()
    
    def calc_hash(self):
        sh = hashlib.sha256()
        data_string = str(self.timestamp)+str(self.prev_hash)+self.data
        sh.update(data_string.encode('utf-8'))
        return sh.hexdigest()
    
    def get_time(self):
        dttime = datetime.utcnow()
        timestamp = calendar.timegm(dttime.utctimetuple())
        return timestamp

    def print_block(self):
        print("*"*15)
        print("TimeStamp: ", self.timestamp)
        print("Prev Hash: ", self.prev_hash)
        print("Data: ", self.data)
        print("Hash: ", self.hash)
    
    def get_hash(self):
        return self.hash
    
    def get_prev_hash(self):
        return self.prev_hash
    
    def gettimestamp(self):
        return self.timestamp
    
    def get_data(self):
        return self.data
    
    def __str__(self):
        return self.get_data()

class Blockchain(object):
    def __init__(self):
        self.head = None
        self.num_entries = 0
    
    def add_block(self):
        if self.head is None:
            self.head = Block(None, None, self.num_entries)
        else:
            prev_hash = self.head.hash
            new_block = Block(self.head, prev_hash, self.num_entries)
            new_block.next = self.head
            self.head = new_block
        self.num_entries += 1

    def get_block_info(self, block):
        if self.head is None:
            return -1
        requested_block_data = "I am block "+str(block)
        blk = self.head
        while blk is not None:
            if blk.get_data() == requested_block_data:                
                if block == 0:
                    return (blk.get_prev_hash(), None)
                else:
                    return (blk.get_prev_hash(), blk.next.get_hash())        
            blk = blk.next
        return(-1, -1)

    def print_blockchain(self):
        if self.head is None:
            return "Empty Blockchain"
        """
        block = self.head
        while block is not None:
            block.print_block()
            block = block.next
        """
        return self.num_entries
    
    def add(self, count):
        for _ in range(count):
            self.add_block()
        

# Test Case 1
# Try to print/access blocks in empty blockchain
blkchain = Blockchain()
expected_output1 = "Empty Blockchain"
print("Input - Not creating any blocks and checking block count")
output1 = blkchain.print_blockchain()             
#print(f"Expected Output: {expected_output1}")

# Test Case 2
# Create 1000 blocks and get the count of created blocks
blkchain = Blockchain()
expected_output2 = 1000
blkchain.add(expected_output2)
print("Input - Adding 1000 blocks to blockchain and checking if all blocks are created successfully")
output2 = blkchain.print_blockchain()             
#print(f"Expected Output: {expected_output2}")

# Test Case 3
# Create 5 blocks and get count of accessed blocks
blkchain = Blockchain()
expected_output3 = 5
blkchain.add(expected_output2)
print("Input - Adding 5 blocks to blockchain and checking if all blocks are created successfully")
output3 = blkchain.print_blockchain()             
#print(f"Expected Output: {expected_output3}")

# Test Case 4
# Add 10 blocks and check if prev_hash in current block is same as hash of prev block
blkchain = Blockchain()
expected_output4 = "Hashes Match"
blkchain.add(10)
print("Input - Adding 10 blocks to blockchain, comparing block 3's prev_hash with block 2's hash value")
prevhash, currhash = blkchain.get_block_info(3)
#print(f"Expected Output: {expected_output4}")

# Test Case 5
# Check if prev hash of first block is set to None
expected_output5 = None
print("Input - Checking block 0's prev hash value")
prevhash, _ = blkchain.get_block_info(0)
#print(f"Expected Output: {expected_output5}")

"""
print("Pass" if output1 == expected_output1 else "Fail")
print("Pass" if output2 == expected_output2 else "Fail")
print("Pass" if output3 == expected_output3 else "Fail")
print("Pass" if prevhash == currhash else "Fail")
print("Pass" if prevhash == expected_output5 else "Fail")
"""