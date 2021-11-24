#!/usr/bin/env python3

import socket
import time
import threading

HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 8008      # The port used by the server
BUFFER = 1024
TIMER = 2

response = False

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
    localAddress = (HOST, PORT)
    sendCount = 5
    timeout = False

    print("=======================================\n")
    print('          A Python Client              ')
    print('   by: Andy Hooker hosted on 8008.')
    print('---------------------------------------')
    print('Connecting...')
    time.sleep(TIMER)
    sock.sendto(b"client connection incoming",localAddress)
    for i in range(10):
        if (timeout):
            timeout = False
            continue
        print("Sending PING...")
        sock.sendto(b'Ping', localAddress)
        while True:
            time.sleep(TIMER)
            try:
                sock.settimeout(TIMER)
                data = sock.recvfrom(BUFFER)
                msg = '{}'.format(data[0])
                print('[Received]  :', msg)
                sock.settimeout(0)
            except:
                print('[Received]  : Timeout...')
                timeout = True
                break
            if data:
                break
    print('Disconnecting... Bye Bye!')
    print('---------------------------------------')
    sock.close()
