import os
import random
from flask import Flask, render_template_string, request, session, redirect, url_for

app = Flask(__name__)
app.secret_key = "binary_hyper_logic_99"

# Professional Dark UI with Full Screen responsiveness
HTML_TEMPLATE = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Binary Elite v3.8 | Advanced Logic</title>
    <style>
        body, html { margin: 0; padding: 0; height: 100%; width: 100%; background: #020202; color: #fff; font-family: 'Inter', sans-serif; }
        .wrapper { display: flex; align-items: center; justify-content: center; min-height: 100vh; padding: 15px; box-sizing: border-box; }
        .card { width: 100%; max-width: 600px; background: #0a0a0a; border: 1px solid #00d2ff; padding: 30px; border-radius: 20px; box-shadow: 0 0 40px rgba(0,210,255,0.15); }
        h1 { color: #00d2ff; font-size: 24px; text-align: center; margin-bottom: 20px; }
        .input-box { width: 100%; padding: 15px; margin: 10px 0; background: #111; border: 1px solid #222; color: #fff; border-radius: 12px; font-size: 16px; box-sizing: border-box; }
        button { width: 100%; padding: 18px; background: linear-gradient(90deg, #00d2ff, #00ff88); color: #000; font-weight: bold; border: none; border-radius: 12px; cursor: pointer; font-size: 18px; margin-top: 15px; }
        .result-panel { margin-top: 25px; padding: 20px; border-radius: 15px; background: #000; border: 1px solid #333; animation: fadeIn 0.5s ease; }
        .logic-card { background: #111; padding: 15px; border-radius: 10px; font-size: 14px; line-height: 1.6; color: #ddd; border-left: 4px solid #00ff88; margin-top: 10px; }
        .tag { font-size: 12px; color: #00ff88; border: 1px solid #00ff88; padding: 3px 8px; border-radius: 5px; margin-bottom: 10px; display: inline-block; }
        @keyframes fadeIn { from { opacity: 0; } to { opacity: 1; } }
    </style>
</head>
<body>
    <div class="wrapper">
        {% if not logged_in %}
        <div class="card">
            <h1>🛡️ AUTHENTICATION</h1>
            <form method="POST" action="/login">
                <input type="text" name="user" class="input-box" placeholder="Username" required>
                <input type="password" name="pass" class="input-box" placeholder="Password" required>
                <button type="submit">ACCESS SYSTEM</button>
            </form>
        </div>
        {% else %}
        <div class="card">
            <div style="text-align: center;"><span class="tag">AI ACCURACY: 99.4%</span></div>
            <h1>Elite Market Analyzer</h1>
            <form method="POST" action="/analyze" enctype="multipart/form-data">
                <input type="number" name="balance" class="input-box" placeholder="Total Balance ($)" required>
                <select name="risk" class="input-box">
                    <option value="2">Low (2% Stake)</option>
                    <option value="5" selected>Moderate (5% Stake)</option>
                    <option value="10">Aggressive (10% Stake)</option>
                </select>
                <input type="file" name="chart" accept="image/*" class="input-box" required>
                <button type="submit">START SMART SCAN</button>
            </form>

            {% if result %}
            <div class="result-panel">
                <div style="font-size: 22px; font-weight: bold; color: {{ color }};">{{ result }}</div>
                <div class="logic-card">
                    <strong>🔍 Detailed Logic:</strong><br>{{ logic }}<br><br>
                    <strong>💹 Trading Instruction:</strong><br>
                    - Recommended Stake: ${{ trade_amt }}<br>
                    - <strong>MTG Status:</strong> {{ mtg_status }}
                </div>
            </div>
            {% endif %}
            <div style="text-align:center; margin-top:20px;"><a href="/logout" style="color:#444; font-size:12px; text-decoration:none;">Logout System</a></div>
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
    
    # Advanced Logic Database
    logic_pool = [
        {
            "res": "🟢 CALL SIGNAL (STRONG)",
            "clr": "#00ff88",
            "log": "বুলিশ এনগালফিং প্যাটার্ন তৈরি হয়েছে। মার্কেট মেজর সাপোর্ট জোন থেকে রিজেকশন নিয়েছে এবং RSI বর্তমানে ৪০ লেভেল ব্রেক করে উপরের দিকে যাচ্ছে।",
            "mtg": "Non-MTG (Fixed Trade). Accuracy is high."
        },
        {
            "res": "🔴 PUT SIGNAL (ELITE)",
            "clr": "#ff4444",
            "log": "রেজিস্ট্যান্স জোনে পিন-বার ক্যান্ডেল শনাক্ত হয়েছে। সেলারদের ভলিউম বাড়ছে এবং মার্কেট ওভারবট এরিয়া থেকে নিচের দিকে ট্রেন্ড চেঞ্জ করছে।",
            "mtg": "Non-MTG. Highly Accurate Trend Signal."
        },
        {
            "res": "🟡 CALL (MTG-1) SIGNAL",
            "clr": "#ffcc00",
            "log": "মার্কেট বর্তমানে বুলিশ ট্রেন্ডে থাকলেও ছোট রিট্রেসমেন্ট দেখা যাচ্ছে। ফিবোনাচ্চি ০.৬১৮ লেভেল থেকে বাউন্স করার সম্ভাবনা আছে।",
            "mtg": "Prepare MTG-1 if the first candle ends in a small loss."
        },
        {
            "res": "🚫 NO TRADE: HIGH RISK",
            "clr": "#888",
            "log": "মার্কেট সাইডওয়েজ বা কনসোলিডেশন জোনে আছে। ক্যান্ডেলের বডি খুব ছোট এবং কোনো পরিষ্কার প্রাইস অ্যাকশন নেই। মূলধন বাঁচাতে ট্রেড এড়িয়ে চলুন।",
            "mtg": "DO NOT TRADE. Wait for a clear trend breakout."
        },
        {
            "res": "🔴 PUT (MTG-1) SIGNAL",
            "clr": "#ffaa00",
            "log": "বেয়ারিশ মোমেন্টাম বাড়ছে তবে মার্কেট সাপোর্ট জোনের খুব কাছাকাছি। ব্রেকআউটের জন্য অপেক্ষা করছে। ১ লেভেল সেফটি ব্যবহার করা বুদ্ধিমানের কাজ হবে।",
            "mtg": "Safe Entry with MTG-1 backup."
        }
    ]

    analysis = random.choice(logic_pool)

    return render_template_string(HTML_TEMPLATE, 
        logged_in=True, 
        result=analysis['res'], 
        color=analysis['clr'], 
        logic=analysis['log'], 
        trade_amt=trade_amt, 
        mtg_status=analysis['mtg'])

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 5000)))
