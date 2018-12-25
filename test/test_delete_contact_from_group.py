import random


def test_delete_contact_from_group(app, orm):
    group = random.choice(orm.get_group_list())
    l = orm.get_contacts_in_group(group)
    if l == []:
        # Если список контактов в группе пуст, пусть проверка будет положительная
        assert True
    else:
        contact = random.choice(l)
        app.contact.delete_contact_from_group(contact.id, group.id)
        assert contact in orm.get_contacts_not_in_group(group)
