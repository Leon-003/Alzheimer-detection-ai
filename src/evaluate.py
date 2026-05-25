import matplotlib.pyplot as plt
from sklearn.metrics import (
    classification_report,
    confusion_matrix
)

def evaluate_model(
    y_true,
    y_pred,
    class_names
):

    print(
        classification_report(
            y_true,
            y_pred,
            target_names=class_names
        )
    )

    cm = confusion_matrix(y_true, y_pred)

    plt.figure(figsize=(8,6))

    plt.imshow(cm, cmap='Blues')

    plt.title("Confusion Matrix")

    plt.colorbar()

    plt.savefig(
        "outputs/confusion_matrix.png"
    )