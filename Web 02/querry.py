from models.services import Service
import mlab

mlab.connect()

all_service = Service.objects()

first_service = all_service[3]

print(first_service['name'])