# =====================================================
# NASA_QIRA_ULTRA_QUANTUM_V5 - Flask Autonomous System
# =====================================================

import numpy as np
import random
import datetime
import time
import json
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from flask import Flask

# =====================================================
# 📡 הגדרות מערכת חכמה לשכבות
# =====================================================
VERSION = "NASA_QIRA_ULTRA_QUANTUM_V5"
MAIN_DRAW = (1, 37)
BONUS_DRAW = (1, 7)
RUN_HOURS = [20]
EMAIL_USER = "avi5588@gmail.com"
EMAIL_PASS = "placeholder_password"
RECIPIENT = "avi5588@gmail.com"

# =====================================================
# 🎲 פונקציית תחזית מספרים (כולל בונוס)
# =====================================================
def generate_prediction():
    main_numbers = sorted(random.sample(range(MAIN_DRAW[0], MAIN_DRAW[1] + 1), 6))
    bonus = random.choice(range(BONUS_DRAW[0], BONUS_DRAW[1] + 1))
    return main_numbers, bonus

# =====================================================
# 📧 שליחת תחזית במייל
# =====================================================
def send_email(main, bonus):
    try:
        msg = MIMEMultipart()
        msg['From'] = EMAIL_USER
        msg['To'] = RECIPIENT
        msg['Subject'] = f"🎯 תחזית חדשה ממערכת {VERSION}"

        body = f"תחזית ראשית: {main}\nמספר בונוס: {bonus}"
        msg.attach(MIMEText(body, 'plain'))

        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(EMAIL_USER, EMAIL_PASS)
        server.send_message(msg)
        server.quit()

        print("✅ מייל נשלח בהצלחה!")
    except Exception as e:
        print(f"⚠️ שגיאה בשליחת מייל: {e}")

# =====================================================
# 🔁 לולאת ההפעלה המרכזית
# =====================================================
def run_autonomic_cycle():
    main, bonus = generate_prediction()
    print(f"\n🎯 תחזית ראשית: {main} | 💫 בונוס: {bonus}")
    send_email(main, bonus)

# =====================================================
# 🌐 Flask Web Server (לענן Render)
# =====================================================
app = Flask(__name__)

@app.route('/')
def home():
    return f"🚀 מערכת {VERSION} פועלת בהצלחה בענן!"

if __name__ == "__main__":
    run_autonomic_cycle()
    app.run(host="0.0.0.0", port=10000)
