import fitz  # PyMuPDF
from pathlib import Path

def extract_text_and_images(pdf_path):
    doc = fitz.open(pdf_path)
    chunks = []
    images = []
    for i, page in enumerate(doc):
        text = page.get_text()
        if text.strip():
            chunks.append({"page": i, "text": text.strip(), "source": str(pdf_path)})
        img_list = page.get_images(full=True)
        for img_index, img in enumerate(img_list):
            xref = img[0]
            base_image = doc.extract_image(xref)
            image_bytes = base_image["image"]
            ext = base_image["ext"]
            image_path = pdf_path.parent / f"{pdf_path.stem}_page{i}_img{img_index}.{ext}"
            with open(image_path, "wb") as f:
                f.write(image_bytes)
            images.append({"page": i, "path": str(image_path), "source": str(pdf_path)})
    return chunks, images
