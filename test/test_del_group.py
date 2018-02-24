__author__ = "C00LSkY"
from model.group import Group

def test_delete_first_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name="undo test", header="default группа", footer="default"))
    app.group.delete_first_group()