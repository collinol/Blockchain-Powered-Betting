import fullNode
from pprint import pprint
import time
import transaction
import blockchain
import txnMemoryPool
import threading
import os
import fullNode
from multiprocessing import Process
import contextlib
import random


def updateMiner(node):
    while True:
        time.sleep(0.1)
        pulledTransactions = node.pullTransactions()
        for t in pulledTransactions:
            there = False
            #print("This is hash trying to be appended " + str(t.transactionHash))
            for aT in node.miner.txnMemoryPool.memoryPool:
                if aT.transactionHash == t.transactionHash:
                    there = True
            if not there:
                node.miner.txnMemoryPool.memoryPool.append(t)
                #print("Transaction appended")

        #print("checking if dupes")
        #for x in node.miner.txnMemoryPool.memoryPool:
            #print(x.transactionHash)

        pulledBlocks = node.pullBlocks()
        for b in pulledBlocks:
            there = False
            #print("This is hash trying to be appended " + str(b.blockHash))
            for aT in node.miner.chain.blockChain:
                if aT.blockHash == b.blockHash:
                    there = True
            if not there:
                node.miner.chain.blockChain.append(b)

            #print("Block appended")
            # if does this you need to start over on calculating nonce !!!

        #print("checking if dupes")
        #for x in node.miner.chain.blockChain:
            #print(x.blockHash)

def discoverAndBroadCastTransaction(node):
    while True:
        time.sleep(0.1)
        node.newTransactionBroadcast()
        time.sleep(random.randint(2, 5))


def findBlock(node):
    while True:
        time.sleep(0.1)
        node.newBlockBroadcast(node.miner.calculateNonce())
        # HALT MINING THREADS FOR A FEW SECONDS
        # TELL EVERYONE TO START OVER
        print("Height: " + str(len(node.miner.chain.blockChain)))
        node.miner.chain.blockChain[-1].printBlock()

def setter():
    time.sleep(4)


server = fullNode.FullNode("58334")
#server = fullNode.FullNode("58335")
#server = fullNode.FullNode("58336")


# Node A
#pprint("Registration.." + str(vars(nodeA)))
prevNodeIp = server.register2()

#print('prevNodeIP is.. ' + str(prevNodeIp))

if prevNodeIp != "":
    print("made it here")
    # Add to registrar
    server.addPeer(prevNodeIp)

    # Handshake
    #print("Starting handshake")
    peers = server.handshake(prevNodeIp)
    #print(peers)


# Analyze handshake peers


#print("nodeA Verified peers: " + str(nodeA.returnPeers(nodeA.registration.addrMe)))
#print(nodeA.peersLocal)


# Start mining
while True:
    print("in loop")
    server.checkMissingPeers(server.returnPeers(server.registration.addrMe))
    dns_server = ":58333"
    dnsPeers = server.returnPeers(dns_server)
    #print("DNS Check: " + str(dnsPeers))
    if (len(dnsPeers) >= 3):
        break
    time.sleep(5)

# Start mining

# Create initial chain
krisChain = blockchain.Blockchain()

# Create memory pool
krisPool = txnMemoryPool.TxnMemoryPool()

# Create Miner
server.makeMiner(krisChain, krisPool)


# Run nodes
thread1 = threading.Thread(target=discoverAndBroadCastTransaction, args=(server,))

thread2 = threading.Thread(target=updateMiner, args=(server,))

thread3 = threading.Thread(target=findBlock, args=(server,))


thread1.start()
time.sleep(10)
thread2.start()
thread3.start()

thread1.join()
thread2.join()
thread3.join()

print("Bottom")