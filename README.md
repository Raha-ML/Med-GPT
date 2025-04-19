# Med-GPT
Med-GPT is a Medical Question Answering bot. This simple app includes:
- RAG
- Rephrase
- Prompot Engineering
- Multi-model
- Ranking
- Evaluation
- Fine-Tuning
- Deployment

## Prerequisites

## Serving/Inference


## Directory Structure
The Directory Structure of the project is like: 
```
# ├── data/                     # Medical PDFs about Breast Cancer
# ├── app/
# │   ├── ingest.py             # PDF loader, cleaner, chunker
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
