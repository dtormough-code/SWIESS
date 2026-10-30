import sqlite3

conn = sqlite3.connect('data.db')
conn.execute('ALTER TABLE notes ADD COLUMN category_id INTEGER REFERENCES categories(id)')
conn.commit()
conn.close()
print("Column added!")