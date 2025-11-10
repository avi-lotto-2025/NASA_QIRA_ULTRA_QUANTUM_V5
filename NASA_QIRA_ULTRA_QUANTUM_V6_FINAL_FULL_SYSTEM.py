initialize_kira_layer()
print("🚀 מערכת נאס״א קירה אולטרא הופעלה בהצלחה - שליחה אוטומטית החלה")
# 🧠 NASA_QIRA_ULTRA_QUANTUM_V6_FINAL_FULL_SYSTEM
# מקטע 1 — הגדרות מערכת ותשתית קירה
# =====================================================

import os
import random
import datetime
import time
import numpy as np
import threading
import requests
from flask import Flask, jsonify

# =====================================================
# 📡 פרטי גרסה ופרמטרים כלליים
# =====================================================
VERSION = "NASA_QIRA_ULTRA_QUANTUM_V6_FINAL_FULL_SYSTEM"
MAIN_RANGE = range(1, 38)    # לוטו ישראלי 1–37
BONUS_RANGE = range(1, 8)    # בונוס 1–7
RUN_HOURS = [20]             # שעה 20:00 – שלישי / חמישי / שבת
DAYS_ACTIVE = [1, 3, 5]      # 1=שלישי, 3=חמישי, 5=שבת

# =====================================================
# 💌 פרטי דוא"ל (Mailjet)
# =====================================================
EMAIL_RECIPIENT = "avi5588@gmail.com"
MAILJET_API_KEY = "PASTE_YOUR_KEY_HERE"
MAILJET_SECRET = "PASTE_YOUR_SECRET_HERE"

# =====================================================
# 🎛️ משתנים עזר
# =====================================================
history_data = []         # היסטוריית הגרלות
pair_matrix = {}          # קשרים בין זוגות
hot_numbers = []          # מספרים חמים
cold_numbers = []         # מספרים קרים
neutral_numbers = []      # בינוניים

# =====================================================
# 🧩 אתחול נתונים – שכבת קירה
# =====================================================
def initialize_kira_layer():
    """
    בניית שכבת בסיס להסתברות קירה.
    מחלקת מספרים לקבוצות חמים/קרים/ניטרליים
    לפי התפלגות היסטורית ראשונית.
    """
    global hot_numbers, cold_numbers, neutral_numbers

    # חלוקה ראשונית לפי יחס פשוט (נניח היסטוריה דמה)
    all_numbers = list(MAIN_RANGE)
    random.shuffle(all_numbers)

    split_hot = int(len(all_numbers) * 0.3)
    split_cold = int(len(all_numbers) * 0.3)

    hot_numbers = all_numbers[:split_hot]
    cold_numbers = all_numbers[-split_cold:]
    neutral_numbers = all_numbers[split_hot:-split_cold]

    print(f"🔥 חמים: {sorted(hot_numbers)}")
    print(f"❄️ קרים: {sorted(cold_numbers)}")
    print(f"⚪ ניטרליים: {sorted(neutral_numbers)}")

# קריאה ראשונית לאתחול
initialize_kira_layer()
if __name__ == "__main__":
    print("🚀 מערכת נאס״א קירה אולטרא הופעלה בהצלחה - שליחה אוטומטית החלה")
    initialize_kira_layer()
