from HashFuncs import *


class Transaction:

    def __init__(self, list_of_inputs=None, list_of_outputs=None):
        self.VersionNumber = 1
        # inputs
        if list_of_inputs is None:
            self.ListOfInputs = ["default input"]
            self.InCounter = 1
        else:
            self.ListOfInputs = list_of_inputs
            self.InCounter = len(list_of_inputs)
        # outputs
        if list_of_outputs is None:
            self.ListOfOutputs = ["default output"]
            self.OutCounter = 1
        else:
            self.ListOfOutputs = list_of_outputs
            self.OutCounter = len(list_of_outputs)

        self.TransactionHash = self.__calc_transaction_hash()

    def print_transaction(self):
        d = {'VersionNumber': self.VersionNumber,
             'InCounter': self.InCounter,
             'ListOfInputs': self.ListOfInputs,
             'OutCounter': self.OutCounter,
             'ListOfOutputs': self.ListOfOutputs,
             'TransactionHash': self.TransactionHash
             }
        print(d)

    def __calc_transaction_hash(self):
        input_list_str = ""
        output_list_str = ""
        for string in self.ListOfInputs:
            input_list_str = input_list_str + string
        for out in self.ListOfOutputs:
            output_list_str = output_list_str + out.script

        return bcStringsConcatHash(str(self.VersionNumber), input_list_str, str(self.InCounter), output_list_str,
                                   str(self.OutCounter))

