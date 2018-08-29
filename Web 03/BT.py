from flask import *
import mlab
from mongoengine import *
from models.services import Service
app = Flask(__name__)
mlab.connect()

# Design pattern(MVC, MVP, )


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search/<int:g>')
def search(g):
    all_service = Service.objects[:10](
        gender = g,
        )
    return render_template('search.html', all_service=all_service)

@app.route('/admin')
def admin():
    all_service = Service.objects()
    return render_template('admin.html', all_service=all_service)

@app.route('/delete/<service_id>')
def delete(service_id):
    cai_de_xoa = Service.objects.with_id(service_id)
    if cai_de_xoa is not None:
        cai_de_xoa.delete()
        return redirect(url_for('admin'))
    else:
        return "Khong thay id"

@app.route('/new-service', methods=["GET", "POST"])
def create():
    if request.method == 'GET':
        return render_template('new-service.html')
    elif request.method == 'POST':
        form = request.form

        name =form['name']
        yob=form['yob']
        phone=form['phone']

        new_service = Service(
            name=name,
            yob=yob,
            phone=phone
        )
        new_service.save()
    return redirect(url_for('admin'))

@app.route('/detail/<service_id>')
def detail(service_id):
    service = Service.objects.with_id(service_id)
    return render_template('detail.html', service = service)

@app.route('/updateservice/<service_id>', methods=["GET", "POST"])
def updateservice(service_id):

    service = Service.objects.with_id(service_id)
    
    if request.method == "GET":
        return render_template('update_service.html', service = service)
    elif request.method == "POST":
        form = request.form
        name = form['name']
        yob = form['yob']
        phone = form['phone']
        height = form['height']
        address = form['address']

        service.name = name
        service.yob = yob
        service.phone = phone
        service.height = height
        service.address = address

        service.save()
        

        return redirect (url_for('admin'))

@app.route('/delete-all')
def deleteall():
    x = Service.objects()
    x.delete()
    return 'Da xoa'
    return redirect(url_for('admin'))

if __name__ == '__main__':
    app.run(debug=True)