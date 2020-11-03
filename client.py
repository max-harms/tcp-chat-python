import socket

# from server import *
host = "127.0.0.1"
port = "12345"


def start_server():
    # create the socket using IPV4, TCP socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # bind the socket using the host and port values
    s.bind((host, int(port)))
    # wait for data to come in from client
    conn, addr = s.accept()

    with conn:
        # print client connection
        print("Client has connected: ", addr)
        # receive data here
        while True:
            data = conn.recv(1024)
            print(data)
            conn.sendall(data)


def start_client():
    cl_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    cl_sock.connect((host, port))
    while True:
        cl_sock.sendall(b"hello!")


def main():
    start_server()
    start_client()

#necessary to run main() function
if __name__ == "__main__":
    main()
