import random
import pickle

# Create output
class NewTransaction:
    def __init__(self, transaction):
        self.transactionData = pickle.dumps(transaction)

