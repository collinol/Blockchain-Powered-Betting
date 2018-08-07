from Block import *
from Transaction import *
from Output import *


class Blockchain:
    def __init__(self):
        self.Blocks = []  # array of blocks
        self.MAX_TXNS = 10  # max transactions per block
        self.__create_genesis_block()

    def print_blocks(self):
        print("BEGIN BLOCKCHAIN")
        for b in self.Blocks:
            b.print_block()
        print("END BLOCKCHAIN\n")

    def get_block(self, index):
        return self.Blocks[index]

    def print_block(self, index):
        self.Blocks[index].print_block()

    def get_blockchain_height(self):
        return len(self.Blocks)

    def __create_genesis_block(self):
        txIds = []
        t0 = Transaction(["input0"], [Output(), Output()])
        txIds.append(t0)
        b0 = Block(txIds, "0" * 16)
        self.Blocks.append(b0)

    def add_block(self, txIds):  # add block containing the array of transactions
        last_block_blockhash = self.Blocks[len(self.Blocks) - 1].BlockHash  # getting last block in Blocks
        new_block = Block(txIds, last_block_blockhash)
        self.Blocks.append(new_block)

    def find_transaction(self, tx):
        for block in self.Blocks:
            if block.find_transaction(tx):
                return block.find_transaction(tx)
        return 0

    def find_and_print_transaction(self, tx):
        self.find_transaction(tx).print_transaction()
