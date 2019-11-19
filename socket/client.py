'''
The data center client requests images from Raspberry Pi
'''
import socket, os, time, zipfile, re
from pathlib import Path

server_ip = '127.0.0.1'
size = 1024
port = 5005
folder = Path.home() / "GPU_Serverless/image_buffer/"


client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connected = False

while not connected:
    try:
        client_socket.connect((server_ip, port))
        print ('port : {0}'.format(port))
        print ("Connected successfully!")
        connected = True
    except ConnectionRefusedError as err:
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        port += 1
        print ("Increment port : {0}".format(port))
        time.sleep(1)
    except OSError as e:
        print (e)
        break

time_stamp = time.time()

file_name = client_socket.recv(size).decode()
print ('file_name : {}'.format(file_name))
zip_name = str(folder) + '/' + file_name
with open(zip_name, 'wb+') as fp:
    while True:
        strng = client_socket.recv(size)
        if not strng:
            break
        fp.write(strng)

print ("Data Received successfully")

with zipfile.ZipFile(zip_name, 'r') as f:
    f.extractall(folder)
print ("zip_name : ", zip_name)
os.remove(zip_name)
client_socket.close()
print ('The client received and extracted all images by {0} seconds! '.format(time.time() - time_stamp))
exit()