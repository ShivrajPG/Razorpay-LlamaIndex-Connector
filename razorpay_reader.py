from llama_index.core import Document
from llama_index.core.readers.base import BaseReader
import requests
import base64
import json

class RazorpayReader(BaseReader):
    def __init__(self, api_key: str, api_secret: str):
        self.api_key = api_key
        self.api_secret = api_secret
        self.base_url = "https://api.razorpay.com/v1"
        
        auth_string = f"{self.api_key}:{self.api_secret}"
        b64_auth = base64.b64encode(auth_string.encode()).decode()
        self.headers = {
            "Authorization": f"Basic {b64_auth}",
            "Content-Type": "application/json"
        }

    def load_data(self, limit: int = 10):
        """Fetches payments and converts them into AI Documents."""
        url = f"{self.base_url}/payments?count={limit}"
        print(f"Fetching {limit} payments from Razorpay...")
        
        response = requests.get(url, headers=self.headers)
        
        if response.status_code != 200:
            raise Exception(f"API Error: {response.text}")
            
        payments = response.json().get('items',[])
        
        documents =[]
        
        for payment in payments:
            payment_text = json.dumps(payment, indent=2)
            
            metadata_tags = {
                "payment_id": payment.get("id"),
                "amount_in_inr": payment.get("amount", 0) / 100, 
                "status": payment.get("status"),
                "method": payment.get("method"),
                "error_reason": payment.get("error_reason", "None")
            }
            
            doc = Document(
                text=payment_text,
                metadata=metadata_tags
            )
            
            documents.append(doc)
            
        return documents

if __name__ == "__main__":
    API_KEY = 
    API_SECRET = 
    
    reader = RazorpayReader(API_KEY, API_SECRET)
    
    try:
        ai_docs = reader.load_data(limit=5)
        print(f"\nSUCCESS! Converted {len(ai_docs)} payments into AI Documents!")
        
        if len(ai_docs) > 0:
            print("\n--- Inspecting the First AI Document ---")
            print(f"Metadata Tags for AI: {ai_docs[0].metadata}")
            
    except Exception as e:
        print(f"Oops, something went wrong: {e}")\
