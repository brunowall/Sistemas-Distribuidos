import socket
import messages_pb2
import threading
import message_pb2
def main():
    ip_service = "" # porta em que o servico esta rodando
    port_service = 8050
    desc = threading.Thread(target=descoberta,args=[ip_service,port_service])
    net = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    net.bind((ip_service,port_service))
    desc.start()
    calculadora(net)

def descoberta(ip_servico,porta_servico):
    net = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # socket recebe as solicitacoes de descoberta
    net.bind(("",8000))
    request = messages_pb2.Request()
    response  = messages_pb2.Reply()
    while True:
        data, ip = net.recvfrom(2048)
        request.ParseFromString(data)
        if request.op ==  messages_pb2.CALCULADORA:
            response.ip = ip_servico
            response.port= porta_servico
            net.sendto(response.SerializeToString(),ip)

def calculadora(net):

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
