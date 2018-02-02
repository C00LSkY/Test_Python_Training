__author__ = "C00LSkY"

class Group:

    def __init__(self, name, header, footer):
        self.name = name
        self.header = header
        self.footer = footer


class Anketa:

    def __init__(self, firstname, midlename, lastname, nickname, company, address, home_tel, mobile_tel, work_tel, email,
                 byear, address2):
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
