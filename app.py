from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

def get_episodes():
    conn = sqlite3.connect('podcasts.db')
    conn.row_factory = sqlite3.Row
    rows = conn.execute(
        "SELECT title, date, video_id, description FROM episodes ORDER BY date DESC"
    ).fetchall()
    conn.close()
    return rows

@app.route('/')
def home():
    conn = sqlite3.connect('podcasts.db')
    conn.row_factory = sqlite3.Row
    
    ep1 = conn.execute("SELECT * FROM episodes WHERE title LIKE '%شخصيات%' ORDER BY date DESC LIMIT 1").fetchone()
    ep2 = conn.execute("SELECT * FROM episodes WHERE title LIKE '%ونسة%' ORDER BY date DESC LIMIT 1").fetchone()
    ep3 = conn.execute("SELECT * FROM episodes WHERE title LIKE '%حكاوي%' ORDER BY date DESC LIMIT 1").fetchone()
    ep4 = conn.execute("SELECT * FROM episodes WHERE title LIKE '%ثانية%' ORDER BY date DESC LIMIT 1").fetchone()
    ep5 = conn.execute("SELECT * FROM episodes WHERE title LIKE '%ضفاف%' ORDER BY date DESC LIMIT 1").fetchone()
    
    conn.close()
    return render_template('index.html', ep1=ep1, ep2=ep2, ep3=ep3, ep4=ep4, ep5=ep5)

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
