import socket

def client():
    socket_client  = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    while True:
        host = raw_input("Digite o ip do host: ")
        port  = raw_input("Digite o numero de porta: ")
        command  = raw_input("Digite o comando")
        if(command=="/CLOSE"):
            socket_client.close()
            exit(0)
        host_tuple = (host,int(port))
        socket_client.sendto(command,host_tuple)
        data, addr = socket_client.recvfrom(1024)
        print(data)



client()
