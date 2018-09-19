from mongoengine import *
import datetime

class Order(Document):
    user=ReferenceField("User")
    service=ReferenceField("Service")
    order_time=DateTimeField()
    is_accepted=BooleanField()