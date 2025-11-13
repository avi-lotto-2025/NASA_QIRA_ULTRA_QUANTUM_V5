import time
from main_quantum_launcher import run_full_system

def autostart():
    while True:
        try:
            print("🚀 הפעלה אוטומטית – מערכת QIRA ULTRA רצה בענן...")
            run_full_system()     # מפעיל את כל המוחות, החישובים והמייל
            print("✔️ תחזית נשלחה בהצלחה. המתנה למחזור הבא...")
            time.sleep(60 * 60)   # המתנה שעה (Heartbeat טבעי)
        except Exception as e:
            print("❌ שגיאה:", e)
            print("⏳ ניסיון מחדש בעוד 30 שניות...")
            time.sleep(30)

if __name__ == "__main__":
    autostart()
