from hashlib import sha256, sha1
from time import time
from binascii import unhexlify, hexlify


# SingleShas
def singleShaFromBytes(bytestr):
    return sha256(bytestr).digest()


def singleShaFromStr(string):
    bytestream = string.encode('utf-8')
    return singleShaFromBytes(bytestream)


def singleShaFromHex(hexstr):
    bytestream = unhexlify(hexstr)
    return singleShaFromBytes(bytestream)


# DoubleShas
def doubleShaFromBytes(bytestr):
    return singleShaFromBytes(singleShaFromBytes(bytestr))


def doubleShaFromString(string):
    return singleShaFromBytes(singleShaFromStr(string))


def doubleShaFromHex(hexstr):
    return singleShaFromBytes(singleShaFromHex(hexstr))


# Reverse Functions
def __reverseBytes(bytesobj):
    return bytesobj[::-1]


# turns hash to bcHash bitcoin shows sha256 hashes backwards by convention
def bcHashHex(bytesobj):
    return __reverseBytes(bytesobj).hex()


def bcConcatHash(hexstr1, hexstr2):
    str1_bytestream = unhexlify(hexstr1)
    str2_bytestream = unhexlify(hexstr2)

    str1_bytestream = __reverseBytes(str1_bytestream)
    str2_bytestream = __reverseBytes(str2_bytestream)

    r = str1_bytestream + str2_bytestream
    return bcHashHex(singleShaFromBytes(singleShaFromBytes(r)))


# like hex(), but displays in bitcoin convention

def bcStringsConcatHash(*strings):
    string = ""
    for s in strings:
        string = string + str(s)
    return bcHashHex(doubleShaFromString(string))
