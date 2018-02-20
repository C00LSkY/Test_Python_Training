__author__ = "C00LSkY"

from model.group import Group


def test_edit_group(app):
    app.group.edit_group(Group(name="edit_test_group", header="измененная тестовая группа", footer=""))
