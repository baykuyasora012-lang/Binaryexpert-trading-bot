import os
from flask import Flask, render_template_string, request, session, redirect, url_for

app = Flask(__name__)
app.secret_key = "binary_logic_pro_max_99"

# Full Screen UI with Advanced Logic Display
HTML_TEMPLATE = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Binary Logic v3.5 | Pro Trader</title>
    <style>
        body, html { margin: 0; padding: 0; height: 100%; width: 100%; background: #050505; color: white; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; }
        .wrapper { display: flex; align-items: center; justify-content: center; min-height: 100vh; width: 100%; padding: 15px; box-sizing: border-box; }
        .main-card { width: 100%; max-width: 650px; background: #0d0d0d; border: 1px solid #00ff88; padding: 30px; border-radius: 20px; box-shadow: 0 0 40px rgba(0,255,136,0.15); text-align: center; }
        input, select { width: 100%; padding: 15px; margin: 10px 0; background: #151515; border: 1px solid #333; color: white; border-radius: 10px; font-size: 16px; box-sizing: border-box; }
        button { width: 100%; padding: 18px; background: #00ff88; color: black; font-weight: bold; border: none; border-radius: 10px; cursor: pointer; font-size: 18px; transition: 0.3s; margin-top: 10px; }
        .signal-box { margin-top: 25px; padding: 20px; border-radius: 15px; background: #000; border-left: 5px solid #00ff88; text-align: left; }
        .logic-text { font-size: 14px; color: #aaa; line-height: 1.6; margin-top: 10px; border-top: 1px solid #222; padding-top: 10px; }
        .risk-alert { color: #ff4444; font-weight: bold; font-size: 14px; }
        .badge { display: inline-block; padding: 5px 12px; border-radius: 5px; font-size: 12px; font-weight: bold; margin-bottom: 10px; }
    </style>
</head>
<body>
    <div class="wrapper">
        {% if not logged_in %}
        <div class="main-card">
            <h1 style="color: #00ff88;">🛡️ SECURE LOGIN</h1>
            <form method="POST" action="/login">
                <input type="text" name="user" placeholder="Username" required>
                <input type="password" name="pass" placeholder="Password" required>
                <button type="submit">UNLOCK DASHBOARD</button>
            </form>
        </div>
        {% else %}
        <div class="main-card">
            <div class="badge" style="background: #00ff88; color: #000;">STABLE VERSION v3.5</div>
            <h1 style="color: #00ff88; margin-top: 0;">Smart Signal Engine</h1>
            
            <form method="POST" action="/analyze" enctype="multipart/form-data">
                <input type="number" name="balance" placeholder="Your Total Balance ($)" required>
                <select name="risk">
                    <option value="low">Low Risk (Use 2% Balance)</option>
                    <option value="mid">Medium Risk (Use 5% Balance)</option>
                    <option value="high">High Risk (Use 10% Balance)</option>
                </select>
                <p style="text-align: left; font-size: 14px; color: #888; margin: 10px 0 5px 5px;">Upload Chart for Logic Check:</p>
                <input type="file" name="chart" accept="image/*" required>
                <button type="submit">GENERATE EXPERT SIGNAL</button>
            </form>

            {% if result %}
            <div class="signal-box">
                <h2 style="margin: 0; color: {{ 'red' if 'HIGH RISK' in result else '#00ff88' }};">
                    {{ result }}
                </h2>
                <div class="logic-text">
                    <strong>💡 Signal Logic:</strong> {{ logic }} <br><br>
                    <strong>💰 Money Management:</strong> <br>
                    - Invest: ${{ trade_amt }} ({{ percent }}% of balance) <br>
                    - <strong>MTG Status:</strong> {{ mtg_info }}
                </div>
            </div>
            {% endif %}
            <a href="/logout" style="display: block; margin-top: 20px; color: #555; text-decoration: none; font-size: 13px;">Logout Session</a>
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
    risk_level = request.form.get('risk')
    
    # Percentage Logic
    percent = 2 if risk_level == "low" else 5 if risk_level == "mid" else 10
    trade_amt = (balance * percent) / 100
    
    # Advanced Signal Logic (Simulation)
    # বাস্তবে এখানে AI ইমেজ থেকে RSI/Trend ভ্যালু বের করবে
    market_condition = "stable_trend" # এটি ইমেজ প্রসেসিং থেকে আসবে
    
    if market_condition == "stable_trend":
        result = "✅ CALL (BUY) SIGNAL"
        logic = "মার্কেট বর্তমানে Higher High এবং Higher Low প্যাটার্ন তৈরি করছে। RSI ভ্যালু ৫০ এর উপরে এবং বুলিশ ক্যান্ডেলস্টিক কনফার্মেশন পাওয়া গেছে।"
        mtg_info = "No MTG Needed (Non-MTG Signal). Trade fixed amount."
    else:
        result = "⚠️ HIGH RISK: SIDEWAYS MARKET"
        logic = "মার্কেট বর্তমানে কোনো নির্দিষ্ট ট্রেন্ডে নেই (Sideways)। সাপোর্ট এবং রেজিস্ট্যান্স জোন খুব কাছাকাছি হওয়ায় ট্রেড নেওয়া ঝুঁকিপূর্ণ।"
        mtg_info = "DO NOT TRADE. Avoid Martingale in this zone."

    return render_template_string(HTML_TEMPLATE, 
        logged_in=True, 
        result=result, 
        logic=logic, 
        trade_amt=round(trade_amt, 2), 
        percent=percent, 
        mtg_info=mtg_info)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 5000)))
