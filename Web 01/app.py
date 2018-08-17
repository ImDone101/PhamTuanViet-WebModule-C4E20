from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def index():
    posts = [
        {
        "title" : "Tho con ech",
        "content": "Noi dung",
        "author" : "me",
        "author_sex" : 1
        },
        {
        "title" : "Tu tu",
        "content": "Tu tu",
        "author" : "Thu Minh",
        "author_sex" : 0

        },
        {
        "title" : "Tho lap trinh",
        "content": "Noi dung",
        "author" : "Huynh Tuan Anh",
        "author_sex" : 1

        },
        {
        "title" : "Den vai",
        "content": "Den vl",
        "author" : "Son",
        "author_sex" : 1

        }
    ]
    return render_template('index.html', posts = posts)

@app.route('/hello')
def say_hello():
    return 'Hello from the other side'

@app.route('/sayhi/<name>/<age>/')
def say_hi(name, age):
    return "Hi {}, you're {} years old".format(name, age)

@app.route('/sum/<int:x>/<int:y>')
def sum(x, y):
    return str(x + y)
    
if __name__ == '__main__':
    app.run(debug=True)
 