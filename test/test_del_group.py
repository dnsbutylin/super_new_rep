from model.group import Group


def test_delete_first_group(app):
    old_groups = app.group.get_group_list()
    if app.group.count() == 0:
        app.group.create(Group(name='test'))
    app.group.delete_first_group()
    new_groups = app.group.get_group_list()
    if len(old_groups) > 0:
        assert len(old_groups) - 1 == len(new_groups)
    else:
        assert len(old_groups) == len(new_groups)
    old_groups[0:1] = []
    assert old_groups == new_groups

