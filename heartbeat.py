import time
import requests

# === NASA_QIRA Quantum Heartbeat Eternal Loop ===
# מנגנון שמחזיק את המערכת בחיים ע"י בקשה חוזרת כל 10 דקות

TARGET_URL = "https://nasa-qira-ultra-quantum-v5-1.onrender.com"

def keep_alive():
    while True:
        try:
            response = requests.get(TARGET_URL)
            print(f"[HEARTBEAT] 🌐 Ping sent — Status {response.status_code}")
        except Exception as e:
            print(f"[HEARTBEAT ERROR] ⚠️ {e}")
        # המתנה של 10 דקות בין כל פעימה
        time.sleep(600)

if __name__ == "__main__":
    print("🚀 NASA_QIRA_HEARTBEAT_AUTONOMIC System Activated")
    keep_alive()
