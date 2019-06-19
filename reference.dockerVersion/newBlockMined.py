import random
import pickle


# Create output
class NewTransaction:
    def __init__(self, block):
        self.blockData = pickle.dumps(block)

