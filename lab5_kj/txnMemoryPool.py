import time
import output
import transaction


# Create memory pool
class TxnMemoryPool:
    def __init__(self):
        self.memoryPool = []
        self.create91()

    # Create 91 transactions in the memory pool
    def create91(self):
        for x in range(0, 91):
            transactionNew = transaction.Transaction([time.time() + 1], [output.Output()])

            self.memoryPool.append(transactionNew)
