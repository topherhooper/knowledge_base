# vector_store.py
import os
import io
from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.http import MediaIoBaseDownload
from dotenv import load_dotenv
from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain_community.document_loaders import TextLoader, PyPDFLoader, UnstructuredImageLoader

# Load environment variables from .env file
load_dotenv()
embedding = OpenAIEmbeddings()
vector_store = None

def initialize_vector_store():
    global vector_store
    try:
        vector_store = FAISS.load_local("vector_store", embedding, allow_dangerous_deserialization=True)
        print("Vector store loaded.")
    except Exception as e:
        print(f"Could not load vector store: {e}")
        # Initialize a new FAISS vector store if loading fails
        vector_store = FAISS.from_texts([""], embedding)
        print("New vector store initialized.")

def save_vector_store():
    if vector_store:
        vector_store.save_local("vector_store")
        print("Vector store saved.")

def create_documents_directory():
    if not os.path.exists("documents"):
        os.makedirs("documents")
        print("Documents directory created.")

def download_google_doc(file_id, credentials_path='.credentials.json'):
    SCOPES = ['https://www.googleapis.com/auth/drive.readonly']
    creds = service_account.Credentials.from_service_account_file(credentials_path, scopes=SCOPES)
    service = build('drive', 'v3', credentials=creds)
    
    request = service.files().export_media(fileId=file_id, mimeType='text/plain')
    file_path = f"documents/{file_id}.txt"
    with io.FileIO(file_path, 'wb') as fh:
        downloader = MediaIoBaseDownload(fh, request)
        done = False
        while done is False:
            status, done = downloader.next_chunk()
            print(f"Download {int(status.progress() * 100)}%.")
    return file_path

def add_document(file_path):
    global vector_store
    if not os.path.exists(file_path):
        print(f"File not found: {file_path}")
        return
    
    file_extension = os.path.splitext(file_path)[1].lower()
    if file_extension == ".txt":
        loader = TextLoader(file_path)
    elif file_extension == ".pdf":
        loader = PyPDFLoader(file_path)
    elif file_extension in [".jpg", ".jpeg", ".png"]:
        loader = UnstructuredImageLoader(file_path)
    elif file_extension == ".gdoc":
        file_id = os.path.splitext(os.path.basename(file_path))[0]
        file_path = download_google_doc(file_id)
        loader = TextLoader(file_path)
    else:
        print(f"Unsupported file type: {file_extension}")
        return

    documents = loader.load()
    splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
    docs = splitter.split_documents(documents)
    vector_store.add_documents(docs)
    print(f"Document added from {file_path}.")
    save_vector_store()

def get_vector_store():
    global vector_store
    return vector_store