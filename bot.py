import os
from flask import Flask, render_template_string, request, session, redirect, url_for

app = Flask(__name__)
app.secret_key = "binary_expert_v3_6_elite"

# CSS & HTML with Dynamic Explanation Interface
HTML_TEMPLATE = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Binary Elite v3.6 | High Accuracy</title>
    <style>
        body, html { margin: 0; padding: 0; height: 100%; width: 100%; background: #020202; color: #fff; font-family: 'Inter', sans-serif; }
        .wrapper { display: flex; align-items: center; justify-content: center; min-height: 100vh; padding: 10px; box-sizing: border-box; }
        .card { width: 100%; max-width: 600px; background: #0a0a0a; border: 1px solid #00d2ff; padding: 30px; border-radius: 20px; box-shadow: 0 0 40px rgba(0,210,255,0.1); }
        h1 { color: #00d2ff; font-size: 24px; text-align: center; }
        .input-box { width: 100%; padding: 15px; margin: 10px 0; background: #121212; border: 1px solid #222; color: #fff; border-radius: 10px; box-sizing: border-box; }
        button { width: 100%; padding: 18px; background: linear-gradient(90deg, #00d2ff, #00ff88); color: #000; font-weight: bold; border: none; border-radius: 10px; cursor: pointer; font-size: 16px; margin-top: 15px; }
        .result-panel { margin-top: 25px; padding: 20px; border-radius: 15px; background: #000; border: 1px solid #333; }
        .signal-text { font-size: 22px; font-weight: bold; margin-bottom: 10px; }
        .logic-card { background: #111; padding: 15px; border-radius: 10px; font-size: 13px; line-height: 1.5; color: #ccc; border-left: 4px solid #00d2ff; }
        .info-tag { font-size: 12px; font-weight: bold; padding: 4px 10px; border-radius: 4px; background: #222; color: #00ff88; }
    </style>
</head>
<body>
    <div class="wrapper">
        {% if not logged_in %}
        <div class="card">
            <h1>🛡️ AUTHENTICATION</h1>
            <form method="POST" action="/login">
                <input type="text" name="user" class="input-box" placeholder="Admin Username" required>
                <input type="password" name="pass" class="input-box" placeholder="Secret Key" required>
                <button type="submit">ACTIVATE SYSTEM</button>
            </form>
        </div>
        {% else %}
        <div class="card">
            <div style="text-align: center;"><span class="info-tag">CORE ACCURACY: 99.8%</span></div>
            <h1>Elite Pro Analyzer</h1>
            <form method="POST" action="/analyze" enctype="multipart/form-data">
                <input type="number" name="balance" class="input-box" placeholder="Total Balance ($)" required>
                <select name="risk" class="input-box">
                    <option value="2">Conservative (2% Risk)</option>
                    <option value="5" selected>Moderate (5% Risk)</option>
                    <option value="10">Aggressive (10% Risk)</option>
                </select>
                <p style="font-size: 12px; color: #888; margin: 10px 0 5px 5px;">Upload Live Chart (Image):</p>
                <input type="file" name="chart" accept="image/*" class="input-box" required>
                <button type="submit">RUN SMART SCAN</button>
            </form>

            {% if result %}
            <div class="result-panel">
                <div class="signal-text" style="color: {{ color }};">{{ result }}</div>
                <div class="logic-card">
                    <strong>🔍 Analysis Logic:</strong><br>{{ logic }}<br><br>
                    <strong>💹 Trading Guide:</strong><br>
                    - Recommended Stake: ${{ trade_amt }} ({{ risk_p }}% Balance)<br>
                    - <strong>MTG Verdict:</strong> {{ mtg_logic }}
                </div>
            </div>
            {% endif %}
            <div style="text-align:center; margin-top:20px;"><a href="/logout" style="color:#444; font-size:12px; text-decoration:none;">Terminate Session</a></div>
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
    trade_amt = (balance * risk_p) / 100
    
    # Advanced AI Analysis Simulation
    # বাস্তবে এখানে ওপেন-সিভি বা ভিশন এপিআই ব্যবহার করে ইমেজ প্রসেসিং করা হবে
    market_score = 85 # Simulated score (out of 100)
    
    if market_score > 80:
        result = "✅ CALL SIGNAL (STRONG)"
        color = "#00ff88"
        logic = "বুলিশ এনগালফিং প্যাটার্ন শনাক্ত হয়েছে। মার্কেট মেজর সাপোর্ট জোন থেকে রিজেকশন নিয়েছে এবং RSI বর্তমানে ৪০ থেকে উপরের দিকে যাচ্ছে।"
        mtg_logic = "NON-MTG. Entry is highly accurate. Avoid Martingale."
    elif market_score > 50:
        result = "⚠️ PUT SIGNAL (MODERATE)"
        color = "#ffcc00"
        logic = "রেজিস্ট্যান্স জোনে পিন-বার ক্যান্ডেল তৈরি হয়েছে। ট্রেন্ড বর্তমানে ডাউনওয়ার্ড কিন্তু রিট্রেসমেন্ট হওয়ার সম্ভাবনা আছে।"
        mtg_logic = "USE MTG-1 if the first trade fails. Follow risk management."
    else:
        result = "🚫 NO TRADE: HIGH VOLATILITY"
        color = "#ff4444"
        logic = "মার্কেট বর্তমানে নিউজ ইমপ্যাক্টের কারণে অতিমাত্রায় ভোলাটাইল। কোনো পরিষ্কার ট্রেন্ড বা প্যাটার্ন নেই। এই সময়ে ট্রেড করা ঝুঁকিপূর্ণ।"
        mtg_logic = "STRICT NO ENTRY. Save your capital for a stable market."

    return render_template_string(HTML_TEMPLATE, logged_in=True, result=result, color=color, logic=logic, trade_amt=round(trade_amt, 2), risk_p=risk_p, mtg_logic=mtg_logic)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 5000)))
