from data_extraction import extract_data
from vector_store import create_vector_store

URL = "https://brainlox.com/courses/category/technical"

print("Extracting Data...")
data = extract_data(URL)

if not data:
    print("Data extraction failed!")
else:
    print(f"Extracted {len(data)} documents.")

print("Creating Vector Store...")
vector_db = create_vector_store(data)

if vector_db is None:
    print("Vector store creation failed!")
else:
    print("Vector store initialized successfully!")
