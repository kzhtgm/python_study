import sqlite3

conn = sqlite3.connect('example.db')
cursor = conn.cursor()

cursor.execute("CREATE TABLE users(id real, name text, birthday text)")

cursor.execute("INSERT INTO users VALUES (1, 'かず', '1978-01-20')")
cursor.execute("INSERT INTO users VALUES (2, 'さき', '1982-11-11')")
cursor.execute("INSERT INTO users VALUES (3, 'あおい', '2018-11-17')")

conn.commit()

for row in cursor.execute('SELECT * FROM users ORDER BY birthday DESC'):
    print(row)

cursor.execute("DROP TABLE users")

conn.close()

