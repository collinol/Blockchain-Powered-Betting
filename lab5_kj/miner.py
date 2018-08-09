from hashlib import sha256
from binascii import unhexlify, hexlify
import block
import transaction
import time
import output



# Create transaction
class Miner:
    def __init__(self, blockchain, txnMemoryPool):
        self.chain = blockchain
        self.txnMemoryPool = txnMemoryPool
        self.targetStr = self.getDifficulty(self.chain.blockChain[-1].blockHeader)

    # Print transaction
    def getDifficulty(self, header):
        exponent = header.bits >> 24
        coefficient = header.bits & 0xffffff
        target_hexstr = '%064x' % (coefficient * 2 ** (8 * (exponent - 3)))
        target_str = target_hexstr.decode('hex')
        return target_str

    # Gets the block reward
    def getSubsidy(self):

        halvings = len(self.chain.blockChain) / 210000
        if halvings >= 64:
            return 0
        subsidy = 50 * 1000
        if (2 * halvings) > 0:
            subsidy = subsidy / (2 * halvings)
        # print(subsidy)
        return subsidy

    # Makes the coinbase transaction for each block
    def makeCoinbase(self):

        coinbase = transaction.Transaction([time.time() + 1], [output.Output(self.getSubsidy())])
        coinbase.transactionHash = "0000000000000000000000000000000000000000000000000000000000000000"
        return coinbase

    # Find nonce to get hash lower than target then add any correct blocks to the blockchain
    def calculateNonce(self):

        # Set nonce to 0 and get MAXNONCE value
        nonce = 0
        MAXNONCE = 2 ** 32 - 1

        # Create transactions list and prepend coinbase to front
        transactionList = []
        transactionList.append(self.chain.makeCoinbase())
        transactionAmount = min(len(self.txnMemoryPool.memoryPool), self.chain.MAX_TXNS - 1)
        for _ in range(transactionAmount):
            transactionList.append(self.txnMemoryPool.memoryPool.pop())

        # Testing
        #for x in transactionList:
        #    print(x.transactionHash)

        # Find nonce that creates hash less than target hash
        while nonce < MAXNONCE:

            # Create candidate block and utilize
            candidateBlock = block.Block(self.chain.blockChain[-1].blockHash, transactionList, nonce)

            # Utilize string
            hash = unhexlify(candidateBlock.blockHash)

            # Testing for results
            #hash1 = candidateBlock.blockHash
            #hashAsNum = long(hash1, 16)
            #targetAsNum = long(hexlify(self.targetStr), 16)
            #if hashAsNum < targetAsNum:
            #    dif = targetAsNum - hashAsNum
            #    print("targetAsNum: " + str(targetAsNum))
            #    print("hashAsNum: " + str(hashAsNum))
            #    print()

            if hash < self.targetStr:
            #    print 'Found Nonce:', nonce
            #    print("target str: " + str(long(hexlify(self.targetStr), 16)))
            #    print("hash done: " + str(long(hexlify(hash), 16)))
            #    print("hex printed: " + str(hash1))
            #    print
                self.chain.addCandidateBlock(candidateBlock)
                break
            nonce += 1
