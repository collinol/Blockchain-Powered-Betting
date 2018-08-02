import hashlib


def encode_and_concenate(strings):
    total_string = "".encode('utf-8')
    for item in strings:
        item = str(item)
        total_string += item.encode('utf-8')
    return total_string


def double_hash(string_to_hash):
    return hashlib.sha256((hashlib.sha256(string_to_hash).hexdigest()).encode('utf-8')).hexdigest()


class BlockChain:

    def __init__(self):
        self.blocks = []

    def is_empty(self):
        return len(self.blocks) == 0

    def add_block(self, block):
        self.blocks.append(block)

    def latest_block(self):
        return self.blocks[-1]

    def size_of_chain(self):
        return len(self.blocks)

    def print_blockchain(self):
        print("printing all blocks:")
        for block in self.blocks:
            print(block.BlockHash)

    def find_block_by_height(self, index):
        return self.blocks[index].BlockHash

    def find_transaction_by_hash(self,hash):
        for block in self.blocks:
            for t in  block.Transactions:
                if t.TransactionHash == hash:
                    return "Transaction Found\n" \
                           "Inputs = {}\n" \
                           "Outputs = {}\n" \
                           "hash = {}".format(t.ListOfInputs,t.ListOfOutputs,t.TransactionHash)

