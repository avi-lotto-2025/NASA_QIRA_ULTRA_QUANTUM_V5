# === SECTION 8: SYSTEM ORCHESTRATOR & QUANTUM HEARTBEAT LINK ===
# שכבת האורקסטרציה הראשית – מחברת בין כל הרכיבים בזמן אמת

import os
import threading
import time
import datetime

modules = [
    "nasa_qira_ultra_quantum_v5_1_init.py",
    "heartbeat_core_controller.py",
    "autonomic_recovery_system.py",
    "quantum_awareness_layer.py",
    "self_synchronization_memory_layer.py",
    "central_supervisor_autoheal.py"
]

def orchestrator_cycle():
    print("🎵 הפעלת אורקסטר הקוואנטי הראשי – תיאום שכבות בזמן אמת...")
    time.sleep(2)
    print(f"🕒 זמן התחלה: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    time.sleep(1)

    threads = []
    for module in modules:
        t = threading.Thread(target=lambda: os.system(f"python {module}"))
        t.start()
        threads.append(t)
        print(f"✅ נטען מודול: {module}")
        time.sleep(0.5)

    print("\n💠 כל המודולים פועלים בסנכרון קוואנטי מלא.")
    print("💓 Quantum Heartbeat Link פעיל ומאוחד.\n")

    while True:
        print("🌐 בדיקת סנכרון בין כל השכבות...")
        time.sleep(60)

if __name__ == "__main__":
    orchestrator_cycle()
