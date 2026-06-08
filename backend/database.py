import sqlite3

conn = sqlite3.connect('portfolio.db')

cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS projects (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT,
    description TEXT
)
''')


cursor.execute('''
CREATE TABLE IF NOT EXISTS messages (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    email TEXT,
    message TEXT
)
''')

#
cursor.execute('''
INSERT INTO projects (title, description)
VALUES
('Student Management System', 'Python + MySQL Project'),
('Portfolio Website', 'HTML, CSS, JavaScript, Flask')
''')

conn.commit()
conn.close()

print("Database created successfully!")