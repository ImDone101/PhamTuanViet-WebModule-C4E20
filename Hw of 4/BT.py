from flask import *
import mlab
from mongoengine import *
from models.services import Service
from models.users import User
from models.orders import Order


app = Flask(__name__)
app.secret_key = "a secret string"
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
    session["service"]=str(service.id)
    if "loggedin" in session:
        if session["loggedin"] == True:
            if service is not None:
                return render_template(
                    "detail.html", 
                    service=service)
            else:
                return "Service is not found"
        else:
            return redirect(url_for("login"))
    else:
        return redirect(url_for("login"))

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


@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template('login.html')
    elif request.method == "POST":
        form = request.form
        username = form["username"]
        password = form["password"]
        found_user = User.objects(
            username=username,
            password=password
        )
        if found_user:
            session["loggedin"] = True
            user = User.objects.get(username=username)
            session["user"] = str(user.id)
            service_id = session["service"]
            return redirect(url_for("detail", service_id=service_id))
        else:
            return redirect(url_for("signin"))

        
@app.route('/sign_in', methods=["GET", "POST"])
def sign_in():
    if request.method == "GET":
        return render_template('sign_in.html')
    elif request.method == "POST":
        form = request.form
        fullname = form["fullname"]
        email = form["email"]
        username = form["username"]
        password = form["password"]

        new_user = User(
            username=username,
            password=password,
            email=email,
            fullname=fullname
        )

        new_user.save()
        return redirect(url_for("index"))

@app.route('/order-ing')
def order_ing():
    if 'loggedin' in session:
        if session['loggedin'] == True:
            new_order = Order(
                user = session['user'],
                service = session["service"],
                order_time=datetime.datetime.now(),
                is_accepted = False
            )
            new_order.save()
            return "Sent"
        else:
            return redirect(url_for("login"))
    else:
        return redirect(url_for("login"))

@app.route("/order")
def order():
    orders = Order.objects()
    return render_template('order.html',orders=orders)

@app.route("/chapnhan/<order_id>")
def chapnhan(order_id):
    order = Order.objects.with_id(order_id)
    email = order.user.email

    order.update(
        is_accepted = True
    )

    gmail = GMail("Viet<vietc4e20@gmail.com>","pass")
    msg = Message(
    "Order accepted",
    to=email,
    text="Your request da duoc xu ly, cam on vi da dung dich vu")
    gmail.send(msg)

    return redirect(url_for("order"))
    
@app.route('/logout')
def logout():
    session["loggedin"]=False
    session.clear()
    return redirect(url_for("index"))        

@app.route('/delete-all')
def deleteall():
    x = Service.objects()
    x.delete()
    return 'Da xoa'
    return redirect(url_for('admin'))

if __name__ == '__main__':
    app.run(debug=True)