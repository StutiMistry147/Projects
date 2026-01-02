import sqlite3
import time
import random

# Connect to (or create) the database
conn = sqlite3.connect('traffic.db')
cursor = conn.cursor()

# Create a table for web traffic
cursor.execute('''
    CREATE TABLE IF NOT EXISTS web_logs (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
        page_path TEXT,
        response_time_ms INTEGER,
        user_id INTEGER
    )
''')

pages = ['/home', '/products', '/cart', '/checkout', '/login']

print("Streaming data into traffic.db... (Press Ctrl+C to stop)")

try:
    while True:
        page = random.choice(pages)
        resp_time = random.randint(50, 1500)
        u_id = random.randint(1000, 9999)
        
        cursor.execute('INSERT INTO web_logs (page_path, response_time_ms, user_id) VALUES (?, ?, ?)', 
                       (page, resp_time, u_id))
        conn.commit()
        time.sleep(0.5) # Add a new log every half second
except KeyboardInterrupt:
    print("\nStream stopped.")
    conn.close()


