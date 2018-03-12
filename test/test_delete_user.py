__author__ = "C00LSkY"

from model.contacts import Anketa
from random import randrange

def test_delete_some_user(app):
    if app.user.count_user() == 0:
        app.user.add_new_user(Anketa(firstname="Вася", midlename="Петрович", lastname='Пупкин', nickname='Пупка',
                                     company='Ромашка+Олень', address='Москва', home_tel='79999999990',
                                     mobile_tel='78888888880', work_tel='', email='pypka@mail.ru',
                                     byear='', address2=''))
    old_users = app.user.get_user_list()
    index = randrange(len(old_users))
    app.user.delete_user_by_index(index)
    new_users = app.user.get_user_list()
    assert len(old_users) - 1 == len(new_users)
    old_users[index:index + 1] = []
    assert old_users == new_users
