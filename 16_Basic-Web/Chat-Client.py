from socket import socket 
from threading import Thread 

def main():
    class RefreshScreenThread(Thread):
        def __init__(self,client):
            super().__init__()
            self._client = client 

        def run(self):
            while running:
                data = self._client.recv(1024)
                print(data.decode('utf-8'))

    nickname = input('Input Nickname: ')
    myclient = socket()
    myclient.connect(('10.186.14.251',56489))
    running = True 
    RefreshScreenThread(myclient).start()
    while running:
        content = input()
        if content == 'bye bye':
            myclient.send(content.encode('utf-8'))
            running = False
        else:
            msg = nickname+': '+content 
            myclient.send(msg.encode('utf-8'))

if __name__ == "__main__":
    main()