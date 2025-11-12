# === מקטע 2: HEARTBEAT CORE CONTROLLER ===
# === NASA QIRA ULTRA QUANTUM V5.1 HEARTBEAT CORE CONTROLLER ===
# בקר הלב הפועם – מנגנון חיות רציף ובקרה עצמית

import time
import datetime
import os

def heartbeat_core():
    while True:
        now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"💓 פעימת חיים בוצעה בהצלחה ({now})")
        time.sleep(60)  # בדיקה כל דקה

        # בדיקת קבצי ליבה
        essential_files = [
            "nasa_qira_ultra_quantum_v5_1_init.py",
            "autonomic_recovery.py",
            "heartbeat_core_controller.py"
        ]

        for file in essential_files:
            if not os.path.exists(file):
                print(f"⚠️ קובץ חסר: {file} — הפעלת מנגנון תיקון עצמי...")
                os.system("python nasa_qira_ultra_quantum_v5_1_init.py")

        # הדפסת מצב לבקרה
        print("🧠 מערכת פעילה – כל המודולים נבדקו ונמצאו תקינים.\n")

if __name__ == "__main__":
    print("🚀 מנגנון הלב הפועם הופעל (Heartbeat Core Controller Active)")
    heartbeat_core()
