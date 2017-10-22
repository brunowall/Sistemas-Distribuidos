import socket
import datetime

def main():
    nrequest = 0
    time = datetime.datetime.utcnow() # salva o tempo atual

    socket_udp = socket.socket(socket.AF_INET,socket.SOCK_DGRAM) #cria socket udp
    port  = raw_input("Digite a porta que o servidor ira rodar")

    socket_udp.bind(("localhost",int(port)))
    print("Escutando...")
    while True:
        msg, address = socket_udp.recvfrom(1024)
        nrequest +=1
        if(msg == "\REQNUM"):
            socket_udp.sendto("Numero de requisicoes: "+str(nrequest),address)
        elif(msg == "\UPTIME"):
            tempo_exec = datetime.datetime.utcnow() - time
            hours  = tempo_exec.seconds/3600
            minutes = (tempo_exec.seconds % 3600)/60
            socket_udp.sendto("Sistema rodando a: %d Dias %d Horas %d Minutos"% (tempo_exec.days,hours,minutes),address)

main()
