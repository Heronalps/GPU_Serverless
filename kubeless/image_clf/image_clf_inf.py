from keras.applications.resnet50 import preprocess_input
from keras.preprocessing import image
from keras.models import load_model
import numpy as np
import time

class_list = ["Birds", "Empty", "Fox", "Humans", "Rodents"]

def handler(event, context):
    start = time.time()
    if 'data' in event and 'path' in event['data']:
        path = event['data']['path']
    else:
        path = "/racelab/SantaCruzIsland_Validation_5Class/Birds/IMG_1304.JPG"
    img = image.load_img(path=path, target_size=(1920, 1080))
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)
    x = preprocess_input(x)

    trained_model = load_model('/racelab/checkpoints/resnet50_model.h5')
    
    y_prob = trained_model.predict(x)
    index = y_prob.argmax()

    return "Predicted : {0}  Probability : {1} Time: {2}".format(class_list[index], 
                                                                 y_prob[0][index], 
                                                                 (time.time() - start))

if __name__ == "__main__":
    handler({"data" : {"path" : "/racelab/SantaCruzIsland_Validation_5Class/Birds/IMG_1304.JPG"}}, {})