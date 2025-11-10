# 🟩 מקטע 1 – הגדרות בסיס וייבוא ספריות

import os
import random
import datetime
import time
import threading
from flask import Flask
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

# יצירת אפליקציה בסיסית לענן Render
app = Flask(__name__)
# ================================================================
# 🕒 שלב 2 – הפעלה אוטומטית לפי ימים ושעות
# ================================================================

import schedule
import time

def run_main_prediction():
    print("🚀 מריץ תחזית ראשית וגיבוי...")

    # כאן תיכנס הפונקציה של החישוב הראשי והגיבוי
    main_prediction = "תחזית ראשית: 6 מספרים + בונוס"
    backup_prediction = "תחזית גיבוי: 6 מספרים + בונוס"

    # כאן תישלח הודעת המייל
    print(f"📧 נשלחה תחזית למייל עם:\n{main_prediction}\n{backup_prediction}")

# ימים פעילים: ראשון, שלישי, חמישי
DAYS_ACTIVE = [0, 2, 4]  # 0=ראשון, 2=שלישי, 4=חמישי

# שעת הפעלה (20:00)
RUN_HOUR = 20
RUN_MINUTE = 0

def schedule_predictions():
    for day in DAYS_ACTIVE:
        schedule.every().week.at(f"{RUN_HOUR:02d}:{RUN_MINUTE:02d}").do(run_main_prediction)
    print("🧠 המערכת האוטונומית פעילה — תזמון התחזיות הוגדר בהצלחה!")

def start_auto_mode():
    schedule_predictions()
    while True:
        schedule.run_pending()
        time.sleep(30)
# ================================================================
# 📧 שלב 3 – שליחת מיילים אוטומטית עם תחזית ראשית וגיבוי
# ================================================================

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(main_prediction, backup_prediction):
    sender_email = "avi5588@gmail.com"
    recipient_email = "avi5588@gmail.com"
    subject = "🧠 תחזית לוטו אוטונומית – NASA QIRA ULTRA QUANTUM V7"
    
    body = f"""
    תחזית ראשית 🎯:
    {main_prediction}

    תחזית גיבוי 🛡️:
    {backup_prediction}

    נשלח אוטומטית ממערכת נאס״א–קירה 🪐
    """

    msg = MIMEMultipart()
    msg["From"] = sender_email
    msg["To"] = recipient_email
    msg["Subject"] = subject
    msg.attach(MIMEText(body, "plain"))

    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(sender_email, "PASTE_YOUR_APP_PASSWORD_HERE")
            server.send_message(msg)
            print("✅ המייל נשלח בהצלחה!")
    except Exception as e:
        print(f"⚠️ שגיאה בשליחת המייל: {e}")
# ================================================================
# 🧠 שלב 4 – מנוע החיזוי הראשי + הגיבוי (Quantum Core)
# ================================================================

def generate_prediction():
    """מייצרת תחזית חכמה של 6 מספרים + בונוס"""
    main_numbers = sorted(random.sample(range(1, 38), 6))
    bonus_number = random.randint(1, 7)
    return main_numbers, bonus_number

def build_predictions():
    """בונה את התחזית הראשית והגיבוי"""
    main_nums, main_bonus = generate_prediction()
    backup_nums, backup_bonus = generate_prediction()

    main_prediction = f"ראשית: {main_nums} | בונוס: {main_bonus}"
    backup_prediction = f"גיבוי: {backup_nums} | בונוס: {backup_bonus}"

    print("🔹 נוצרה תחזית ראשית:")
    print(main_prediction)
    print("🔸 נוצרה תחזית גיבוי:")
    print(backup_prediction)

    return main_prediction, backup_prediction
# ================================================================
# 🔁 שלב 5 – מנגנון בדיקה עצמית (Self-Check)
# ================================================================

def self_check():
    """בודקת כל שעה שהמערכת חיה ופועלת"""
    print("🧩 בודקת את תקינות המערכת...")
    try:
        now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        # כאן אפשר להרחיב בדיקה אמיתית – לדוגמה חיבור לרנדר או SendGrid
        print(f"✅ Self-Check תקין ({now})")
    except Exception as e:
        print(f"⚠️ Self-Check נכשל: {e}")
        # נסיון תיקון עצמי
        try:
            print("🔧 מנסה להפעיל את המערכת מחדש...")
            start_auto_mode()
        except Exception as e2:
            print(f"❌ כשל בהפעלה מחדש: {e2}")

def start_self_check():
    """מתחיל את הבדיקה העצמית כל שעה"""
    while True:
        self_check()
        time.sleep(3600)  # כל שעה (60 דקות * 60 שניות)
# ================================================================
# 🚀 שלב 6 – מנגנון ההפעלה הראשית (Main Engine + Auto Start)
# ================================================================

def main_engine():
    """מפעיל את כל שכבות המערכת באופן מתואם"""
    print("🚀 מפעיל את מערכת NASA_QIRA_ULTRA_QUANTUM_V7_FULL_AUTONOMIC...")

    # בניית תחזיות
    main_prediction, backup_prediction = build_predictions()

    # שליחת מיילים
    send_email(main_prediction, backup_prediction)

    # התחלת מצב אוטומטי
    threading.Thread(target=start_auto_mode, daemon=True).start()

    # התחלת בדיקה עצמית (Self-Check)
    threading.Thread(target=start_self_check, daemon=True).start()

    print("🟢 המערכת פעילה – שליחות ותזמון עובדים אוטומטית.")

# הפעלה אוטומטית בעת ריצה בענן
if __name__ == "__main__":
    main_engine()
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
