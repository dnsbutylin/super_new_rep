#from model.contact import Contact
#from fixture.orm import ORMFixture#

#import random


#def test_add_contact_to_group(app, db=ORMFixture(host='127.0.0.1', name='addressbook', user='root',
#                             password='')):
#    if len(db.get_contact_list()) == 0:
#        app.contact.create(Contact(firstname='test_firstname', lastname='test_lastname',
#                                   address='test_address'))
#    contact = random.choice(db.get_contact_list())
#    group = random.choice(db.get_group_list())
#    app.contact.add_to_group(contact.id, group.name)
#    l = db.get_contacts_in_group(group)
#    assert contact in l
