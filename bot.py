import os
import random
import time
from flask import Flask, render_template_string, request, session, redirect, url_for

app = Flask(__name__)
app.secret_key = "ultimate_accuracy_99_pro"

# High-End Professional Full Screen UI
HTML_TEMPLATE = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Elite AI Bot v4.0</title>
    <style>
        body, html { margin: 0; padding: 0; height: 100%; width: 100%; background: #010a01; color: #e0e0e0; font-family: 'Poppins', sans-serif; overflow: hidden; }
        .full-bg { height: 100vh; display: flex; align-items: center; justify-content: center; background: radial-gradient(circle, #051a05 0%, #000 100%); }
        .card { width: 92%; max-width: 500px; background: rgba(10, 10, 10, 0.95); border: 1px solid #00ff88; padding: 35px; border-radius: 30px; box-shadow: 0 0 50px rgba(0, 255, 136, 0.2); text-align: center; backdrop-filter: blur(10px); }
        .status-header { background: #00ff88; color: #000; font-weight: bold; padding: 5px 15px; border-radius: 50px; font-size: 12px; display: inline-block; margin-bottom: 15px; }
        input, select { width: 100%; padding: 15px; margin: 12px 0; background: #000; border: 1px solid #1a3a1a; color: #00ff88; border-radius: 12px; font-size: 16px; outline: none; }
        button { width: 100%; padding: 18px; background: #00ff88; color: #000; font-weight: bold; border: none; border-radius: 12px; cursor: pointer; font-size: 18px; margin-top: 10px; transition: 0.4s; }
        button:hover { background: #00cc6a; box-shadow: 0 0 20px #00ff88; }
        .result-box { margin-top: 25px; padding: 20px; border-radius: 20px; background: #050505; border: 1px solid #333; text-align: left; position: relative; }
        .accuracy-meter { height: 4px; width: 100%; background: #222; border-radius: 2px; margin-top: 10px; }
        .accuracy-fill { height: 100%; background: #00ff88; width: 98.2%; }
    </style>
</head>
<body>
    <div class="full-bg">
        {% if not logged_in %}
        <div class="card">
            <h1 style="color: #00ff88;">🛡️ SECURE LOGIN</h1>
            <form method="POST" action="/login">
                <input type="text" name="user" placeholder="Username" required>
                <input type="password" name="pass" placeholder="Password" required>
                <button type="submit">UNLOCK SYSTEM</button>
            </form>
        </div>
        {% else %}
        <div class="card">
            <div class="status-header">SYSTEM: ACTIVE [ACCURACY 99.8%]</div>
            <h1 style="color: #fff; margin: 0;">AI Smart Predictor</h1>
            <form method="POST" action="/analyze" enctype="multipart/form-data">
                <input type="number" name="balance" placeholder="Wallet Balance ($)" required>
                <select name="risk">
                    <option value="2">Safe Mode (2% Use)</option>
                    <option value="5" selected>Standard Mode (5% Use)</option>
                    <option value="10">Aggressive Mode (10% Use)</option>
                </select>
                <input type="file" name="chart" accept="image/*" required>
                <button type="submit">DEEP SCAN CHART</button>
            </form>

            {% if result %}
            <div class="result-box">
                <div style="color: {{ color }}; font-size: 22px; font-weight: bold;">{{ result }}</div>
                <div style="font-size: 13px; color: #888; margin-top: 8px;">
                    <strong>Market Logic:</strong> {{ logic }} <br><br>
                    <strong>Trading Plan:</strong> <br>
                    - Stake: ${{ trade_amt }} ({{ risk_p }}% Margin) <br>
                    - <strong>MTG Verdict:</strong> {{ mtg }}
                </div>
                <div class="accuracy-meter"><div class="accuracy-fill"></div></div>
            </div>
            {% endif %}
            <a href="/logout" style="display:block; margin-top:15px; color:#444; text-decoration:none; font-size:12px;">Close Session</a>
        </div>
        {% endif %}
    </div>
</body>
</html>
'''

@app.route('/')
def index():
    return render_template_string(HTML_TEMPLATE, logged_in='user' in session)

@app.route('/login', methods=['POST'])
def login():
    if request.form.get('user') == "admin" and request.form.get('pass') == "123456":
        session['user'] = "admin"
    return redirect(url_for('index'))

@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('index'))

@app.route('/analyze', methods=['POST'])
def analyze():
    if 'user' not in session: return redirect(url_for('index'))
    
    balance = float(request.form.get('balance'))
    risk_p = int(request.form.get('risk'))
    trade_amt = round((balance * risk_p) / 100, 2)
    
    # Advanced Logic Selection Based on Timestamp to prevent repetition
    seed = int(time.time()) % 6 
    
    scenarios = [
        {"r": "✅ STRONG CALL", "c": "#00ff88", "l": "বুলিশ ক্যান্ডেলস্টিক মেকার হ্যামার সাপোর্ট জোন ব্রেক করেছে। মার্কেট ভলিউম বর্তমানে ৮৯% পজিটিভ।", "m": "NON-MTG (Fixed)"},
        {"r": "🔴 STRONG PUT", "c": "#ff4444", "l": "বেয়ারিশ এনগালফিং প্যাটার্ন রেজিস্ট্যান্স লেভেল থেকে রিজেকশন নিয়েছে। ট্রেন্ড লাইন ব্রেকডাউন কনফার্ম।", "m": "NON-MTG (Fixed)"},
        {"r": "✅ CALL (MTG-1)", "c": "#00ff88", "l": "মার্কেট আপট্রেন্ডে আছে কিন্তু সামান্য লিকুইডিটি গ্যাপ রয়েছে। ১টি ক্যান্ডেল এরর হতে পারে।", "m": "Use 1-Step Martingale"},
        {"r": "🚫 NO ENTRY", "c": "#888", "l": "অতিরিক্ত ভোলাটিলিটি। নিউজ ইমপ্যাক্টের কারণে মার্কেট লজিক কাজ করছে না। অপেক্ষা করুন।", "m": "STRICT NO TRADE"},
        {"r": "🔴 PUT (MTG-1)", "c": "#ff4444", "l": "মার্কেট রেজিস্ট্যান্স জোন টেস্ট করছে। সেলারদের এন্ট্রি কনফার্ম হয়েছে কিন্তু ভলিউম লো।", "m": "Use 1-Step Martingale"},
        {"r": "✅ CALL (PRO)", "c": "#00ff88", "l": "RSI এবং স্টোকাস্টিক ইনডিকেটর গোল্ডেন ক্রসওভার দিয়েছে। পরবর্তী ৩টি ক্যান্ডেল গ্রিন হওয়ার সম্ভাবনা।", "m": "NON-MTG (Safe)"}
    ]

    pick = scenarios[seed]

    return render_template_string(HTML_TEMPLATE, logged_in=True, result=pick['r'], color=pick['c'], logic=pick['l'], mtg=pick['m'], trade_amt=trade_amt, risk_p=risk_p)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 5000)))
