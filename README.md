# 🧠 Alzheimer Detection AI System

An AI-powered deep learning system for Alzheimer’s disease classification using MRI brain images.

This project utilizes a Convolutional Neural Network (CNN) to classify different stages of Alzheimer’s disease from MRI scans and provides a user-friendly Streamlit web application for real-time prediction.

---

# 📌 Project Overview

Alzheimer’s disease is a progressive neurological disorder that affects memory, cognition, and behavior. Early diagnosis is essential for effective treatment planning and patient care.

This project applies Deep Learning and Computer Vision techniques to classify MRI brain scans into multiple Alzheimer disease stages.

The system includes:

- CNN-based MRI image classification
- MRI preprocessing pipeline
- Real-time prediction interface
- Training and evaluation workflow
- Streamlit deployment-ready application
- Modular AI engineering structure

---

# 🚀 Features

- MRI image classification
- CNN-based deep learning model
- Real-time prediction system
- Streamlit web application
- Confidence score generation
- Training visualization
- Clean modular architecture
- Deployment-ready project structure

---

# 🗂️ Dataset

### Dataset Used
- Alzheimer MRI Dataset

### Classes
The dataset contains MRI images categorized into:

- Mild Demented
- Moderate Demented
- Non Demented
- Very Mild Demented

---

# 🛠️ Tech Stack

## Programming Language
- Python

## Deep Learning Frameworks
- TensorFlow
- Keras

## Data Processing
- NumPy
- Matplotlib

## Deployment & UI
- Streamlit

---

# 📁 Project Structure

```bash
alzheimer-detection-ai/
│
├── app/
│   ├── main.py
│   ├── inference.py
│   └── utils.py
│
├── src/
│   ├── model.py
│   ├── preprocess.py
│   ├── dataset.py
│   ├── train.py
│   └── evaluate.py
│
├── notebooks/
│   └── experimentation.ipynb
│
├── models/
│   └── alzheimer_cnn.h5
│
├── outputs/
│   ├── confusion_matrix.png
│   ├── training_curve.png
│   └── sample_predictions/
│
├── data/
│   ├── raw/
│   └── processed/
│
├── requirements.txt
├── README.md
├── .gitignore
└── Dockerfile
```

---

# 🧠 Model Architecture

The project uses a Convolutional Neural Network (CNN) for MRI image classification.

### Architecture Components

- Convolution Layers
- MaxPooling Layers
- Batch Normalization
- Dropout Regularization
- Dense Fully Connected Layers
- Softmax Output Layer

### CNN Workflow

```text
MRI Image
   ↓
Preprocessing
   ↓
CNN Feature Extraction
   ↓
Dense Classification Layers
   ↓
Alzheimer Stage Prediction
```

---

# ⚙️ Training Pipeline

The model training workflow includes:

- Data preprocessing
- Image normalization
- Data augmentation
- Train-validation split
- CNN training
- Early stopping
- Model checkpointing
- Performance evaluation

---

# 📊 Evaluation Metrics

The model performance is evaluated using:

- Accuracy
- Validation Accuracy
- Loss Curve
- Confusion Matrix
- Classification Report

---

# 🌐 Streamlit Web Application

The project includes a Streamlit-based web application where users can:

- Upload MRI brain images
- View Alzheimer stage predictions
- See confidence scores
- Test the trained model in real time

---

# ⚡ Installation

## 1️⃣ Clone Repository

```bash
git clone https://github.com/Leon-003/alzheimer-detection-ai.git
```

---

## 2️⃣ Navigate Into Project

```bash
cd alzheimer-detection-ai
```

---

## 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 🏋️ Run Model Training

```bash
python src/train.py
```

---

# ▶️ Run Streamlit Application

```bash
streamlit run app/main.py
```

---

# 🔮 Future Improvements

Future improvements for this project include:

- Grad-CAM explainability visualization
- FastAPI backend deployment
- Docker containerization
- Cloud deployment
- Transfer learning implementation
- Larger MRI datasets
- Model optimization

---

# 🔬 Research Motivation

This project was developed as part of research work focused on applying Artificial Intelligence in healthcare and medical image analysis.

The primary goal is to contribute toward intelligent healthcare systems capable of assisting medical professionals in early disease diagnosis and clinical decision-making.

---

# 👨‍💻 Author

## Abul Khayer Leon

AI/ML Engineer | Medical AI Researcher | Deep Learning Enthusiast

### Research Interests
- Medical AI
- Deep Learning
- NLP
- Computer Vision
- Healthcare AI

---

# 📜 License

This project is intended for educational and research purposes.
