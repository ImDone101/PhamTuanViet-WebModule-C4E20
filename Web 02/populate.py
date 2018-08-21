import mlab
from models.services import Service
from faker import Faker
from random import randint, choice

mlab.connect()

fake = Faker()

for i in range(50):
    print('Saving services', i+1,".......")
    new_service = Service(
        name=fake.name(),
        yob=randint(1990, 2000),
        gender=randint(0,1),
        height=randint(150,190),
        phone=fake.phone_number(),
        address=fake.address(),
        status=choice([True, False])
    )

    new_service.save()


