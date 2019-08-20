from socket import socket 
from json import loads 
from base64 import b64decode 

def main():
    client = socket() 
    client.connect(('10.186.14.251',5678))
    in_data = bytes()
    # Everytime client receive 1024 bytes data
    data = client.recv(1024)
    while data:
        # combine the data client received every time
        in_data += data
        data = client.recv(1024) 
    # transfer receiveds bytes data to json string then dict
    my_dict = loads(in_data.decode('utf-8'))
    filename = my_dict['filename']
    filedata = my_dict['filedata'].encode('utf-8')
    with open('client_'+filename,'wb') as f:
        f.write(b64decode(filedata))
    print('image saved')

if __name__ == "__main__":
    main()