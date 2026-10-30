import sqlite3

conn = sqlite3.connect('data.db')
conn.row_factory = sqlite3.Row

for row in conn.execute('SELECT * FROM categories'):
    print(dict(row))

for row in conn.execute('SELECT id, title, category_id FROM notes'):
    print(dict(row))
for row in conn.execute('SELECT id, title, summary, study_questions FROM notes'):
    print(dict(row))

conn.close()