# ============================================
# NASA_ULTRA_KIRA_AUTONOMIC_FINAL_V3.2.py
# Quantum-Aware Autonomous Lotto Prediction System
# ============================================

import numpy as np
import random
import datetime
import time
import json
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# =====================================================
# ⚙️ הגדרות מערכת בסיסיות
# =====================================================

VERSION = "NASA_ULTRA_KIRA_AUTONOMIC_FINAL_V3.2"
MAIN_DRAW = (6, 37)   # 6 מתוך 37
BONUS_DRAW = (1, 7)   # בונוס אחד מתוך 7
DAILY_TRAIN_HOUR = 2  # 02:00
RUN_HOURS = [20]      # שלישי / חמישי / שבת 20:00

EMAIL_USER = "avi5588@gmail.com"
EMAIL_PASS = "placeholder_password"  # נחליף אח"כ במשתנה סביבה
RECIPIENT = "avi5588@gmail.com"

# =====================================================
# 🧩 שכבת רדינסקי (Kira Layer): חיזוי לפי דפוסי זמן
# =====================================================

def kira_time_pattern_layer(history):
    """
    ניתוח לפי תדירות, מרווחי זמן, וסטיות תקן.
    מחקה את הגישה של קירה רדינסקי – חיזוי לפי הקשרים הסתברותיים בזמן.
    """
    all_numbers = [num for draw in history for num in draw['main']]
    freq = {i: all_numbers.count(i) for i in range(1, MAIN_DRAW[1]+1)}
    avg = np.mean(list(freq.values()))
    std = np.std(list(freq.values()))

    # משקל יתר למספרים שהופיעו בתדירות קרובה לממוצע + סטייה קטנה
    weights = {n: 1 / (abs(freq[n] - avg) + std + 0.1) for n in freq}
    return weights

# =====================================================
# 🌌 שכבת נאס"א-על: שכבת הסתברות חכמה
# =====================================================

def nasa_ultra_layer(weights):
    """
    בונה שכבת הסתברות הסתגלותית לפי משקלים דינמיים.
    """
    numbers = list(weights.keys())
    probs = np.array(list(weights.values()))
    probs = probs / np.sum(probs)
    chosen = np.random.choice(numbers, size=MAIN_DRAW[0], replace=False, p=probs)
    return sorted(chosen)

# =====================================================
# 🎲 שכבת Monte Carlo
# =====================================================

def monte_carlo_layer(weights, iterations=40000):
    results = []
    numbers = list(weights.keys())
    probs = np.array(list(weights.values()))
    probs = probs / np.sum(probs)

    for _ in range(iterations):
        draw = tuple(sorted(np.random.choice(numbers, size=MAIN_DRAW[0], replace=False, p=probs)))
        results.append(draw)

    # ספירת שכיחות
    unique, counts = np.unique(results, axis=0, return_counts=True)
    top = sorted(list(zip(unique, counts)), key=lambda x: x[1], reverse=True)[:5]
    return [list(x[0]) for x in top]

# =====================================================
# 🧬 שכבת למידה עצמית
# =====================================================

def self_learning_layer(history, new_prediction):
    """
    מעדכן את ההיסטוריה באופן הסתגלותי.
    """
    timestamp = datetime.datetime.now().isoformat()
    history.append({
        "timestamp": timestamp,
        "main": new_prediction,
        "bonus": random.randint(1, BONUS_DRAW[1])
    })
    return history[-200:]  # שומר רק את 200 האחרונים

# =====================================================
# 💌 שליחת תחזית במייל
# =====================================================

def send_email(pred_main, pred_bonus, backups):
    subject = f"🎯 תחזית לוטו אוטונומית – גרסה {VERSION}"
    body = f"""
    🧠 תחזית ראשית: {pred_main} | בונוס: {pred_bonus}
    🔄 סטי גיבוי:
    1️⃣ {backups[0]}
    2️⃣ {backups[1]}
    3️⃣ {backups[2]}
    4️⃣ {backups[3]}
    5️⃣ {backups[4]}

    הופק אוטומטית על ידי המוח האוטונומי NASA-ULTRA-KIRA 🪐
    """

    msg = MIMEMultipart()
    msg['From'] = EMAIL_USER
    msg['To'] = RECIPIENT
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(EMAIL_USER, EMAIL_PASS)
        server.send_message(msg)
        server.quit()
        print("✅ מייל נשלח בהצלחה.")
    except Exception as e:
        print("⚠️ שגיאה בשליחת המייל:", e)

# =====================================================
# 🧩 פונקציית הרצה כוללת
# =====================================================

def run_autonomic_cycle():
    print(f"\n🚀 הרצה אוטונומית – גרסה {VERSION}")
    # טעינת היסטוריה
    try:
        with open("quantum_brain_state.json", "r", encoding="utf-8") as f:
            history = json.load(f)
    except FileNotFoundError:
        history = []

    # שכבות
    weights = kira_time_pattern_layer(history)
    main_prediction = nasa_ultra_layer(weights)
    backups = monte_carlo_layer(weights)
    bonus = random.randint(1, BONUS_DRAW[1])

    # עדכון המוח
    updated_history = self_learning_layer(history, main_prediction)

    # שמירה
    with open("quantum_brain_state.json", "w", encoding="utf-8") as f:
        json.dump(updated_history, f, ensure_ascii=False, indent=2)

    # שליחה
    send_email(main_prediction, bonus, backups)

# =====================================================
# 🕒 תזמון חכם (אוטונומי)
# =====================================================

def autonomic_scheduler():
    while True:
        now = datetime.datetime.now()
        if now.hour == DAILY_TRAIN_HOUR:
            print("🧠 שלב אימון עצמי יומי...")
            run_autonomic_cycle()

        if now.hour in RUN_HOURS and now.weekday() in [1, 3, 5]:
            print("🎯 הרצה קבועה ליום הגרלה...")
            run_autonomic_cycle()

        time.sleep(3600)  # בדיקה כל שעה

# =====================================================
# ▶️ הרצה חד פעמית (לבדיקה)
# =====================================================

if __name__ == "__main__":
    print(f"🤖 מערכת {VERSION} הופעלה.")
    run_autonomic_cycle()
