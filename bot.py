import os
from flask import Flask, render_template_string, request

app = Flask(__name__)

# v3.2 Advanced UI & Logic Template
HTML_TEMPLATE = '''
<!DOCTYPE html>
<html>
<head>
    <title>Expert Bot v3.2 Pro</title>
    <style>
        body { background: #0a0a0a; color: #e0e0e0; font-family: 'Segoe UI', sans-serif; text-align: center; padding: 20px; }
        .container { max-width: 500px; margin: auto; background: #151515; border: 1px solid #333; padding: 20px; border-radius: 15px; box-shadow: 0 0 20px rgba(0,255,136,0.1); }
        .status-box { background: #000; border: 1px dashed #00ff88; padding: 15px; margin: 15px 0; border-radius: 10px; }
        .input-group { margin: 10px 0; text-align: left; }
        input, select { width: 100%; padding: 10px; background: #222; border: 1px solid #444; color: white; border-radius: 5px; box-sizing: border-box; }
        button { background: #00ff88; color: black; font-weight: bold; width: 100%; padding: 12px; border: none; border-radius: 5px; cursor: pointer; margin-top: 10px; }
        .credit { font-size: 14px; color: #888; margin-top: 10px; }
    </style>
</head>
<body>
    <div class="container">
        <h2 style="color: #00ff88;">Expert Trading v3.2</h2>
        <div class="credit">Credits: 1000 USD (Virtual)</div>
        
        <form method="POST" enctype="multipart/form-data">
            <div class="input-group">
                <label>Money Management Mode:</label>
                <select name="mgmt">
                    <option value="non-mtg">Non-MTG (Safe)</option>
                    <option value="mtg-1">MTG Level 1</option>
                    <option value="mtg-2">MTG Level 2 (High Risk)</option>
                </select>
            </div>
            
            <div class="input-group">
                <label>Initial Trade Amount ($):</label>
                <input type="number" name="amount" value="10" min="1">
            </div>

            <div class="input-group">
                <label>Upload Chart Screenshot:</label>
                <input type="file" name="chart" accept="image/*" required>
            </div>

            <button type="submit">START SMART ANALYSIS</button>
        </form>

        {% if result %}
        <div class="status-box">
            <h3 style="margin: 0;">Analysis Results:</h3>
            <p style="color: #ffcc00;">Strategy: {{ mgmt_mode }}</p>
            <p style="color: #00ff88; font-size: 18px; font-weight: bold;">{{ result }}</p>
            <p style="font-size: 12px;">Next Trade: ${{ next_amt }}</p>
        </div>
        {% endif %}
    </div>
</body>
</html>
'''

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        mgmt = request.form.get('mgmt')
        amount = int(request.form.get('amount'))
        
        # Martingale Logic
        next_trade = amount
        if mgmt == "mtg-1":
            next_trade = amount * 2.2
        elif mgmt == "mtg-2":
            next_trade = amount * 4.5

        # Signal Logic (Simulated for UI)
        return render_template_string(HTML_TEMPLATE, 
            result="✅ SIGNAL: Strong BUY Found (Accuracy 94%)", 
            mgmt_mode=mgmt.upper(),
            next_amt=round(next_trade, 2))
            
    return render_template_string(HTML_TEMPLATE)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
