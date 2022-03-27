# -*- coding: utf-8 -*-
from model.contact import Contact
import pytest
import random
import string


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " " * 10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


def random_numbers(prefix, maxlen):
    symbols = string.digits
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


testdata = [
    Contact(first_name=first_name, middle_name=middle_name, last_name=last_name, nickname=nickname, title=title,
            company=company, address=address, phone_home=phone_home, phone_mobile=phone_mobile, phone_work=phone_work,
            fax=fax, email_1=email_1, email_2=email_2, email_3=email_3, homepage=homepage, address_2=address_2,
            phone_2=phone_2, notes=notes)
    for first_name in ["", random_string("first name", 10)]
    for middle_name in ["", random_string("middle name", 10)]
    for last_name in ["", random_string("last name", 10)]
    for nickname in ["", random_string("nickname", 10)]
    for title in ["", random_string("title", 5)]
    for company in ["", random_string("company", 10)]
    for address in ["", random_string("address", 20)]
    for phone_home in ["", random_numbers("22", 7)]
    for phone_mobile in ["", random_numbers("22", 7)]
    for phone_work in ["", random_numbers("22", 7)]
    for fax in ["", random_numbers("22", 7)]
    for email_1 in ["", random_string("email1", 10)]
    for email_2 in ["", random_string("email2", 10)]
    for email_3 in ["", random_string("email2", 10)]
    for homepage in ["", random_string("homepage", 10)]
    for address_2 in ["", random_string("address2", 10)]
    for phone_2 in ["", random_numbers("22", 7)]
    for notes in ["", random_string("notes", 20)]
]


@pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])
def test_add_contact(app, contact):
    old_contacts = app.contact.get_contact_list()
    app.contact.create(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
