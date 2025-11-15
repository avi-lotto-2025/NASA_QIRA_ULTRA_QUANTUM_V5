import importlib
import os
from flask import Flask, jsonify

app = Flask(__name__)

def load_latest_version():
    files = [f for f in os.listdir('.') if f.startswith('NASA_QIRA_ULTRA_QUANTUM_') and f.endswith('.py')]
    if not files:
        raise FileNotFoundError("❌ לא נמצא שום קובץ NASA_QIRA_ULTRA_QUANTUM")
    latest = sorted(files)[-1].replace('.py', '')
    module = importlib.import_module(latest)
    print(f"🟢 נטען המודול: {latest}")
    return module

engine = load_latest_version()

@app.route("/")
def home():
    return "🚀 NASA QIRA ULTRA QUANTUM — המערכת פעילה!"

@app.route("/run")
def run_once():
    try:
        result = engine.run_once()
        return jsonify({"status": "ok", "result": result})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
