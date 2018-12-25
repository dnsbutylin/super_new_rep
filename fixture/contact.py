from selenium.webdriver.support.ui import Select
from model.contact import Contact
import re


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
        self.contact_cache = None

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
        self.delete_contact_by_index(0)

    def delete_contact_by_index(self, index):
        wd = self.app.wd
        self.open_contact_list()
        self.select_contact_by_index(index)
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to.alert.accept()
        self.open_contact_list()
        self.contact_cache = None

    def delete_contact_by_id(self, id):
        wd = self.app.wd
        self.open_contact_list()
        self.select_contact_by_id(id)
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to.alert.accept()
        self.open_contact_list()
        self.contact_cache = None

    def delete_contact_from_group(self, contact_id, group):
        wd = self.app.wd
        self.open_contact_list()
        #wd.find_element_by_name("group").click()
        #Select(wd.find_element_by_name("group")).select_by_visible_text(group.name)
        wd.find_element_by_xpath("//option[@value='%s']" % str(group.id)).click()
        self.select_contact_by_id(contact_id)
        wd.find_element_by_name("remove").click()


    def modify_first_contact(self, new_contact_data):
        self.modify_contact_by_index(0, new_contact_data)

    def modify_contact_by_index(self, index, new_contact_data):
        wd = self.app.wd
        self.open_contact_list()
        self.select_contact_by_index(index)
        # Нажимаем нужный карандашик по индексу выбранного элемента + 1 (редактировать)
        wd.find_element_by_xpath("(//img[@alt='Edit'])[" + str(index+1) + "]").click()
        self.fill_contact_form(new_contact_data)
        wd.find_element_by_name("update").click()
        self.contact_cache = None

    def modify_contact_by_id(self, id, new_contact_data):
        wd = self.app.wd
        self.open_contact_list()
        #Закомменчено, так как не обязательно ставить галочку у элемента
        #перед тем, как нажать карандашик
        #self.select_contact_by_id(id)
        # Нажимаем нужный карандашик по индексу выбранного элемента + 1 (редактировать)
        wd.find_element_by_css_selector("a[href='edit.php?id=%s']" % id).click()
        self.fill_contact_form(new_contact_data)
        wd.find_element_by_name("update").click()
        self.contact_cache = None

    def select_first_contact(self):
        wd = self.app.wd
        wd.find_element_by_name('selected[]').click()

    def select_contact_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_name('selected[]')[index].click()

    def select_contact_by_id(self, id):
        wd = self.app.wd
        wd.find_element_by_id('%s' % id).click()

    def open_contact_list(self):
        wd = self.app.wd
        if not(wd.current_url.endswith('/addressbook/') and
               len(wd.find_elements_by_link_text("Last name")) == 1):
            wd.find_element_by_link_text("home").click()

    def count(self):
        wd = self.app.wd
        self.open_contact_list()
        return len(wd.find_elements_by_name('selected[]'))

    def add_to_group(self, contact_id, group_id):
        wd = self.app.wd
        self.open_contact_list()
        self.select_contact_by_id(contact_id)
        #Select(wd.find_element_by_name("to_group")).select_by_visible_text(group_name)
        wd.find_element_by_css_selector("select[name=\"to_group\"] > option[value=\"%s\"]" %group_id).click()
        wd.find_element_by_name("add").click()


    contact_cache = None
    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.open_contact_list()
            self.contact_cache = []
            for element in wd.find_elements_by_name('entry'):
                cells = element.find_elements_by_tag_name("td")
                id = cells[0].find_element_by_name('selected[]').get_attribute('value')
                lastname = cells[1].text
                firstname = cells[2].text
                address = cells[3].text
                all_emails = cells[4].text
                all_phones = cells[5].text
                self.contact_cache.append(Contact(firstname=firstname, lastname=lastname, address=address, id=id,
                                                  all_phones_from_home_page=all_phones, all_emails_from_home_page=all_emails))
        # Возвращаем копию кеша
        return list(self.contact_cache)

    def open_contact_to_edit_by_index(self, index):
        wd = self.app.wd
        self.app.open_homepage()
        row = wd.find_elements_by_name('entry')[index]
        cell = row.find_elements_by_tag_name('td')[7]
        cell.find_element_by_tag_name('a').click()

    def open_contact_view_by_index(self, index):
        wd = self.app.wd
        self.app.open_homepage()
        row = wd.find_elements_by_name('entry')[index]
        cell = row.find_elements_by_tag_name('td')[6]
        cell.find_element_by_tag_name('a').click()

    def get_contact_info_from_edit_page(self, index):
        wd = self.app.wd
        self.open_contact_to_edit_by_index(index)
        firstname = wd.find_element_by_name('firstname').get_attribute('value')
        lastname = wd.find_element_by_name('lastname').get_attribute('value')
        address = wd.find_element_by_name('address').get_attribute('value')
        id = wd.find_element_by_name('id').get_attribute('value')
        home = wd.find_element_by_name('home').get_attribute('value')
        work = wd.find_element_by_name('work').get_attribute('value')
        mobile = wd.find_element_by_name('mobile').get_attribute('value')
        phone2 = wd.find_element_by_name('phone2').get_attribute('value')
        email = wd.find_element_by_name('email').get_attribute('value')
        email2 = wd.find_element_by_name('email2').get_attribute('value')
        email3 = wd.find_element_by_name('email3').get_attribute('value')
        return Contact(firstname=firstname, lastname=lastname, address=address, id=id,
                       home=home, work=work,
                       mobile=mobile, phone2=phone2, email=email, email2=email2, email3=email3)

    def get_contact_from_view_page(self, index):
        def clear(s):
            return re.sub("[() -]", "", s)
        wd = self.app.wd
        self.open_contact_view_by_index(index)
        text = wd.find_element_by_id('content').text
        try:
            home = re.search('H: (.*)', text).group(1)
        except AttributeError:
            home = ''
        try:
            work = re.search('W: (.*)', text).group(1)
        except AttributeError:
            work = ''
        try:
            mobile = re.search('M: (.*)', text).group(1)
        except AttributeError:
            mobile = ''
        try:
            phone2 = re.search('P: (.*)', text).group(1)
        except AttributeError:
            phone2 = ''
        # Получаем все емейлы и homepage из контакта, осталось взять у них .text
        cells = wd.find_elements_by_xpath("//div[@id='content']/a")
        #Оставляем только емейлы
        cells = cells[:-1]

        return Contact(all_phones_from_home_page='\n'.join(filter(lambda x: x !='',
                                                                  map(lambda x: clear(x),
                                                                      filter(lambda x: x is not None,[home, mobile, work, phone2])))),
                       # Берём у всех .text, склеиваем в строку, добавляя \n после каждого элемента
                       all_emails_from_home_page='\n'.join(map(lambda x: x.text, cells)))


