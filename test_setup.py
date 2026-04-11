import ollama
import chromadb
from sentence_transformers import SentenceTransformer

print("Testing Ollama...")
response = ollama.chat(model='mistral', messages=[{'role': 'user', 'content': 'Say OK'}])
print("Ollama ✅:", response['message']['content'])

print("\nTesting ChromaDB...")
client = chromadb.Client()
print("ChromaDB ✅")

print("\nTesting Embeddings...")
model = SentenceTransformer('all-MiniLM-L6-v2')
vec = model.encode("test sentence")
print(f"Embeddings ✅ - Vector size: {len(vec)}")

print("\n✅ All systems ready!")