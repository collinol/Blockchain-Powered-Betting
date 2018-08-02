from random import random

from BlockChain import encode_and_concenate, double_hash


class Transactions:

    def __init__(self,  output, inputs=None):
        self.version = 1
        self.ListOfInputs = ['input1', 'input2', 'other'] if inputs is None else inputs
        self.ListOfOutputs = [output.value, output.index, output.script] if output is not None else ['a'+str(random())]
        self.InCounter = len(self.ListOfInputs)
        self.OutCounter = len(self.ListOfOutputs)
        self._string_to_hash = encode_and_concenate([self.version, self.InCounter,
                                                     self.OutCounter]
                                                    + self.ListOfOutputs + self.ListOfInputs)
        self.TransactionHash = double_hash(self._string_to_hash)


class CoinbaseTransaction(Transactions):

    def __init__(self, current, output=None, inputs=None):
        super().__init__(output, inputs)
        self.current_total = current

    def set_current_total(self, val):
        self.current_total = self.current_total + val


class output:
    # TODO
    '''
    should also have a bitcoin address
    and a locking script with DUP, HASH160 -> gets target's public key hash, is it equal to the one we have?
    followed by operation OpCheckSig -> operates on unlocking script of next transaction
    '''

    def __init__(self, value, index, script):
        self.value = value
        self.index = index
        self.script = script
