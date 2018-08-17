from hashlib import sha256

# Create transaction
class Transaction:
    def __init__(self, listOfInputs, listOfOutputs):
        self.versionNumber = 1
        self.inCounter = len(listOfInputs)
        self.listOfInputs = listOfInputs
        self.outCounter = len(listOfOutputs)
        self.listOfOutputs = listOfOutputs
        self.transactionHash = self.getTransactionHash()

    # Get the transaction's hash
    def getTransactionHash(self):
        string = str(self.versionNumber) + str(self.inCounter) + str(self.listOfInputs) + str(self.outCounter) + str(
            self.listOfOutputs)

        return sha256(sha256(bytearray(string, 'utf-8')).digest()).hexdigest()

    # Print transaction
    def printTransaction(self):
        print("Printing Transaction...")
        print("\tVersionNumber: " + str(self.versionNumber))
        print("\tInCounter: " + str(self.inCounter))
        print("\tListOfInputs: " + str(self.listOfInputs))
        print("\tOutCounter: " + str(self.outCounter))
        for x in self.listOfOutputs:
            print("\tListOfOuputs: ")
            print("\t\tValue: " + (str(x.value)))
            print("\t\tIndex: " + (str(x.index)))
            print("\t\tScript: " + (str(x.script)))
        print("\tTransactionHash: " + str(self.transactionHash))
        print("#################################################################################")

