import socket
import messages_pb2
import message_pb2
def main():
    net = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    request = messages_pb2.Request()
    response = messages_pb2.Reply()
    net.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    net.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

    flag = True
    while flag:
        op = int(raw_input("Digite 0 para impressao, 1  Calculadora, 2 Som, 3 projetor"))
        request.op = op
        net.sendto(request.SerializeToString(),("255.255.255.255",8000))
        net.settimeout(4) # seta o tempo de timeout para 4 segundos
        try:
            data, ip = net.recvfrom(2048)
            response.ParseFromString(data)
            flag = False # para o laco se encontrar o dispositivo
        except:
            print("Dispositivos nao encontrado")
            continue

    print("Encontrado!")
    tupla = (response.ip,response.port)

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

        net.sendto(operation.SerializeToString(),tupla)
        data, add = net.recvfrom(1024)
        resposta.ParseFromString(data)
        print (resposta.res);

main()
