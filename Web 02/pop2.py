import mlab
from models.d_vu import K_Hang
from faker import Faker
from random import randint, choice

mlab.connect()

fake = Faker()

for i in range(60):
    print('Luu khach hang', i+1, ".......")
    ten = fake.name()
    new_dVu = K_Hang(
        name = ten,
        gender = randint(0,1),
        email=ten.replace(' ', '') + '@gmail.com',
        phone=fake.phone_number(),
        job=fake.job(),
        company=fake.company(),
        contacted=choice([True, False])
    )

    new_dVu.save()