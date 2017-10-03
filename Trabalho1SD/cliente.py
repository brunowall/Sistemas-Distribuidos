import socket

def cliente():
        ip =  raw_input("Digite o ip do servidor");
        port  = raw_input("Digite a porta do servidor")
        connection = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        print("Conectando ao servidor...")
        connection.connect((ip,int(port)))
        print ("Conectado!")
        while True:
            command = raw_input("Digite um comando")
            if(command=="/CLOSE"):
                print("Encerrando o cliente...")
                connection.close()
                exit(0)
            connection.send(command)
            print(connection.recv(2048))
        connection.close()

cliente()
