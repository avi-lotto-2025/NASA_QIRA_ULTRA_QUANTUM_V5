# === מקטע 5: SELF-SYNCHRONIZATION & MEMORY PERSISTENCE LAYER ===
# === NASA QIRA ULTRA QUANTUM V5.1 MEMORY CORE ===
# שכבת הזיכרון והסנכרון העצמי – שימור מצב, שחזור והתאוששות חלקה

import json
import os
import datetime
import time

STATE_FILE = "system_memory_state.json"

def load_state():
    if os.path.exists(STATE_FILE):
        with open(STATE_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)
            print(f"🧠 מצב קודם נטען ({data.get('last_update')})")
            return data
    else:
        print("🧠 לא נמצא מצב קודם – אתחול זיכרון חדש...")
        return {"status": "initialized", "last_update": None}

def save_state(data):
    data["last_update"] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(STATE_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
    print(f"💾 מצב נשמר ({data['last_update']})")

def sync_memory_cycle():
    print("🔄 מחזור סנכרון זיכרון פעיל...")
    state = load_state()

    # עדכון דינמי
    state["system_status"] = "active"
    state["last_sync"] = datetime.datetime.now().strftime("%H:%M:%S")
    save_state(state)

    print("✅ סנכרון הושלם – המערכת מעודכנת ומודעת לעצמה.\n")
    time.sleep(5)

if __name__ == "__main__":
    while True:
        sync_memory_cycle()
