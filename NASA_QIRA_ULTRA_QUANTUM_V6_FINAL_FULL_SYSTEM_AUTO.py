# ================================================================
#  NASA_QIRA_ULTRA_QUANTUM_V6_FINAL_FULL_SYSTEM_AUTO.py
#  גרסה סופית, נקייה, אוטונומית, מוכנה לענן (Render)
#  כולל: שכבת "קירה", תחזית ראשית + גיבוי, שליחת מייל, Flask,
#         והרצות אוטומטיות ג'/ה'/שבת ב-20:00 (שעון ישראל),
#         + הרצה חד-פעמית מיד עם עליית השרות.
# ================================================================

import os
import random
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from flask import Flask, jsonify
from threading import Thread
import schedule
import time
from datetime import datetime
try:
    # Python 3.9+
    from zoneinfo import ZoneInfo
    TZ_IL = ZoneInfo("Asia/Jerusalem")
except Exception:
    TZ_IL = None  # אם אין zoneinfo, נלך לפי זמן שרת

# ===================== פרמטרים וכללים ===========================
VERSION = "NASA_QIRA_ULTRA_QUANTUM_V6_FINAL_FULL_SYSTEM"
EMAIL_USER = "avi5588@gmail.com"
EMAIL_PASS = os.getenv("EMAIL_PASS", "")  # שים סיסמת אפליקציה ב-Render → Environment
RECIPIENT = "avi5588@gmail.com"

MAIN_RANGE = range(1, 38)     # לוטו ישראלי 1-37
BONUS_RANGE = range(1, 8)     # בונוס 1-7
DRAW_DAYS = ("tuesday", "thursday", "saturday")  # ימים להרצה אוטומטית
DRAW_TIME = "20:00"           # שעת ההרצה האוטומטית

# משקלים לשכבת קירה: חלוקה חמה/ניטרלית/קרה
WEIGHTS_MAIN   = {"hot": 0.60, "neutral": 0.30, "cold": 0.10}
WEIGHTS_BACKUP = {"hot": 0.25, "neutral": 0.50, "cold": 0.25}

# מצב אחרון להצגה ב-API
LAST_STATUS = {
    "version": VERSION,
    "last_run_at": None,
    "main": None,
    "bonus_main": None,
    "backup": None,
    "bonus_backup": None,
    "email_sent": False,
    "email_error": None
}

# =============== שכבת "קירה" — חלוקה חם/קר/ניטרלי =================
hot_numbers = []
cold_numbers = []
neutral_numbers = []

def initialize_kira_layer():
    """
    מחלק את המספרים לקטגוריות "חמים", "קרים", "ניטרליים".
    פה אנחנו מסמלצים היסטוריה ע"י ערבוב וחלוקה יחסית (30/40/30),
    אפשר להחליף בהמשך בחלוקה אמיתית לפי היסטוריית הגרלות.
    """
    global hot_numbers, cold_numbers, neutral_numbers
    nums = list(MAIN_RANGE)
    random.shuffle(nums)

    # 30% חמים, 40% ניטרליים, 30% קרים
    n = len(nums)
    n_hot = int(n * 0.30)
    n_cold = int(n * 0.30)
    hot_numbers     = sorted(nums[:n_hot])
    cold_numbers    = sorted(nums[-n_cold:])
    neutral_numbers = sorted(nums[n_hot:n - n_cold])

# =================== מחוללי תחזיות (ראשית/גיבוי) =================
def _choose_from_groups(weights, k=6):
    """
    בוחר k מספרים מתוך שלוש הקבוצות לפי משקלים נתונים.
    דואג ללא כפילויות; אם חסר – משלים באקראי מכל הטווח.
    """
    pool = []
    group_choices = ["hot", "neutral", "cold"]
    group_weights = [weights["hot"], weights["neutral"], weights["cold"]]

    while len(pool) < k:
        grp = random.choices(group_choices, weights=group_weights, k=1)[0]
        if grp == "hot" and hot_numbers:
            pool.append(random.choice(hot_numbers))
        elif grp == "neutral" and neutral_numbers:
            pool.append(random.choice(neutral_numbers))
        elif grp == "cold" and cold_numbers:
            pool.append(random.choice(cold_numbers))

        pool = sorted(set(pool))

        if len(pool) < k and len(pool) + 1 > len(set(pool)):
            # אם נתקענו מחוסר גיוון, נשלים אקראי מהטווח כולו
            pool.append(random.choice(list(MAIN_RANGE)))
            pool = sorted(set(pool))

    return sorted(pool)

