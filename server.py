#TCP Chat Server and Client Program
#Created by Max Harms

import socket


#set host IP to local host
host = "127.0.0.1"
#set port to an arbitrary port
port = "12345"


def start_server():
    #create the socket using IPV4, TCP socket
    serv_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #bind the socket using the host and port values
    serv_sock.bind((host, port))
    #wait for data to come in from client
    cl, addr = serv_sock.accept()

    with cl:
        #print client connection
        print("Client has connected: ", addr)
        #receive data here
        while True:
            data = cl.recv(1024)
            cl.sendall(data)