from Transaction import *

class TxnMemoryPool:
    def __init__(self):
        self.Transactions = []  # array/list of Transactions

    def print_transactions(self):
        for t in self.Transactions:
            t.print_transaction()

    def add_transaction(self, transaction):
        self.Transactions.append(transaction)

