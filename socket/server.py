'''
The Raspberry Pi that sends batch of images to data center
'''
import os, sys, time, socket, zipfile

# Constants
port = 5005
size = 1024
folder = '/Users/michaelzhang/Downloads/Github/GPU_Serverless/data/SantaCruzIsland_Labeled_5Class/Birds/test_image/'
zip_name = 'images.zip'
connected = False

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

while not connected:
    try:
        server_socket.bind((socket.gethostname(), port))
        connected = True
        print ('port : {0}'.format(port))
    except:
        port += 1
server_socket.listen(5)

client_socket, address = server_socket.accept()
print ("Conencted to - ",address,"\n")

time_stamp = time.time()
while True:
    files = os.listdir(folder)
    images = [img for img in files if img.endswith('.JPG')]
    print ('images : {0}'.format(images))
    # Send all .jpg files in the folder from server to client
    with zipfile.ZipFile(zip_name, 'w') as fp:
        for img in images:
            print ('image : {0}'.format(img))
            # Second arg is to specifiy the directory in zip file
            fp.write(folder + img, "images/" + img)
            print ('{0} is zipped successfully !'.format(img))
    
    client_socket.send(zip_name.encode())

    with open(zip_name, 'rb') as f:
        l = f.read()
    
    client_socket.sendall(l)
    os.remove(zip_name)
    
    print ("All data is sent successfully!")
    server_socket.close()
    print ('The server transfers {0} images by {1} seconds! '.format(len(images), time.time() - time_stamp))
    exit()