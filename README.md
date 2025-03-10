# LangChain Chatbot with Web Scraping & FAISS

A custom chatbot that:
- Extracts course data from [Brainlox](https://brainlox.com/courses/category/technical) using **LangChain URL loader**  
- Stores embeddings in a **FAISS vector database**  
- Serves responses via a **Flask REST API**  

## 🚀 Setup & Run  
```sh
python app.py
```

## 🚀 API Usage

### 🔹 **Endpoint:** `POST /chat`
- **Request:**
  ```json
  {
      "query": "What is Python?"
  }
