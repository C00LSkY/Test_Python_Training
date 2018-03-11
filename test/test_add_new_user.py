# -*- coding: utf-8 -*-
__author__ = "C00LSkY"


from model.contacts import Anketa



def test_add_new_user(app):
    old_users = app.user.get_user_list()
    user = Anketa(firstname="Вася", midlename="Петрович", lastname='Пупкин', nickname='Пупка',
                                     company='Ромашка', address='Москва', home_tel='79999999999',
                                     mobile_tel='78888888888', work_tel='77777777777', email='pypka@mail.ru',
                                     byear='1990', address2='Москва 2')
    app.user.add_new_user(user)
    assert len(old_users) + 1 == app.user.count_user()
    new_users = app.user.get_user_list()
    old_users.append(user)
    assert sorted(old_users, key=Anketa.id_or_max) == sorted(new_users, key=Anketa.id_or_max)





