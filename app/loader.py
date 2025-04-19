from langchain.document_loaders import PyPDFLoader, PyPDFDirectoryLoader
from langchain.text_splitter    import RecursiveCharacterTextSplitter


def load_pdf(pdf_path, chunk_size=512, chunk_overlap=50):

  loader = PyPDFDirectoryLoader(pdf_path)
  docs   = loader.load()
  
  splitter = RecursiveCharacterTextSplitter(
                chunk_size=chunk_size,
	              chunk_overlap=chunk_overlap,
	              separators=["\n\n", "\n", ".", " "]
              )

  chunks = splitter.split_documents(docs)
  return chunks


