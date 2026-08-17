from flask import Flask, request, jsonify
import requests
import random
import time

app = Flask(__name__)

# သင်စစ်ချင်တဲ့ Site တွေကို ဒီမှာထည့်ပါ (သို့) Database ကနေယူပါ
SITES = [
    "https://riverbendhomedev.myshopify.com",
    "https://another-shop.myshopify.com",
]

# User Agent အမျိုးမျိုး
USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/120.0.0.0",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 Safari/17.2",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 17_2 like Mac OS X) AppleWebKit/605.1.15 Mobile/15E148",
]

@app.route('/shopify', methods=['GET'])
def check_card():
    # Bot ကနေ လာတဲ့ Parameter တွေ
    site = request.args.get('site')
    cc = request.args.get('cc')
    proxy = request.args.get('proxy')

    if not site or not cc:
        return jsonify({"Status": False, "Response": "Missing site or cc"})

    # Proxy format ကို ပြင်ရန် (http://user:pass@ip:port ပုံစံ)
    proxies = {}
    if proxy:
        if "@" in proxy:
            # SOCKS5 / HTTP proxy format
            proxies = {"http": proxy, "https": proxy}
        else:
            # Simple IP:Port format
            proxies = {"http": f"http://{proxy}", "https": f"http://{proxy}"}
    
    headers = {
        "User-Agent": random.choice(USER_AGENTS),
        "Accept": "application/json",
        "Content-Type": "application/json"
    }

    try:
        # Shopify Checkout Logic (ဒါက Mock/Test Logic ပါ)
        # တကယ်အလုပ်လုပ်ဖို့အတွက် ဒီနေရာမှာ Shopify checkout URL ကို request ပို့ပြီး 
        # Response ကို parse လုပ်ရပါမယ်။
        
        # ဒီဥပမာမှာ ကျွန်တော်တို့ စမ်းသပ် Response ပြန်ပေးမယ်
        statuses = ["Charged", "Approved", "Dead"]
        chosen_status = random.choice(statuses)
        
        time.sleep(1) # စစ်နေသလိုမျိုး delay လုပ်ထားတာ

        if chosen_status == "Charged":
            return jsonify({"Status": "Charged", "Response": "Order Placed Successfully", "Price": "1.00", "Gateway": "Shopify Payments"})
        elif chosen_status == "Approved":
            return jsonify({"Status": "Approved", "Response": "OTP Required", "Price": "1.00", "Gateway": "Shopify Payments"})
        else:
            return jsonify({"Status": False, "Response": "Card Declined", "Price": "-", "Gateway": "Shopify Payments"})

    except Exception as e:
        return jsonify({"Status": False, "Response": str(e), "Price": "-", "Gateway": "Error"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
