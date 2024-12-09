from socket import *
import time
import os
serverPort = 9955 #port number
# creating tcp socket
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(("", serverPort))
serverSocket.listen(1)
print("The server is ready to receive")
def is_valid_id (id): # this function will check if given input is ine of our IDs
    groupIDS = ["1211756","1212386","1213205"]
    return id in groupIDS
# function that will lockscreen
def lock():
    os.system("rundll32.exe user32.dll,LockWorkStation")
while True:
    # Accept an incoming connection and get the connection socket and client address
    connectionSocket, addr = serverSocket.accept()
    print(f"Accepted connection from {addr}")
    data = connectionSocket.recv(1024).decode("utf-8")
    #check if id is valid
    if is_valid_id(data):
        print("the server will lock in 10 seconds")
        time.sleep(10)
        lock()
    else:
        print("invalid id")

    connectionSocket.close() # closing connection







