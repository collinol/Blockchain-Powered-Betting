import block
import transaction
import cPickle
import sys
import time
import output


# Create blockchain
class Blockchain:
    def __init__(self):
        self.blockChain = []
        self.createGenesisBlock()
        self.MAX_TXNS = 10

    # Create first block
    def createGenesisBlock(self):
        transactionSet0 = [self.makeCoinbase()]
        block0 = block.Block("0000000000000000000000000000000000000000000000000000000000000000", transactionSet0, 0, None)
        block0.renewSize()
        self.blockChain.append(block0)

    # Method to add more blocks
    def addBlock(self, transactions, nonce):
        newBlock = block.Block(self.blockChain[-1].blockHash, transactions, nonce, None)
        newBlock.renewSize()
        self.blockChain.append(newBlock)

    def addCandidateBlock(self, block):
        self.blockChain.append(block)

    # Retrieve a block by height
    def getBlockByHeight(self, height):
        if (len(self.blockChain) >= height):
            return self.blockChain[height]
        print("Block not found")
        return None

    # Retrieve a block by hash
    def getBlockByHash(self, hash):
        for x in self.blockChain:
            block = next((x for x in self.blockChain if x.blockHash == hash), None)
            return block
        print("Block not found")

    # Get a specified transaction hash from the blockchain through the transaction hash
    def getTransaction(self, transactionHash):

        for block in self.blockChain:
            for transaction in block.transactions:
                if (transaction.transactionHash == transactionHash):
                    return transaction
        print("Transaction hash not found")
        print("#################################################################################")
        return None

    def getSubsidy(self):

        halvings = len(self.blockChain) / 210000
        if halvings >= 64:
            return 0
        subsidy = 50 * 1000
        if (2 * halvings) > 0:
            subsidy = subsidy / (2 * halvings)
        return subsidy

    def makeCoinbase(self):
        #print(self.getSubsidy())
        coinbase = transaction.Transaction([time.time() + 1], [output.Output(self.getSubsidy())])
        coinbase.transactionHash = "0000000000000000000000000000000000000000000000000000000000000000"
        return coinbase
