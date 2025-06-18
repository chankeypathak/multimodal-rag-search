# Multimodal RAG Search

A Streamlit-based application for searching and retrieving information from a knowledge base built from PDF documents using Retrieval-Augmented Generation (RAG) techniques. Supports both text and image (diagram) queries.

---

## Features

- **Multimodal Search:** Query both text and images (e.g., diagrams) within PDF documents.
- **Streamlit UI:** Simple web interface for entering queries and viewing results.
- **Knowledge Base Construction:** Extracts and indexes content from PDFs for efficient retrieval.
- **Extensible:** Easily add more documents or customize the pipeline.

---

## Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/multimodal-rag-search.git
cd multimodal-rag-search
```

### 2. Add Sample PDFs

Place PDF files in the `data/sample_reports/` directory.  
Example:

```bash
mkdir -p data/sample_reports
wget -O data/sample_reports/apple_10k_2023.pdf https://www.apple.com/investor/static/pdf/10-K_2023.pdf
```

### 3. Build the Knowledge Base

```bash
python src/build_kb.py
```

### 4. Run the App

#### Locally

```bash
streamlit run app.py
```

#### With Docker

```bash
docker build -t multimodal-rag-search .
docker run -p 8501:8501 multimodal-rag-search
```

---

## Usage

- Open your browser and go to [http://localhost:8501](http://localhost:8501).
- Enter a query (e.g., "technical diagram of report" or "Apple revenue analysis").
- View top results, including extracted text and images from your PDFs.

---

## Project Structure

```
├── app.py                  # Streamlit app entry point
├── src/
│   ├── build_kb.py         # Script to build the knowledge base from PDFs
│   ├── search.py           # Search logic
│   └── utils.py            # Utility functions
├── data/
│   └── sample_reports/     # Directory for sample PDF files
├── requirements.txt        # Python dependencies
├── Dockerfile              # Docker setup
```

---

## Requirements

- Python 3.10+
- See `requirements.txt` for dependencies

---

## License

This project is for educational and research purposes.

---

## Acknowledgements

- [Streamlit](https://streamlit.io/)
- [PyTorch](https://pytorch.org/)
- [OpenCLIP](https://github.com/mlfoundations/open_clip)