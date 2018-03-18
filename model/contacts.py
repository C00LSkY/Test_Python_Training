__author__ = "C00LSkY"

from sys import maxsize

class Anketa:

    def __init__(self, firstname = None, midlename = None, lastname = None, nickname = None, company = None,
                 address = None, home_tel = None, mobile_tel = None, work_tel = None, email = None,byear = None,
                 address2 = None, id=None, all_phones_from_home_page=None):
        self.firstname = firstname
        self.midlename = midlename
        self.lastname = lastname
        self.nickname = nickname
        self.company = company
        self.address = address
        self.home_tel = home_tel
        self.mobile_tel = mobile_tel
        self.work_tel = work_tel
        self.email = email
        self.byear = byear
        self.address2 = address2
        self.all_phones_from_home_page = all_phones_from_home_page
        self.id = id

    def __repr__(self):
        return "%s:%s:%s" % (self.id, self.lastname, self.firstname)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and self.lastname == other.lastname \
               and self.firstname == other.firstname

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize

