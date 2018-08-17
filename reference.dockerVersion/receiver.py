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

_ONE_DAY_IN_SECONDS = 60 * 60 * 24


class Greeter(helloworld_pb2_grpc.GreeterServicer):
    def __init__(self):
        self.registrar = []
        self.registrar_HS = []

    # Register w DNS
    def SayHello(self, request, context):

        if request.address not in self.registrar:
            self.registrar.append(request.address)
            print("Seen: " + str(self.registrar))
            if len(self.registrar) > 1:
                print("will do something" + self.registrar[-2])
                return helloworld_pb2.HelloReply(message=self.registrar[-2])
        return helloworld_pb2.HelloReply(message=None)

    # Handshake Peer
    def SayHello2(self, request, context):
        print ("HANDSHAKING" + request.address)
        if request.address not in self.registrar:
            self.registrar.append(request.address)
            for x in self.registrar:
                print("known nodes:" + str(x))

        print("Peers: " + str(self.registrar))
        return helloworld_pb2.HelloReply2(message=self.registrar)

    # Add Peer to Own
    def SayHello3(self, request, context):
        print ("Adding peer" + request.address)
        if request.address not in self.registrar:
            self.registrar.append(request.address)
            for x in self.registrar:
                print("known nodes:" + str(x))

        print("Peers: " + str(self.registrar))
        return helloworld_pb2.HelloReply3(message="Added peer (Y)")

    # Pull Peers
    def SayHello4(self, request, context):
        print("Pulling peers")
        return helloworld_pb2.HelloReply2(peers=self.registrar, hs=self.registrar_HS)



def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    helloworld_pb2_grpc.add_GreeterServicer_to_server(Greeter(), server)
    #server.add_insecure_port('[::]:58333')
    server.add_insecure_port('[::]:58334')
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
