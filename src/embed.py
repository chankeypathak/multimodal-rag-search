import torch
import open_clip
from PIL import Image

device = "cuda" if torch.cuda.is_available() else "cpu"
model, _, preprocess = open_clip.create_model_and_transforms("ViT-B-32", pretrained="laion2b_s34b_b79k")
tokenizer = open_clip.get_tokenizer("ViT-B-32")
model = model.to(device)
model.eval()

def embed_text(text):
    with torch.no_grad():
        tokenized = tokenizer([text]).to(device)
        return model.encode_text(tokenized).cpu().squeeze(0).numpy()

def embed_image(image_path):
    with torch.no_grad():
        image = preprocess(Image.open(image_path)).unsqueeze(0).to(device)
        return model.encode_image(image).cpu().squeeze(0).numpy()
