__author__ = "C00LSkY"

from model.group import Group
from random import randrange


def test_edit_group_name(app):
    if app.group.count() == 0:
        app.group.create(Group(name="undo test", header="default группа", footer="default"))
    old_groups = app.group.get_group_list()
    index = randrange(len(old_groups))
    group = Group(name="edit_test_group")
    group.id = old_groups[index].id
    app.group.edit_group_by_index(index, group)
    assert len(old_groups) == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups[index] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


#def test_edit_group_header(app):
#    if app.group.count() == 0:
#        app.group.create(Group(name="undo test", header="default группа", footer="default"))
#    old_groups = app.group.get_group_list()
#    group = Group(header="edit_header_group")
#    group.id = old_groups[0].id
#    app.group.edit_group(group)
#    new_groups = app.group.get_group_list()
#    assert len(old_groups) == len(new_groups)
#    old_groups[0] = group
#    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
