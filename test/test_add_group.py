# -*- coding: utf-8 -*-
from model.group import Group


def test_add_group(app):
    old_groups = app.group.get_group_list()
    app.group.create(Group(name="sadsdasda", header="sadassdadasd", footer="sfaffafa"))
    new_group = app.group.get_group_list()
    assert len(old_groups) + 1 == len(new_group)


def test_add_empty_group(app):
    old_groups = app.group.get_group_list()
    app.group.create(Group(name="", header="", footer=""))
    new_group = app.group.get_group_list()
    assert len(old_groups) + 1 == len(new_group)

