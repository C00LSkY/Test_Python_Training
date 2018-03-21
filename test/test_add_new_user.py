# -*- coding: utf-8 -*-
__author__ = "C00LSkY"


from model.contacts import Anketa
import pytest
import random
import string


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " "
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

def random_digits_string(prefix, maxlen):
    symbols_num = string.digits
    return prefix + "".join([random.choice(symbols_num) for i in range(random.randrange(maxlen))])



testdata = [
            Anketa(firstname=random_string("firstname", 10), midlename=random_string("midlename", 10),
                   lastname=random_string("lastname", 10), nickname=random_string("nickname", 10),
                   company=random_string("company", 10), address=random_string("address", 10),
                   home_tel=random_digits_string("+", 10), mobile_tel=random_digits_string("+", 10),
                   work_tel=random_digits_string("+", 10), email=random_string("@", 10), email2=random_string("@", 10),
                   email3=random_string("@", 10), byear=random_digits_string("", 4), address2=random_string("address2", 15))
             for i in range(5)
]

@pytest.mark.parametrize("user", testdata, ids=[repr(x) for x in testdata])
def test_add_new_user(app, user):
    old_users = app.user.get_user_list()
    app.user.add_new_user(user)
    assert len(old_users) + 1 == app.user.count_user()
    new_users = app.user.get_user_list()
    old_users.append(user)
    assert sorted(old_users, key=Anketa.id_or_max) == sorted(new_users, key=Anketa.id_or_max)





