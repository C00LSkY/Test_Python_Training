
from model.contacts import Anketa
from random import randrange
import re



def test_check_contact_home_page_with_edit_page(app):
    if app.user.count_user() == 0:
        app.user.add_new_user(Anketa(firstname="Вася", midlename="Петрович", lastname='Пупкин', nickname='Пупка',
                                     company='Ромашка+Олень', address='Москва', home_tel='79999999990',
                                     mobile_tel='78888888880', work_tel='555', email='pypka@mail.ru',
                                     email2='pyp2@l.ru', email3='pyp2@r.ru', byear='', address2='тест моск'))
    contact_from_home_page = app.user.get_user_list()
    index = randrange(len(contact_from_home_page))
    contact_from_home_page = app.user.get_user_list()[index]
    contact_from_edit_page = app.user.get_user_info_from_edit_page(index)
    assert contact_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(contact_from_edit_page)
    assert contact_from_home_page.all_email_from_home_page == merge_email_like_on_home_page(contact_from_edit_page)
    assert contact_from_home_page.firstname == contact_from_edit_page.firstname
    assert contact_from_home_page.lastname == contact_from_edit_page.lastname
    assert contact_from_home_page.address == contact_from_edit_page.address


def clear(s):
    return re.sub("[() -]", "", s)


def merge_phones_like_on_home_page(contacts):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x), filter(lambda x: x is not None,
                                                          [contacts.home_tel, contacts.mobile_tel, contacts.work_tel]))))

def merge_email_like_on_home_page(contacts):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x), filter(lambda x: x is not None,
                                                          [contacts.email, contacts.email2, contacts.email3]))))