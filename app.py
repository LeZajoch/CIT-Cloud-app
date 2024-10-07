from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

# Initialize MySQL
mysql = MySQL(app)

# Main route to list all blog posts
@app.route('/')
def index():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM posts ORDER BY created_at DESC")
    posts = cur.fetchall()
    cur.close()
    return render_template('index.html', posts=posts)

# Route for adding a new post
@app.route('/add', methods=['GET', 'POST'])
def add_post():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']

        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO posts (title, content) VALUES (%s, %s)", (title, content))
        mysql.connection.commit()
        cur.close()

        flash('Post added successfully!', 'success')
        return redirect(url_for('index'))

    return render_template('add_post.html')

# Route for viewing a single post
@app.route('/post/<int:id>')
def view_post(id):
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM posts WHERE id = %s", (id,))
    post = cur.fetchone()
    cur.close()
    return render_template('view_post.html', post=post)

if __name__ == '__main__':
    app.secret_key = 'supersecretkey'
    app.run(host='0.0.0.0', port=5000)
