from HashFuncs import * 
import codecs
from binascii import unhexlify, hexlify
from hashlib import sha256, sha1
from math import *


class MerkleTree:
    def __init__(self, txIds):
        d = {}
        self.tree = self.__makeTree(txIds, d)

    def get_root(self):
        if self.tree is None:
            return None
        return self.tree.get(0)[0]

    def get_size(self):
        if (len(self.tree) == 0):
            return None
        return len(self.tree) - 1

    def printMerkleTree(self):
        print (self.tree)

    def getPosition(self, depth, index):
        return self.tree.get(depth)[index]

    def __makeTree(self, txIds, d):
        size = len(txIds)
        if (size == 0):
            return None
        ls = []
        depth = 0
        depth = ceil(log2(len(txIds)))
        if (size == 1):
            ls.append(txIds[0])
            d[depth] = ls
            return d
        else:
            i = 0
            while(i < size-1):
                hexstr1 = txIds[i]
                hexstr2 = txIds[i+1]
                hexstr3 = bcConcatHash(hexstr1, hexstr2)
                ls.append(hexstr3)
                i = i + 2

            if(size % 2 == 1): #if odd, append last element
                lastElement = txIds[size-1]
                ls.append(bcConcatHash(lastElement, lastElement))
            d[depth] = txIds
            x = self.__makeTree(ls, d)
            return x





    def getMinSet(self, txLeaf):
        minset = []
        tree = self.tree
        depth = self.get_size()
        node = txLeaf
        while depth > 0:
            ls = tree[depth]
            i = ls.index(node)
            if (i % 2 == 1): #if leaf is odd
                h1 = ls[i-1]
                node = tree.get(depth-1)[int((i-1) / 2)]
            else:           #if leaf is even
                if(i == len(ls) - 1):   #if even leaf is last on list
                    h1 = node                 
                else:                   #else even leaf is not last on list
                    h1 = ls[i+1]
                node = tree.get(depth-1)[int(i/2)]
            minset.append(h1)
            depth = depth - 1
        minset.append(self.get_root())

        return minset

    def printMinSetVerifyRootProof(self, txLeaf):
        global concatHash
        minset = self.getMinSet(txLeaf)
        depth = self.get_size()
        tree = self.tree
        node1 = txLeaf
        m = 0
        node2 = minset[m]

        while (depth > 0):
            if (tree.get(depth).index(node1) % 2 == 1): #if node1 is odd index
                concatHash = bcConcatHash(node2, node1)
            else:   
                concatHash = bcConcatHash(node1, node2)
            print("Begin Depth " + str(depth) + '\n')
            print("First Branch hash is: " + node1)
            print("Second Branch hash is: " + node2)
            print("Branch hash is: " + concatHash + '\n')
            print("Depth " + str(depth) + " Complete\n")
            depth = depth - 1
            node1 = concatHash
            m = m + 1
            node2 = minset[m]
        print("Root = " + self.get_root())
        b = (self.get_root() == concatHash) # if root equals last concat has
        print("Result Match: " + str(b))
      
    def verifyRoot(self, mroot):
        return self.get_root() == mroot

    #printVerifyRootProof uses lookups as opposed to calculating 
    #the bcConcatHash function. This is because these calculations
    #are performed when the MerkleTree is constructed. Then only
    #if the provided merkle root matches the root derived from the
    #construction of the MerkleTree, the proof is provided.
    def printVerifyRootProof(self, mroot):
        tree = self.tree
        if (self.verifyRoot(mroot)):
            size = self.get_size()
            print("Size = " + str(size))
            if (len(self.tree) == 1):
                print("FINAL MERKLE ROOT AT DEPTH 0: " + str(size))
            depth = size
            while (depth > 0):      
                i = 0
                nodes = tree.get(depth)
                print("Number of Branches at Depth " + str(depth) + " is " + str(len(nodes)) + '\n')
                while (i < len(nodes)-1):
                    node1 = nodes[i]
                    node2 = nodes[i+1]
                    parent = tree.get(depth-1)[int(i/2)]
                    print("Branch " + str(i) +  " hash is: " + node1)
                    print("Branch " + str(i+1) + " hash is: " + node2)
                    print("Branch hash is: " + parent + '\n')
                    i = i + 2
                if (len(nodes) % 2 == 1):
                    lastnode = nodes[len(nodes) - 1]
                    print("Branch " + str(i) +  " hash is: " + lastnode)
                    print("Branch " + str(i+1) + " hash is: " + lastnode)
                    print("Branch hash is: " + bcConcatHash(lastnode, lastnode))
                print("\nCompleted Depth: " + str(depth) + '\n')
                depth = depth - 1
            print("FINAL MERKLE ROOT AT DEPTH 0: \n\nRESULT = " + str(self.get_root()))

        else:
            print(self.verifyRoot(mroot))











        

