__author__ = "C00LSkY"

from model.contacts import Anketa

def test_edit_user(app):
    app.session.login(username="admin", password="secret")
    app.user.edit_first_user(Anketa(firstname="Николай", midlename="Петрович", lastname='Пупкин', nickname='Pypka',
                                     company='Ромашка+Олень', address='Москва', home_tel='79999999990',
                                     mobile_tel='78888888880', work_tel='', email='pypka@mail.ru',
                                     byear='1990', address2='Москва 2'))
    app.session.logout()