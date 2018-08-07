from Blockchain import *
from Transaction import *
from Output import *
from TxnMemoryPool import *
from Miner import *


#creating TxnMemoryPool
txn_memory_pool = TxnMemoryPool()
for i in range(0,91):
    t = Transaction(["input" + str(i)], [Output(), Output()])
    txn_memory_pool.add_transaction(t)


print("CREATING NEW BLOCKCHAIN: ")
b = Blockchain()
print("SUCCESS!")

print("\nCREATING MINER: ")
miner = Miner(b, txn_memory_pool)
print("SUCCESS!")
print("\nGETTING BITS: ")
print(miner.get_bits())
print("\nGETTING TARGET: ")
print(miner.get_target())
print("\nLAST ROOT: ")
print(miner.get_last_merkle_root())

print("\nMINING:")
miner.mine_indefinitely()
# print("\nFINAL BLOCKCHAIN: ")
# miner.blockchain.print_blocks()
print("\nFINAL BLOCKCHAIN HEIGHT: ")
print(miner.blockchain.get_blockchain_height())













