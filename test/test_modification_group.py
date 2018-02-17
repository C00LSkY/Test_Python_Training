__author__ = "C00LSkY"

from model.group import Group


def test_edit_group(app):
    app.session.login(username="admin", password="secret")
    app.group.edit_group(Group(name="edit_test_group", header="измененная тестовая группа", footer=""))
    app.session.logout()
