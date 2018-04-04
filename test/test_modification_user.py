__author__ = "C00LSkY"

from model.contacts import Anketa
import random

def test_edit_some_user(app, db, check_ui):
    if len(db.get_user_list()) == 0:
        app.user.add_new_user(Anketa(firstname="Вася", midlename="Петрович", lastname='Пупкин', nickname='Пупка',
                                     company='Ромашка+Олень', address='Москва', home_tel='79999999990',
                                     mobile_tel='78888888880', work_tel='555', email='pypka@mail.ru',
                                     byear='', address2=''))
    old_users = db.get_user_list()
    index = random.choice(old_users)
    user = Anketa(firstname="Николай", midlename="Фигович", lastname='Трушкин', nickname='Pypka',
                  company='Ромашка+Олень', address='Москва', home_tel='79999999990', mobile_tel='78888888880',
                  work_tel='555', email='pypka@mail.ru', email2='ddfdf@df', email3='rrrr@ff.ty', byear='1990',
                  address2='Москва 2')
    app.user.edit_user_by_id(id, user)
    new_users = db.get_user_list()
    old_users[index] = user
    assert sorted(old_users, key=Anketa.id_or_max) == sorted(new_users, key=Anketa.id_or_max)
    if check_ui:
        assert sorted(new_users, key=Anketa.id_or_max) == sorted(app.user.get_user_list(), key=Anketa.id_or_max)



