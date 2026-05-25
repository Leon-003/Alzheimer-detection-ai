import tensorflow as tf
import numpy as np

model = tf.keras.models.load_model(
    "models/final_model.h5"
)

def predict(image):

    image = image / 255.0

    image = np.expand_dims(image, axis=0)

    prediction = model.predict(image)

    predicted_class = np.argmax(prediction)

    return predicted_class