#from fixture.db import Dbfixture

#db = Dbfixture(host='127.0.0.1', name='addressbook', user='root',
#                             password='')
#
#try:
#    contacts = db.get_contact_list()
#    for contact in contacts:
#        print(contact)
#    print(len(contacts))
#finally:
#    db.destroy()

from fixture.orm import ORMFixture
from model.group import Group

#db = ORMFixture(host='127.0.0.1', name='addressbook', user='root',
#                             password='')

#try:
#    l = db.get_contact_list()
#    for item in l:
#        print(item)
#    print(len(l))
#finally:
#    pass #db.destroy()

db = ORMFixture(host='127.0.0.1', name='addressbook', user='root',
                             password='')

try:
    l = db.get_contacts_in_group(Group(id='122'))
    for item in l:
        print(item)
    print(len(l))
finally:
    pass
