import sqlite3
conn = sqlite3.connect('data.db')
cursor= conn.cursor()
conn.execute ('''
    CREATE TABLE IF NOT EXISTS notes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        content TEXT,
        created_at TEXT DEFAULT CURRENT_TIMESTAMP
    )
''')
conn.commit()
conn.close()
print("Database and table created successfully.")