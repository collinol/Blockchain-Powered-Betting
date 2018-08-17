import random


# Create output
class Output:
    def __init__(self, value=None):
        if value is None:
            self.value = self.createValue()
            self.index = 0
        else:
            self.value = value
            self.index = 0xFFFFFFFF
        self.script = "Nothing"

    def getValue(self):
        return self.value

    def getIndex(self):
        return self.index

    def getScript(self):
        return self.script

    def createValue(self):
        return random.randint(1, 100000)
