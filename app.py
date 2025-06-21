import streamlit as st
import requests
from PIL import Image, ImageDraw, ImageFont
from io import BytesIO

# Hugging Face model
MODEL_ID = "stabilityai/stable-diffusion-xl-base-1.0"
API_URL = f"https://api-inference.huggingface.co/models/{MODEL_ID}"

# Load your secret token securely
HUGGINGFACE_API_KEY = st.secrets["HUGGINGFACE_API_KEY"]

# Function to call Hugging Face API
def generate_image(prompt):
    headers = {
        "Authorization": f"Bearer {HUGGINGFACE_API_KEY}"
    }
    payload = {
        "inputs": prompt,
        "options": {"wait_for_model": True}
    }
    response = requests.post(API_URL, headers=headers, json=payload)

    if response.status_code == 200:
        image_bytes = response.content
        img = Image.open(BytesIO(image_bytes))
        return img
    else:
        st.error(f"Image generation failed: {response.status_code} - {response.text}")
        return None

# Function to overlay text onto the generated image
def add_text_to_image(img, text):
    # Get image dimensions
    width, height = img.size
    draw = ImageDraw.Draw(img)
    
    # Load a font (you can provide your own path to a .ttf file if needed)
    font = ImageFont.load_default()
    
    # Set text position (top of the image)
    text_position = (20, 20)
    
    # Set text color (white with slight transparency)
    text_color = (255, 255, 255)
    
    # Add the text
    draw.text(text_position, text, font=font, fill=text_color)
    
    return img

# UI
st.set_page_config(page_title="Story to Comic Generator", layout="wide")
st.title("Story to Comic Generator")

story_input = st.text_area("Enter a short story or narration:", height=200)
panel_count = st.slider("Number of panels", 2, 6, 4)

if st.button("Generate Comic") and story_input:
    st.subheader("Comic Panels")
    
    # Split the story input by newlines, each line becomes a new panel
    panels = story_input.split('\n')

    # Generate comic images for each panel
    comic_images = []
    for i, panel in enumerate(panels):
        if panel.strip():  # Only process non-empty panels
            with st.spinner(f"Generating Panel {i + 1}: {panel}"):
                prompt = f"Cartoon comic style illustration, colorful and child-friendly: {panel}"
                img = generate_image(prompt)
                if img:
                    img_with_text = add_text_to_image(img, panel)  # Add text on top of the image
                    comic_images.append((i + 1, img_with_text, panel))

    if comic_images:
        st.subheader("📷 Comic Strip")
        cols = st.columns(len(comic_images))
        for (panel_num, img, caption), col in zip(comic_images, cols):
            col.image(img, caption=f"Panel {panel_num}: {caption}", use_column_width=True)
    else:
        st.warning("No comic panels generated. Please try again.")
else:
    st.info("Enter a story and click Generate Comic.")
