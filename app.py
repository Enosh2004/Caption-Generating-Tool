import streamlit as st
from gtts import gTTS
from PIL import Image
import torch
from transformers import BlipProcessor, BlipForConditionalGeneration
from deep_translator import GoogleTranslator
import base64
import os

# Convert background GIF to base64
def get_base64_gif(file_path):
    with open(file_path, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()

# Set animated background and frosted black panel
def set_background():
    gif_base64 = get_base64_gif("background.gif")
    st.markdown(f"""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700&display=swap');

        .stApp {{
            background-image: url("data:image/gif;base64,{gif_base64}");
            background-size: cover;
            background-repeat: no-repeat;
            background-attachment: fixed;
            font-family: 'Orbitron', sans-serif;
            color: #e0e0e0;
        }}

        .frosted-panel {{
            background: rgba(0, 0, 0, 0.65);
            padding: 30px;
            margin: 40px auto;
            border-radius: 16px;
            max-width: 900px;
            box-shadow: 0 0 25px #00ffff88;
            backdrop-filter: blur(6px);
            -webkit-backdrop-filter: blur(6px);
        }}

        h1, h2, h3, h4, h5, h6 {{
            color: #ffffff;
            text-align: center;
            font-weight: 700;
            text-shadow: 0 0 10px #00fff7, 0 0 20px #00fff7;
        }}

        .stButton > button {{
            background-color: #00bfff;
            color: white;
            font-weight: bold;
            padding: 10px 20px;
            border: none;
            border-radius: 12px;
            box-shadow: 0 0 10px #00bfff;
            transition: 0.3s ease;
        }}

        .stButton > button:hover {{
            background-color: #1ac9ff;
            box-shadow: 0 0 20px #00ffff;
        }}

        .stFileUploader > div, .stImage img {{
            background-color: rgba(0, 0, 0, 0.5);
            border-radius: 10px;
            border: 1px solid #00ffff;
            box-shadow: 0 0 10px #00ffff;
        }}

        </style>
    """, unsafe_allow_html=True)

# Load model
def load_model():
    processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
    model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")
    return processor, model

# Generate caption
def generate_caption(image, processor, model):
    image = image.convert("RGB")
    inputs = processor(images=image, return_tensors="pt")
    output = model.generate(**inputs)
    return processor.decode(output[0], skip_special_tokens=True)

# Translate caption
def translate_text(text, lang):
    return GoogleTranslator(source='auto', target=lang).translate(text)

# Run background setup
set_background()

# Load model
processor, model = load_model()

# Session state init
if "translated_description" not in st.session_state:
    st.session_state.translated_description = None

# Frosted panel UI starts
st.markdown('<div class="frosted-panel">', unsafe_allow_html=True)

st.title("\U0001F4F7 Image to Speech Converter \U0001F3A4")
st.write("Upload an image, generate a description, and listen to it in your preferred language!")

uploaded_file = st.file_uploader("\U0001F4E4 Upload an image...", type=["jpg", "jpeg", "png"])

if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image, caption="\U0001F4F8 Uploaded Image", use_container_width=True)

    with st.spinner("\U0001F4DD Generating description... ⏳"):
        caption = generate_caption(image, processor, model)

    if caption:
        st.subheader("\U0001F4DD Description (English):")
        st.write(caption)

        if st.button("\U0001F509 Speak English Description"):
            tts = gTTS(text=caption, lang="en")
            tts.save("english_description.mp3")
            st.audio("english_description.mp3")

        st.subheader("\U0001F30D Translate to Another Language")
        langs = {"English": "en", "French": "fr", "Tamil": "ta", "Punjabi": "pa", "Malayalam": "ml",
                 "Spanish": "es", "Korean": "ko", "Japanese": "ja", "Hindi": "hi", "German": "de",
                 "Marathi": "mr", "Arabic": "ar", "Russian": "ru", "Malay": "ms"}
        selected_lang = st.selectbox("Select Language", list(langs.keys()))

        if st.button("\U0001F310 Translate Description"):
            translated = translate_text(caption, langs[selected_lang])
            st.session_state.translated_description = translated
            st.subheader(f"Translated Description ({selected_lang}):")
            st.write(translated)

        if st.session_state.translated_description:
            if st.button("\U0001F509 Speak Translated Description"):
                tts = gTTS(text=st.session_state.translated_description, lang=langs[selected_lang])
                tts.save("translated_description.mp3")
                st.audio("translated_description.mp3")

            if st.button("\U00002B07\U0000FE0F Download Translated Audio"):
                with open("translated_description.mp3", "rb") as file:
                    st.download_button(
                        label="Download",
                        data=file,
                        file_name=f"description_{selected_lang}.mp3",
                        mime="audio/mpeg"
                    )

st.markdown('</div>', unsafe_allow_html=True)