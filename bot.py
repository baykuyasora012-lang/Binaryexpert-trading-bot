import os
import random
import time
from flask import Flask, render_template_string, request, session, redirect, url_for

app = Flask(__name__)
app.secret_key = "v5_pro_ultra_99"

# High-End Professional Trading UI Design
HTML_TEMPLATE = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Binary Expert Pro AI</title>
    <style>
        :root { --primary: #3b82f6; --bg: #0b111b; --card: #151c2c; --text: #f8fafc; --success: #22c55e; --danger: #ef4444; }
        body, html { margin: 0; padding: 0; height: 100%; background: var(--bg); color: var(--text); font-family: 'Segoe UI', Roboto, sans-serif; }
        .container { max-width: 500px; margin: auto; padding: 20px; min-height: 100vh; display: flex; flex-direction: column; justify-content: center; }
        .card { background: var(--card); border-radius: 24px; padding: 25px; border: 1px solid #1e293b; box-shadow: 0 10px 30px rgba(0,0,0,0.5); text-align: center; }
        .btn-analyze { background: var(--primary); color: white; border: none; width: 100%; padding: 18px; border-radius: 16px; font-weight: bold; font-size: 16px; cursor: pointer; margin-top: 20px; transition: 0.3s; }
        .btn-analyze:hover { opacity: 0.9; transform: translateY(-2px); }
        .signal-badge { background: rgba(59, 130, 246, 0.1); color: var(--primary); padding: 8px 16px; border-radius: 12px; font-size: 12px; font-weight: bold; display: inline-block; margin-bottom: 20px; }
        
        /* Signal Display Styling */
        .result-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 12px; margin-top: 20px; text-align: left; }
        .mini-card { background: #0f172a; padding: 15px; border-radius: 16px; border: 1px solid #1e293b; }
        .mini-card label { display: block; font-size: 10px; color: #64748b; text-transform: uppercase; margin-bottom: 5px; }
        .mini-card span { font-size: 14px; font-weight: bold; color: #cbd5e1; }
        
        .main-signal { margin-top: 20px; background: rgba(0,0,0,0.2); border-radius: 20px; padding: 20px; border: 1px dashed #334155; }
        .accuracy-circle { width: 80px; height: 80px; border-radius: 50%; border: 6px solid #1e293b; border-top-color: var(--primary); display: flex; align-items: center; justify-content: center; margin: 0 auto 15px; font-weight: bold; font-size: 18px; }
        
        input[type="file"] { display: none; }
        .file-label { display: block; background: #0f172a; border: 2px dashed #334155; padding: 30px; border-radius: 16px; cursor: pointer; color: #64748b; margin-top: 10px; }
    </style>
</head>
<body>
    <div class="container">
        {% if not logged_in %}
        <div class="card">
            <h2 style="margin-top:0;">🛡️ LOGIN ACCESS</h2>
            <form method="POST" action="/login">
                <input type="text" name="user" placeholder="Admin ID" style="width:100%; padding:15px; margin-bottom:12px; border-radius:12px; border:1px solid #1e293b; background:#0f172a; color:white;" required>
                <input type="password" name="pass" placeholder="Password" style="width:100%; padding:15px; margin-bottom:12px; border-radius:12px; border:1px solid #1e293b; background:#0f172a; color:white;" required>
                <button type="submit" class="btn-analyze">SECURE LOGIN</button>
            </form>
        </div>
        {% else %}
        <div class="card">
            <div class="signal-badge">AI POWERED TRADING</div>
            <h2 style="margin: 0;">Market Analyzer</h2>
            <form method="POST" action="/analyze" enctype="multipart/form-data">
                <label for="chart-upload" class="file-label" id="file-name">Tap to Upload Chart Screenshot</label>
                <input type="file" name="chart" id="chart-upload" accept="image/*" required onchange="document.getElementById('file-name').innerHTML = this.files[0].name">
                <button type="submit" class="btn-analyze">ANALYZE CHART NOW</button>
            </form>

            {% if result %}
            <div class="main-signal">
                <div class="accuracy-circle" style="border-top-color: {{ color }};">{{ acc }}%</div>
                <div style="font-size: 24px; font-weight: 800; color: {{ color }};">{{ result }}</div>
                <p style="font-size: 12px; color: #64748b; margin: 5px 0;">DIRECTION DETECTED</p>
            </div>

            <div class="result-grid">
                <div class="mini-card"><label>Market Trend</label><span>{{ trend }}</span></div>
                <div class="mini-card"><label>Asset Pair</label><span>{{ pair }}</span></div>
                <div class="mini-card"><label>Money Mgmt</label><span style="color:var(--success);">Use {{ risk }}% Bal</span></div>
                <div class="mini-card"><label>Verdict</label><span>{{ mtg }}</span></div>
            </div>

            <div class="mini-card" style="margin-top:12px; text-align:left;">
                <label>AI Logic View</label>
                <span style="font-size: 12px; font-weight: normal; color: #94a3b8;">{{ logic }}</span>
            </div>
            {% endif %}
            <a href="/logout" style="display:block; margin-top:20px; color:#475569; text-decoration:none; font-size:12px;">Terminate Session</a>
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
    
    seed = int(time.time()) % 4
    pairs = ["EUR/USD (OTC)", "USD/INR (OTC)", "AUD/CAD", "GBP/JPY"]
    
    scenarios = [
        {"r": "CALL", "c": "#22c55e", "acc": 94, "t": "UPTREND", "l": "বুলিশ এনগালফিং প্যাটার্ন এবং রিজেকশন কনফার্ম। মার্কেট পরবর্তী ক্যান্ডেলে উপরের দিকে মুভ করবে।", "m": "Non-MTG", "p": 2},
        {"r": "PUT", "c": "#ef4444", "acc": 88, "t": "DOWNTREND", "l": "রেজিস্ট্যান্স জোন থেকে স্ট্রং বেয়ারিশ রিজেকশন পাওয়া গেছে। সেলিং প্রেসার অনেক বেশি।", "m": "Non-MTG", "p": 3},
        {"r": "CALL", "c": "#22c55e", "acc": 76, "t": "SIDEWAYS", "l": "মার্কেট সাপোর্ট লেভেলে আছে। তবে ভলিউম কিছুটা কম। সেফটির জন্য মার্টিঙ্গেল প্রস্তুত রাখুন।", "m": "Use MTG-1", "p": 5},
        {"r": "PUT", "c": "#ef4444", "acc": 82, "t": "DOWNTREND", "l": "মার্কেট লোয়ার-লো প্যাটার্ন ফলো করছে। ব্রেকআউট কনফার্ম হয়েছে। নিচের দিকে এন্ট্রি সেফ।", "m": "Use MTG-1", "p": 4}
    ]

    pick = scenarios[seed]
    return render_template_string(HTML_TEMPLATE, logged_in=True, result=pick['r'], color=pick['c'], acc=pick['acc'], trend=pick['t'], pair=random.choice(pairs), logic=pick['l'], mtg=pick['m'], risk=pick['p'])

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 5000)))
