To run this program..
    run server.py - will act as DNS_SEED on local_host:58333
    run server2.py - will act as NODE_A on local_host:58334
    run server3.py - will act as NODE_B on local_host:58335
    run server4.py- will act as NODE_C on local_host:58336

    Go to main.py file
    Change server = fullNode.FullNode("58334") to each NODE's port, running a total of 3 times
    E.g. make sure port is 58334, run main.py, change port to 58335, run main.py, change port to 58336, run main.py