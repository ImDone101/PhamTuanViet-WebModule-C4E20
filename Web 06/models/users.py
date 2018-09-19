from mongoengine import *
class User(Document):
    username=StringField()
    password=StringField()
    email=EmailField()
    fullname=StringField()