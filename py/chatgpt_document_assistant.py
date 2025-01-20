# chatgpt_document_assistant.py
from vector_store_handler import initialize_vector_store, add_document
from chatgpt import ask_chatgpt, save_conversation
from datetime import datetime

def main():
    initialize_vector_store()
    print("Welcome to ChatGPT Document Assistant!")
    while True:
        print("\nOptions:")
        print("1. Add Document")
        print("2. Ask Question")
        print("3. Save Conversation")
        print("4. Exit")
        choice = input("Enter your choice: ").strip()
        if choice == "1":
            file_path = input("Enter the file path of the document: ").strip()
            add_document(file_path)
        elif choice == "2":
            query = input("Enter your question: ").strip()
            ask_chatgpt(query)
        elif choice == "3":
            file_path = f"documents/chat_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
            save_conversation(file_path)
        elif choice == "4":
            print("Exiting. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()