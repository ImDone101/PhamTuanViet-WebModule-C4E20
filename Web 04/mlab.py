import mongoengine
# mongodb:/dbpassword>@ds233228.mlab.com:33228/youtube/<dbuser>:<

host = "ds233228.mlab.com"
port = 33228
db_name = "youtube"
user_name = "viet"
password = "phamtuanviet1998"


def connect():
    mongoengine.connect(
        db_name, 
        host=host, 
        port=port, 
        username=user_name,
        password=password
        )
