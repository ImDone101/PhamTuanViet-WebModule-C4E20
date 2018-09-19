import mlab
from models.services import Service
from faker import Faker
from random import randint, choice

mlab.connect()

fake = Faker()

for i in range(50):
    print('Saving services', i+1,".......")
    measurement = [randint(70,100), randint(60,70), randint(70,100)]
    gender=randint(0,1)
    descrip_male = ['handsome', 'strong', 'gay', 'smart', 'athletic', 'great cook', 'tall', 'short']
    descrip_female = ['cute', 'beautiful', 'sexy', 'tall', 'gentle', 'great cook', 'lesbian', 'short', 'play Dota']
    image_female=['female1.jpg','female2.jpg','female3.jpg','female4.jpg','female5.jpg','female6.jpg','female7.jpg']
    image_male=['male1.jpg','male2.jpg','male3.jpg','male4.jpg','male5.jpg','male6.jpg','male7.jpg']
    if gender == 1:
        new_service = Service(
            name=fake.name(),
            yob=randint(1990, 2000),
            height=randint(150,180),
            gender = gender,
            phone=fake.phone_number(),
            address=fake.address(),
            status=choice([True, False]),
            measurement=measurement,
            description=fake.words(nb=3, ext_word_list=descrip_female),
            image=choice(image_female),
    )
    else:
        new_service = Service(
            name=fake.name(),
            yob=randint(1990, 2000),
            height=randint(150,190),
            gender = gender,
            phone=fake.phone_number(),
            address=fake.address(),
            status=choice([True, False]),
            measurement=measurement,
            description=fake.words(nb=3, ext_word_list=descrip_male),
            image=choice(image_male),

    )

    new_service.save()


