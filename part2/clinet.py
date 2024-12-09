from socket import *

while True:
    serverName = "localhost"
    serverPort = 9955
    #create tcp socket
    clientSocket = socket(AF_INET, SOCK_STREAM)
    #creatinf connection between client and server
    clientSocket.connect((serverName, serverPort))
    id = input("inter id\n")
    #sending id
    clientSocket.send((str(id).encode()))

    clientSocket.close()
