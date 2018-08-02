# EchoCoins
run   
$ Mining.py  
to see execution of code. It builds two blocks, adds transactions
until the block is full and then mines the block.  
At the beginning of each new block, a coinbase transaction is added that 
has a variable to keep track of the current total of echo coins. 

The difficulty that's set seems a little too easy. Uncomment line 15 in Mining.py
to use a different "last_block_target" that takes a few thousand attempts to reach.