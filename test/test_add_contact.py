# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_new_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.create(Contact(firstname="Denis", middlename="Butylin", lastname="lastname",
                               nickname="nickname", photo=r"C:\PycharmProjects\123\OklqbFQ_dbA.jpg", title="title", company="company", address="address",
                               home="home", mobile="mobile", work="work", fax="fax",
                               email="email1", email2="email2", email3="email3",
                               homepage="homepage", bday="29", bmonth="April", byear="1992",
                               aday="1", amonth="January", ayear="2000",
                               address2="address2", phone2="phone2", notes="notes"))
    app.session.logout()

