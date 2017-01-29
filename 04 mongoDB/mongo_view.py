from mongo import *

#------------------------------INSERTing values
# manoher = User(name='Manoher', password='pass')
# manoher.save()
# savita = User(name='Savita', password='pass@123')
# savita.save()

#------------------------------SELECTing values
# res = User.query.filter(User.name == 'Manoher' ).first()
# print(res.password)
# print(res.password)

# res = User.query.filter(User.name == 'Manoher' ).all()
# for i in res:
#     print(i.password)
    # print(res.password)

# print(res.name)
# print(res.password)

#------------------------------UPDATINGing values
# res.password = 'newpass'
# res.save()
# print(res.password)


#------------------------------DELETINGing values
res = User.query.filter(User.name == 'Manoher' ).first()
res.remove()
print(res.password)