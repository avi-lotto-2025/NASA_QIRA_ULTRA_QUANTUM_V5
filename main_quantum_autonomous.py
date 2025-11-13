import time
from main_quantum_launcher import auto_cycle

def autostart():
    """
    הפעלה אוטונומית מלאה של מערכת QIRA ULTRA.
    אין שום שימוש ב-input, אין שאלה למשתמש.
    המערכת רצה לנצח, או עד קריסה – ואז מבצעת התאוששות.
    """
    while True:
        try:
            print("\n🚀 הפעלה אוטומטית – מערכת QIRA ULTRA פועלת בענן ללא הפסקה...\n")
            
            # הפעלת המנוע הראשי (הפעלה של כל המודולים והמחזורים)
            auto_cycle()

            # אם auto_cycle תחזור (זה נדיר), נחכה קצת ונחזור למחזור הבא
            print("✔️ מחזור הסתיים. המערכת תחזור בעוד 10 שניות...\n")
            time.sleep(10)

        except Exception as e:
            print("❌ שגיאה במערכת:", e)
            print("⏳ ניסיון התאוששות בעוד 30 שניות...\n")
            time.sleep(30)

if __name__ == "__main__":
    autostart()
