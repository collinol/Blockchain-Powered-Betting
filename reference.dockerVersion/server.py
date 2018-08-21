# Copyright 2015 gRPC authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""The Python implementation of the GRPC helloworld.Greeter server."""

from concurrent import futures
import time

import grpc

import helloworld_pb2
import helloworld_pb2_grpc

import pickle
import fullNode

from pprint import pprint

_ONE_DAY_IN_SECONDS = 60 * 60 * 24


class Greeter(helloworld_pb2_grpc.GreeterServicer):
    def __init__(self):
        self.peers = []
        self.blockLobby = []
        self.transactionLobby = []
        self.node = fullNode.FullNode("58334")

    # Register w DNS
    def SendRegistration(self, request, context):

        registration = pickle.loads(request.message)

        if registration.addrMe not in self.peers:
            self.peers.append(registration.addrMe)
            print("Seen: " + str(self.peers))
            if len(self.peers) > 1:
                print("will do something" + self.peers[-2])
                return helloworld_pb2.PrevServer(message=self.peers[-2])
        return helloworld_pb2.PrevServer(message=None)

    def SendRegistration2(self, request, context):

        registration = pickle.loads(request.message)
        if registration.addrMe not in self.peers:
            self.peers.append(registration.addrMe)
            print("Seen: " + str(self.peers))
            if len(self.peers) > 1:
                print("will do something" + self.peers[-2])
                return helloworld_pb2.PrevServer2(message=self.peers[-2])
        return helloworld_pb2.PrevServer(message=None)

    # Handshake Peer
    def SendHandshake(self, request, context):

        handshake = pickle.loads(request.message)

        print ("HANDSHAKING" + handshake.addrMe)
        if handshake.addrMe not in self.peers:
            self.peers.append(handshake.addrMe)
            for x in self.peers:
                print("known nodes:" + str(x))

        print("Peers: " + str(self.peers))
        return helloworld_pb2.KnownPeerList(message=self.peers)

    # Add Peer to Own
    def SendPeer(self, request, context):
        print ("Adding peer" + request.message)
        if request.message not in self.peers:
            self.peers.append(request.message)
            for x in self.peers:
                print("known nodes:" + str(x))

        print("Peers: " + str(self.peers))
        return helloworld_pb2.Blank(message="Added peer (Y)")

    # Pull Peer
    def PullPeers(self, request, context):
        return helloworld_pb2.KnownPeerList(message=self.peers)

    # Receive Broadcasted Transaction
    def BroadcastTransaction(self, request, context):

        transaction = pickle.loads(request.message)

        self.transactionLobby.append(transaction)

        return helloworld_pb2.Blank(message="Transaction Received")

    # Receive Broadcasted Transaction
    def BroadcastBlock(self, request, context):

        block = pickle.loads(request.message)

        self.blockLobby.append(block)

        return helloworld_pb2.Blank(message="Block Received")

    # Pull Transactions
    def PullTransactions(self, request, context):

        pullTransactions = self.transactionLobby

        pickedPullTransactions = pickle.dumps(pullTransactions)

        self.transactionLobby = []

        return helloworld_pb2.Transactions(message=pickedPullTransactions)

   # Pull Blocks
    def PullBlocks(self, request, context):

        pullBlocks = self.blockLobby

        pickledPullBlocks = pickle.dumps(pullBlocks)

        self.blockLobby = []

        return helloworld_pb2.Blocks(message=pickledPullBlocks)

   # Pull Transaction Lobby Size
    def PullTransactionSize(self, request, context):

        return helloworld_pb2.Number(size=len(self.transactionLobby))

   # Pull Block Lobby Size
    def PullBlockSize(self, request, context):

        return helloworld_pb2.Number(size=len(self.blockLobby))


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    helloworld_pb2_grpc.add_GreeterServicer_to_server(Greeter(), server)
    server.add_insecure_port('[::]:58333')
    #server.add_insecure_port('[::]:58334')
    #server.add_insecure_port('[::]:58335')
    #server.add_insecure_port('[::]:58336')


    server.start()
    try:
        while True:
            time.sleep(_ONE_DAY_IN_SECONDS)
    except KeyboardInterrupt:
        server.stop(0)


if __name__ == '__main__':
    serve()
