import socket
import messages_pb2
def main():
    net = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    net.bind(("",8000))
    request = messages_pb2.Request()
    data, ip = net.recvfrom(2048)

    print (request.SerializeToString().)
