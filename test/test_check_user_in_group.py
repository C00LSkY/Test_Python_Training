
__author__ = "C00LSkY"

from fixture.user import Anketa
from fixture.group import Group
from fixture.orm import ORMFixture
import random
import time

def test_add_some_user_in_group(app, db):
    orm = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")
    groups = orm.get_group_list()
    users = orm.get_user_list()
    if len(db.get_user_list()) == 0:
        app.user.add_new_user(Anketa(firstname="Вася", midlename="Петрович", lastname='Пупкин', nickname='Пупка',
                                     company='Ромашка+Олень', address='Москва', home_tel='79999999990',
                                     mobile_tel='78888888880', work_tel='', email='pypka@mail.ru',
                                     byear='', address2=''))
    if len(groups) == 0:
        app.group.create(Group(name="test_default_db"))
    user = random.choice(users)
    user_id = user.id
    group = random.choice(groups)
    group_name = group.name
    group_id = group.id
    old_users_in_groups = orm.get_users_in_group(Group(id=group_id))
    app.user.add_user_to_group(user_id, group_name)
    new_users_in_groups = orm.get_users_in_group(Group(id=group_id))
    assert len(old_users_in_groups) + 1 == len(new_users_in_groups)
    for user_in_group in new_users_in_groups:
        assert (user_in_group.id == user_id)




