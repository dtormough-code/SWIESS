import sqlite3

conn = sqlite3.connect('data.db')
cursor = conn.cursor()
cursor.execute("""CREATE TABLE IF NOT EXISTS categories (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE
)"""    )
conn.execute
('ALTER TABLE notes ADD COLUMN category_id INTEGER REFERENCES categories(id)')
conn.cursor
conn.execute("INSERT INTO categories (name) VALUES (?)", ("Personal",))

# TODO: do the same for "School"
conn.execute("INSERT INTO categories (name) VALUES (?)", ("School",))

conn.commit()   
conn.close()
print("Database updated!")