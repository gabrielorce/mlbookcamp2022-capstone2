# Originally from: https://github.com/gabrielorce/mlbookcamp-code/blob/master/chapter-08-serverless/convert.py
# Added locally so h5 model can be converted to tflite

import tensorflow as tf
from tensorflow import keras


model = keras.models.load_model('xception_v2_0_5_11_0.955.h5')


converter = tf.lite.TFLiteConverter.from_keras_model(model)

tflite_model = converter.convert()

with tf.io.gfile.GFile('electronics-components-v2.tflite', 'wb') as f:
    f.write(tflite_model)