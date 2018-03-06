# -*- coding: utf-8 -*-
__author__ = "C00LSkY"

from model.group import Group


def test_add_group(app):
    old_group = app.group.get_group_list()
    app.group.create(Group(name="test_group", header="тестовая группа", footer="группа 2018"))
    new_groups = app.group.get_group_list()
    assert len(old_group) + 1 == len(new_groups)


def test_empty_group(app):
    app.group.create(Group(name="", header="", footer=""))

