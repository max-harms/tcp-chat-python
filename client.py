import socket
from server import *
host = "127.0.0.1"
port = "12345"


def start_client():
    cl_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    cl_sock.connect((host, port))
    while True:
        cl_sock.sendall(input().encode())


def main():
    start_server()
    start_client()
