import requests
import json
import urllib3
from urllib.parse import urlencode

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

print("Enter card: ", end="")
card = input().strip()

session = requests.Session()
session.verify = False

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/131.0.0.0',
    'Accept': '*/*',
    'Connection': 'keep-alive'
}

base_url = "http://157.230.248.42/stripe.php"
params = {'card': card}

resp = session.get(base_url, params=params, headers=headers, timeout=30)

print(f"\nStatus: {resp.status_code}")
try:
    data = resp.json()
    print(json.dumps(data, indent=2))
except:
    print(resp.text)
