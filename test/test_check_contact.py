import re
from model.contact import Contact
from random import randrange

def test_check_emails_on_home_page(app, db):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname='test_firstname', lastname='test_lastname',
                                   address='test_address', all_emails_from_home_page='eemail\neemail2\neemail3',
                                   all_phones_from_home_page='12345\n(123)45\n5432 1-\n333333'))
    index = randrange(len(db.get_contact_list()))
    contact_from_home_page = app.contact.get_contact_list()[index]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(index)
    assert contact_from_home_page.all_emails_from_home_page == merge_emails_like_on_home_page(contact_from_edit_page)
    # сравнение данных о контактах, загруженных с главной страницы, с данными,
    # загруженными из базы данных. для всех имеющихся на главной странице контактов
    all_contact_from_UI = app.contact.get_contact_list()
    all_contact__from_DB = db.get_contact_list()
    assert sorted(all_contact_from_UI, key=Contact.id_or_max) == sorted(all_contact__from_DB, key=Contact.id_or_max)


def test_check_phones_on_home_page(app, db):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname='test_firstname', lastname='test_lastname',
                                   address='test_address', all_emails_from_home_page='eemail\neemail2\neemail3',
                                   all_phones_from_home_page='12345\n(123)45\n5432 1-\n333333'))
    index = randrange(len(db.get_contact_list()))
    contact_from_home_page = app.contact.get_contact_list()[index]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(index)
    assert contact_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(contact_from_edit_page)


def test_check_firstname_lastname_address_on_home_page(app, db):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname='test_firstname', lastname='test_lastname',
                                   address='test_address', all_emails_from_home_page='eemail\neemail2\neemail3',
                                   all_phones_from_home_page='12345\n(123)45\n5432 1-\n333333'))
    index = randrange(len(db.get_contact_list()))
    contact_from_home_page = app.contact.get_contact_list()[index]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(index)
    assert contact_from_home_page.firstname == contact_from_edit_page.firstname
    assert contact_from_home_page.lastname == contact_from_edit_page.lastname
    assert contact_from_home_page.address == contact_from_edit_page.address


def merge_emails_like_on_home_page(contact):
    return '\n'.join(filter(lambda x: x !='',
                                filter(lambda x: x is not None,
                                       [contact.email, contact.email2, contact.email3] )))
def clear(s):
    return re.sub("[() -]", "", s)

def merge_phones_like_on_home_page(contact):
    return '\n'.join(filter(lambda x: x !='',
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [contact.home, contact.mobile, contact.work, contact.phone2]))))
