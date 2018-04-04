
from model.contacts import Anketa
import re



def test_check_contact_home_page_with_edit_page(app, db):
    if len(db.get_user_list()) == 0:
        app.user.add_new_user(Anketa(firstname="Вася", midlename="Петрович", lastname='Пупкин', nickname='Пупка',
                                     company='Ромашка+Олень', address='Москва', home_tel='79999999990',
                                     mobile_tel='78888888880', work_tel='555', email='pypka@mail.ru',
                                     email2='pyp2@l.ru', email3='pyp2@r.ru', byear='', address2='тест моск'))
    contact_ui = sorted(app.user.get_user_list(), key=Anketa.id_or_max)
    contact_db = sorted(db.get_user_list(), key=Anketa.id_or_max)
    assert len(contact_ui) == len(contact_db)
    for i in range (len(contact_db)):
        assert contact_ui[i].all_phones_from_home_page == merge_phones_like_on_home_page(contact_db[i])
        assert contact_ui[i].all_email_from_home_page == merge_email_like_on_home_page(contact_db[i])
        assert contact_ui[i].firstname == contact_db[i].firstname
        assert contact_ui[i].lastname == contact_db[i].lastname
        assert contact_ui[i].address == contact_db[i].address


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