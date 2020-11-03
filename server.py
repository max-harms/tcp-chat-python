#TCP Chat Server and Client Program
#This is both a network exercise and a little intro to python for me.
#Created by Max Harms

import socket


#set host IP to local host
host = "127.0.0.1"
#set port to an arbitrary port
port = "12345"


def start_server():
    #create the socket using IPV4, TCP socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #bind the socket using the host and port values
    s.bind((host, int(port)))
    #wait for data to come in from client
    cl, addr = s.accept()

    with cl:
        #print client connection
        #print("Client has connected: ", addr)
        #receive data here
        while True:
            data = cl.recv(1024)
            print(data)
            cl.sendall(data)