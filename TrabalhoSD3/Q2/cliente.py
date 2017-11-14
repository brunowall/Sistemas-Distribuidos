import socket
import messages_pb2

def main():
    net = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    request = messages_pb2.Request()
    request.op =  messages_pb2.CALCULADORA
    net.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    net.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    net.sendto(request.SerializeToString(),("255.255.255.255",8000))

main()
