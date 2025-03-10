from flask import Flask, request, jsonify
from vector_store import create_vector_store
from data_extraction import extract_data

app = Flask(__name__)

# Load and embed data
URL = "https://brainlox.com/courses/category/technical"
data = extract_data(URL)
vector_db = create_vector_store(data)

@app.route("/chat", methods=["POST"])
def chat():
    """Handles chatbot conversation"""
    user_query = request.json.get("query")
    
    if not user_query:
        return jsonify({"error": "Query not provided"}), 400
    if vector_db is None:
        return jsonify({"error": "Vector store not initialized"}), 500

    # Perform similarity search
    results = vector_db.similarity_search(user_query, k=3)
    response = [res.page_content for res in results]

    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=True)
