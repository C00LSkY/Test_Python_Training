__author__ = "C00LSkY"

from model.contacts import Anketa
from random import randrange

def test_edit_some_user(app):
    if app.user.count_user() == 0:
        app.user.add_new_user(Anketa(firstname="Вася", midlename="Петрович", lastname='Пупкин', nickname='Пупка',
                                     company='Ромашка+Олень', address='Москва', home_tel='79999999990',
                                     mobile_tel='78888888880', work_tel='555', email='pypka@mail.ru',
                                     byear='', address2=''))
    old_users = app.user.get_user_list()
    index = randrange(len(old_users))
    user = Anketa(firstname="Николай", midlename="Фигович", lastname='Трушкин', nickname='Pypka',
                                     company='Ромашка+Олень', address='Москва', home_tel='79999999990',
                                     mobile_tel='78888888880', work_tel='555', email='pypka@mail.ru',
                                     byear='1990', address2='Москва 2')
    user.id = old_users[index].id
    app.user.edit_user_by_index(index, user)
    assert len(old_users) == app.user.count_user()
    new_users = app.user.get_user_list()
    old_users[index] = user
    assert sorted(old_users, key=Anketa.id_or_max) == sorted(new_users, key=Anketa.id_or_max)



