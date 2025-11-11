# ==============================================================
# 🚀 NASA_QIRA_ULTRA_QUANTUM_V7.1_FULL_AUTONOMIC_HEARTBEAT
# מערכת נאס״א קירה עם מנגנון התעוררות שקטה כל 10 דקות
# ==============================================================
import os
import random
import datetime
import threading
import time
from flask import Flask, jsonify

app = Flask(__name__)

# ==============================================================
# ⚙️ הגדרות בסיסיות
# ==============================================================
VERSION = "NASA_QIRA_ULTRA_QUANTUM_V7.1_FULL_AUTONOMIC_HEARTBEAT"
RUN_INTERVAL_MINUTES = 10  # התעוררות כל 10 דקות

# ==============================================================
# 🔄 מנגנון התעוררות שקט (Heartbeat)
# ==============================================================
def heartbeat():
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"[💓] מנגנון התעוררות פעיל - שעה: {current_time}")
    # לא נשלח מייל – רק שומר את המערכת חיה
    threading.Timer(RUN_INTERVAL_MINUTES * 60, heartbeat).start()

# התחלה אוטומטית
heartbeat()

# ==============================================================
# 🌐 שרת Flask לשירותי המערכת
# ==============================================================
@app.route('/')
def home():
    return jsonify({
        "status": "🟢 LIVE",
        "version": VERSION,
        "heartbeat": "מערכת ערה ומוכנה"
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
# ==========================================================
# 💓 מנגנון התעוררות אוטומטי כל 10 דקות (ללא שליחת מייל)
# ==========================================================

def heartbeat():
    while True:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        print(f"[💓] מנגנון התעוררות פעיל - שעה: {current_time}")
        time.sleep(600)  # כל 10 דקות

# הפעלת המנגנון ברקע
heartbeat_thread = threading.Thread(target=heartbeat, daemon=True)
heartbeat_thread.start()
