import requests
import base64
import json

class RazorpayDataFetcher:
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

    def fetch_payments(self, limit: int = 10):
        url = f"{self.base_url}/payments?count={limit}"
        print(f"Asking Razorpay for your last {limit} payments...")
        
        response = requests.get(url, headers=self.headers)
        
        if response.status_code != 200:
            raise Exception(f"API Error: {response.text}")
            
        return response.json().get('items',[])

if __name__ == "__main__":
    API_KEY = 
    API_SECRET = 
    
    fetcher = RazorpayDataFetcher(API_KEY, API_SECRET)
    
    try:
        # Fetch the last 5 payments
        recent_payments = fetcher.fetch_payments(limit=5)
        
        print(json.dumps(recent_payments, indent=4))
        print(f"\nSuccess!! Found {len(recent_payments)} payment records.")
        
    except Exception as e:
        print(f"Oops, something went wrong: {e}")
        