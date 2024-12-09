import socket
from socket import * # importing socket programming librariy
serverPort=9966 # used port number
serverSocket = socket(AF_INET,SOCK_STREAM) # creating tcp socket
#serverSocket.bind(("",serverPort))
serverSocket.bind(("0.0.0.0", serverPort))
serverSocket.listen(1)# server begin listining to TCP request


print ("The server is ready to receive")
while True:
    conn, addr = serverSocket.accept()
    sentence = conn.recv(2048).decode()
    print(addr)
    print(sentence)
    #spliting the request and taking the first line
    request = sentence.split("\n")
    #taking ip and address
    ip = addr[0]
    port = addr[1]

    #cases for diffrent requests
    if request[0].__contains__("GET /index.html HTTP/1.1") or request[0].__contains__("GET /main_in.html HTTP/1.1")or (request[0].__contains__("GET /en HTTP/1.1")or request[0].__contains__("GET / HTTP/1.1")):
        conn.send("HTTP/1.1 200 OK\r\n".encode())
        conn.send("Content-Type: text/html \r\n".encode())
        conn.send("\r\n".encode())
        f1 = open('main_en.html', "rb")
        conn.send(f1.read())
    elif request[0].__contains__("/ar HTTP/1.1"):
        conn.send("HTTP/1.1 200 OK\r\n".encode())
        conn.send("Content-Type: text/html \r\n".encode())
        conn.send("\r\n".encode())
        f1 =open('main_ar.html',"rb")
        conn.send(f1.read())
    elif request[0].__contains__("main_ar.html HTTP/1.1"):
        conn.send("HTTP/1.1 200 OK\r\n".encode())
        conn.send("Content-Type: text/html \r\n".encode())
        conn.send("\r\n".encode())
        f1= open('main_ar.html',"rb")
        conn.send(f1.read())
    elif request[0].__contains__("first.html HTTP/1.1"):
        conn.send("HTTP/1.1 200 OK\r\n".encode())
        conn.send("Content-Type: text/html \r\n".encode())
        conn.send("\r\n".encode())
        f1= open('first.html',"rb")
        conn.send(f1.read())
    elif request[0].__contains__("main_en.html HTTP/1.1"):
        conn.send("HTTP/1.1 200 OK\r\n".encode())
        conn.send("Content-Type: text/html \r\n".encode())
        conn.send("\r\n".encode())
        f1= open('main_en.html',"rb")
        conn.send(f1.read())

    elif request[0].__contains__("main_en.css HTTP/1.1"):
        conn.send("HTTP/1.1 200 OK\r\n".encode())
        conn.send("Content-Type: text/css \r\n".encode())
        conn.send("\r\n".encode())
        f1 = open("main_en.css","rb")
        conn.send(f1.read())
    elif request[0].__contains__("main_ar.css HTTP/1.1"):
        conn.send("HTTP/1.1 200 OK\r\n".encode())
        conn.send("Content-Type: text/css \r\n".encode())
        conn.send("\r\n".encode())
        f1 = open("main_ar.css","rb")
        conn.send(f1.read())
    elif request[0].__contains__("s.css HTTP/1.1"):
        conn.send("HTTP/1.1 200 OK\r\n".encode())
        conn.send("Content-Type: text/css \r\n".encode())
        conn.send("\r\n".encode())
        f1 = open("s.css","rb")
        conn.send(f1.read())
    elif request[0].__contains__("palestine.png HTTP/1.1"):
        conn.send("HTTP/1.1 200 OK\r\n".encode())
        conn.send("Content-Type: image/png \r\n".encode())
        conn.send("\r\n".encode())
        f1 = open("palestine.png","rb")
        conn.send(f1.read())
    elif request[0].__contains__("nature.png HTTP/1.1"):
        conn.send("HTTP/1.1 200 OK\r\n".encode())
        conn.send("Content-Type: image/png \r\n".encode())
        conn.send("\r\n".encode())
        f1 = open("nature.png","rb")
        conn.send(f1.read())
    elif request[0].__contains__("pal.jpeg HTTP/1.1"):
        conn.send("HTTP/1.1 200 OK\r\n".encode())
        conn.send("Content-Type: image/png \r\n".encode())
        conn.send("\r\n".encode())
        f1 = open("pal.jpeg","rb")
        conn.send(f1.read())
    elif request[0].__contains__("qais.jpg HTTP/1.1"):
        conn.send("HTTP/1.1 200 OK\r\n".encode())
        conn.send("Content-Type: image/png \r\n".encode())
        conn.send("\r\n".encode())
        f1 = open("qais.jpg", "rb")
        conn.send(f1.read())
    elif request[0].__contains__("dog.jpg HTTP/1.1"):
        conn.send("HTTP/1.1 200 OK\r\n".encode())
        conn.send("Content-Type: image/png \r\n".encode())
        conn.send("\r\n".encode())
        f1 = open("dog.jpg", "rb")
        conn.send(f1.read())
    elif request[0].__contains__("ghandy.jpg HTTP/1.1"):
        conn.send("HTTP/1.1 200 OK\r\n".encode())
        conn.send("Content-Type: image/png \r\n".encode())
        conn.send("\r\n".encode())
        f1 = open("ghandy.jpg", "rb")
        conn.send(f1.read())
    elif request[0].__contains__("kareem.jpg HTTP/1.1"):
        conn.send("HTTP/1.1 200 OK\r\n".encode())
        conn.send("Content-Type: image/png \r\n".encode())
        conn.send("\r\n".encode())
        f1 = open("kareem.jpg", "rb")
        conn.send(f1.read())
    elif request[0].__contains__("/cr HTTP/1.1"):
        conn.send("HTTP/1.1 307 Temporary Redirect\r\n".encode())
        conn.send("Location: https://www.cornell.edu/ \r\n".encode())
        conn.send("\r\n".encode())
    elif request[0].__contains__("/so HTTP/1.1"):
        conn.send("HTTP/1.1 307 Temporary Redirect\r\n".encode())
        conn.send("Location: https://stackoverflow.com/ \r\n".encode())
        conn.send("\r\n".encode())
    elif request[0].__contains__("/rt HTTP/1.1"):
        conn.send("HTTP/1.1 307 Temporary Redirect\r\n".encode())
        conn.send("Location: https://ritaj.birzeit.edu/ \r\n".encode())
        conn.send("\r\n".encode())
    else: # this handle error cases
        conn.send("HTTP/1.1 404 Not Found  \r\n".encode())
        # content type
        conn.send("Content-Type: text/html; charset=utf-8\r\n".encode())
        conn.send("\r\n".encode())
        # s contain the html page of the error 404
        s = "<html><head><title>Error 404</title><style type=\"text/css\">        h1{        font-size:4em;        text-align:center;        margin:0;        padding:0;        position:absolute;        top:50%;        left:50%;        transform:translateX(-50%);       }em{         font-size:3em;        text-align:left;        margin:0;        padding:0;        position:absolute;        top:0%;        left:50%;       transform:translateX(-50%); }   </style></head><body><font color=\"red\"><h1 >The file is not found</h1></font><strong>Kareem Qutob1211756</strong></p><p><strong>Qais Ayyash 1213205</strong></p><p><strong>Ghandy ghanem 1212386</strong></p><p><em>IP=" + str(
            ip) + "   Port=" + str(port) + "</em></p></body></html>\r\n"
        data = s.encode()
        conn.send(data)

    conn.close()#closing connections