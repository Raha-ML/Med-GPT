# Med-GPT
Med-GPT is an End-to-End Medical Question Answering bot. This simple app includes:
- RAG 
- Rephrase
- Prompot Engineering
- Multi-model
- Ranking
- Evaluation
- Fine-Tuning
- Deployment

Its RAG pipeline uses Real Medical PDFs + Ollama (LLama3) + Stable ChromaDB + Prompt Eng + Rephrasing 

## Prerequisites
You need to install the following packages:
```
pip install langchain chromadb sentence-transformers pypdf pdfplumber nltk
pip install llama-index              #(for advanced prompt/llm handling)
```

## Phases

###  ✅ Phase 1: Basic LLM RAG with PDF

Goal: Build a working local RAG app using one open-source model.

Includes:
    PDF parser (medical PDF)
    Vector DB: Chroma (persistent)
    Embedding model: BGE-M3 or all-MiniLM
    LLM: Mistral via transformers (local or HuggingFace)
    Simple prompt template
    Terminal or FastAPI interface
Tech:
- langchain
- transformers
- chromadb
- sentence-transformers
- PyMuPDF / pdfplumber

### 🔁 Phase 2: Query Rephrasing + Prompt Engineering

    LLM-based rephraser
    Prompt template using chat format
    Role-based prompts: “Act like a medical assistant”
    Few-shot examples for rare questions

### 🤖 Phase 3: Multi-Model Comparison

Goal: Query goes to 3 models → rank answers → return best.

Models:
    Mistral (via transformers or vLLM)
    Zephyr (transformers or Ollama)
    LLaMA3 (via Ollama)

Ranking Methods:
    LLM-based scoring (meta-evaluator)
    Cosine sim to ground truth
    Token length + answer relevance

### ⚙️ Phase 4: Model Serving Options

You’ll be able to run the app using any of:
    🐳 Ollama
    🚀 vLLM
    🧠 Triton + KServe on Kubernetes

Includes:
    Dockerfiles
    Ollama model pull + run
    K8s YAML manifests (for KServe, Triton, vLLM)
    Deployment instructions

### 🧪 Phase 5: Evaluation Scripts + Benchmarks

    Evaluation of generated answers vs. gold set
    BLEU / ROUGE / cosine similarity
    Script to test multiple models on same queries

### 🧰 Phase 6: Optional Tooling

    Add Streamlit or FastAPI interface
    Vector DB swapping (e.g., Chroma ↔ FAISS)
    Advanced logging, caching, fallback

    ✅ First working local version using:
        1 PDF
        Chroma DB
        Mistral model
        Simple prompt template

 ### Future:
  multi-lingual support

## Serving/Inference
python main.py

## Directory Structure
The Directory Structure of the project is like: 
```
# ├── data/                     # Medical PDFs about Breast Cancer
# ├── app/
# │   ├── loader.py             # PDF loader, cleaner, chunker
# │   ├── embed.py              # Create embeddings and store in Chroma/FAISS
# │   ├── query.py              # Answer query using RAG (multi-model)
# │   ├── reranker.py           # Rank model outputs
# │   ├── evaluation.py         # Metrics, logs, etc.
# │   └── server.py             # API endpoint for external access
# ├── models/
# │   ├── config.yaml           # Models to use (llama3, mistral, zephyr)
# ├── k8s/                      # Kubernetes manifests (vLLM, Triton, etc.)
# ├── notebooks/                # Dev/test playgrounds
# ├── README.md                 # The current doc
# └── requirements.txt
```

## Contributing
We welcome contributions to improve this simple LLM sample. If you want to contribute, please fork this repository, create a feature branch, and submit a pull request.

## License
This project is licensed under the Apache 2.0 License - See the LICENSE file for details.
