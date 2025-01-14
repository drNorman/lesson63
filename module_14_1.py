import sqlite3

connection1 = sqlite3.connect("not_telegram.db")
cursor1 = connection1.cursor()

cursor1.execute('''
CREATE TABLE IF NOT EXISTS Users(
id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER,
balance INTEGER NOT NULL
)
''')

cursor1.execute(" CREATE INDEX IF NOT EXISTS idx_email ON Users (email)")

for i in range(10):
    cursor1.execute(" INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)", (f"User{i+1}", f"example{i+1}@gmail.com", (i+1)*10, 1000))

for i in range(5):
    cursor1.execute(" UPDATE Users SET balance = ? WHERE id = ?", (500, (i*2)+1))

for i in range(1,11,3):
    cursor1.execute(" DELETE FROM Users WHERE id = ?", (i,))

cursor1.execute("SELECT username, email, age, balance FROM Users WHERE age != 60")

users = cursor1.fetchall()
for user in users:
    print(f"Имя: {user[0]} | Почта: {user[1]} | Возраст: {user[2]} | Баланс: {user[3]}")

connection1.commit()
connection1.close()