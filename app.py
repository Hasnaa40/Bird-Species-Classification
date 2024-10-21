import streamlit as st
from PIL import Image
import numpy as np
from tensorflow.keras import models

# Load your trained model
model = models.load_model('CNN_best_model.keras')

def load_image(image_file):
    img = Image.open(image_file)
    return img

# Add an image at the top of the app (adjust path or URL to your image)
st.image("image.png", use_column_width=True)

# Title with custom purple color using HTML
st.markdown(
    "<h1 style='text-align: center; color: purple;'>Bird Species Classification</h1>", 
    unsafe_allow_html=True
)

# File uploader for users to upload an image
image_file = st.file_uploader("Upload Images", type=["png", "jpg", "jpeg"])

if image_file is not None:
    # Display the uploaded image
    st.image(load_image(image_file), width=250)

    # Process the image for prediction
    image = Image.open(image_file)
    image = image.resize((224, 224))
    image_arr = np.array(image.convert('RGB'))
    image_arr = image_arr.reshape((1, 224, 224, 3))

    # Predict the bird species
    result = model.predict(image_arr)
    ind = np.argmax(result)

    # Class labels
    classes = ['AMERICAN GOLDFINCH', 'BARN OWL', 'CARMINE BEE-EATER', 
               'DOWNY WOODPECKER', 'EMPEROR PENGUIN', 'FLAMINGO']

    # Display the prediction result
    st.header(f"Prediction: {classes[ind]}")
