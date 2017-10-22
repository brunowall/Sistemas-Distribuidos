import socket
import threading
import time

def main():
  socket_tcp = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
  socket_tcp.connect(("localhost",8000));
  t1 = threading.Thread(target=listen_print,args=[socket_tcp])
  t1.start()

  while True:
     mensagem = raw_input()
     try:
         t2 = threading.Thread(target=socket_tcp.send,args=[mensagem])
         t2.start()
     except Exception as exp:
        pass

def listen_print(socket):
    while True:
        msg = socket.recv(2048)
        if msg == "/TIME":
            tempo = time.strftime("%d/%M/%y %H:%M")
            t2 = threading.Thread(target=socket.send,args=[tempo])
            t2.start()
        elif len(msg) == 0:
            pass
        else:
            print ("Participante 1: "+msg)

main()
