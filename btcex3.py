import hashlib
import time

class Block:
    def __init__(self, data, previous_hash):
        self.timestamp = time.time()
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        sha = hashlib.sha256()
        sha.update(str(self.timestamp).encode('utf-8') + str(self.data).encode('utf-8') + str(self.previous_hash).encode('utf-8'))
        return sha.hexdigest()

class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]

    def create_genesis_block(self):
        return Block("Genesis Block", "0")

    def get_last_block(self):
        return self.chain[-1]

    def add_block(self, new_block):
        new_block.previous_hash = self.get_last_block().hash
        new_block.hash = new_block.calculate_hash()
        self.chain.append(new_block)

blockchain = Blockchain()
blockchain.add_block(Block("Block 1", ""))
blockchain.add_block(Block("Block 2", ""))
blockchain.add_block(Block("Block 3", ""))

for block in blockchain.chain:
    print("Timestamp:", block.timestamp)
    print("Data:", block.data)
    print("Previous Hash:", block.previous_hash)
    print("Hash:", block.hash)
    print()
