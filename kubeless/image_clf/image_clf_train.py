from keras.applications.resnet50 import ResNet50, preprocess_input, decode_predictions
from keras.applications.nasnet import NASNetMobile
from keras.preprocessing import image
from keras.models import Sequential, Model
from keras.layers import Dense, Activation, Flatten, Dropout, GlobalAveragePooling2D
from keras import backend as K
from keras.optimizers import SGD, Adam
from keras.callbacks import ModelCheckpoint
from keras.models import load_model
# from matplotlib import pyplot as plt
from PIL import Image, ImageFile
ImageFile.LOAD_TRUNCATED_IMAGES = True
import numpy as np
import time

# from keras.backend.tensorflow_backend import set_session
# import tensorflow as tf
# config = tf.ConfigProto()
# config.gpu_options.allow_growth = True  # dynamically grow the memory used on the GPU
# config.log_device_placement = True  # to log device placement (on which device the operation ran)

TRAIN_DIR = "/racelab/SantaCruzIsland_Labeled_5Class"
VALID_DIR = "/racelab/SantaCruzIsland_Validation_5Class"
MODEL_DIR = "/racelab/checkpoints/resnet50_model.h5"
BATCH_SIZE = 8
NUM_EPOCHS = 10
WIDTH = 1920
HEIGHT = 1080
num_train_images = 100
num_valid_images = 10

num_birds = 127
num_empty = 249
num_fox = 11
num_humans = 32
num_rodents = 251

class_list = ["Birds", "Empty", "Fox", "Humans", "Rodents"]
FC_LAYERS = [1024, 1024]
dropout = 0.5

def handler(event, context):
    start = time.time()

    total_num = [num_birds, num_empty, num_fox, num_humans, num_rodents]
    reciprocal = [1/x for x in total_num]
    class_weights = [ x / sum(reciprocal) for x in reciprocal]
    # print (class_weights)

    # The total size of training dataset
    total_train_size = num_train_images * NUM_EPOCHS

    train_datagen = image.ImageDataGenerator(preprocessing_function=preprocess_input, rotation_range=90, \
                                             horizontal_flip=True, vertical_flip=True)
    train_generator = train_datagen.flow_from_directory(TRAIN_DIR, target_size=(WIDTH, HEIGHT), \
                                                        batch_size = BATCH_SIZE)

    valid_datagen = image.ImageDataGenerator(preprocessing_function=preprocess_input, rotation_range=90, \
                                             horizontal_flip=True, vertical_flip=True)
    valid_generator = valid_datagen.flow_from_directory(VALID_DIR, target_size=(WIDTH, HEIGHT), \
                                                        batch_size = BATCH_SIZE)

    resnet50_model = ResNet50(input_shape=(WIDTH, HEIGHT, 3), weights='imagenet', include_top=False)
    layered_model = build_model(resnet50_model, dropout=dropout, fc_layers=FC_LAYERS, num_classes=len(class_list))

    history, trained_model = train_model(layered_model, "ResNet50", train_generator, valid_generator, class_weights)

    # plot_training(history)

    trained_model.save(MODEL_DIR)

    return "The total time of training is {0} seconds".format(time.time() - start)


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

def train_model(model, model_name, train_data_gen, valid_data_gen, class_weight):

    # create adam optimizer with learning rate
    adam = Adam(lr=0.00001)

    # compile the model (should be done *after* setting layers to non-trainable)
    model.compile(optimizer=adam, loss='categorical_crossentropy', metrics=['accuracy'])
    
    # TODO - Save to ceph
    checkpoint = ModelCheckpoint("/racelab/checkpoints/{0}_model_weights.h5".format(model_name), monitor=["acc"], verbose=1, mode='max')
    
    history = model.fit_generator(generator=train_data_gen, epochs = NUM_EPOCHS, workers = 8, verbose=2, \
                                  steps_per_epoch=num_train_images // BATCH_SIZE, \
                                  shuffle=True, callbacks=[checkpoint], validation_data=valid_data_gen, \
                                  validation_steps = num_valid_images // BATCH_SIZE, class_weight = class_weight)

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
    handler({}, {})