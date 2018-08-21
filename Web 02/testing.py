from flask import Flask, render_template
import mlab
from mongoengine import *
from models.services import Service
from models.d_vu import K_Hang
app = Flask(__name__)
mlab.connect()

# Design pattern(MVC, MVP, )


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search/<int:g>')
def search(g):
    all_service = Service.objects(
        gender = g,
        yob__lte=1998,
        height__gte=165,
        address__icontains = "Hanoi" 
        )
    return render_template('search.html', all_service=all_service)

@app.route('/khachhang/<int:g>')
def khachhang(g):
    toan_bo = K_Hang.objects[:10](
        gender = g,
        contacted = False
    )
    return render_template('khang.html', toan_bo=toan_bo)

if __name__ == '__main__':
    app.run(debug=True)