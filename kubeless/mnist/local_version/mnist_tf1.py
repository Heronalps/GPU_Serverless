import tensorflow as tf
import time

from tensorflow.keras.backend import set_session

config = tf.ConfigProto(
    # gpu_options = tf.GPUOptions(per_process_gpu_memory_fraction=0.5),
    device_count={'GPU': 0},
    log_device_placement=False
)
set_session(tf.Session(config=config))

mnist = tf.keras.datasets.mnist

(x_train, y_train),(x_test, y_test) = mnist.load_data()
x_train, x_test = x_train / 255.0, x_test / 255.0

start_ts = time.time()

model = tf.keras.models.Sequential([
  tf.keras.layers.Flatten(input_shape=(28, 28)),
  tf.keras.layers.Dense(512, activation=tf.nn.relu),
  tf.keras.layers.Dropout(0.2),
  tf.keras.layers.Dense(10, activation=tf.nn.softmax)
])

EPOCHS = 5

model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

model.fit(x_train, y_train, epochs=EPOCHS)
model.evaluate(x_test, y_test, verbose=0)

print ("CNN takes {0} seconds training on {1} and testing on {2} images {3} epoches.".format(time.time() - start_ts,
                                                                                     len(x_train), len(x_test), EPOCHS))