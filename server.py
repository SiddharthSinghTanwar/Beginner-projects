import socket
CHUNK = 65535# receive at most these bytes of data at once
port = 3000
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#create a socket object
#socket.socket(family, address)
#AF_NET : family of ipv4 ip address
#Sock_Dgram : UDP, Sock_stream:tcp

# some ip address that the server wil listen to when message comes
hostname = '127.0.0.1'#ip address of local machine, same for everyone

s.bind((hostname, port))
#bind the socket with host machine and on port 3000

print(f"server is live on{s.getsockname()}")

#run ths infinitely, till i stop manually
while True:
    #infinite loop
    data, clientAdd = s.recvfrom(CHUNK)
    message = data.decode('ascii')
    #data travels in byte
    print(f"the guy says{clientAdd}: {message}")
    message_send = input('Reply: ')
    data = message_send.encode('ascii')
    #send data to the ip address that sent the data
    s.sendto(data, clientAdd)