import socket 

#AF_INT : IP version 4 ,address family
#AF_INT6 : IP version 6 ,address family
#SOCK_STREAM: TCP connection
#SOCK_DGRAM: UDP connection 

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

ip_address = '127.0.0.1'
port = 8000

server.bind((ip_address,port))
server.listen()

clients = []

print("Server is running......")