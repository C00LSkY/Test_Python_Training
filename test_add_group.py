# -*- coding: utf-8 -*-
__author__ = "C00LSkY"

import unittest

from selenium.webdriver.firefox.webdriver import WebDriver

from group import Group

from application import Application


def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False

class test_add_group(unittest.TestCase):
    def setUp(self):
        self.wd = WebDriver(capabilities={"marionette": False}, firefox_binary="C:/Program Files/Mozilla Firefox/firefox.exe")
        self.wd.implicitly_wait(60)

    def logout(self):
        wd = self.wd
        wd.find_element_by_link_text("Logout").click()

    def create_group(self, group):
        wd = self.wd
        # create group
        wd.find_element_by_link_text("groups").click()
        wd.find_element_by_name("new").click()
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys(group.name)
        wd.find_element_by_name("group_header").click()
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys(group.header)
        wd.find_element_by_name("group_footer").click()
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys(group.footer)
        wd.find_element_by_name("submit").click()
        wd.find_element_by_link_text("groups").click()



    def login(self, username, password):
        wd = self.wd
        wd.get("http://localhost/addressbook/")
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys("%s" % username)
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys("%s" % password)
        wd.find_element_by_xpath("//form[@id='LoginForm']/input[3]").click()



    def test_add_group(self):
        self.login( username="admin", password="secret"))
        self.create_group( Group(name="test_group", header="тестовая группа", footer="группа 2018"))
        self.logout()

    def test_empty_group(self):
        self.login(username="admin", password="secret")
        self.create_group(Group(name="", header="", footer=""))
        self.logout()


    def tearDown(self):
        self.wd.quit()

if __name__ == '__main__':
    unittest.main()
