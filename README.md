# Alzheimer Detection AI System

An AI-powered deep learning system for Alzheimer’s disease classification using MRI brain images.

This project uses a Convolutional Neural Network (CNN) to classify Alzheimer’s disease stages from MRI scans and provides a user-friendly Streamlit web interface for real-time prediction.

---

# Project Overview

Alzheimer’s disease is a progressive neurological disorder that affects memory and cognitive function. Early diagnosis plays an important role in treatment and patient care.

This project applies Deep Learning and Computer Vision techniques to classify MRI brain scans into different Alzheimer stages.

The system includes:
- CNN-based image classification
- MRI preprocessing pipeline
- Real-time prediction interface
- Training and evaluation workflow
- Streamlit deployment-ready application

---

# Features

- MRI image classification
- CNN-based deep learning model
- Streamlit web application
- Real-time prediction
- Confidence score generation
- Modular project structure
- Training visualization
- Clean engineering workflow

---

# Dataset

Dataset used:
- Alzheimer MRI Dataset

The dataset contains MRI images classified into:
- Mild Demented
- Moderate Demented
- Non Demented
- Very Mild Demented

---

# Tech Stack

## Programming Language
- Python

## Deep Learning
- TensorFlow
- Keras

## Data Processing
- NumPy
- Matplotlib

## Deployment/UI
- Streamlit

---

# Project Structure


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


---

# Model Architecture

The project uses a Convolutional Neural Network (CNN) for image classification.

The CNN architecture contains:
- Convolution layers
- MaxPooling layers
- Dropout regularization
- Dense fully connected layers
- Softmax output layer

---

# Pipeline

MRI Image
→ Preprocessing
→ CNN Model
→ Prediction
→ Alzheimer Classification


---

# Training Process

The model training pipeline includes:
- Data preprocessing
- Data normalization
- Train-validation split
- CNN training
- Early stopping
- Model checkpointing
- Performance evaluation

---

# Evaluation Metrics

The model performance is evaluated using:
- Accuracy
- Validation Accuracy
- Loss Curve
- Confusion Matrix

---

# Streamlit Web Application

The project includes a Streamlit application where users can:
- Upload MRI images
- View predictions
- See confidence scores
- Test the trained model in real time

---

# Installation

## Clone Repository


git clone https://github.com/YOUR_USERNAME/alzheimer-detection-ai.git


---

## Navigate Into Project


cd alzheimer-detection-ai


---

## Install Dependencies


pip install -r requirements.txt


---

# Run Training


python src/train.py


---

# Run Streamlit App


streamlit run app/main.py


---

# Future Improvements

Future improvements for this project include:
- Grad-CAM explainability visualization
- FastAPI deployment
- Docker containerization
- Cloud deployment
- Improved CNN architecture
- Larger MRI datasets
- Transfer learning implementation

---

# Research Motivation

This project was developed as part of research work focused on applying Artificial Intelligence in healthcare and medical image analysis.

The goal is to contribute toward intelligent healthcare systems capable of assisting medical professionals in early disease diagnosis.

---

# Author

## Abul Khayer Leon

AI/ML Engineer | Medical AI Researcher | Deep Learning Enthusiast

- Research Interests:
  - Medical AI
  - Deep Learning
  - NLP
  - Computer Vision
  - Healthcare AI

---

# License

This project is for educational and research purposes.
