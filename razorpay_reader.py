from llama_index.core import Document
from llama_index.core.readers.base import BaseReader
import json

from fetcher import RazorpayDataFetcher 

class RazorpayReader(BaseReader):
    def __init__(self, api_key: str, api_secret: str):
        self.fetcher = RazorpayDataFetcher(api_key, api_secret)

    def load_data(self, limit: int = 10):
        """Fetches payments and converts them into AI Documents."""
        
        print(f"Fetching {limit} payments using the fetcher...")
        payments = self.fetcher.fetch_payments(limit=limit)
        
        documents = []
        
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

