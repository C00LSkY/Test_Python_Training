__author__ = "C00LSkY"

from model.contacts import Anketa

def test_edit_user(app):
    if app.user.count_user() == 0:
        app.user.add_new_user(Anketa(firstname="Вася", midlename="Петрович", lastname='Пупкин', nickname='Пупка',
                                     company='Ромашка+Олень', address='Москва', home_tel='79999999990',
                                     mobile_tel='78888888880', work_tel='', email='pypka@mail.ru',
                                     byear='', address2=''))
    old_users = app.user.get_user_list()
    app.user.edit_first_user(Anketa(firstname="Николай", midlename="Петрович", lastname='Пупкин', nickname='Pypka',
                                     company='Ромашка+Олень', address='Москва', home_tel='79999999990',
                                     mobile_tel='78888888880', work_tel='', email='pypka@mail.ru',
                                     byear='1990', address2='Москва 2'))
    new_users = app.user.get_user_list()
    assert len(old_users) == len(new_users)



