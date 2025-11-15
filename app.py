import importlib
import os
from flask import Flask

app = Flask(__name__)

def load_latest_version():
    files = [f for f in os.listdir('.') if f.startswith('NASA_QIRA_ULTRA_QUANTUM_') and f.endswith('.py')]
    if not files:
        raise FileNotFoundError("❌ לא נמצא קובץ גרסה של NASA_QIRA_ULTRA_QUANTUM")
    latest = sorted(files)[-1].replace('.py', '')
    module = importlib.import_module(latest)
    print(f"🟢 נטען המודול: {latest}")
    return module.app

app = load_latest_version()

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # ⭐ תיקון מלא – רנדר יקצה פורט תקין
    app.run(host="0.0.0.0", port=port)
