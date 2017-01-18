from one_to_many import db, Person, Pet

#commit all objects
db.create_all()
db.session.commit()

#create and insert object into table Person
person_one = Person(name='Raj')
person_two = Person(name='Manohar')
db.session.add(person_one)
db.session.add(person_two)
db.session.commit()

#create objects for table Pet
pet_one = Pet(name='Boxer', owner=person_one)
pet_two = Pet(name='Manohar', owner=person_two)
pet_three = Pet(name='Gennie', owner=person_one)
pet_four = Pet(name='Mac', owner=person_two)

#insert into table Pet
db.session.add(pet_one)
db.session.add(pet_two)
db.session.add(pet_three)
db.session.add(pet_four)
db.session.commit()


