from model.contact import Contact
from model.group import Group
import random


def test_add_contact_to_group(app, orm):
    if len(orm.get_contact_list()) == 0:
        app.contact.create(Contact(firstname='test_firstname', lastname='test_lastname',
                                   address='test_address'))
    if len(orm.get_group_list()) == 0:
        app.group.create(Group(name='test_name1', header='test_header1', footer='test_footer1'))
    contact = random.choice(orm.get_contact_list())
    # Пошел цикл по всем группам, если контакт есть во всех группах, то ничего, иначе добавит контакт в группу
    i = 0
    group = orm.get_group_list()[i]
    while i < len(orm.get_group_list()):
        group = orm.get_group_list()[i]
        if contact in orm.get_contacts_not_in_group(group):
            app.contact.add_to_group(contact.id, group.id)
            break
        i += 1
    # Если выбранный контакт есть во всех группах, добавляем новый контакт, добавляем его в группу
    if i == len(orm.get_group_list()):
        app.contact.create(Contact(firstname='test_firstname1', lastname='test_lastname1',
                                   address='test_address1'))
    contact = sorted(orm.get_contact_list(), key=lambda contact: int(contact.id) ,reverse=True)[0]
    app.contact.add_to_group(contact.id, group.id)

    l = orm.get_contacts_in_group(group)
    assert contact in l