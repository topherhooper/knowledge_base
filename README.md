# knowledge_base

## Overview

`knowledge_base` is a document assistant application that leverages OpenAI's GPT-4 model to provide intelligent responses based on the documents you add to its vector store. It uses FAISS for efficient similarity search and supports various document formats including text, PDF, and images.

## Features

- Add documents to the vector store
- Ask questions based on the added documents
- Save and load conversations
- Supports text, PDF, and image documents
- Integration with Google Drive for downloading Google Docs

## Installation

1. Clone the repository:
```sh
git clone https://github.com/yourusername/knowledge_base.git
cd knowledge_base
```

2. Install the required dependencies:
```sh
pip install -r requirements.txt
```

3. Set up your environment variables:
    - Create a [.env](http://_vscodecontentref_/1) file in the root directory and add your OpenAI API key:
```env
OPENAI_API_KEY="your-openai-api-key"
```

4. Ensure you have your Google service account credentials in [.credentials.json](http://_vscodecontentref_/2).

## Usage

### Running Locally

1. Initialize the vector store and start the document assistant:
```sh
python py/chatgpt_document_assistant.py
```

2. Follow the on-screen prompts to add documents, ask questions, and save conversations.

### Running with Docker

1. Build the Docker image:
```sh
docker-compose build
```

2. Run the Docker container:
```sh
docker-compose up
```

## Project Structure

- [py](http://_vscodecontentref_/3): Contains the main Python scripts.
  - [chatgpt_document_assistant.py](http://_vscodecontentref_/4): Main script to run the document assistant.
  - [chatgpt.py](http://_vscodecontentref_/5): Handles interactions with the OpenAI API.
  - [vector_store_handler.py](http://_vscodecontentref_/6): Manages the vector store and document operations.
- [documents](http://_vscodecontentref_/7): Directory to store added documents and saved conversations.
- [vector_store](http://_vscodecontentref_/8): Directory to store the FAISS index files.
- [.env](http://_vscodecontentref_/9): Environment variables file.
- [.credentials.json](http://_vscodecontentref_/10): Google service account credentials file.
- [requirements.txt](http://_vscodecontentref_/11): Python dependencies.
- [Dockerfile](http://_vscodecontentref_/12): Docker configuration.
- [docker-compose.yml](http://_vscodecontentref_/13): Docker Compose configuration.

## License

This project is licensed under the MIT License. See the [LICENSE](http://_vscodecontentref_/14) file for details.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## Acknowledgements

- [OpenAI](https://openai.com) for the GPT-4 model.
- [FAISS](https://github.com/facebookresearch/faiss) for the similarity search library.
- [LangChain](https://github.com/langchain/langchain) for the document processing utilities.
- [Google API Python Client](https://github.com/googleapis/google-api-python-client) for Google Drive integration.