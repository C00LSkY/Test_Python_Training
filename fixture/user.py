__author__ = "C00LSkY"

from model.contacts import Anketa
import re

class UserHelper:

    def __init__(self, app):
        self.app = app

    def open_home(self):
        wd = self.app.wd
        if not ((wd.current_url.endswith("/addressbook/")) and (wd.find_element_by_link_text("Logout"))):
            wd.find_element_by_link_text("home").click()

    def add_new_user(self, contacts):
        wd = self.app.wd
        self.open_home()
        # input user parametrs
        wd.find_element_by_link_text("add new").click()
        self.fill_user_form(contacts)
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()
        self.user_list_cashe = None

    def select_first_user(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def select_user_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()

    def delete_first_user(self):
        self.delete_user_by_index(0)


    def delete_user_by_index(self, index):
        wd = self.app.wd
        self.open_home()
        #select first user
        self.select_user_by_index(index)
        #submit deletion
        wd.find_element_by_xpath("//div[@id='content']/form[2]/div[2]/input").click()
        wd.switch_to_alert().accept()
        self.user_list_cashe = None

    def edit_first_user(self, contacts):
        self.edit_user_by_index(0, contacts)


    def edit_user_by_index(self, index, contacts):
        wd = self.app.wd
        self.open_home()
        # input user parametrs
        self.select_user_edit_by_index(index)
        self.fill_user_form(contacts)
        wd.find_element_by_xpath("//div[@id='content']/form[1]/input[22]").click()
        self.user_list_cashe = None

    def edit_user_by_id(self, id, contacts):
        wd = self.app.wd
        self.open_home()
        self.select_user_by_id(id)
        #wd.find_element_by_xpath("//tr[td[input[@id='%s']]]/td/a/img[@title='Edit']" % id).click()
        # input user parametrs
        self.fill_user_form(contacts)
        wd.find_element_by_xpath("//input[@value='Update']").click()
        self.user_list_cashe = None


    def fill_user_form(self, contacts):
        wd = self.app.wd
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(contacts.firstname)
        wd.find_element_by_name("middlename").click()
        wd.find_element_by_name("middlename").clear()
        wd.find_element_by_name("middlename").send_keys(contacts.midlename)
        wd.find_element_by_name("lastname").click()
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(contacts.lastname)
        wd.find_element_by_name("nickname").click()
        wd.find_element_by_name("nickname").clear()
        wd.find_element_by_name("nickname").send_keys(contacts.nickname)
        wd.find_element_by_name("title").click()
        wd.find_element_by_name("company").click()
        wd.find_element_by_name("company").clear()
        wd.find_element_by_name("company").send_keys(contacts.company)
        wd.find_element_by_name("address").click()
        wd.find_element_by_name("address").clear()
        wd.find_element_by_name("address").send_keys(contacts.address)
        wd.find_element_by_name("home").click()
        wd.find_element_by_name("home").clear()
        wd.find_element_by_name("home").send_keys(contacts.home_tel)
        wd.find_element_by_name("mobile").click()
        wd.find_element_by_name("mobile").clear()
        wd.find_element_by_name("mobile").send_keys(contacts.mobile_tel)
        wd.find_element_by_name("work").click()
        wd.find_element_by_name("work").clear()
        wd.find_element_by_name("work").send_keys(contacts.work_tel)
        wd.find_element_by_name("email").click()
        wd.find_element_by_name("email").clear()
        wd.find_element_by_name("email").send_keys(contacts.email)
        if not wd.find_element_by_xpath("//div[@id='content']/form/select[1]//option[3]").is_selected():
            wd.find_element_by_xpath("//div[@id='content']/form/select[1]//option[3]").click()
        if not wd.find_element_by_xpath("//div[@id='content']/form/select[2]//option[2]").is_selected():
            wd.find_element_by_xpath("//div[@id='content']/form/select[2]//option[2]").click()
        wd.find_element_by_name("byear").click()
        wd.find_element_by_name("byear").clear()
        wd.find_element_by_name("byear").send_keys(contacts.byear)
        wd.find_element_by_name("address2").click()
        wd.find_element_by_name("address2").clear()
        wd.find_element_by_name("address2").send_keys(contacts.address2)

    def select_user_edit_by_index(self, index):
        wd = self.app.wd
        self.open_home()
        wd.find_elements_by_xpath(".//img[@title='Edit']")[index].click()

    def select_user_view_by_index(self, index):
        wd = self.app.wd
        self.open_home()
        wd.find_elements_by_xpath(".//img[@title='Details']")[index].click()

    def count_user(self):
        wd = self.app.wd
        self.open_home()
        # select first user
        return len(wd.find_elements_by_name("selected[]"))


    user_list_cashe = None

    def get_user_list(self):
        if self.user_list_cashe is None:
            wd = self.app.wd
            self.open_home()
            self.user_list_cashe = []
            for element in wd.find_elements_by_name("entry"):
               cell = element.find_elements_by_tag_name("td")
               text = cell[1].text
               text2 = cell[2].text
               id = element.find_element_by_name("selected[]").get_attribute("value")
               address = cell[3].text
               all_phones = cell[5].text
               all_emails = cell[4].text
               self.user_list_cashe.append(Anketa(lastname=text, id=id, firstname=text2,
                                                  all_phones_from_home_page=all_phones,
                                                  all_email_from_home_page=all_emails, address=address))
        return list(self.user_list_cashe)

    def get_user_info_from_edit_page(self, index):
        wd = self.app.wd
        self.select_user_edit_by_index(index)
        firstname = wd.find_element_by_name('firstname').get_attribute('value')
        lastname = wd.find_element_by_name('lastname').get_attribute('value')
        id = wd.find_element_by_name('id').get_attribute('value')
        home_tel = wd.find_element_by_name('home').get_attribute('value')
        mobile_tel = wd.find_element_by_name('mobile').get_attribute('value')
        work_tel = wd.find_element_by_name('work').get_attribute('value')
        email = wd.find_element_by_name('email').get_attribute('value')
        email2 = wd.find_element_by_name('email2').get_attribute('value')
        email3 = wd.find_element_by_name('email3').get_attribute('value')
        address = wd.find_element_by_name('address').get_attribute('value')
        return Anketa(firstname=firstname, lastname=lastname, id=id, home_tel=home_tel, mobile_tel=mobile_tel,
                      work_tel=work_tel, email=email, email2=email2, email3=email3, address=address)

    def get_user_list_on_view_page(self, index):
        wd = self.app.wd
        self.select_user_view_by_index(index)
        text = wd.find_element_by_id("content").text
        home_tel = re.search("H: (.*)", text).group(1)
        mobile_tel = re.search("M: (.*)", text).group(1)
        work_tel = re.search("W: (.*)", text).group(1)
        return Anketa(home_tel=home_tel, mobile_tel=mobile_tel, work_tel=work_tel)

    def delete_user_by_id(self, id):
        wd = self.app.wd
        self.open_home()
        # select first user
        self.select_user_by_id(id)
        # submit deletion
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to_alert().accept()
        self.user_list_cashe = None


    def select_user_by_id(self, id):
        wd = self.app.wd
        wd.find_element_by_id(id).click()




