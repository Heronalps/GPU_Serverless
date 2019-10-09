from keras.applications.resnet50 import ResNet50, preprocess_input, decode_predictions
from keras.applications.nasnet import NASNetMobile
from keras.preprocessing import image
from keras.utils import multi_gpu_model
from keras.models import Sequential, Model
from keras.layers import Dense, Activation, Flatten, Dropout, GlobalAveragePooling2D
from keras import backend as K
from keras.optimizers import SGD, Adam
from keras.callbacks import ModelCheckpoint
from keras.models import load_model
# from matplotlib import pyplot as plt
from tensorflow.python.client import device_lib
from PIL import Image, ImageFile
ImageFile.LOAD_TRUNCATED_IMAGES = True
import numpy as np
import time, os

# from keras.backend.tensorflow_backend import set_session
# import tensorflow as tf
# config = tf.ConfigProto()
# config.gpu_options.allow_growth = True  # dynamically grow the memory used on the GPU
# config.log_device_placement = True  # to log device placement (on which device the operation ran)

TRAIN_DIR = "../../../data/SantaCruzIsland_Labeled_5Class"
VALID_DIR = "../../../data/SantaCruzIsland_Validation_5Class"
MODEL_DIR = "../../../checkpoints/resnet50_model.h5"

NUM_EPOCHS = 10
WIDTH = 1920
HEIGHT = 1080
NUM_TRAIN_IMAGES_PER_EPOCH = 100
NUM_VALID_IMAGES_PER_EPOCH = 10

NUM_BIRDS = 127
NUM_EMPTY = 250
NUM_FOX = 11
NUM_HUMANS = 32
NUM_RODENTS = 251

CLASS_LIST = ["Birds", "Empty", "Fox", "Humans", "Rodents"]
FC_LAYERS = [1024, 1024]
DROPOUT = 0.5

def handler(event, context):
    
    if isinstance(event['data'], dict) and "img_per_epoch" in event['data']:
        global NUM_TRAIN_IMAGES_PER_EPOCH
        NUM_TRAIN_IMAGES_PER_EPOCH = int(event['data']['img_per_epoch'])

    if isinstance(event['data'], dict) and "num_epoch" in event['data']:
        global NUM_EPOCHS
        NUM_EPOCHS = int(event['data']['num_epoch'])

    total_num = [NUM_BIRDS, NUM_EMPTY, NUM_FOX, NUM_HUMANS, NUM_RODENTS]
    reciprocal = [1/x for x in total_num]
    class_weights = [ x / sum(reciprocal) for x in reciprocal]
    # print (class_weights)

    # Parallel with multiple GPUs
    available_devices = device_lib.list_local_devices()
    NUM_GPU = len([x for x in available_devices if x.device_type == 'GPU'])

    # Increase BATCH_SIZE based on number of GPUs to harness the quasi-linear speedup of multiple GPUS
    BATCH_SIZE = 8 * NUM_GPU if NUM_GPU > 0 else 8


    # The total size of training dataset
    total_train_size = NUM_TRAIN_IMAGES_PER_EPOCH * NUM_EPOCHS

    train_datagen = image.ImageDataGenerator(preprocessing_function=preprocess_input, rotation_range=90, \
                                             horizontal_flip=True, vertical_flip=True)
    train_generator = train_datagen.flow_from_directory(TRAIN_DIR, target_size=(WIDTH, HEIGHT), \
                                                        batch_size = BATCH_SIZE)

    valid_datagen = image.ImageDataGenerator(preprocessing_function=preprocess_input, rotation_range=90, \
                                             horizontal_flip=True, vertical_flip=True)
    valid_generator = valid_datagen.flow_from_directory(VALID_DIR, target_size=(WIDTH, HEIGHT), \
                                                        batch_size = BATCH_SIZE)

    resnet50_model = ResNet50(input_shape=(WIDTH, HEIGHT, 3), weights='imagenet', include_top=False)
    
    if NUM_GPU > 1:
        raw_model = multi_gpu_model(resnet50_model, gpus=NUM_GPU)
    else:
        raw_model = resnet50_model

    # Build layered model
    layered_model = build_model(raw_model, dropout=DROPOUT, fc_layers=FC_LAYERS, num_classes=len(CLASS_LIST))

    start = time.time()

    history, trained_model = train_model(layered_model, train_generator, valid_generator, class_weights, BATCH_SIZE)

    # plot_training(history)

    trained_model.save(MODEL_DIR)

    print ("The total time of training {0} images is {1} seconds".format(total_train_size, \
                                                                         time.time() - start))

    return "The total time of training {0} images is {1} seconds".format(total_train_size, \
                                                                         time.time() - start)


def build_model(base_model, dropout, fc_layers, num_classes):

    # first: train only the top layers (which were randomly initialized)
    # i.e. freeze all convolutional InceptionV3 layers
    for layer in base_model.layers:
        layer.trainable = False
    
    # add a global spatial average pooling layer
    x = base_model.output
    x = GlobalAveragePooling2D()(x)

    # let's add fully-connected layers
    # Every FC layer has a dropout probability
    for fc in fc_layers:
        x = Dense(fc, activation='relu')(x)
        x = Dropout(dropout)(x)

    # and a logistic layer -- let's say we have 200 classes
    predictions = Dense(num_classes, activation='softmax')(x)
    
    # this is the model we will train
    model = Model(inputs=base_model.input, outputs=predictions)    
    
    return model

def train_model(model, train_data_gen, valid_data_gen, class_weight, batch_size):

    # create adam optimizer with learning rate
    adam = Adam(lr=0.00001)

    # compile the model (should be done *after* setting layers to non-trainable)
    model.compile(optimizer=adam, loss='categorical_crossentropy', metrics=['accuracy'])
    
    checkpoint = ModelCheckpoint(MODEL_DIR, monitor=["acc"], verbose=1, mode='max')
    
    history = model.fit_generator(generator=train_data_gen, epochs = NUM_EPOCHS, workers = 8, verbose=2, \
                                  steps_per_epoch=NUM_TRAIN_IMAGES_PER_EPOCH // batch_size, \
                                  shuffle=True, callbacks=[checkpoint], validation_data=valid_data_gen, \
                                  validation_steps = NUM_VALID_IMAGES_PER_EPOCH // batch_size, class_weight = class_weight)

    return history, model


# def plot_training(history):
#     acc = history.history['acc']
#     val_acc = history.history['val_acc']
#     loss = history.history['loss']
#     val_loss = history.history['val_loss']
#     epochs = range(len(acc))
    
#     plt.plot(epochs, acc, 'b.')
#     plt.plot(epochs, val_acc, 'r-')
#     plt.title('Training and validation accuracy')

#     plt.figure()
#     plt.plot(epochs, loss, 'b.')
#     plt.plot(epochs, val_loss, 'r-')
#     plt.title('Training and validation loss')
#     plt.show()
    
#     plt.savefig('/imageclf/charts/training_history.png')

if __name__ == "__main__":
    handler({"data" : {"img_per_epoch" : "10", "num_epoch": "10"}}, {})