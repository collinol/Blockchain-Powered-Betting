from __future__ import print_function

import time
import socket
import json

import grpc
import socket
import helloworld_pb2
import helloworld_pb2_grpc
import handshake


# Create transaction
class Handshake:
    def __init__(self, thisNode):
        self.nVersion = 1
        self.nTime = time.time()
        self.addrMe = thisNode
        self.bestHeight = 0

