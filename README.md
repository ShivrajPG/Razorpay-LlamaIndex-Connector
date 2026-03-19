# 💳 LlamaIndex Razorpay Connector

**An official data loader connecting Razorpay's Financial API to LLMs.**

### 🛑 The Problem
FinTech companies, e-commerce brands, and merchants generate thousands of payment data points daily. However, modern LLMs (Large Language Models) cannot natively read or access this structured financial data to provide business insights.

### 💡 The Solution
I built the `RazorpayReader` for LlamaIndex. This custom data connector securely extracts payment records, refunds, and transaction statuses from the Razorpay API, injecting them as rich, metadata-tagged `Document` objects into Vector Databases for RAG (Retrieval-Augmented Generation) applications.

This allows developers and business owners to ask AI questions like: 
*"How many payments failed yesterday, and what were the most common error reasons?"*

### ⚙️ Features
* **Instant Conversion:** Converts raw Razorpay JSON into AI-ready LlamaIndex `Document` objects.
* **Smart Metadata Tagging:** Automatically captures and tags crucial data (`amount_in_inr`, `status`, `method`, `error_reason`) so the AI can filter data instantly.
* **Currency Formatting:** Automatically converts Razorpay's base unit (paise) back into standard INR (₹).
* **Lightweight:** Built with pure Python and `requests` for zero-bloat deployment.

### 🚀 Usage Example

```python
from razorpay_reader import RazorpayReader

# 1. Initialize the AI Reader
reader = RazorpayReader("YOUR_RAZORPAY_KEY_ID", "YOUR_RAZORPAY_KEY_SECRET")

# 2. Fetch the latest financial data and convert to AI Documents
documents = reader.load_data(limit=10)

# 3. The documents are now ready to be fed into any LLM (Gemini, OpenAI, etc.)
```

###🛠️ Built With
* Python 3.x
* LlamaIndex
* Google Gemini 2.5 (for querying)
* Razorpay API

