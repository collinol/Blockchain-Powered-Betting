import time
from random import random

from Transaction import Transactions, output


class TxnMemoryPool:

    def __init__(self):
        self.transactions = []

    def add_new_transaction(self, transaction):
        self.transactions.append(transaction)

    def print_pool(self):
        for txn in self.transactions:
            print("txn_in: {}\ntxn_out: {}".format(txn.ListOfInputs,txn.ListOfOutputs))

    def generate_n_transaction(self, n):
        for i in range(n):
            transaction_in = 'random transaction input, varies by {} {} {}'.format(time, random(), i)
            transaction_out = output(random()*100, i, "output script message appended by {}".format(i))
            transaction = Transactions(transaction_out, [transaction_in])
            self.transactions.append(transaction)


if __name__ == '__main__':
    txn_pool = TxnMemoryPool()
    txn_pool.generate_n_transaction(1000)
    txn_pool.print_pool()