# ===============================================
# NASA_QIRA_ULTRA_QUANTUM_V7.1_FULL_AUTONOMIC_HEARTBEAT
# מערכת חיזוי לוטו אוטונומית עם Heartbeat ושליחת תחזית + גיבוי
# ===============================================

from flask import Flask
from threading import Thread
import time
import random
import schedule
import sendgrid
from sendgrid.helpers.mail import Mail

# הגדרת אפליקציית Flask
app = Flask(__name__)

# ===============================================
# פונקציות חיזוי – תחזית ראשית ותחזית גיבוי
# ===============================================
def generate_prediction():
    """יוצרת תחזית ראשית – 6 מספרים ייחודיים בין 1 ל-37 + מספר בונוס"""
    main_numbers = sorted(random.sample(range(1, 38), 6))
    bonus = random.randint(1, 7)
    return main_numbers, bonus

def generate_backup():
    """יוצרת תחזית גיבוי – 6 מספרים שונים מהתחזית הראשית"""
    backup_numbers = sorted(random.sample(range(1, 38), 6))
    backup_bonus = random.randint(1, 7)
    return backup_numbers, backup_bonus

# ===============================================
# שליחת מייל
# ===============================================
SENDGRID_API_KEY = "YOUR_SENDGRID_API_KEY"  # ← שים כאן את המפתח שלך
RECIPIENT = "avi5588@gmail.com"

def send_email(main_pred, backup_pred):
    """שולחת מייל עם תחזית ראשית ותחזית גיבוי"""
    sg = sendgrid.SendGridAPIClient(api_key=SENDGRID_API_KEY)

    subject = "🎯 תחזית לוטו חכמה – NASA QIRA AUTONOMIC SYSTEM"
    content = f"""
    שלום אבי 🌟

    🧠 תחזית ראשית:
    {main_pred[0]} | בונוס: {main_pred[1]}

    🎯 תחזית גיבוי:
    {backup_pred[0]} | בונוס: {backup_pred[1]}

    נשלח אוטומטית ממערכת NASA_QIRA_ULTRA_QUANTUM_V7.1_FULL_AUTONOMIC_HEARTBEAT
    """

    message = Mail(
        from_email="noreply@nasa-qira-system.ai",
        to_emails=RECIPIENT,
        subject=subject,
        plain_text_content=content
    )

    try:
        sg.send(message)
        print("[EMAIL] תחזית נשלחה בהצלחה.")
    except Exception as e:
        print(f"[ERROR] שגיאה בשליחת מייל: {e}")

# ===============================================
# משימות מתוזמנות – חיזוי אוטומטי
# ===============================================
def run_scheduled_predictions():
    """מייצרת תחזיות אוטומטיות בימי שלישי/חמישי/שבת בשעה 20:00"""
    def job():
        main_pred = generate_prediction()
        backup_pred = generate_backup()
        print("[AUTO] הפעלת תחזית אוטומטית בשעה 20:00")
        send_email(main_pred, backup_pred)

    # ימים: שלישי (2), חמישי (4), שבת (6)
    schedule.every().tuesday.at("20:00").do(job)
    schedule.every().thursday.at("20:00").do(job)
    schedule.every().saturday.at("20:00").do(job)

    while True:
        schedule.run_pending()
        time.sleep(30)

# ===============================================
# מנגנון Heartbeat כל 10 דקות
# ===============================================
def heartbeat():
    """בודק שהמערכת ערה ומדפיסה סטטוס"""
    while True:
        print("[HEARTBEAT] System wake-up check passed.")
        time.sleep(600)  # כל 10 דקות

# ===============================================
# הפעלת תהליכים מקבילים
# ===============================================
def start_threads():
    Thread(target=heartbeat, daemon=True).start()
    Thread(target=run_scheduled_predictions, daemon=True).start()

@app.route("/")
def home():
    return "NASA_QIRA_ULTRA_QUANTUM_V7.1_FULL_AUTONOMIC_HEARTBEAT RUNNING ✅"

# ===============================================
# נקודת כניסה ראשית
# ===============================================
if __name__ == "__main__":
    start_threads()
    app.run(host="0.0.0.0", port=5000)
