import importlib
import os
from flask import Flask, jsonify

app = Flask(__name__)

# --- טעינת גרסה אחרונה ---
def load_latest_version():
    files = [
        f for f in os.listdir('.')
        if f.startswith('NASA_QIRA_ULTRA_QUANTUM_') and f.endswith('.py')
    ]

    if not files:
        raise FileNotFoundError("❌ לא נמצא שום קובץ שמתחיל בשם של NASA_QIRA_ULTRA_QUANTUM")

    latest = sorted(files)[-1].replace('.py', '')
    module = importlib.import_module(latest)
    print(f"🟢 נטען בהצלחה: {latest}")
    return module

engine = load_latest_version()

# --- נקודת הרצה יחידה /run ---
@app.route("/run")
def run_once():
    if not hasattr(engine, "run_once"):
        return jsonify({
            "status": "error",
            "message": f"הפונקציה {engine.__name__} לא כוללת run_once"
        })

    try:
        # תחזית ראשית
        main_prediction = engine.run_main()

        # תחזית גיבוי אחת בלבד
        backup_prediction = engine.run_backup()

        result = {
            "main": main_prediction,
            "backup": backup_prediction
        }

        return jsonify({
            "status": "ok",
            "result": result
        })

    except Exception as e:
        return jsonify({
            "status": "error",
            "message": str(e)
        })

# --- הפעלה ---
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
