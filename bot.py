import os
from flask import Flask, render_template_string, request, session, redirect, url_for

app = Flask(__name__)
app.secret_key = "binary_ultra_secret_123"

# লগইন এবং ড্যাশবোর্ডের পূর্ণাঙ্গ ডিজাইন
HTML_TEMPLATE = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Expert Bot v3.3 Pro</title>
    <style>
        body, html { margin: 0; padding: 0; height: 100%; width: 100%; background: #080808; color: white; font-family: 'Segoe UI', sans-serif; overflow-x: hidden; }
        .full-screen { display: flex; flex-direction: column; align-items: center; justify-content: center; min-height: 100vh; width: 100%; padding: 20px; box-sizing: border-box; }
        .card { width: 95%; max-width: 600px; background: #111; border: 1px solid #00ff88; padding: 30px; border-radius: 20px; box-shadow: 0 0 30px rgba(0,255,136,0.2); text-align: center; }
        input, select { width: 100%; padding: 15px; margin: 10px 0; background: #1a1a1a; border: 1px solid #333; color: white; border-radius: 8px; font-size: 16px; box-sizing: border-box; }
        button { width: 100%; padding: 15px; background: #00ff88; color: black; font-weight: bold; border: none; border-radius: 8px; cursor: pointer; font-size: 18px; transition: 0.3s; }
        button:hover { background: #00cc6a; transform: scale(1.02); }
        .status { margin-top: 20px; padding: 15px; background: #000; border: 1px dashed #00ff88; border-radius: 10px; }
        .credit-info { color: #00ff88; font-weight: bold; margin-bottom: 20px; font-size: 1.2rem; }
    </style>
</head>
<body>
    <div class="full-screen">
        {% if not logged_in %}
        <div class="card">
            <h1 style="color: #00ff88;">🛡️ SYSTEM LOGIN</h1>
            <form method="POST" action="/login">
                <input type="text" name="user" placeholder="Username" required>
                <input type="password" name="pass" placeholder="Security Key" required>
                <button type="submit">UNLOCK SYSTEM</button>
            </form>
        </div>
        {% else %}
        <div class="card">
            <h1 style="color: #00ff88;">Expert Trading v3.3</h1>
            <div class="credit-info">Available Credit: $5,000.00</div>
            
            <form method="POST" action="/analyze" enctype="multipart/form-data">
                <select name="mgmt">
                    <option value="non-mtg">Non-MTG (Fixed Amount)</option>
                    <option value="mtg-1">Martingale Level 1</option>
                    <option value="mtg-2">Martingale Level 2</option>
                </select>
                <input type="number" name="amount" placeholder="Trade Amount ($)" value="10">
                <p style="text-align: left; margin: 10px 0 5px 5px; font-size: 14px; color: #888;">Upload Chart Screenshot:</p>
                <input type="file" name="chart" accept="image/*" required>
                <button type="submit">START FULL ANALYSIS</button>
            </form>

            {% if result %}
            <div class="status">
                <h3 style="margin: 0; color: #00ff88;">Result: {{ result }}</h3>
                <p style="margin: 5px 0 0 0; font-size: 14px;">Next Trade Suggestion: ${{ next_amt }}</p>
            </div>
            {% endif %}
            <a href="/logout" style="color: #ff4444; text-decoration: none; display: block; margin-top: 20px; font-size: 14px;">Logout from Session</a>
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
    mgmt = request.form.get('mgmt')
    amount = float(request.form.get('amount'))
    next_amt = amount * (2.2 if mgmt == "mtg-1" else 4.5 if mgmt == "mtg-2" else 1.0)
    return render_template_string(HTML_TEMPLATE, logged_in=True, result="✅ STRONG BUY SIGNAL", next_amt=round(next_amt, 2))

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 5000)))
