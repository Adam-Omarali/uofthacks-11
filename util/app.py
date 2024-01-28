import streamlit as st
import os

# Import your backend functions here
from img_to_text import process_image

# Set the title of the app
st.title('Image Narration App')

# Directory for saving uploaded images
image_dir = "uploaded_images"
os.makedirs(image_dir, exist_ok=True)  # Create the directory if it doesn't exist

# Image upload
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
if uploaded_file is not None:
    # Generate a unique filename
    file_path = os.path.join(image_dir, "test.jpg")
        # Save the uploaded image
    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())
        # Process the image using your backend function
        audio_path = process_image()

    # Display the audio player if the audio file exists
    if os.path.exists(audio_path):
        audio_file = open(audio_path, 'rb')
        audio_bytes = audio_file.read()
        st.audio(audio_bytes, format='audio/mp3')
