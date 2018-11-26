from model.group import Group


def test_delete_first_group(app):
    old_groups = app.group.get_group_list()
    if app.group.count() == 0:
        app.group.create(Group(name='test'))
    app.group.delete_first_group()
    new_group = app.group.get_group_list()
    assert len(old_groups) - 1 == len(new_group)
