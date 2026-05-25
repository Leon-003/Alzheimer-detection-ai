import streamlit as st

st.title("Alzheimer Detection AI")

uploaded_file = st.file_uploader(
    "Upload MRI Image",
    type=["jpg","png","jpeg"]
)

if uploaded_file:

    st.image(uploaded_file)

    st.success(
        "Prediction system coming next"
    )