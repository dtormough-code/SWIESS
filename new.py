import sqlite3
conn = sqlite3.connect('data.db')
cursor = conn.cursor()
conn.execute('''INSERT INTO notes (title, content) VALUES (?, ?)''',
             ("Shopping List", "Milk, eggs, bread"))
conn.commit()
# SELECT - read all notes
cursor.execute("SELECT * FROM notes")
rows = cursor.fetchall()
for row in rows:
    print(row)
#update
conn.execute('''UPDATE notes SET content = ?
 WHERE id = ?''', ("Milk, eggs, bread, butter", 1)) 
conn.commit()
#select after update
cursor.execute("SELECT * FROM notes")
rows = cursor.fetchall()
for row in rows:
    print(row)
# DELETE - remove the duplicate note
cursor.execute("DELETE FROM notes WHERE id = ?", (2,))
conn.commit()

# SELECT again to confirm
cursor.execute("SELECT * FROM notes")
for row in cursor.fetchall():
    print(row)
conn.close()    