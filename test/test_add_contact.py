# -*- coding: utf-8 -*-
from model.contact import Contact
import pytest
import random
import string

def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits
    return prefix + ''.join([random.choice(symbols) for i in range(random.randrange(maxlen))])

#test_data = [Contact(firstname="Denis", middlename="middlename", lastname="Butylin",
#        nickname="nickname",
#        photo=r"C:\OklqbFQ_dbA.jpg",
##        title="title", company="company", address="address",
 #       home="home", mobile="mobile", work="work", fax="fax",
 #       email="email1", email2="email2", email3="email3",
 #      homepage="homepage", bday="29", bmonth="April", byear="1992",
 #      aday="1", amonth="January", ayear="2000",
 #      address2="address2", phone2="phone2", notes="notes")]

test_data = [
    Contact(firstname=random_string('firstname', 15), middlename=random_string('middlename', 15),
            lastname=random_string('lastname', 15), nickname=random_string('nickname', 15),
            photo=r"C:\Projects_Selenium\super_new_rep\OklqbFQ_dbA.jpg",
            title=random_string('title', 15),
            company=random_string('company', 15), address=random_string('address', 15),
            home=random_string('home', 15),
            mobile=random_string('mobile', 15), work=random_string('work', 15),
            fax=random_string('fax', 15),
            email=random_string('email', 15), email2=random_string('email2', 15),
            email3=random_string('email3', 15),
            homepage=random_string('homepage', 15), bday="29", bmonth="April",
            byear=random_string('', 15),
            aday="1", amonth="January", ayear=random_string('', 15),
            address2=random_string('address2', 15),
            phone2=random_string('phone2', 15), notes=random_string('notes', 15))
    for i in range(2)
]

@pytest.mark.parametrize('contact', test_data, ids=[repr(x) for x in test_data])
def test_add_contact(app, contact):
    old_contacts = app.contact.get_contact_list()
    app.contact.create(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key = Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

