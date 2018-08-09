import transaction
import blockchain
import txnMemoryPool
import miner

# Create blockchain and genesis block in the process
krisChain = blockchain.Blockchain()
print("Height: " + str(len(krisChain.blockChain)))
krisChain.blockChain[-1].printBlock()

# Add two sets of transactions as blocks
krisPool = txnMemoryPool.TxnMemoryPool()

krisMiner = miner.Miner(krisChain, krisPool)

while (len(krisPool.memoryPool)) > 0:
    krisMiner.calculateNonce()
    print("Height: " + str(len(krisChain.blockChain)))
    krisChain.blockChain[-1].printBlock()

print("Height: " + str(len(krisChain.blockChain)))
