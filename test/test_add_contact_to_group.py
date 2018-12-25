from model.contact import Contact

import random

def test_add_contact_to_group(app, orm):
    if len(orm.get_contact_list()) == 0:
        app.contact.create(Contact(firstname='test_firstname', lastname='test_lastname',
                                   address='test_address'))
    # Оставляю выбор группы и контакта случайным, так как если контакт в группе уже есть,
    # ничего не происходит (т.е. повторно он не добавляется), и тест завршится при этом положительно
    contact = random.choice(orm.get_contact_list())
    group = random.choice(orm.get_group_list())
    app.contact.add_to_group(contact.id, group.id)
    l = orm.get_contacts_in_group(group)
    assert contact in l
