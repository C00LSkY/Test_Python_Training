# -*- coding: utf-8 -*-
__author__ = "C00LSkY"

from model.group import Group


def test_add_group(app):
    app.group.create(Group(name="test_group", header="тестовая группа", footer="группа 2018"))


def test_empty_group(app):
    app.group.create(Group(name="", header="", footer=""))

