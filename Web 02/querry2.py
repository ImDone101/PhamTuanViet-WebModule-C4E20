from models.d_vu import K_Hang
import mlab

mlab.connect()

id_to_find = '5b7c2692465a1119244babea'

# khach = K_Hang.objects(id=id_to_find) #=> []
# khach = K_Hang.objects.get(id=id_to_find) #=> Service obj
khach = K_Hang.objects.with_id(id_to_find)

if khach is not None:
    # khach.delete()
    # print("Deleted")
    print('Before')
    print(khach.to_mongo())
    khach.update(set__gender=5, set__job='Assasin')
    khach.reload()
    print(khach.to_mongo())
else:
    print('Not found')