from keras.applications.resnet50 import preprocess_input
from keras.preprocessing import image
from keras.models import load_model
import numpy as np
import time

class_list = ["Birds", "Empty", "Fox", "Humans", "Rodents"]
NUM_IMAGE = 1
PATH = "/racelab/data/SantaCruzIsland_Validation_5Class/Birds/IMG_1304.JPG"

def handler(event, context): 
    start = time.time()
    if isinstance(event['data'], dict) and "path" in event['data']:
        global PATH
        PATH = event['data']['path']

    if isinstance(event['data'], dict) and "num_image" in event['data']:
        global NUM_IMAGE
        print ("inside if - condition !!!")
        print ("num_image : ", int(event['data']['num_image']))
        NUM_IMAGE = int(event['data']['num_image'])
    
    img = image.load_img(path=PATH, target_size=(1920, 1080))
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)
    x = preprocess_input(x)

    trained_model = load_model('/racelab/checkpoints/resnet50_model.h5')
    
    for _ in range(NUM_IMAGE):
        y_prob = trained_model.predict(x)
        index = y_prob.argmax()
        print ("index : ", index)

    print ("Predicted : {0}  Probability : {1} Time: {2} for {3} images.".format(class_list[index], y_prob[0][index], (time.time() - start), NUM_IMAGE))
    return ("Predicted : {0}  Probability : {1} Time: {2} for {3} images.".format(class_list[index], y_prob[0][index], (time.time() - start), NUM_IMAGE))

if __name__ == "__main__":
    handler({"data" : {"path" : "/racelab/data/SantaCruzIsland_Validation_5Class/Birds/IMG_1304.JPG", "num_image" : 1}}, {})