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


testdata = [Contact(first_name="", middle_name="", last_name="", nickname="", title="", company="", address="",
                    phone_home="", phone_mobile="", phone_work="", fax="", email_1="", email_2="", email_3="",
                    homepage="", address_2="", phone_2="", notes="")] + [
               Contact(first_name=random_string("first name", 10), middle_name=random_string("middle name", 10),
                       last_name=random_string("last name", 10), nickname=random_string("nickname", 10),
                       title=random_string("title", 5), company=random_string("company", 10),
                       address=random_string("address", 20), phone_home=random_numbers("22", 7),
                       phone_mobile=random_numbers("22", 7), phone_work=random_numbers("22", 7),
                       fax=random_numbers("22", 7), email_1=random_string("email1", 10),
                       email_2=random_string("email2", 10), email_3=random_string("email2", 10),
                       homepage=random_string("homepage", 10), address_2=random_string("address2", 10),
                       phone_2=random_numbers("22", 7), notes=random_string("notes", 20))
               for i in range(5)
           ]


@pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])
def test_add_contact(app, contact):
    old_contacts = app.contact.get_contact_list()
    app.contact.create(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
