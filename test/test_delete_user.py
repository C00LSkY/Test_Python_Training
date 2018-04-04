__author__ = "C00LSkY"

from model.contacts import Anketa
import random
import time

def test_delete_some_user(app, db, check_ui):
    if len(db.get_user_list()) == 0:
        app.user.add_new_user(Anketa(firstname="Вася", midlename="Петрович", lastname='Пупкин', nickname='Пупка',
                                     company='Ромашка+Олень', address='Москва', home_tel='79999999990',
                                     mobile_tel='78888888880', work_tel='', email='pypka@mail.ru',
                                     byear='', address2=''))
    old_users = db.get_user_list()
    user = random.choice(old_users)
    app.user.delete_user_by_id(user.id)
    time.sleep(1)
    new_users = db.get_user_list()
    old_users.remove(user)
    assert sorted(old_users, key=Anketa.id_or_max) == sorted(new_users, key=Anketa.id_or_max)
    if check_ui:
        assert sorted(new_users, key=Anketa.id_or_max) == sorted(app.user.get_user_list(), key=Anketa.id_or_max)
