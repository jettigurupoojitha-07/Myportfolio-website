from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():

    conn = sqlite3.connect('portfolio.db')
    cursor = conn.cursor()

    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']

        cursor.execute(
            "INSERT INTO messages (name, email, message) VALUES (?, ?, ?)",
            (name, email, message)
        )
        conn.commit()

    cursor.execute("SELECT title, description FROM projects")
    projects = cursor.fetchall()

    conn.close()

    return render_template('index.html', projects=projects)

if __name__ == '__main__':
    app.run(debug=True)