# -*- coding: utf-8 -*-
__author__ = "C00LSkY"


from model.contacts import Anketa



def test_add_new_user(app):
    app.session.login(username="admin", password="secret")
    app.user.add_new_user(Anketa(firstname="Вася", midlename="Петрович", lastname='Пупкин', nickname='Пупка',
                                     company='Ромашка', address='Москва', home_tel='79999999999',
                                     mobile_tel='78888888888', work_tel='77777777777', email='pypka@mail.ru',
                                     byear='1990', address2='Москва 2'))
    app.session.logout()




