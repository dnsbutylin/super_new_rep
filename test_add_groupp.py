# -*- coding: utf-8 -*-
import unittest, pytest
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from group import Group
from application import Application

class TestAddGroupp(unittest.TestCase):
    def setUp(self):
        self.app = Application()

    def test_add_groupp(self):
        self.app.login(username="admin", password="secret")
        self.app.create_group(Group(name="sadsdasda", header="sadassdadasd", footer="sfaffafa"))
        self.app.logout()

    def test_add_empty_groupp(self):
        self.app.login(username="admin", password="secret")
        self.app.create_group(Group(name="", header="", footer=""))
        self.app.logout()

    def tearDown(self):
        self.app.destroy()

if __name__ == "__main__":
    unittest.main()
