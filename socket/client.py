'''
The data center client requests images from Raspberry Pi
'''
import socket, os, time

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((socket.gethostname(), 5005))

size = 1024
folder = "/Users/michaelzhang/Downloads/image_buffer/"


fname = "image.jpg"
path = folder + fname
fp = open(path, 'wb+')
while True:
    strng = client_socket.recv(size)
    if not strng:
        break
    fp.write(strng)

fp.close()
print ("Data Received successfully")
exit()