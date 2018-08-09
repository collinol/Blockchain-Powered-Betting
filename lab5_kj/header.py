from binascii import unhexlify, hexlify
from hashlib import sha256
import time


# Create header
class Header:
    def __init__(self, hashPrevBlock, transactionHashList, nonce, bits=None):
        self.version = 1
        self.nonce = nonce

        if (bits is None):
            self.bits = 0x207fffff
        else:
            self.bits = bits

        self.hashPrevBlock = hashPrevBlock
        self.hashMerkleRoot = self.createMerkle(transactionHashList)
        self.timeStamp = time.time()

    # Double hash on byte strings on left and right concatenation
    def hashAlgo(self, left, right):

        combinedByte = left + right
        combinedHash = sha256(sha256(combinedByte).digest()).digest()

        retVal = combinedHash

        return retVal

    # To convert a hex string to bytes, put it in a byte array
    def reverser(self, str):
        binstr = unhexlify(str)
        ba = bytearray(binstr)
        # ba.reverse()
        return ba

    # Return byte string array as a hex string
    def reverser2(self, binstr):
        ba = bytearray(binstr)
        # ba.reverse()
        retval = hexlify(ba)
        return retval

    # Create Merkle Tree based off the transaction hashes
    def createMerkle(self, hashList):

        # Check if list is 0 or 1 and return appropriate results
        if (len(hashList) == 0):
            return None
        elif len(hashList) == 1:
            return hashList[0]

        # Find the depth of the tree
        depthLevel = self.findHashDepth(hashList)

        # for val in hashList:
        #    print(val)

        # Convert to byte string and keep like that except for printing
        for idx, val in enumerate(hashList):
            # print(val)
            hashList[idx] = self.reverser(val)

        # Loop through hash list
        while len(hashList) > 1:

            # Print branch and depth analysis
            # print("Number of branches at Depth " + str(depthLevel) + " is " + str(len(hashList)))
            # print("")

            # Duplicate last branch if odd number of branches
            if (len(hashList) % 2 != 0):
                hashList.append(hashList[-1])

            # Hash list to provide next depth's calculations
            newHashList = []

            # Cycle through hash list
            for count, element in enumerate(hashList, 0):  # Start counting from 1

                # Use odd branches to double-SHA256 the next branch together
                if count % 2 == 0:
                    # Print branch info before calculation and make hex
                    # print("Branch " + str(count + 1) + " is " + str(self.reverser2(hashList[count]).decode()))
                    # print("Branch " + str(count + 2) + " is " + str(self.reverser2(hashList[count + 1]).decode()))

                    # Hash algo to find parent hash
                    hashFinal = self.hashAlgo(hashList[count], hashList[count + 1])

                    # Print calculation
                    # print("Branch hash is " + self.reverser2(hashFinal).decode())
                    # print("")

                    # Add calculation to next depth's list
                    newHashList.append(hashFinal)

            # Make the hash list have the next completed depth's list
            hashList = newHashList

            # Completion print and depth reduction
            # print("Completed depth " + str(depthLevel))
            depthLevel -= 1
            # print("#################################################################################")

        # List result and decode byte to hex string
        result = [depthLevel, self.reverser2(hashFinal).decode()]
        return result[1]

    # Find the depth of the merkle tree
    def findHashDepth(self, hashList):
        # Print amount of transactions
        hashListSize = len(hashList)
        # print("Size: " + str(hashListSize))

        # Find number of depths to calculate through
        depthLevel = 0
        while hashListSize > 0:
            depthLevel += 1
            hashListSize //= 2

        return depthLevel

    # Print header method
    def printHeader(self):

        print("Header:")
        print("\tVersion: " + str(self.version))
        print("\tHashPrevBlock: " + str(self.hashPrevBlock))
        print("\tHashMerkleRoot: " + str(self.hashMerkleRoot))
        print("\tTimeStamp: " + str(self.timeStamp))
        print("\tBits: " + str(self.bits))
        print("\tNonce: " + str(self.nonce))
