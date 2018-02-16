# -*- coding: utf-8 -*-
import pytest
from model.contacts import Anketa
from fixture.application_user import Application_user



@pytest.fixture()
def app(request):
    fixture = Application_user()
    request.addfinalizer(fixture.destroy)
    return fixture



def test_add_new_user(app):
    app.login(username="admin", password="secret")
    app.add_new_user(Anketa(firstname="Вася", midlename="Петрович", lastname='Пупкин', nickname='Пупка',
                                     company='Ромашка', address='Москва', home_tel='79999999999',
                                     mobile_tel='78888888888', work_tel='77777777777', email='pypka@mail.ru',
                                     byear='1990', address2='Москва 2'))
    app.logout()



