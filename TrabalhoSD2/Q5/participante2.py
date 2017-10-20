import socket
import threading

def main():
  socket_tcp = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
  socket_tcp.connect(("localhost",8000));
  
  t1 = threading.Thread(target=listen_print,args=[socket_tcp])
  t1.start()

  while True:
    mensagem = raw_input()
    socket_tcp.send(mensagem)

def listen_print(socket):
    while True:
         msg = socket.recv(2048)
         print ("Participante 1: "+msg)

main()
