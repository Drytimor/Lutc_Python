"""
import shelve

db = shelve.open('persondb')
for person in sorted(db):
    print(person, db[person])

sue = db['Sue Jones']
sue.give_raise(.10)
db['Sue Jones'] = sue
db.close()"""