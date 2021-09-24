# import socket module
from socket import *
# In order to terminate the program
import sys


def webServer(port=13331):
    serverSocket = socket(AF_INET, SOCK_STREAM)
    # Prepare a server socket
    serverSocket.bind(("", port))
    # Fill in start
    serverSocket.listen(1)
    #print("The server is ready to receive")
    # Fill in end

    while True:
        # Establish the connection
        # print('Ready to serve...')
        connectionSocket, addr =   serverSocket.accept()# Fill in start      #Fill in end
        try:
            try:
                message = connectionSocket.recv(1024).decode()# Fill in start    #Fill in end
                #print("connect by", addr)
                filename = message.split()[1]
                print(filename[1:])
                f = open(filename[1:])
                #print("File Opened!")
                outputdata = f.read()# Fill in start     #Fill in end
                #print(outputdata)
                # Send one HTTP header line into socket.
                # Fill in start
                #print("200 OK")
                #connectionSocket.send(.encode())
                # Fill in end
                responseCode = 'HTTP/1.0 200 OK\n\n'
                connectionSocket.sendall(responseCode.encode())
                # Send the content of the requested file to the client
                for i in range(0, len(outputdata)):
                    connectionSocket.send(outputdata[i].encode())
                connectionSocket.send("\r\n".encode())
                connectionSocket.close()
            except IOError:
                print("404 Not Found")
                responseCode = 'HTTP/1.0 404 OK\n\n404 Not Found'
                connectionSocket.sendall(responseCode.encode())
        # Send response message for file not found (404)
        #Fill in start
                connectionSocket.close()
        #Fill in end

        # Close client socket
        # Fill in start

        # Fill in end

        except (ConnectionResetError, BrokenPipeError):
            pass

    serverSocket.close()
    sys.exit()  # Terminate the program after sending the corresponding data


if __name__ == "__main__":
    webServer(13331)

