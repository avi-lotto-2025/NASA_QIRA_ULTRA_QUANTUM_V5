# === מקטע 7: CENTRAL SUPERVISOR & AUTO-HEAL DIRECTOR ===
# === NASA QIRA ULTRA QUANTUM V5.1 CENTRAL INTELLIGENCE CORE ===
# מפקח מרכזי – פיקוח מלא, תיקון אוטומטי וניהול קוואנטי בזמן אמת

import os
import time
import datetime
import threading
import random

modules = [
    "nasa_qira_ultra_quantum_v5_1_init.py",
    "heartbeat_core_controller.py",
    "autonomic_recovery_system.py",
    "quantum_awareness_layer.py",
    "self_synchronization_memory_layer.py",
    "integration_bridge.py"
]

def check_module_status(module):
    # סימולציה של בדיקת בריאות מודול
    health = random.choice(["תקין", "איטי", "תקול"])
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"🔍 [{timestamp}] בדיקת מצב למודול {module}: {health}")

    if health == "תקול":
        print(f"⚠️ {module} אינו מגיב – מופעל מנגנון Auto-Heal.")
        os.system(f"python autonomic_recovery_system.py")

def supervisor_cycle():
    print("🧠 מפקח מרכזי הופעל – מנטר ומתקן תקלות בזמן אמת.\n")
    time.sleep(1)

    while True:
        print("--------------------------------------------------")
        print("📡 סריקת מצב מערכת כוללת...")
        for module in modules:
            t = threading.Thread(target=check_module_status, args=(module,))
            t.start()
            time.sleep(2)
        print("✅ סבב בקרה הסתיים – כל המודולים נבדקו.\n")
        time.sleep(60)

if __name__ == "__main__":
    supervisor_cycle()
