import sqlite3
import os

DB_PATH = os.path.join(os.path.dirname(__file__), "alerts.db")

def init_db():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("""
    CREATE TABLE IF NOT EXISTS alerts (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        camera TEXT,
        reason TEXT,
        priority TEXT,
        evidence TEXT,
        time TEXT
    )
    """)
    conn.commit()
    conn.close()

def save_alert(camera, reason, priority, evidence, time):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute(
        "INSERT INTO alerts (camera, reason, priority, evidence, time) VALUES (?, ?, ?, ?, ?)",
        (camera, reason, priority, evidence, time)
    )
    conn.commit()
    conn.close()
