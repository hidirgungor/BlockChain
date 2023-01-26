import hashlib

class Block:
    def __init__(self, data, previous_hash):
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calculate_hash()
    
    def calculate_hash(self):
        sha = hashlib.sha256()
        sha.update(str(self.data).encode('utf-8') + str(self.previous_hash).encode('utf-8'))
        return sha.hexdigest()

class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]
    
    def create_genesis_block(self):
        return Block("Genesis Block", "0")
    
    def add_block(self, data):
        previous_hash = self.chain[-1].hash
        new_block = Block(data, previous_hash)
        self.chain.append(new_block)
    
    def is_valid(self):
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i-1]
            if current_block.hash != current_block.calculate_hash():
                return False
            if current_block.previous_hash != previous_block.hash:
                return False
        return True

blockchain = Blockchain()
blockchain.add_block("Transaction 1")
blockchain.add_block("Transaction 2")
blockchain.add_block("Transaction 3")

print(blockchain.is_valid()) # should return True



# This sample code creates a basic blockchain with blocks containing data and a previous_hash field. Each block's hash is calculated by taking the data and previous_hash, running it through a SHA256 hash function, and returning the hexadecimal representation of the hash. The Blockchain class creates a genesis block, allows for the addition of new blocks, and has a method to check if the chain is valid.

# Please note that this is a very basic example and should not be used for production systems as it lacks features like difficulty, proof of work, and network communication.