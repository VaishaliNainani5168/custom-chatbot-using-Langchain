import re
from bs4 import BeautifulSoup
from langchain_community.document_loaders import WebBaseLoader

def extract_data(url):
    """Extracts clean text from a web page"""
    loader = WebBaseLoader(url)
    documents = loader.load()

    extracted_data = []
    for doc in documents:
        soup = BeautifulSoup(doc.page_content, "html.parser")
        text = soup.get_text(separator=" ", strip=True)

        # Remove unwanted metadata like pricing and lesson counts
        clean_text = re.sub(r'\$\d+per session|\d+ LessonsView Details', '', text)

        extracted_data.append({"content": clean_text})

    print(f"Extracted {len(extracted_data)} documents.")
    return extracted_data
