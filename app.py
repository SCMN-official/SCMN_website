from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

def get_episodes():
    conn = sqlite3.connect('podcasts.db')
    conn.row_factory = sqlite3.Row
    rows = conn.execute(
        "SELECT title, date, video_id, description FROM episodes ORDER BY id DESC"
    ).fetchall()
    conn.close()
    return rows

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/podcasts')
def podcasts():
    episodes = get_episodes()
    return render_template('podcasts.html', episodes=episodes)

@app.route('/summaries')
def summaries():
    return render_template('summaries.html')

@app.route('/articles')
def articles():
    return render_template('articles.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)