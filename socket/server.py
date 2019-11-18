'''
The Raspberry Pi that sends batch of images to data center
'''
import os, sys, time, socket, zipfile
'''
Constants
'''
port = 5005
size = 1024
folder = '/Users/michaelzhang/Downloads/Github/GPU_Serverless/data/SantaCruzIsland_Labeled_5Class/Birds/test_image/'

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((socket.gethostname(), port))
server_socket.listen(5)

client_socket, address = server_socket.accept()
print ("Conencted to - ",address,"\n")

while True:
    files = os.listdir(folder)
    images = [img for img in files if img.endswith('.JPG')]
    print (f'images : {images}')
    # Send all .jpg files in the folder from client to server
    for img in images:
        print (f'image : {img}')
        
        file_name = open(folder + img,'rb')
        while True:
            strng = file_name.readline(size)
            if not strng:
                break
            client_socket.send(strng)
        file_name.close()
        print (f'{img} is sent successfully !')
    
    print ("All data is sent successfully!")
    exit()