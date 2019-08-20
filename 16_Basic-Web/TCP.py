"""
In Python we can use TCP by creating a
socket object and let the type be 
SOCK_STREAM

In this case, let's build a server
to show date and time
"""

from socket import socket, SOCK_STREAM,AF_INET
from datetime import datetime 

def main():
    # 1. create socket object
    # family: AF_INET - IPv4
    #         AF_INET6 - IPv6
    # type: SOCK_STREAM - TCP
    #       SOCK_DGRAM - UDP
    #       SOCK_RAW - original
    server = socket(family = AF_INET, type = SOCK_STREAM)
    # 2. connect IP address and port
    server.bind(('10.186.14.251',6789))
    # 3. listen client connecting to server
    server.listen(512) 
    print('Server starts listening')
    while True:
        # 4. Use accept to monitor if client is connected to server
        client, addr = server.accept()
        print(str(addr) + 'Connected to Server')
        # 5. Send data
        client.send(str(datetime.now()).encode('utf-8'))
        # 6. Disconnect
        client.close()

if __name__ == "__main__":
    main()

""" telnet 10.186.14.251 6789 """ 