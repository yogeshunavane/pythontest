from one_to_many import db, Person, Pet
from execute import *

#to display data from table
exe = Person.query.filter_by(name='Manohar').first()
for indi in exe.pets.all():
    print(indi.name)