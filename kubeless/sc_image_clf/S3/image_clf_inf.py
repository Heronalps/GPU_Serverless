from keras.applications.resnet50 import preprocess_input
from keras.preprocessing import image
import numpy as np

class_list = ["Birds", "Empty", "Fox", "Humans", "Rodents"]

def handler(event, context):
    path = event['path']
    img = image.load_img(path="../../data/SantaCruzIsland_Labeled_5Class/Empty/IMG_0047.JPG", target_size=(1920, 1080))
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)
    x = preprocess_input(x)

    layered_model.load_weights("../checkpoints/{0}_model_weights.h5".format("ResNet50"))
    y_prob = layered_model.predict(x)
    index = y_prob.argmax()
    print ("Predictde : {0}".format(class_list[index]) + " Probability : {0}".format(y_prob[0][index]))