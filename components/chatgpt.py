# components/chatgpt.py
import os
from dotenv import load_dotenv
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
from components.vector_store import get_vector_store, add_document, VectorStore

# Initialize the vector store
vector_store = VectorStore()

# Load environment variables from .env file
load_dotenv()

# Set up OpenAI API key

import threading

conversation_history = []
conversation_history_lock = threading.Lock()

def ask_chatgpt(query):
    vector_store = get_vector_store()
    if not vector_store:
        print("No vector store initialized. Add documents first.")
        return
    docs = vector_store.similarity_search(query, k=3)
    context = "\n\n".join([doc.page_content for doc in docs])
    
    messages = [
        {"role": "system", "content": "You are a helpful assistant. Use the following context to answer the user's question."},
        {"role": "user", "content": f"Context:\n{context}\n\nQuery: {query}"}
    ]
    
    with conversation_history_lock:
        for entry in conversation_history:
            messages.append({"role": "user", "content": entry["user"]})
            messages.append({"role": "assistant", "content": entry["assistant"]})
    
    response = client.chat.completions.create(model="gpt-4", messages=messages)
    answer = response.choices[0].message.content
    print(answer)
    
    with conversation_history_lock:
        conversation_history.append({"user": query, "assistant": answer})

def save_conversation(file_path):
    with open(file_path, 'w') as f:
        for entry in conversation_history:
            f.write(f"User: {entry['user']}\n")
            f.write(f"Assistant: {entry['assistant']}\n\n")
    add_document(file_path)
    print(f"Conversation saved to {file_path} and added to vector store.")