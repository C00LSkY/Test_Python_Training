# -*- coding: utf-8 -*-
__author__ = "C00LSkY"

import pytest

from group import Group

from application import Application


@pytest.fixture()
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_group(app):
    app.login(username="admin", password="secret")
    app.create_group(Group(name="test_group", header="тестовая группа", footer="группа 2018"))
    app.logout()

def test_empty_group(app):
    app.login(username="admin", password="secret")
    app.create_group(Group(name="", header="", footer=""))
    app.logout()

