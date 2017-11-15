import socket
import messages_pb2

def main():
    net = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    request = messages_pb2.Request()
    response = messages_pb2.Reply()
    request.op =  messages_pb2.CALCULADORA
    net.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    net.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    net.sendto(request.SerializeToString(),("255.255.255.255",8000))
    data, ip = net.recvfrom(2048)
    response.ParseFromString(data)
    print("Calculadora encontrada ")
    net_tcp  = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    net_tcp.connect((response.ip,response.port))
    
main()
