import mongoengine

#mongodb://viet:phamtuanviet1998@ds223812.mlab.com:23812/muadongkhonglanh

host = "ds223812.mlab.com"
port = 23812
db_name = "muadongkhonglanh"
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



