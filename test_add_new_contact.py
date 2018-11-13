# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import unittest, pytest
from contact import Contact

class TestAddNewContact(unittest.TestCase):
    def setUp(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)

    def test_add_new_contact(self):
        self.login(username="admin", password="secret")
        self.create_new_contact(Contact(firstname="Denis", middlename="Butylin", lastname="lastname",
                                        nickname="nickname", title="title", company="company", address="address",
                                        home="home", mobile="mobile", work="work", fax="fax",
                                        email="email1", email2="email2", email3="email3",
                                        homepage="homepage",  bday="29", bmonth="April", byear="1992",
                                        aday="1", amonth="January", ayear="2000",
                                        address2="address2", phone2="phone2", notes="notes"))

        self.logout()

    def logout(self):
        wd = self.wd
        wd.find_element_by_link_text("Logout").click()

    def try_to_upload_foto(self):
        wd = self.wd
        wd.find_element_by_name("photo").send_keys(r"C:\PycharmProjects\123\OklqbFQ_dbA.jpg")

    def create_new_contact(self, contact):
        wd = self.wd
        self.click_add_new()
        self.try_to_upload_foto()
        # Заполняет данные в форму
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(contact.firstname)
        wd.find_element_by_name("middlename").clear()
        wd.find_element_by_name("middlename").send_keys(contact.middlename)
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(contact.lastname)
        wd.find_element_by_name("nickname").clear()
        wd.find_element_by_name("nickname").send_keys(contact.nickname)
        wd.find_element_by_name("title").clear()
        wd.find_element_by_name("title").send_keys(contact.title)
        wd.find_element_by_name("company").clear()
        wd.find_element_by_name("company").send_keys(contact.company)
        wd.find_element_by_name("address").clear()
        wd.find_element_by_name("address").send_keys(contact.address)
        wd.find_element_by_name("home").clear()
        wd.find_element_by_name("home").send_keys(contact.home)
        wd.find_element_by_name("mobile").clear()
        wd.find_element_by_name("mobile").send_keys(contact.mobile)
        wd.find_element_by_name("work").clear()
        wd.find_element_by_name("work").send_keys(contact.work)
        wd.find_element_by_name("fax").clear()
        wd.find_element_by_name("fax").send_keys(contact.fax)
        wd.find_element_by_name("email").clear()
        wd.find_element_by_name("email").send_keys(contact.email)
        wd.find_element_by_name("email2").clear()
        wd.find_element_by_name("email2").send_keys(contact.email2)
        wd.find_element_by_name("email3").clear()
        wd.find_element_by_name("email3").send_keys(contact.email3)
        wd.find_element_by_name("homepage").clear()
        wd.find_element_by_name("homepage").send_keys(contact.homepage)

        Select(wd.find_element_by_name("bday")).select_by_visible_text(contact.bday)
        Select(wd.find_element_by_name("bmonth")).select_by_visible_text(contact.bmonth)
        wd.find_element_by_name("byear").send_keys(contact.byear)
        Select(wd.find_element_by_name("aday")).select_by_visible_text(contact.aday)
        Select(wd.find_element_by_name("amonth")).select_by_visible_text(contact.amonth)
        wd.find_element_by_name("ayear").send_keys(contact.ayear)

        wd.find_element_by_name("address2").click()
        wd.find_element_by_name("address2").clear()
        wd.find_element_by_name("address2").send_keys(contact.address2)
        wd.find_element_by_name("phone2").click()
        wd.find_element_by_name("phone2").clear()
        wd.find_element_by_name("phone2").send_keys(contact.phone2)
        wd.find_element_by_name("notes").click()
        wd.find_element_by_name("notes").clear()
        wd.find_element_by_name("notes").send_keys(contact.notes)
        wd.find_element_by_name("submit").click()


    def open_homepage(self):
        wd = self.wd
        wd.get("http://localhost/addressbook/")

    def click_add_new(self):
        wd = self.wd
        wd.find_element_by_link_text("add new").click()

    def login(self, username, password):
        wd = self.wd
        self.open_homepage()
        # Login
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(username)
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_id("LoginForm").submit()

    def tearDown(self):
        self.wd.quit()

if __name__ == "__main__":
    unittest.main()
