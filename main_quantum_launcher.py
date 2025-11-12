# === NASA QIRA ULTRA QUANTUM V5.1 – MAIN QUANTUM LAUNCHER ===
# מנגנון הפעלה ראשי: שליטה אוטונומית מלאה + תיקון עצמי + שליטה ידנית

import os
import time
import threading
import datetime

modules = [
    "nasa_qira_ultra_quantum_v5_1_init.py",
    "heartbeat_core_controller.py",
    "autonomic_recovery_system.py",
    "quantum_awareness_layer.py",
    "self_synchronization_memory_layer.py",
    "integration_bridge.py",
    "central_supervisor_autoheal.py",
    "system_orchestrator_quantum_link.py"
]

def run_module(module):
    print(f"🚀 מפעיל מודול: {module}")
    os.system(f"python {module}")

def manual_trigger():
    print("\n🟢 מצב ידני הופעל – הפעלה מיידית של כל המערכת!\n")
    for module in modules:
        threading.Thread(target=run_module, args=(module,)).start()

def auto_cycle():
    while True:
        print(f"\n🕒 [{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] הפעלה אוטונומית מחזורית – בודקת את כל המערכת...\n")
        for module in modules:
            if not os.path.exists(module):
                print(f"⚠️ קובץ חסר: {module} — ניסיון שחזור...")
                os.system("python autonomic_recovery_system.py")
            else:
                threading.Thread(target=run_module, args=(module,)).start()
        print("💤 מצב תחזוקה – מנוחה לשעתיים לפני המחזור הבא...\n")
        time.sleep(7200)  # 120 דקות = שעתיים

if __name__ == "__main__":
    print("🌌 מערכת NASA QIRA ULTRA QUANTUM V5.1 מוכנה להפעלה.\n")
    print("בחר פעולה:\n1️⃣ הפעלה ידנית (Manual Trigger)\n2️⃣ מצב אוטונומי (Auto Cycle)\n")
    mode = input("הקלד 1 או 2 והקש Enter: ").strip()
    
    if mode == "1":
        manual_trigger()
    else:
        auto_cycle()
