#from model.contact import Contact
#from fixture.orm import ORMFixture#

#import random


#def test_delete_contact_from_group(app, db=ORMFixture()):
#    group = random.choice(db.get_group_list())
#    l = db.get_contacts_in_group(group)
#   if l == []:
#        # Если список контактов в группе пуст, пусть проверка будет положительная
#        assert True
#    else:
#        contact = random.choice(l)
#        app.contact.delete_contact_from_group(contact.id, group)
#       assert contact in db.get_contacts_not_in_group(group)
