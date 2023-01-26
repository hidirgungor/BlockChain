import hashlib

class Crypto:
    def __init__(self, data):
        self.data = data
        self.hash = None
        self.previous_hash = None

    def hash_block(self):
        sha = hashlib.sha256()
        hash_str = f"{self.data}{self.previous_hash}".encode('utf-8')
        sha.update(hash_str)
        self.hash = sha.hexdigest()

    def __str__(self):
        return f"Data: {self.data}\nHash: {self.hash}\nPrevious Hash: {self.previous_hash}"

class Blockchain:
    def __init__(self):
        self.blockchain = []

    def add_block(self, data):
        block = Crypto(data)
        if len(self.blockchain) > 0:
            block.previous_hash = self.blockchain[-1].hash
        block.hash_block()
        self.blockchain.append(block)

    def __str__(self):
        output = ""
        for i, block in enumerate(self.blockchain):
            output += f"Block {i}:\n{block}\n"
        return output

blockchain = Blockchain()
blockchain.add_block("Transaction 1")
blockchain.add_block("Transaction 2")
blockchain.add_block("Transaction 3")

print(blockchain)
