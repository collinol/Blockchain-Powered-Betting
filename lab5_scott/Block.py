from Header import *
from Transaction import *


class Block:
    def __init__(self, transactions_array, last_block_hash, nonce = None):

        self.MagicNumber = "D9B4BEF9"
        self.BlockSize = self.__sizeof__()
        self.Transactions = transactions_array  # array of transactions
        self.TransactionCounter = len(transactions_array)
        self.mtree = self.__generate_merkle_tree(transactions_array)
        self.BlockHeader = Header(self.mtree, last_block_hash, nonce)
        self.BlockHash = self.__calc_block_hash()  # BlockHash

    def print_block(self):
        print("BEGIN BLOCK")
        d = {'BlockHash': self.BlockHash,
             'BlockSize': self.BlockSize,
             'MagicNumber': self.MagicNumber,
             'TransactionCounter': self.TransactionCounter,
             'Transactions': self.Transactions,
             }
        print(d)
        self.BlockHeader.print_header()
        print("END BLOCK")


    def __calc_block_hash(self):
        return bcStringsConcatHash(self.BlockHeader.Timestamp,
                                   self.BlockHeader.HashMerkleRoot,
                                   self.BlockHeader.Bits,
                                   self.BlockHeader.Nonce,
                                   self.BlockHeader.HashPrevBlock
                                   )

    def __generate_merkle_tree(self, transactions_array):
        tx_hash_array = []
        for transaction in transactions_array:
            tx_hash_array.append(transaction.TransactionHash)
        return MerkleTree(tx_hash_array)

    def find_transaction(self, tx):
        for t in self.Transactions:
            if tx == t.TransactionHash:
                return t
        return None

    def get_transaction(self, index):
        return self.Transactions[index]

