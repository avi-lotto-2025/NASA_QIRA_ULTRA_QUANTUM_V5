# === מקטע 2 – AUTONOMIC RECOVERY MODULE ===
# מנגנון חיצוני ששולח פולסים לשרת אחת ל-8 דקות, כדי לשמור אותו ער וחי לנצח.

import time
import requests

TARGET_URL = "https://nasa-qira-ultra-quantum-v5-1.onrender.com"

def recovery_loop():
    print("🩵 [AUTONOMIC_RECOVERY] System initiated. Eternal monitoring started.")
    while True:
        try:
            response = requests.get(TARGET_URL, timeout=15)
            if response.status_code == 200:
                print("💚 [RECOVERY] System stable – server alive.")
            else:
                print(f"🟠 [RECOVERY ALERT] Unexpected status {response.status_code} – attempting restart...")
        except Exception as e:
            print(f"❤️‍🔥 [RECOVERY WARNING] Connection failed: {e}")
        time.sleep(480)  # 8 דקות

if __name__ == "__main__":
    recovery_loop()
