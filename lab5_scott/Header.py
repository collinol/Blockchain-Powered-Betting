from time import time
from MerkleTree import *


class Header:
    def __init__(self, mtree, last_block_hash, nonce):
        self.Version = 1
        self.HashPrevBlock = last_block_hash
        self.HashMerkleRoot = mtree.get_root()
        self.Timestamp = time()    # decimal value, would be better if int possibly
        self.Bits = 0x207fffff #'0x1fffffff' # SET BACK TO ORIGINAL TO SUBMIT
        #get target on mainnet with several leading zeros
        if nonce == None:
            self.Nonce = 0
        else:
            self.Nonce = nonce
        #8388607fffff

    def print_header(self):
        print("BEGIN HEADER")
        d = {'Version': self.Version,
             'HashPrevBlock': self.HashPrevBlock,
             'HashMerkleRoot': self.HashMerkleRoot,
             'Timestamp': self.Timestamp,
             'Bits': self.Bits,
             'Nonce': self.Nonce
             }

        print(d)
        print("END HEADER")

