
Lab5 is creating a mining my own blockchain

txnMemoryPool holds the transactions in memory for mining

miner attempts to create a candidate block whose blockhash is less than the target hash. The target determines the difficulty and the time consumption to find a valid solution. A block reward called the coinbase transaction is the first transaction in each block to reward the miner.

To run the code in python2, run python main.py in your terminal