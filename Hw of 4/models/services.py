from mongoengine import *

# Desgin database
class Service(Document):
    name = StringField()
    yob = IntField()
    gender = IntField()
    height = IntField()
    phone = StringField()
    address = StringField()
    status = BooleanField()
    measurement = ListField()
    description = ListField()
    image = StringField()