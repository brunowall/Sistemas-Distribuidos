import socket
import threading

def main():
  tcp = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
  tcp.bind(("localhost",8000))
  tcp.listen(1)
  con,addr = tcp.accept()

  t1 = threading.Thread(target=listen_print,args=[con])
  t1.start()

  while True:
     mensagem = raw_input()
     t2 = threading.Thread(target=con.send,args=[mensagem])
     t2.start()


def listen_print(socket):
    while True:
      msg = socket.recv(2048)
      print ("Participante 2: "+msg)

main()
