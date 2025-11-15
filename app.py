import importlib
import os
from flask import Flask

app = Flask(__name__)

# ===============================
#  טוען את הגרסה האחרונה אוטומטית
# ===============================
def load_latest_version():
    files = [
        f for f in os.listdir('.')
        if f.startswith('NASA_QIRA_ULTRA_QUANTUM_') and f.endswith('.py')
    ]

    if not files:
        raise FileNotFoundError("❌ לא נמצאו קבצי מערכת של NASA_QIRA_ULTRA_QUANTUM")

    latest = sorted(files)[-1].replace('.py', '')
    module = importlib.import_module(latest)
    print(f"🟢 נטען מודול: {latest}")
    return module.app


# ===============================
#  דף בית — למניעת שגיאת 404
# ===============================
@app.route("/")
def home():
    return "<h1>🚀 NASA QIRA ULTRA – LIVE</h1><p>המערכת פעילה ומחוברת.</p>"


# ===============================
#  מטעין את הגרסה העדכנית
# ===============================
app = load_latest_version()


# ===============================
#  מריץ את השרת עם הפורט של Render
# ===============================
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    print(f"🚀 הפעלה על פורט: {port}")
    app.run(host="0.0.0.0", port=port)
