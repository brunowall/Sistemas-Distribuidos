import socket
import message_pb2
def main():
    net = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    net.bind(("localhost",8000))

    while True:
        print("Escutando requisicao...")
        operation = message_pb2.Request()
        resposta = message_pb2.Reply()
        data, addr = net.recvfrom(1024) #receive 1024 bytes
        operation.ParseFromString(data)
        resposta.res = calcula(operation.n1,operation.op,operation.n2)
        net.sendto(resposta.SerializeToString(),addr)
        print ("resultado enviado para: ",addr)

def calcula(num1,op,num2):
        if op == message_pb2.Request.SOM:
            return num1+num2
        elif op == message_pb2.Request.SUB :
            return num1-num2
        elif op == message_pb2.Request.MUL:
            return num1*num2
        elif op == message_pb2.Request.DIV:
            return num1/num2


main()
