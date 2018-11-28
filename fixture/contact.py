from selenium.webdriver.support.ui import Select


class ContactHelper:

    def __init__(self, app):
        self.app = app

    def click_add_new(self):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()

    def create(self, contact):
        wd = self.app.wd
        self.click_add_new()
        self.fill_contact_form(contact)
        # Нажимаем подтвердить
        wd.find_element_by_name("submit").click()

    def fill_contact_form(self, contact):
        # Заполняет данные в форму
        wd = self.app.wd
        self.change_field_value('firstname', contact.firstname)
        self.change_field_value('middlename', contact.middlename)
        self.change_field_value('lastname', contact.lastname)
        self.change_field_value('nickname', contact.nickname)
        self.change_field_value('photo', contact.photo)
        self.change_field_value('title', contact.title)
        self.change_field_value('company', contact.company)
        self.change_field_value('address', contact.address)
        self.change_field_value('home', contact.home)
        self.change_field_value('mobile', contact.mobile)
        self.change_field_value('work', contact.work)
        self.change_field_value('fax', contact.fax)
        self.change_field_value('email', contact.email)
        self.change_field_value('email2', contact.email2)
        self.change_field_value('email3', contact.email3)
        self.change_field_value('homepage', contact.homepage)
        self.change_field_value('bday', contact.bday)
        self.change_field_value('bmonth', contact.bmonth)
        self.change_field_value('byear', contact.byear)
        self.change_field_value('aday', contact.aday)
        self.change_field_value('amonth', contact.amonth)
        self.change_field_value('ayear', contact.ayear)
        self.change_field_value('address2', contact.address2)
        self.change_field_value('phone2', contact.phone2)
        self.change_field_value('notes', contact.notes)

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            if field_name == 'bday' or field_name == 'bmonth' or field_name == 'aday' or field_name == 'amonth':
                Select(wd.find_element_by_name(field_name)).select_by_visible_text(text)
            else:
                wd.find_element_by_name(field_name).clear()
                wd.find_element_by_name(field_name).send_keys(text)

    def delete_first_contact(self):
        wd = self.app.wd
        self.open_contact_list()
        self.select_first_contact()
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to.alert.accept()
        self.open_contact_list()

    def modify_first_contact(self, new_contact_data):
        wd = self.app.wd
        self.open_contact_list()
        self.select_first_contact()
        # Нажимаем карандашик (редактировать)
        wd.find_element_by_xpath("//img[@alt='Edit']").click()
        #Заполняем новые данные в форму
        self.fill_contact_form(new_contact_data)
        # Нажимаем кнопку update
        wd.find_element_by_name("update").click()

    def select_first_contact(self):
        wd = self.app.wd
        wd.find_element_by_name('selected[]').click()

    def open_contact_list(self):
        wd = self.app.wd
        if not(wd.current_url.endswith('/addressbook/') and
               len(wd.find_elements_by_link_text("Last name")) == 1):
            wd.find_element_by_link_text("home").click()

    def count(self):
        wd = self.app.wd
        self.open_contact_list()
        return len(wd.find_elements_by_name('selected[]'))


