import socket
import datetime
def server():
    time = datetime.datetime.utcnow()


    nrequest = 0
    ip  = "localhost"
    port  = raw_input("Digote a porta que o servidor ira rodar")
    server  = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

    server.bind((ip,int(port)))

    server.listen(1)
    print("Escutando...")
    while True:
        socket_cliente,address = server.accept();
        print("Conexao Aceita")
        while True:
            request = socket_cliente.recv(1024)
            nrequest +=1

            try:
                if(request == "\REQNUM"):
                    socket_cliente.send("Numero de requisicoes: "+str(nrequest))
                elif(request == "\UPTIME"):
                    tempo_exec = datetime.datetime.utcnow() - time
                    hours  = tempo_exec.seconds/3600
                    minutes = (tempo_exec.seconds % 3600)/60
                    socket_cliente.send("Sistema rodando a: %d Dias %d Horas %d Minutos"% (tempo_exec.days,hours,minutes))
                else:
                    socket_cliente.send("Bad Request!")
            except Exception as e:
                break ## caso a conexao seja encerrada volta a escutar conexao



    server.close
    socket_cliente.close;

server()
