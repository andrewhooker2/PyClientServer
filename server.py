#!/usr/bin/env python3

import socket
import time
import random

HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 8008    
BUFFER = 1024  


with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:

    sock.bind((HOST, PORT))

    bytesAddressPair = sock.recvfrom(BUFFER)
    message = bytesAddressPair[0]
    address = bytesAddressPair[1]

    lossList = []
    pongSent = 0
    
    lossList = random.sample(range(0,9), 3)
    print("=======================================\n")
    print('Welcome to the Server')
    print('---------------------------------------')
    print('[server] : Ready to connect')
    time.sleep(4)
    with sock:
        print('[server] : Client Connected :)')
        time.sleep(4)
        print('[server] : ready to accept data... ')

        while True:
            while True:
                data = sock.recvfrom(BUFFER)
                msg = '{}'.format(data[0])
                print('[client] : ', msg)
                if(pongSent in lossList):
                    print('[server] : packet loss... wow...')
                    pongSent = pongSent + 1
                    break
                else:
                    print('[server] : sending PONG')
                    time.sleep(1)
                    pongSent = pongSent + 1 
                    sock.sendto(b'PONG', address)

                if not data:
                    break
          
    sock.close()