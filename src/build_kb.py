import os
import torch
import pickle
import pandas as pd
from tqdm import tqdm
from PIL import Image
import fitz  # PyMuPDF
from open_clip import create_model_and_transforms, tokenize

device = "cuda" if torch.cuda.is_available() else "cpu"

# Initialize CLIP model
model, _, preprocess = create_model_and_transforms("ViT-B-32", pretrained="laion2b_s34b_b79k")
model = model.to(device).eval()

# Paths
DATA_DIR = "data/sample_reports"
KB_FILE = "knowledge_base.pkl"

# Storage
records = []

from pathlib import Path

def extract_chunks_from_pdf(pdf_path):
    chunks = []
    doc = fitz.open(pdf_path)
    for i, page in enumerate(doc):
        text = page.get_text()
        if text.strip():
            chunks.append(("text", f"{Path(pdf_path).name}_page{i+1}", text))
    return chunks

def get_clip_embedding(modality, content):
    with torch.no_grad():
        if modality == "text":
            tokens = tokenize([content]).to(device)
            return model.encode_text(tokens).cpu().squeeze(0)
        elif modality == "image":
            image = Image.open(content).convert("RGB")
            image_tensor = preprocess(image).unsqueeze(0).to(device)
            return model.encode_image(image_tensor).cpu().squeeze(0)
    return None

def build_knowledge_base():
    all_records = []

    pdfs = [f for f in os.listdir(DATA_DIR) if f.endswith(".pdf")]
    for pdf in tqdm(pdfs, desc="Processing PDFs"):
        pdf_path = os.path.join(DATA_DIR, pdf)
        chunks = extract_chunks_from_pdf(pdf_path)

        for modality, source, content in chunks:
            try:
                if modality == "text":
                    embedding = get_clip_embedding("text", content)
                    all_records.append({
                        "type": "text",
                        "source": source,
                        "text": content,
                        "embedding": embedding
                    })
                elif modality == "image":
                    embedding = get_clip_embedding("image", source)
                    all_records.append({
                        "type": "image",
                        "source": source,
                        "text": None,
                        "embedding": embedding
                    })
                    # Optionally delete image after embedding to keep clean
                    os.remove(source)
            except Exception as e:
                print(f"⚠️ Failed to embed {source}: {e}")

    # Convert to DataFrame
    if all_records:
        df = pd.DataFrame(all_records)
        df.to_pickle(KB_FILE)
        print(f"✅ Saved {len(df)} records to {KB_FILE}")
    else:
        print("⚠️ No valid records to embed.")

if __name__ == "__main__":
    build_knowledge_base()
