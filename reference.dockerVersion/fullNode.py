from __future__ import print_function
from pprint import pprint

import time
import socket
import json
import miner

import grpc
import socket
import helloworld_pb2
import helloworld_pb2_grpc
import handshake
import registration
import blockchain
import txnMemoryPool
import transaction

from hashlib import sha256
from binascii import unhexlify, hexlify
import block
import transaction
import time
import output
from pprint import pprint
import pickle

# Create transaction
class FullNode:
    def __init__(self, port):
        self.registration = registration.Registration(port)
        self.handshakePackage = handshake.Handshake(self.registration.addrMe)
        self.peersLocal = {}
        self.memPool = {}
        self.miner = None

    def register(self):

        channel = grpc.insecure_channel(":58333")

        stub = helloworld_pb2_grpc.GreeterStub(channel)

        myPickle = pickle.dumps(self.registration)

        response = stub.SendRegistration2(helloworld_pb2.Registration(message=myPickle))

        #print ("this is the response" + str(response.message))

        return response.message

    def register2(self):

        channel = grpc.insecure_channel(":58333")

        stub = helloworld_pb2_grpc.GreeterStub(channel)

        myPickle = pickle.dumps(self.registration)

        response = stub.SendRegistration2(helloworld_pb2.Registration2(message=myPickle))

        #print ("this is the response" + str(response.message))

        return response.message

    def handshake(self, otherIp):

        #print("Handshaking... checking other nodes peers " + otherIp)

        self.peersLocal[otherIp] = 1

        channel = grpc.insecure_channel(otherIp)

        stub = helloworld_pb2_grpc.GreeterStub(channel)

        myPickle = pickle.dumps(self.handshakePackage)

        response = stub.SendHandshake(helloworld_pb2.Handshake(message=myPickle))

        knownPeers = []
        for x in response.message:
            knownPeers.append(x)

        return knownPeers

    def addPeer(self, peer):

        self.peersLocal.update({peer: 0})

        channel = grpc.insecure_channel(self.registration.addrMe)

        stub = helloworld_pb2_grpc.GreeterStub(channel)

        response = stub.SendPeer(helloworld_pb2.Peer(message=peer))

        print(response.message)

    def checkMissingPeers(self, knownPeers):

        for ip in knownPeers:
            if ip not in self.peersLocal and ip != self.registration.addrMe:
                self.addPeer(ip)
                self.checkMissingPeers(self.handshake(ip))

    def returnPeers(self, address):

        channel = grpc.insecure_channel(address)

        stub = helloworld_pb2_grpc.GreeterStub(channel)

        response = stub.PullPeers(helloworld_pb2.Blank(message=""))

        knownPeers = []
        for x in response.message:
            knownPeers.append(x)

        return knownPeers

    def pullTransactions(self):

        channel = grpc.insecure_channel(self.registration.addrMe)

        stub = helloworld_pb2_grpc.GreeterStub(channel)

        response = stub.PullTransactions(helloworld_pb2.Blank(message=""))

        transaction = pickle.loads(response.message)

        #print("pulled transactions " + str(transaction))

        return transaction

    def pullBlocks(self):

        channel = grpc.insecure_channel(self.registration.addrMe)

        stub = helloworld_pb2_grpc.GreeterStub(channel)

        response = stub.PullBlocks(helloworld_pb2.Blank(message=""))

        blocks = pickle.loads(response.message)

        knownBlocks = []
        for x in blocks:
            knownBlocks.append(x)

        return knownBlocks

    def makeMiner(self, blockchain, txnMemoryPool):

        self.miner = miner.Miner(blockchain, txnMemoryPool)

    def newTransactionBroadcast(self):

        transaction = self.miner.txnMemoryPool.createNewTransaction()

        transactionPickle = pickle.dumps(transaction)

        #print("sending to.. " + str(self.peersLocal))
        for ip in self.peersLocal:

            channel = grpc.insecure_channel(ip)

            stub = helloworld_pb2_grpc.GreeterStub(channel)

            response = stub.BroadcastTransaction(helloworld_pb2.Peer(message=transactionPickle))

            print(response.message)

    def newBlockBroadcast(self, block):

        blockPickle = pickle.dumps(block)

        for ip in self.peersLocal:

            channel = grpc.insecure_channel(ip)

            stub = helloworld_pb2_grpc.GreeterStub(channel)

            response = stub.BroadcastBlock(helloworld_pb2.Peer(message=blockPickle))

            print(response.message)

    def pullTransactionSize(self):


        channel = grpc.insecure_channel(self.registration.addrMe)

        stub = helloworld_pb2_grpc.GreeterStub(channel)

        response = stub.PullTransactionSize(helloworld_pb2.Blank(message=""))

        size = response.size

        #print("size is : " + str(size))

        return size

    def pullBlockSize(self):

        channel = grpc.insecure_channel(self.registration.addrMe)

        stub = helloworld_pb2_grpc.GreeterStub(channel)

        response = stub.PullBlockSize(helloworld_pb2.Blank(message=""))

        size = response.size

        #print("size is : " + str(size))

        return size
