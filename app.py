from flask import Flask, jsonify
import os
import random

app = Flask(__name__)

# ---------------------------------------------------
# שכבת תחזית ראשית
# ---------------------------------------------------
def run_main():
    try:
        numbers = random.sample(range(1, 38), 6)
        return sorted(numbers)
    except Exception as e:
        return {"error": True, "message": str(e)}

# ---------------------------------------------------
# שכבת גיבוי
# ---------------------------------------------------
def run_backup():
    try:
        numbers = random.sample(range(1, 38), 6)
        return sorted(numbers)
    except Exception as e:
        return {"error": True, "message": str(e)}

# ---------------------------------------------------
# פונקציה חד-פעמית — זו שרנדר קורא ב־/run
# ---------------------------------------------------
def run_once():
    try:
        main_numbers = run_main()
        backup_numbers = run_backup()

        return {
            "main": main_numbers,
            "backup": backup_numbers
        }

    except Exception as e:
        return {
            "error": True,
            "message": str(e)
        }

# ---------------------------------------------------
# ניתוב Flask — הבקשה ש־Render שולח
# ---------------------------------------------------
@app.route("/run", methods=["GET"])
def run_endpoint():
    try:
        result = run_once()
        return jsonify({
            "status": "success",
            "result": result
        })
    except Exception as e:
        return jsonify({
            "status": "error",
            "message": str(e)
        })

# ---------------------------------------------------
# הפעלת השרת ב־Render
# ---------------------------------------------------
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
