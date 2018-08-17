from hashlib import sha256
import header
import sys
import cPickle


# Create Block
class Block:
    def __init__(self, previousHash, transactionsList, nonce, merkle):
        self.magicNumber = 0xD9B4BEF9
        self.transactionCounter = len(transactionsList)


        self.blockHeader = header.Header(previousHash, self.transactionListHashesOnly(transactionsList), nonce, merkle)


        self.transactions = transactionsList
        self.blockHash = self.calculateHash()
        # Temp size - renewSize method will update size before adding to blockchain
        self.blockSize = sys.getsizeof(cPickle.dumps(self))

    # Find Blockhash of a block
    def calculateHash(self):
        string = str(self.blockHeader.timeStamp) + str(self.blockHeader.hashMerkleRoot) + str(
            self.blockHeader.bits) + str(
            self.blockHeader.nonce) + str(self.blockHeader.hashPrevBlock)

        return sha256(sha256(bytearray(string, 'utf-8')).digest()).hexdigest()

    # Find transaction hashes only from the transaction list
    def transactionListHashesOnly(self, transactionList):
        transactionHashesList = []

        for t in transactionList:
            transactionHashesList.append(t.transactionHash)

        return transactionHashesList

    # Print the blocks data
    def printBlock(self):
        print("Printing Block...")
        print("\tBlockHash: " + str(self.blockHash))
        print("\tMagicNumber: " + str(self.magicNumber))
        print("\tBlockSize: " + str(self.blockSize))
        print("\tBlockHeader:")
        print("\t\tVersion: " + str(self.blockHeader.version))
        print("\t\tHashPrevBlock: " + str(self.blockHeader.hashPrevBlock))
        print("\t\tHashMerkleRoot: " + str(self.blockHeader.hashMerkleRoot))
        print("\t\tTimeStamp: " + str(self.blockHeader.timeStamp))
        print("\t\tBits: " + str(self.blockHeader.bits))
        print("\t\tNonce: " + str(self.blockHeader.nonce))
        print("\tTransactionCounter: " + str(self.transactionCounter))
        # print("\tTransactions: ")
        # for t in self.transactions:
        #    print("\t\t" + t.transactionHash)
        print("")
        print("#################################################################################")

    def renewSize(self):
        self.blockSize = sys.getsizeof(cPickle.dumps(self))
