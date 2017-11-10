import socket
import message_pb2
from decimal import Decimal

def main():
    net = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

    while True:
        operation = message_pb2.Request()
        operation.n1 = float(raw_input("Digite o primeiro numero"))
        op = raw_input("digite a operacao")
        operation.n2 = float(raw_input("Digite o segundo numero"))
        resposta = message_pb2.Reply()
        if op == "+":
            operation.op=message_pb2.Request.SOM
        elif op == "-" :
            operation.op=message_pb2.Request.SUB
        elif op == "*":
            operation.op=message_pb2.Request.MUL
        elif op == "/":
            operation.op=message_pb2.Request.DIV

        net.sendto(operation.SerializeToString(),("localhost",8000))
        data, add = net.recvfrom(1024)
        resposta.ParseFromString(data)
        print (resposta.res);

main()
