# 서버 사이드
from socket import *
port = 5000


def send(sock):
    sendData = input(">>>")
    sock.send(sendData.encode("utf-8"))

def recive(sock):
    recvData = sock.recv(1024)
    print("클라이언트 메시지 :" , recvData.decode("utf-8"))

severSock = socket(AF_INET,SOCK_STREAM)
severSock.bind(('',port))
severSock.listen(1)

print("%d번 포트로 접속 대기중"%port)

connectionSock , addr = severSock.accept()

print(str(addr),"에 접속 되었습니다.")

while True:
    send(connectionSock)
    recive(connectionSock)