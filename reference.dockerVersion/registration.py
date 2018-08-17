from __future__ import print_function
from pprint import pprint

import time
import socket
import json

import grpc
import socket
import helloworld_pb2
import helloworld_pb2_grpc
import handshake


# Create transaction
class Registration:
    def __init__(self, port):
        self.nVersion = 1
        self.nTime = time.time()
        self.addrMe = str(socket.gethostbyname(socket.gethostname())) + ':' + port
        print(str(socket.gethostbyname(socket.gethostname())) + ':' + port)



