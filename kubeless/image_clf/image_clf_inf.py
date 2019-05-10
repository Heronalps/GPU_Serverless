from keras.applications.resnet50 import preprocess_input
from keras.preprocessing import image
from keras.models import load_model
import numpy as np

class_list = ["Birds", "Empty", "Fox", "Humans", "Rodents"]

def handler(event, context):
    path = event['data']['path']
    img = image.load_img(path=path, target_size=(1920, 1080))
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)
    x = preprocess_input(x)

    trained_model = load_model('/racelab/checkpoints/resnet50_model.h5')
    
    y_prob = trained_model.predict(x)
    index = y_prob.argmax()
    return "Predictde : {0}  Probability : {1}".format(class_list[index], y_prob[0][index])

if __name__ == "__main__":
    handler({"data" : {"path" : "../../data/SantaCruzIsland_Validation_5Class/Birds/IMG_1304.JPG"}})