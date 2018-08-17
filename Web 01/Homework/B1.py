from flask import Flask, redirect, render_template
app = Flask(__name__)

@app.route('/about')
def about_me():
    me = {
            'Name' : 'Viet Pham',
            'Age' : '20',
            'Work' : 'Student',
            'School' : 'PTIT',
            'Hobbies' : 'Reading, Cooking, Gaming,....',
            'Favourites': 'Dota 2, Berserk, War and Peace,...'
        }
    return render_template('me.html', me = me)

@app.route('/school')
def school():
    return redirect("http://techkids.vn",code = 302)

if __name__ == '__main__':
  app.run(debug=True)
