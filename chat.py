from llama_index.llms.google_genai import GoogleGenAI
from llama_index.embeddings.google_genai import GoogleGenAIEmbedding
from llama_index.core import VectorStoreIndex, Settings
from razorpay_reader import RazorpayReader  
# ==========================================
# 1. PASTE YOUR API KEYS HERE
# ==========================================
GEMINI_API_KEY = 

RAZORPAY_KEY_ID = 
RAZORPAY_KEY_SECRET =

# ==========================================
# 2. CONFIGURE THE NEW GOOGLE AI BRAIN
# ==========================================
Settings.llm = GoogleGenAI(
    api_key=GEMINI_API_KEY, 
    model="gemini-2.5-flash"
)
Settings.embed_model = GoogleGenAIEmbedding(
    api_key=GEMINI_API_KEY, 
    model="text-embedding-004"
)

try:
    # ==========================================
    # 3. LOAD YOUR FINANCIAL DATA
    # ==========================================
    print("Fetching data from Razorpay...")
    reader = RazorpayReader(RAZORPAY_KEY_ID, RAZORPAY_KEY_SECRET)
    documents = reader.load_data(limit=5)

    # ==========================================
    # 4. BUILD THE AI KNOWLEDGE BASE
    # ==========================================
    print("Building the AI Brain... (this takes a few seconds)")
    index = VectorStoreIndex.from_documents(documents)

    # ==========================================
    # 5. CHAT WITH YOUR DATA!
    # ==========================================
    query_engine = index.as_query_engine()

    print("\n=======================================================")
    print("AI: I have securely read your Razorpay data.")
    print("=======================================================\n")

    question = "How many payments were captured successfully, and what methods were used?"
    
    print(f"You: {question}")
    print("AI is thinking...\n")
    
    response = query_engine.query(question)
    
    print(f"AI Answer: {response}")

    

except Exception as e:
    print(f"Oops, something went wrong: {e}")

    