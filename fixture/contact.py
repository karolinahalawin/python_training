from selenium.webdriver.support.ui import Select
from model.contact import Contact
import re


class ContactHelper:

    def __init__(self, app):
        self.app = app

    def open_new_contact_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()

    def create(self, contact):
        wd = self.app.wd
        self.open_contacts_page()
        self.open_new_contact_page()
        self.fill_contact_form(contact)
        # submit contact creation
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()
        self.contact_cache = None

    def fill_contact_form(self, contact):
        wd = self.app.wd
        self.change_field_value("firstname", contact.first_name)
        self.change_field_value("middlename", contact.middle_name)
        self.change_field_value("lastname", contact.last_name)
        self.change_field_value("nickname", contact.nickname)
        self.change_field_value("title", contact.title)
        self.change_field_value("company", contact.company)
        self.change_field_value("address", contact.address)
        self.change_field_value("home", contact.phone_home)
        self.change_field_value("mobile", contact.phone_mobile)
        self.change_field_value("work", contact.phone_work)
        self.change_field_value("fax", contact.fax)
        self.change_field_value("email", contact.email_1)
        self.change_field_value("email2", contact.email_2)
        self.change_field_value("email3", contact.email_3)
        self.change_field_value("homepage", contact.homepage)
        self.change_dropdown_value("bday", contact.birthday_day)
        self.change_dropdown_value("bmonth", contact.birthday_month)
        self.change_field_value("byear", contact.birthday_year)
        self.change_dropdown_value("aday", contact.anniversary_day)
        self.change_dropdown_value("amonth", contact.anniversary_month)
        self.change_field_value("ayear", contact.anniversary_year)
        self.change_field_value("address2", contact.address_2)
        self.change_field_value("phone2", contact.phone_2)
        self.change_field_value("notes", contact.notes)

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def change_dropdown_value(self, field_name, value):
        wd = self.app.wd
        if value is not None:
            wd.find_element_by_name(field_name).click()
            Select(wd.find_element_by_name(field_name)).select_by_visible_text(value)
            wd.find_element_by_xpath("//option[@value='13']").click()

    def edit_first_contact(self):
        self.edit_contact_by_index(0)

    def edit_contact_by_index(self, index, new_contact_data):
        wd = self.app.wd
        self.open_contacts_page()
        self.select_contact_by_index(index)
        # click on details button
        wd.find_element_by_xpath("//img[@alt='Details']").click()
        # click on modify button
        wd.find_element_by_name("modifiy").click()
        self.fill_contact_form(new_contact_data)
        # click on update button
        wd.find_element_by_name("update").click()
        self.contact_cache = None

    def select_first_contact(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def select_contact_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()

    def delete_first_contact(self):
        self.delete_contact_by_index(0)

    def delete_contact_by_index(self, index):
        wd = self.app.wd
        self.open_contacts_page()
        self.select_contact_by_index(index)
        # click on details button
        wd.find_element_by_xpath("//img[@alt='Details']").click()
        # click on modify button
        wd.find_element_by_name("modifiy").click()
        # submit deletion
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        self.open_contacts_page()
        self.contact_cache = None

    def count(self):
        wd = self.app.wd
        self.open_contacts_page()
        return len(wd.find_elements_by_name("selected[]"))

    def open_contacts_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("addressbook/") and len(
                wd.find_elements_by_xpath("//input[@value='Send e-Mail']")) > 0):
            wd.find_element_by_link_text("home").click()

    contact_cache = None

    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.open_contacts_page()
            self.contact_cache = []
            for element in wd.find_elements_by_name("entry"):
                rows = element.find_elements_by_tag_name("td")
                last_name = rows[1].text
                first_name = rows[2].text
                id = rows[0].find_element_by_tag_name("input").get_attribute("value")
                all_phones = rows[5].text.splitlines()
                self.contact_cache.append(
                    Contact(first_name=first_name, last_name=last_name, id=id, phone_home=all_phones[0],
                            phone_mobile=all_phones[1], phone_work=all_phones[2], phone_2=all_phones[3]))
        return self.contact_cache

    def open_contact_to_edit_by_index(self, index):
        wd = self.app.wd
        self.open_contacts_page()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[7]
        cell.find_element_by_tag_name("a").click()

    def open_contact_view_by_index(self, index):
        wd = self.app.wd
        self.open_contacts_page()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[6]
        cell.find_element_by_tag_name("a").click()

    def get_contact_info_from_edit_page(self, index):
        wd = self.app.wd
        self.open_contact_to_edit_by_index(index)
        first_name = wd.find_element_by_name("firstname").get_attribute("value")
        last_name = wd.find_element_by_name("lastname").get_attribute("value")
        id = wd.find_element_by_name("id").get_attribute("value")
        phone_home = wd.find_element_by_name("home").get_attribute("value")
        phone_work = wd.find_element_by_name("work").get_attribute("value")
        phone_mobile = wd.find_element_by_name("mobile").get_attribute("value")
        phone_2 = wd.find_element_by_name("phone2").get_attribute("value")
        return Contact(first_name=first_name, last_name=last_name, id=id, phone_home=phone_home, phone_work=phone_work,
                       phone_mobile=phone_mobile, phone_2=phone_2)

    def get_contact_from_view_page(self, index):
        wd = self.app.wd
        self.open_contact_view_by_index(index)
        text = wd.find_element_by_id("content").text
        phone_home = re.search("H: (.*)", text).group(1)
        phone_work = re.search("W: (.*)", text).group(1)
        phone_mobile = re.search("M: (.*)", text).group(1)
        phone_2 = re.search("P: (.*)", text).group(1)
        return Contact(phone_home=phone_home, phone_work=phone_work, phone_mobile=phone_mobile, phone_2=phone_2)
