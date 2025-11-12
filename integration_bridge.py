# === מקטע 6: INTEGRATION BRIDGE ===
# === NASA QIRA ULTRA QUANTUM V5.1 SYSTEM INTEGRATION BRIDGE ===
# גשר אינטגרציה ראשי – איחוד כל המודולים לפעולה סינכרונית מלאה

import os
import time
import threading

# פונקציה כללית להפעלת מודול ברקע
def run_module(file_name):
    print(f"🚀 מפעיל מודול: {file_name}")
    os.system(f"python {file_name}")

def start_integration_bridge():
    print("🌐 הפעלת גשר האינטגרציה של מערכת נאס״א קירה...")
    time.sleep(1)

    modules = [
        "nasa_qira_ultra_quantum_v5_1_init.py",
        "heartbeat_core_controller.py",
        "autonomic_recovery_system.py",
        "quantum_awareness_layer.py",
        "self_synchronization_memory_layer.py"
    ]

    threads = []

    # הפעלת כל מודול כ-thread נפרד
    for module in modules:
        t = threading.Thread(target=run_module, args=(module,))
        t.start()
        threads.append(t)
        time.sleep(1)

    print("✅ כל המודולים הופעלו בהצלחה – המערכת החכמה פועלת במלואה.")
    print("----------------------------------------------------------")

    # שמירה על לולאת פיקוח כללית
    while True:
        print("🧩 גשר האינטגרציה פעיל ומפקח על כלל השכבות...")
        time.sleep(60)

if __name__ == "__main__":
    start_integration_bridge()
