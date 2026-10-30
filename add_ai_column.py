import sqlite3

conn = sqlite3.connect('data.db')
conn.execute('ALTER TABLE notes ADD COLUMN summary TEXT')
conn.execute('ALTER TABLE notes ADD COLUMN study_questions TEXT')
conn.commit()
conn.close()
print("Columns added!")