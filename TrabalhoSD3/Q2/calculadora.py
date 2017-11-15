import socket
import messages_pb2
import threading

def main():
    ip_service = "" # porta em que o servico esta rodando
    port_service = 8010
    desc = threading.Thread(target=descoberta,args=[ip_service,port_service])
    desc.start()

    net_tcp = socket.socket(socket.AF_INET,socket.SOCK_STREAM) # esse socket recebe as operacoes da calculadora
    net_tcp.bind((ip_service,port_service))
    net_tcp.listen(5)
    con,addr =  net_tcp.accept()
    print("Connectado a um cliente")

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
main()
