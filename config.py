import os

# Base paths
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
KNOWLEDGE_BASE_RAW = os.path.join(BASE_DIR, "knowledge_base/raw")
CHROMA_DB_PATH = os.path.join(BASE_DIR, "knowledge_base/chroma_db")
DECISIONS_PATH = os.path.join(BASE_DIR, "decisions")
REPORTS_PATH = os.path.join(BASE_DIR, "reports")

# LLM settings
LLM_MODEL = "mistral"
EMBEDDING_MODEL = "BAAI/bge-small-en-v1.5"

# RAG settings
CHUNK_SIZE = 500
CHUNK_OVERLAP = 50
TOP_K_RESULTS = 5

ELEVENLABS_API_KEY  = "sk_780b925adb80bc3f3fe71f827d06276fa72350c34a1a0955"
ELEVENLABS_VOICE_ID = "hpp4J3VqNfWAUOO0d1Us" 