# Story to Comic Generator

This Streamlit app takes a short story or narration and converts each line into a separate comic panel using a Hugging Face model for image generation.

## Features
- Input a multi-line story where each new line represents a comic panel.
- Comic-style illustrations are generated for each scene.
- Displays each panel with its corresponding text above the image.

## Model Used
- [stabilityai/stable-diffusion-xl-base-1.0](https://huggingface.co/stabilityai/stable-diffusion-xl-base-1.0)

## Requirements

Create a `requirements.txt` with the following:
```
streamlit
requests
Pillow
```

## Running the App Locally
```bash
git clone https://github.com/your-username/story-to-comic
cd story-to-comic
pip install -r requirements.txt
streamlit run app.py
```

## Deployment
Deploy it easily on [Hugging Face Spaces](https://huggingface.co/spaces) using the `app.py` and `requirements.txt` files.

## Example Input
```
A boy wakes up.
He walks his dog.
It starts to rain.
They find shelter under a tree.
```

Each line becomes a separate panel.



