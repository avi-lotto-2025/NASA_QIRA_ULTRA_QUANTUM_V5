# === NASA QIRA ULTRA QUANTUM V5.1 INIT CORE ===
# ליבת האתחול של המערכת האוטונומית

import time
import datetime
import os

def system_init():
    print("🚀 אתחול מערכת נאס״א קירה – גרסה 5.1 התחיל...")
    print("⏳ טוען מודולים בסיסיים...")

    time.sleep(1)
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"🧠 ליבה הופעלה בהצלחה ({now})")
    print("❤️ מנגנון החיים הראשוני פעיל (Heartbeat Initiated)")
    print("🔁 מצב תיקון עצמי מוכן (Auto-Heal Standby)")
    print("--------------------------------------------------")

if __name__ == "__main__":
    system_init()