def generate_main_prediction():
    main = _choose_from_groups(WEIGHTS_MAIN, k=6)
    bonus = random.choice(list(BONUS_RANGE))
    return main, bonus

def generate_backup_prediction():
    backup = _choose_from_groups(WEIGHTS_BACKUP, k=6)
    bonus = random.choice(list(BONUS_RANGE))
    return backup, bonus

# ========================= דוא"ל ================================
def send_email(main, bonus_main, backup, bonus_backup):
    subject = f"תחזית לוטו — {VERSION}"
    body = (
        "✅ תחזית ראשית:\n"
        f"{main} | בונוס: {bonus_main}\n\n"
        "🟣 תחזית גיבוי:\n"
        f"{backup} | בונוס: {bonus_backup}\n\n"
        f"גרסה: {VERSION}"
    )

    try:
        msg = MIMEMultipart()
        msg["From"] = EMAIL_USER
        msg["To"] = RECIPIENT
        msg["Subject"] = subject
        msg.attach(MIMEText(body, "plain", "utf-8"))

        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(EMAIL_USER, EMAIL_PASS)
        server.send_message(msg)
        server.quit()
        return True, None
    except Exception as e:
        return False, str(e)

# ======================= ריצת מערכת =============================
def run_once():
    initialize_kira_layer()
    main, bonus_main = generate_main_prediction()
    backup, bonus_backup = generate_backup_prediction()

    ok, err = send_email(main, bonus_main, backup, bonus_backup)

    now = datetime.now(TZ_IL) if TZ_IL else datetime.utcnow()
    LAST_STATUS.update({
        "last_run_at": now.strftime("%Y-%m-%d %H:%M:%S") + (" Asia/Jerusalem" if TZ_IL else " UTC"),
        "main": main,
        "bonus_main": bonus_main,
        "backup": backup,
        "bonus_backup": bonus_backup,
        "email_sent": ok,
        "email_error": err
    })

    # הדפסה ללוגים של Render (בעברית)
    print("==============================================")
    print(f"🟢 הרצה בוצעה ({LAST_STATUS['last_run_at']}):")
    print(f"   תחזית ראשית: {main} | בונוס: {bonus_main}")
    print(f"   תחזית גיבוי: {backup} | בונוס: {bonus_backup}")
    if ok:
        print("   ✉️ מייל נשלח בהצלחה!")
    else:
        print(f"   ⚠️ כשל בשליחת מייל: {err}")
    print("==============================================")

# ===================== תזמון אוטומטי ============================
def _scheduler_loop():
    # 3 מועדים בשבוע בשעה 20:00
    schedule.every().tuesday.at(DRAW_TIME).do(run_once)
    schedule.every().thursday.at(DRAW_TIME).do(run_once)
    schedule.every().saturday.at(DRAW_TIME).do(run_once)

    while True:
        schedule.run_pending()
        time.sleep(1)

def start_scheduler_thread():
    t = Thread(target=_scheduler_loop, daemon=True)
    t.start()

# ========================= Flask API ============================
app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({
        "version": VERSION,
        "status": "OK",
        "last_run": LAST_STATUS
    })

# ====================== הפעלה בענן Render =======================
if __name__ == "__main__":
    # מריצים פעם אחת מיד בהפעלה
    run_once()
    # מפעילים מתזמן שבועי
    start_scheduler_thread()
    # שרת Flask להצגת סטטוס (Render מצפה לשירות מאזין)
    app.run(host="0.0.0.0", port=10000)
# ==========================================================
# שליחת עדכון תחזיות במייל – מנגנון אוטומטי
# ==========================================================
import smtplib
from email.mime.text import MIMEText
from datetime import datetime

def send_update_email():
    now = datetime.now().strftime("%d/%m/%Y %H:%M")
    subject = f"תחזית לוטו אוטומטית - עדכון {now}"
    body = f"🚀 התחזית החדשה הופעלה בהצלחה במערכת NASA_QIRA_ULTRA_QUANTUM_V6_AUTO\n\nזמן הפעלה: {now}\n\nנשלח אוטומטית מהשרת ברנדר."
    msg = MIMEText(body)
    msg["Subject"] = subject
    msg["From"] = "avi5588@gmail.com"
    msg["To"] = "avi5588@gmail.com"

    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login("avi5588@gmail.com", os.getenv("EMAIL_PASS"))
        server.send_message(msg)
        server.quit()
        print("✅ נשלח מייל עדכון בהצלחה")
    except Exception as e:
        print("⚠️ שגיאה בשליחת מייל:", e)

# קריאה אוטומטית בעת סיום הריצה
send_update_email()
