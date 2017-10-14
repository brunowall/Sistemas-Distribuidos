import socket

def main():
    net = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

    while True:
        expression = raw_input("Digite a expressao a ser calculada no formato: num1[espaco]operacao[espaco]num2")
        net.sendto(expression,("localhost",8000))
        data, add = net.recvfrom(1024)
        print (data);

main()
