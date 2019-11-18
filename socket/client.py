'''
The data center client requests images from Raspberry Pi
'''
import socket, os, time, zipfile, re

size = 1024
port = 5005
folder = "/Users/michaelzhang/Downloads/image_buffer/"

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connected = False

while not connected:
    try:
        client_socket.connect((socket.gethostname(), port))
        print (f'port : {port}')
        print ("Connected successfully!")
        connected = True
    except ConnectionRefusedError as err:
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        port += 1
        print (f"Increment port : {port}")
        time.sleep(1)
    except OSError as e:
        print (e)
        break

time_stamp = time.time()

file_name = client_socket.recv(size).decode()
print (f'file_name : {file_name}')
zip_name = folder + file_name
with open(zip_name, 'wb+') as fp:
    while True:
        strng = client_socket.recv(size)
        if not strng:
            break
        fp.write(strng)

print ("Data Received successfully")

with zipfile.ZipFile(zip_name, 'r') as f:
    f.extractall(folder)

os.remove(zip_name)
client_socket.close()
print (f'The client received and extracted all images by {time.time() - time_stamp} seconds! ')
exit()