import datetime as date

from BlockChain import double_hash, encode_and_concenate


class Header:
    def __init__(self, previoushash, list_of_transactions=None):
        self.version = 1
        self.previousHash = previoushash
        self.transactions = list_of_transactions
        self.hashPreviousBlock = double_hash(encode_and_concenate(previoushash))
        self.TimeStamp = date.datetime.now()
        self.bits = 0x207fffff
        self.nonce = 0

