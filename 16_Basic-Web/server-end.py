"""
The previous codes don't have multi-thread to deal with 
requests from various clients. Thus, this server would not 
satisfy our needs. Our server needs to be able to receive and 
process quests from multi-users. 

So, let's design a server using multi-threads. This server will
send a picture to the client. 
"""

from socket import socket, SOCK_STREAM, AF_INET
from base64 import b64encode
from json import dumps
from threading import Thread 

def main():
    class FileTransferHandler(Thread):
        def __init__(self,cclient):
            super().__init__()
            self.cclient = cclient 

        def run(self):
            my_dict = {}
            my_dict['filename'] = 'dva.jpg'
            # Since JSON is a text instead of 100101010
            # we need to transfer it to binary 
            my_dict['filedata'] = data 
            # dumps() is used to transfer a dict into a json 
            json_str = dumps(my_dict)
            # send json string 
            self.cclient.send(json_str.encode('utf-8'))
            self.cclient.close()

    server = socket()
    server.bind(('10.186.14.251',5678))
    server.listen(512)
    print('server starts listening')
    with open('dva.jpg','rb') as f:
        data = b64encode(f.read()).decode('utf-8')
    while True:
        client,addr = server.accept()
        FileTransferHandler(client).start()

if __name__ == "__main__":
    main()