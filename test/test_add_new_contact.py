# -*- coding: utf-8 -*-
import pytest
from model.contact import Contact
from fixture.application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_new_contact(app):
    app.login(username="admin", password="secret")
    app.create_new_contact(Contact(firstname="Denis", middlename="Butylin", lastname="lastname",
                                    nickname="nickname", title="title", company="company", address="address",
                                    home="home", mobile="mobile", work="work", fax="fax",
                                    email="email1", email2="email2", email3="email3",
                                    homepage="homepage",  bday="29", bmonth="April", byear="1992",
                                    aday="1", amonth="January", ayear="2000",
                                    address2="address2", phone2="phone2", notes="notes"))
    app.logout()

