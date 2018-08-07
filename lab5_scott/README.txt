This program should have all the required functionalities. This is a python3 file called
blockchainMain.py runnable from the command line.

blockchainMain.py:
	- creates a TxnMemoryPool with 91 transactions
	- miner mines the pool until 0 are remaining
	- We end up with a blockchain with a height of 12. This is because the 
	miner keeps taking 9 transactions from the pool until 1 remains. This 1 
	is mined into the final block, which gives the blockchain a final height of 12

Output.py, Miner.py, TxnMemoryPool.py
	-new classes
	-blockchainMain.py showcases functionalities from many of the key Miner.py 
	functions 
