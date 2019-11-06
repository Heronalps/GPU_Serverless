import tensorflow as tf
import time
# import matplotlib.pyplot as plt

from keras.models import Sequential
from keras.layers import Dense, Conv2D, Dropout, Flatten, MaxPooling2D
from keras import backend
EPOCHS = 20

def handler(event, context):
    # backend.tensorflow_backend._get_available_gpus()
    start = time.time()

    # x is grayscale code [0 - 255]
    # y is the label of number [0 - 9]
    (x_train, y_train), (x_test, y_test) = tf.keras.datasets.mnist.load_data()

    image_index = 218
    # print (y_train[image_index])
    # plt.imshow(x_train[image_index], cmap="Greys")
    # plt.show()

    # print (x_train[image_index])
    # print (x_train.shape)

    x_train = x_train.reshape(x_train.shape[0], 28, 28, 1)
    x_test = x_test.reshape(x_test.shape[0], 28, 28, 1)
    input_shape = (28, 28, 1)

    x_train = x_train.astype('float32')
    x_test = x_test.astype('float32')

    # Normalize the image Grayscale RGB code to [0, 1]
    # This is required by neural network
    x_train /= 255
    x_test /= 255

    print ("x_train shape :", x_train.shape)
    print ("Number of image in x_train :", x_train.shape[0])
    print ("Number of image in x_test :", x_test.shape[0])

    model = Sequential()
    model.add(Conv2D(32, kernel_size = (3,3), input_shape = input_shape))
    model.add(MaxPooling2D(pool_size = (2,2)))
    model.add(Flatten())
    model.add(Dense(128, activation=tf.nn.relu))
    model.add(Dropout(0.2))
    model.add(Dense(10, activation=tf.nn.softmax))

    model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
    model.fit(x=x_train, y=y_train, epochs=EPOCHS, verbose=0)

    model.evaluate(x_test, y_test)

    # plt.imshow(x_test[image_index].reshape([28, 28]), cmap='Greys')
    # plt.show()
    pred = model.predict(x_test[image_index].reshape(1, 28, 28, 1))
    print (pred.argmax())

    print ("The total time used is {0} seconds".format(time.time() - start))

if __name__ == "__main__":
    handler({}, {})