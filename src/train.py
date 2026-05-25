from tensorflow.keras.callbacks import (
    EarlyStopping,
    ModelCheckpoint
)

from model import build_model
from preprocess import create_generators

BASE_PATH = "data/raw/AugmentedAlzheimerDataset"

model = build_model()

model.compile(
    optimizer='adam',
    loss='categorical_crossentropy',
    metrics=['accuracy']
)

train_generator, val_generator = create_generators(BASE_PATH)

callbacks = [

    EarlyStopping(
        patience=5,
        restore_best_weights=True
    ),

    ModelCheckpoint(
        "models/best_cnn_model.h5",
        save_best_only=True
    )
]

history = model.fit(
    train_generator,
    validation_data=val_generator,
    epochs=25,
    callbacks=callbacks
)

model.save("models/final_model.h5")