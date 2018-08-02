import hashlib
import math
from binascii import unhexlify

class MerkleTreeHash(object):
    elements = {}

    def __init__(self, file_hashes, depth):
        self.merkle_root = self.find_merkle_hash(file_hashes, depth)

    def find_merkle_hash(self, file_hashes, depth_level):
        # find the merkle tree hash of all the file hashes passed to this function

        blocks = []

        if not file_hashes:
            raise ValueError("Missing file hashes")

        # sort hashes

        for m in file_hashes:
            blocks.append(m)

        list_len = len(blocks)

        # adjust the block of hashes until we have an even number of items
        # print("number of branches at depth {} is {} ".format(depth_level, len(blocks)))
        while list_len % 2 != 0:
            blocks.extend(blocks[-1:])
            list_len = len(blocks)

        # now we have an even number of items
        # slide 46
        secondary = []
        counter = 1

        def reversebytes(str):
            return str[::-1]

        for k in [blocks[x:x + 2] for x in range(0, len(blocks), 2)]:
            concat = reversebytes(unhexlify(k[0])) + reversebytes(unhexlify(k[1]))
            doublesha_branch = hashlib.sha256(hashlib.sha256(concat).digest()).digest()
            # print("branch {} is {}".format(counter, k[0]))
            # print("branch {} is {}".format(counter, k[1]))
            self.elements[k[0]] = depth_level
            self.elements[k[1]] = depth_level
            counter += 1
            branch_hash = reversebytes(doublesha_branch).hex()
            self.elements[branch_hash] = depth_level - 1
            # print("branch hash is {} ".format(branch_hash))
            secondary.append(branch_hash)

        # bottom of recursion

        if len(secondary) == 1:
            return secondary[0]
        else:
            return self.find_merkle_hash([i.encode('utf-8') for i in secondary], depth_level - 1)

    def path_proof(self, leaf, minimum_set):
        def reversebytes(str):
            return str[::-1]

        print("\nproof")
        for s in [k for k in self.elements.keys() if self.elements[k] == self.elements[leaf]]:
            print("leaf: ", leaf)
            print("possible sibling: ", s)
            possible_combination1 = reversebytes(unhexlify(leaf)) + reversebytes(unhexlify(s))
            possible_combination2 = reversebytes(unhexlify(s)) + reversebytes(unhexlify(leaf))
            doublesha_parent1 = hashlib.sha256(hashlib.sha256(possible_combination1).digest()).digest()
            doublesha_parent2 = hashlib.sha256(hashlib.sha256(possible_combination2).digest()).digest()
            print("combined 1", reversebytes(doublesha_parent1).hex())
            print("combined 2", reversebytes(doublesha_parent2).hex())
            upper_depth = [k for k in self.elements.keys() if self.elements[k] == self.elements[leaf]-1]
            if reversebytes(doublesha_parent1).hex() in upper_depth:
                print("found sibling: ", s)
                minimum_set.append(s)
                self.path_proof(reversebytes(doublesha_parent1).hex(), minimum_set)
            if reversebytes(doublesha_parent2).hex() in upper_depth:
                print("found sibling: ", s)
                minimum_set.append(s)
                self.path_proof(reversebytes(doublesha_parent2).hex(), minimum_set)
        return minimum_set


if __name__ == '__main__':
    transactions = [
        "b5f60977102f95a9ed855b61acec86e2e434248b38c5f263ccf708a302832f3c",
        "e6922d44c520c52dca2cd5300784af55944c11839684e5c1671d9b330f871f55",
        "a72ef0e0240fb592dd1d6ec3d1ab24890def0870f5c44d478f1feb1f87701e43",
        "51ef089bd2fc330cd02ee9d5a3cb5532ed48d8668ed78a92b84c8da97922975a",
        "ae22ea6889a5712eb2e13736ce4586afd310295c6ddbbc2b56b1305441017a70",
        "cfce9664889e17fa006cfa23dd82852a999f9a748478cf325e3791241dd27a50",
        "4db4ac98aa68d75dc3602f8f3b06157ac93485268df220cc6dc4aa39f6f9d7a9",
        "a0337aef8e3739e6b705c51202a9d58addc375e2830e3429727a461052279d46",
        "0dc7b3bf9b1a98859d694146a0acd5a988d4184ab9c048ea91d8be7fd1cd84e6",
        "72e15234eb42c9f4b650dec5727205dacbbcb039e8c22034b00bf805192abec7",
        "dca4db368d5241219a0f5f8c744c42293b9bc4959b99e4ed43abc075c284b78c",
        "a5e67793f9193a7b9192e4c3e7cd27268ef354b0513a9cd595c04778d3fa3eef",
        "4d53b64a343589f9b76643c80eacdd632cc50fcec6ece4dd7d3c0c65dba1d0f9",
        "3495a4fab0ff587f6050a22035e12253b250d088413dbd30b1cb44365b87bd86"
    ]
    initial_depth = math.ceil(math.log2(len(transactions)))
    MT = MerkleTreeHash(transactions, initial_depth)
    hashes = [i.encode('utf-8') for i in transactions]
    mk = MT.find_merkle_hash(hashes, initial_depth)
    print("merkle root:", mk)
    initial_leaf = "cfce9664889e17fa006cfa23dd82852a999f9a748478cf325e3791241dd27a50"
    min_set = MT.path_proof(initial_leaf.encode('utf-8'), [])
    min_path = [i for i in set(min_set) if type(i) == bytes]
    print("Minimum number of nodes required for path proof is {} "
          "\nRequired hashes are {}".format(len(min_path), [b.decode() for b in min_path]))
