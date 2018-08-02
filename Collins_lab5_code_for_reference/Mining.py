from time import sleep

from Block import Block
from BlockChain import double_hash, encode_and_concenate, BlockChain
from Header import Header
from Transaction import CoinbaseTransaction
from txn_mem_pool import TxnMemoryPool


def miner(transaction_pool):
    last_block_header = '0'*64 # genesis header
    last_block_target = '%064x' % (0x7ffff * 2 ** (8 * (0x20 - 3)))
    #uncomment the line below for harder difficulty

    #last_block_target = '000fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff'

    # init the block chains
    block_chain = BlockChain()

    block = Block(Header(last_block_header), last_block_target)
    # use variable to keep track of where in the pool we left off reading from
    # so that we're not going to re-mine the same block
    left_off_in_pool = 0
    # add coinbase transaction
    block.add_transaction(CoinbaseTransaction(0))
    for i in range(1, 9):
        block.add_transaction(transaction_pool.transactions[i])
        left_off_in_pool = i

    # now that our block is full, we can start to mine it.
    while not block.mine_this_block():
        continue

    block_chain.add_block(block)
    print("current blockchain height ", block_chain.size_of_chain())
    sleep(5)
    # our new header for block 2 will need the hash of block 1
    last_block_header = double_hash(encode_and_concenate([block_chain.latest_block().BlockHash]))

    block_2 = Block(Header(last_block_header), last_block_target)
    block_2.add_transaction(CoinbaseTransaction(block.transactions[0].current_total))
    for i in range(left_off_in_pool+9):
        block_2.add_transaction(transaction_pool.transactions[i])
        left_off_in_pool = i

    # now that our block is full, we can start to mine it.
    while not block_2.mine_this_block():
        continue

    block_chain.add_block(block_2)
    print("current blockchain height ", block_chain.size_of_chain())
    print()
    for i, block_added in enumerate(block_chain.blocks):
        print('Block #{} was added. It took {} steps to find it.'.format(i, block_added.nonce))


if __name__ == '__main__':
    txn_pool = TxnMemoryPool()
    txn_pool.generate_n_transaction(10000) # creates list of transactions (the class object) for miner to read from
    miner(txn_pool)