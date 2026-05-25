from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import (
    Conv2D,
    MaxPooling2D,
    Flatten,
    Dense,
    Dropout,
    BatchNormalization
)

IMG_SIZE = 128
NUM_CLASSES = 4

def build_model():

    model = Sequential([

        Conv2D(
            32,
            (3,3),
            activation='relu',
            input_shape=(IMG_SIZE, IMG_SIZE, 3)
        ),

        BatchNormalization(),

        MaxPooling2D(2,2),

        Conv2D(
            64,
            (3,3),
            activation='relu'
        ),

        BatchNormalization(),

        MaxPooling2D(2,2),

        Conv2D(
            128,
            (3,3),
            activation='relu'
        ),

        BatchNormalization(),

        MaxPooling2D(2,2),

        Flatten(),

        Dense(128, activation='relu'),

        Dropout(0.5),

        Dense(NUM_CLASSES, activation='softmax')
    ])

    return model