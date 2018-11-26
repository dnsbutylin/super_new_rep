from model.group import Group


def test_modify_group_name(app):
    old_groups = app.group.get_group_list()
    if app.group.count() == 0:
        app.group.create(Group(name='test'))
    app.group.modify_first_group(Group(name="New name"))
    new_group = app.group.get_group_list()
    assert len(old_groups) == len(new_group)
