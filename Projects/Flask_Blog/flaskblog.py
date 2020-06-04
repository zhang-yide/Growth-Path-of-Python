from flask import Flask, render_template, url_for
app = Flask(__name__)

posts = [
    {
        'author': 'zhangfei',
        'title': 'Blog Post 1',
        'content': 'First Blog.',
        'date_posted': 'April 20, 2018'
    },
    {
        'author': 'zhangyide',
        'title': 'Blog Post 2',
        'content': 'Second Blog.',
        'date_posted': 'April 20, 2018'
    }
]


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', posts=posts, title='Home')


@app.route('/article')
def article():
    return render_template('article.html', posts=posts, title='Article')


@app.route('/about')
def about():
    return render_template('about.html', title='Article')


if __name__ == '__main__':
    app.run(debug=True)
