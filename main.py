from app import loader, embed
from app import loader, embed

import os

def run_loader():
    data_dir  = './data'
    chuncks   = loader.load_pdf(pdf_path=data_dir)
    vector_db = embed.embed_and_store(chuncks=chuncks)

    # all_chunks = []
    # for file in os.listdir(data_dir):
    #     if file.endswith(".pdf"):
    #         print(f"Processing: {file}")
    #         chunks = load_and_chunk(os.path.join(data_dir, file))
    #         all_chunks.extend(chunks)
    # embed_and_store(all_chunks)

if __name__ == "__main__":
    run_loader()