import importlib
import os
from flask import Flask

app = Flask(__name__)

# ======================================================
#  טעינת הגרסה החדשה ביותר של מערכת NASA_QIRA_ULTRA
# ======================================================
def load_latest_version():
    files = [
        f for f in os.listdir('.')
        if f.startswith('NASA_QIRA_ULTRA_QUANTUM_') and f.endswith('.py')
    ]

    if not files:
        raise FileNotFoundError("❌ לא נמצאה גרסה עדכנית של NASA_QIRA_ULTRA_QUANTUM")

    # לוקחים את הקובץ העדכני ביותר לפי מיון אלפביתי
    latest = sorted(files)[-1].replace('.py', '')
    module = importlib.import_module(latest)

    print(f"🌍 נטען המודול: {latest}")
    return module.app   # כל גרסה מכילה app פנימי

# טוען את הגרסה החדשה ביותר
app = load_latest_version()

# ======================================================
#  הרצה על Render – חובה להשתמש ב־PORT מהרנדר
# ======================================================
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))  
    print(f"🚀 שרת Flask מופעל על PORT {port}")
    app.run(host="0.0.0.0", port=port)
