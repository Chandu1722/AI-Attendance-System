import sqlite3
from datetime import datetime

DB_NAME = "attendance.db"


def init_db():

    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS attendance (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        date TEXT,
        time TEXT,
        session_id TEXT
    )
    """)

    conn.commit()
    conn.close()


def mark_attendance(name, session_id):

    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    date_now = datetime.now().date()
    time_now = datetime.now().strftime("%H:%M:%S")

    cursor.execute("""
        INSERT INTO attendance (name, date, time, session_id)
        VALUES (?, ?, ?, ?)
    """, (name, date_now, time_now, session_id))

    conn.commit()
    conn.close()


def get_total_attendance():

    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
        SELECT name, COUNT(*) as total
        FROM attendance
        GROUP BY name
        ORDER BY total DESC
    """)

    data = cursor.fetchall()

    conn.close()
    return data