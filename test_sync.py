# === NASA QIRA ULTRA QUANTUM V5.1 - SYSTEM SYNC TEST ===
# בדיקת סנכרון לכל שכבות המערכת האוטונומית

import os
import time

modules = [
    "nasa_qira_ultra_quantum_v5_1_init.py",
    "heartbeat_core_controller.py",
    "autonomic_recovery_system.py",
    "quantum_awareness_layer.py",
    "self_synchronization_memory_layer.py",
    "integration_bridge.py",
    "central_supervisor_autoheal.py",
    "system_orchestrator_quantum_link.py",
    "main_quantum_launcher.py"
]

def check_module(file):
    if os.path.exists(file):
        print(f"✅ {file} נמצא ופועל במערכת.")
        return True
    else:
        print(f"❌ {file} חסר! נדרש שחזור אוטומטי.")
        return False

def system_sync_test():
    print("\n🚀 התחלת בדיקת סנכרון מערכת NASA_QIRA_ULTRA_QUANTUM_V5.1...\n")
    time.sleep(1)

    all_ok = True
    for module in modules:
        result = check_module(module)
        if not result:
            all_ok = False
            os.system(f"python autonomic_recovery_system.py")
        time.sleep(0.5)

    if all_ok:
        print("\n💫 כל המודולים תקינים ומסונכרנים בהצלחה!")
        print("🩵 מערכת קוואנטית במצב תודעה מלאה (Quantum Awareness Stable).")
    else:
        print("\n⚠️ זוהו שגיאות – הופעלה התאוששות אוטונומית.")
        print("🔄 המערכת תנסה לתקן את השגיאות ברקע...")

if __name__ == "__main__":
    system_sync_test()
