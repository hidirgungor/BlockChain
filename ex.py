import hashlib

class Block:
    def __init__(self, data, previous_hash):
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calc_hash()

    def calc_hash(self):
        sha = hashlib.sha256()
        hash_str = self.data.encode('utf-8') + self.previous_hash.encode('utf-8')
        sha.update(hash_str)
        return sha.hexdigest()

class Blockchain:
    def __init__(self):
        self.tail = None

    def append(self, data):
        if self.tail is None:
            self.tail = Block(data, "0")
        else:
            self.tail = Block(data, self.tail.hash)

bc = Blockchain()
bc.append("First block")
bc.append("Second block")
bc.append("Third block")
print(bc.tail.hash)
