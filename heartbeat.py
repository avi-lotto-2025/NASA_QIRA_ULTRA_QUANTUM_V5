import time
import requests

# === NASA_QIRA Quantum Heartbeat Eternal Engine ===
# מנגנון שמוודא שהמערכת נשארת פעילה ומעיר אותה כל 10 דקות בדיוק

TARGET_URL = "https://nasa-qira-ultra-quantum-v5-1.onrender.com"

def keep_alive():
    retry_delay = 60  # השהיה במצב שגיאה (בדקות × שניות)
    normal_delay = 600  # השהיה רגילה – 10 דקות

    while True:
        try:
            response = requests.get(TARGET_URL, timeout=20)
            if response.status_code == 200:
                print(f"[HEARTBEAT ✅] Ping sent successfully to {TARGET_URL}")
            else:
                print(f"[HEARTBEAT ⚠️] Unexpected status {response.status_code}")
        except requests.exceptions.RequestException as e:
            print(f"[HEARTBEAT ❌] Error: {e}")
            print(f"Retrying in {retry_delay} seconds...")
            time.sleep(retry_delay)
            continue  # מנסה שוב

        # השהיה של 10 דקות בין בדיקות
        time.sleep(normal_delay)

if __name__ == "__main__":
    print("🚀 NASA_QIRA_HEARTBEAT_AUTONOMIC_ENGINE initiated...")
    keep_alive()
