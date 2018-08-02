from BlockChain import encode_and_concenate, double_hash


class Block:
    def __init__(self, header, target):
        self.MagicNumber = 0xD9B4BEF9
        self.transaction_hashes = []
        self.transactions = []
        self.hash_prev_block = header.hashPreviousBlock
        self.hash_merkle_block = None #gets updated later once transactions are added
        self.target = target
        self.nonce = header.nonce
        self.to_dsha = encode_and_concenate([header.hashPreviousBlock, header.TimeStamp,
                                             header.bits, header.nonce])

        self.BlockHash = double_hash(self.to_dsha)

    def add_transaction(self, new_transac):
        if not self.block_is_full():
            self.transaction_hashes.append(new_transac.TransactionHash)
            self.transactions.append(new_transac)
            self.hash_merkle_block = double_hash(encode_and_concenate(str('-'.join(self.transaction_hashes))))

    def block_is_full(self):
        return len(self.transaction_hashes) >= 10

    def ready_to_mine(self):
        return self.block_is_full()

    def update(self):
        return '-'.join([self.hash_merkle_block, str(self.nonce)])

    def mine_this_block(self):
        current_block_hash = double_hash(encode_and_concenate(self.update()))
        print('current block hash = {}, target hash = {}'.format(current_block_hash, self.target))
        #print("current block decimal = {} target decimal = {}".format(int(current_block_hash, 16), int(self.target, 16)))
        if int(current_block_hash, 16) < int(self.target, 16):
            print('Block was mined! You\'ve been rewarded {} ECC!'.format(20))
            self.transactions[0].set_current_total(20)
            print("current EchoCoin total: {}".format(self.transactions[0].current_total))
            return True
        else:
            self.nonce += 1
        return False

