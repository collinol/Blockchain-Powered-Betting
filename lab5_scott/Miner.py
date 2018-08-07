import struct
import binascii
from Transaction import *
from Output import *
from Block import *
from Header import *
from Blockchain import *


class Miner:
    def __init__(self, blockchain, txn_memory_pool):
        self.blockchain = blockchain
        self.txn_memory_pool = txn_memory_pool

    def get_last_block(self):
        return self.blockchain.get_block(-1)

    def get_last_header(self):
        return self.get_last_block().BlockHeader

    def get_last_merkle_root(self):
        return self.get_last_header().HashMerkleRoot

    def get_bits(self):
        return self.get_last_header().Bits #bits of block header of last block

    def get_target(self):
        bits = self.get_bits()
        if type(bits) == str:
            bits = int(bits)
        shift = bits >> 24
        value = bits & 0x007fffff
        value <<= 8 * (shift - 3)
        target = value
        return target

    def calc_difficulty(self):
        difficulty_one_target = 0x00ffff * 2 ** (8 * (0x1d - 3))
        target = self.get_target()
        calculated_difficulty = difficulty_one_target / float(target)
        return calculated_difficulty

    def __make_coinbase_txn(self):
        coinbase_txn = Transaction(["coinbase input"], [Output(), Output()])
        return coinbase_txn

    def __collect_txn_array(self):
        txn_array = []
        txn_array.append(self.__make_coinbase_txn())
        MAX_TXNS = self.blockchain.MAX_TXNS
        txn_pool_len = len(self.txn_memory_pool.Transactions)
        if txn_pool_len < MAX_TXNS-1:
            for txn in self.txn_memory_pool.Transactions:
                txn_array.append(txn)
        else:
            for txn in self.txn_memory_pool.Transactions[0:MAX_TXNS-1]:
                txn_array.append(txn)
        return txn_array

    def __make_new_block(self, txn_array, last_block_hash, nonce):
        new_block = Block(txn_array, last_block_hash, nonce)
        return new_block

    def mine_block(self):
        txn_array = self.__collect_txn_array()
        last_block_hash = self.get_last_merkle_root()
        target = self.get_target()
        max_nonce = 2 ** 32

        for nonce in range(0, max_nonce):
            new_block = self.__make_new_block(txn_array, last_block_hash, nonce)
            block_hash = new_block.BlockHash
            hash_value = int(block_hash, 16)
            if hash_value > target:
                print(".", end="")
                continue
            else:
                break
        print("\nSUCCESS: ")
        print("NEW BLOCK'S BLOCKHASH: " + block_hash)

        #append new block to blockchain
        self.blockchain.Blocks.append(new_block)

        #remove transactions from txn pool
        self.txn_memory_pool.Transactions = self.txn_memory_pool.Transactions[self.blockchain.MAX_TXNS - 1:]
        print("NEW TXN_MEM_POOL length: " + str(len(self.txn_memory_pool.Transactions)))
        print("NEW BLOCKCHAIN height: " + str(self.blockchain.get_blockchain_height()))


    def mine_indefinitely(self):
        txn_pool_len = len(self.txn_memory_pool.Transactions)
        while txn_pool_len > 0:
            self.mine_block()
            txn_pool_len = len(self.txn_memory_pool.Transactions)
        print("\nTXN POOL EMPTY: NO MORE TXNs TO MINE")

