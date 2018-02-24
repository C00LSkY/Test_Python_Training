__author__ = "C00LSkY"

from model.group import Group


def test_edit_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name="undo test", header="default группа", footer="default"))
    app.group.edit_group(Group(name="edit_test_group"))
