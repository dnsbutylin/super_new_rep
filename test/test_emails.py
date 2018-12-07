from model.contact import Contact


def test_emails_on_home_page(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname='test_firstname', lastname='test_lastname',
                                   address='test_address', all_emails_from_home_page='eemail\neemail2\neemail3',
                                   all_phones_from_home_page='12345\n(123)45\n5432 1-\n333333'))
    contact_from_home_page = app.contact.get_contact_list()[0]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert contact_from_home_page.all_emails_from_home_page == merge_emails_like_on_home_page(contact_from_edit_page)


def test_emails_on_view_page(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname='test_firstname', lastname='test_lastname',
                                   address='test_address', all_emails_from_home_page='eemail\neemail2\neemail3',
                                   all_phones_from_home_page='12345\n(123)45\n5432 1-\n333333'))
    contact_from_view_page = app.contact.get_contact_from_view_page(0)
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert contact_from_view_page.all_emails_from_home_page == merge_emails_like_on_home_page(contact_from_edit_page)

def merge_emails_like_on_home_page(contact):
    return '\n'.join(filter(lambda x: x !='',
                                filter(lambda x: x is not None,
                                       [contact.email, contact.email2, contact.email3] )))