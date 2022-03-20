# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contact(first_name="first name", middle_name="middle name", last_name="last name",
                      nickname="nickname", title="title", company="company",
                      address="street 1/10, 01-059 Warsaw", phone_home="22 837 94 83",
                      phone_mobile="738 928 736", phone_work="938 728 738", fax="22 948 03 84",
                      email_1="email1@gmail.com", email_2="email2@gmail.com",
                      email_3="email3@gmail.com", homepage="www.testingpython.com",
                      birthday_day="13", birthday_month="September", birthday_year="1990",
                      anniversary_day="14", anniversary_month="November", anniversary_year="2020",
                      address_2="street 9/33, 03-254 Warsaw", phone_2="22 474 94 73", notes="notes")
    app.contact.create(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
