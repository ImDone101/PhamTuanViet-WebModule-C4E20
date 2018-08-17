from flask import Flask, render_template
app = Flask(__name__)

ngDung = {
    'Viet' : {
        'name': 'Viet',
        'age': 20,
        'gender': 'Male',
        'hobby': 'Gaming' 
    },
    'Phan' :{
        'name': 'Phan',
        'age': 30,
        'gender': 'Male',
        'hobby': 'Reading'
    },
    'Phuong Anh': {
        'name': 'Phuong Anh',
        'age': 19,
        'gender': 'Female',
        'hobby': 'Cooking'
    }
}

@app.route('/user/<username>')
def check(username):
    if username in ngDung.keys():
        return render_template('dung.html', info = ngDung[username])
    else:
        return 'User not found'

if __name__ == '__main__': 
  app.run(debug=True) 
