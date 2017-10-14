import socket

def main():
    net = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    net.bind(("localhost",8000))

    while True:
        print("Escutando requisicao...")
        data, addr = net.recvfrom(1024) #receive 1024 bytes
        list = data.split(" ")
        net.sendto(str(calcula(list[0],list[1],list[2])),addr)
        print ("resultado enviado para: ",addr)
def calcula(num1,op,num2):
    if op == "+":
        return (float(num1)+float(num2))
    elif op == "-" :
        return (float(num1)-float(num2))
    elif op == "*":
        return (float(num1)*float(num2))
    elif op == "/":
        if(num2 != "0" ):
            return (float(num1)/float(num2))
        else: return "operacao invalida"

main()
