# -*- coding: utf-8 -*-

__author__ = "C00LSkY"


from model.contacts import Anketa


def test_add_new_user(app, db, json_users, check_ui):
    user = json_users
    old_users = db.get_user_list()
    app.user.add_new_user(user)
    assert len(old_users) + 1 == len(db.get_user_list()) #app.user.count_user()
    new_users = db.get_user_list()
    old_users.append(user)
    assert sorted(old_users, key=Anketa.id_or_max) == sorted(new_users, key=Anketa.id_or_max)
    if check_ui:
        assert sorted(new_users, key=Anketa.id_or_max) == sorted(app.user.get_user_list(), key=Anketa.id_or_max)





