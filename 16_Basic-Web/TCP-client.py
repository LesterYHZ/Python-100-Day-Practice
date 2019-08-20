from socket import socket 

def main():
    # 1. default: IPv4 and TCP 
    client = socket() 
    # 2. Connect to server 
    client.connect(('10.186.14.251',6789))
    # 3. Receive data
    print(client.recv(1024).decode('utf-8'))
    client.close() 

if __name__ == "__main__":
    main()