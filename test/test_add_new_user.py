# -*- coding: utf-8 -*-
__author__ = "C00LSkY"


from model.contacts import Anketa


def test_add_new_user(app, json_users):
    user = json_users
    old_users = app.user.get_user_list()
    app.user.add_new_user(user)
    assert len(old_users) + 1 == app.user.count_user()
    new_users = app.user.get_user_list()
    old_users.append(user)
    assert sorted(old_users, key=Anketa.id_or_max) == sorted(new_users, key=Anketa.id_or_max)





