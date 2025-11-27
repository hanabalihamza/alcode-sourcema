# Final check
# automation_script.py
import requests
import json
from datetime import datetime

# --- CONFIGURATION (MUST BE CUSTOMIZED!) ---
# 1. Base URL: Change this to your live domain
BASE_URL = "https://YOUR-FINAL-DOMAIN.com" 

# 2. Authorization: Use an API Key or Token for secure access
AUTH_HEADER = {'Authorization': 'Bearer YOUR_JWT_OR_API_KEY_HERE'} 

# 3. Action Goal: Replace this with the actual endpoint you want to hit
TASK_ENDPOINT = "/api/v1/health-check/" 
HTTP_METHOD = "GET" 
PAYLOAD = {} 

# ----------------------------------------

def run_automation_task():
    url = f"{BASE_URL}{TASK_ENDPOINT}"
    print(f"[{datetime.now()}] Running automation task: {HTTP_METHOD} {url}")
    
    try:
        if HTTP_METHOD.upper() == "POST":
            response = requests.post(url, headers=AUTH_HEADER, json=PAYLOAD, timeout=20)
        elif HTTP_METHOD.upper() == "GET":
            response = requests.get(url, headers=AUTH_HEADER, timeout=20)
        else:
            print("❌ Error: Unsupported HTTP method.")
            return

        # Check if the request was successful
        if 200 <= response.status_code < 300:
            print(f"✅ Success! Status Code: {response.status_code}")
            print(f"Response: {response.text[:200]}...")
        else:
            print(f"❌ API Error: Status Code {response.status_code}")
            print(f"Error Details: {response.text}")

    except requests.exceptions.RequestException as e:
        print(f"🛑 Network/Connection Error: {e}")

if __name__ == "__main__":
    run_automation_task()