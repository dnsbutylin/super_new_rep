from model.group import Group
from random import randrange


def test_modify_group_name(app, db, check_ui):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name='test'))
    old_groups = db.get_group_list()
    index = randrange(len(old_groups))
    group = Group(name='New_group')
    group.id = old_groups[index].id
    #app.group.modify_group_by_index(index, group)
    app.group.modify_group_by_id(group.id, group)
    new_groups = db.get_group_list()
    assert len(old_groups) == len(new_groups)
    old_groups[index] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
    if check_ui:
        new_ui_groups = app.group.get_group_list()
        assert sorted(new_groups, key=Group.id_or_max) == sorted(new_ui_groups, key=Group.id_or_max)
