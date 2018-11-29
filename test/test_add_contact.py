# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname="Denis", middlename="Butylin", lastname="lastname",
                               nickname="nickname",
                               photo=r"C:\Projects_Selenium\super_new_rep\OklqbFQ_dbA.jpg",
                               title="title", company="company", address="address",
                               home="home", mobile="mobile", work="work", fax="fax",
                               email="email1", email2="email2", email3="email3",
                               homepage="homepage", bday="29", bmonth="April", byear="1992",
                               aday="1", amonth="January", ayear="2000",
                               address2="address2", phone2="phone2", notes="notes")
    app.contact.create(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)


