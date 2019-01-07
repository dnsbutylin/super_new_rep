import random
from model.contact import Contact
from model.group import Group


def test_delete_contact_from_group(app, orm):
    if len(orm.get_contact_list()) == 0:
        app.contact.create(Contact(firstname='test_firstname4', lastname='test_lastname4',
                                   address='test_address4'))
    group = random.choice(orm.get_group_list())
    l = orm.get_contacts_in_group(group)
    # Если контактов нет в группе, создаем новый, добавляем его в группу, затем удаляем
    if l == []:
        app.contact.create(Contact(firstname='test_firstname2', lastname='test_lastname2',
                                   address='test_address2'))
        contact = sorted(orm.get_contact_list(), key=lambda contact: int(contact.id), reverse=True)[0]
        app.contact.add_to_group(contact.id, group.id)
        assert contact in orm.get_contacts_not_in_group(group)
    # Если контакты есть в группе, выбираем случайный, затем удалям
    else:
        contact = random.choice(l)
        app.contact.delete_contact_from_group(contact.id, group.id)
        assert contact in orm.get_contacts_not_in_group(group)
