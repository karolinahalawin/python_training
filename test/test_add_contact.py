# -*- coding: utf-8 -*-
import pytest
from model.contact import Contact
from fixture.application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_contact(app):
    app.login(username="admin", password="secret")
    app.create_contact(Contact(first_name="first name", middle_name="middle name", last_name="last name",
                               nickname="nickname", title="title", company="company",
                               address="street 1/10, 01-059 Warsaw", phone_home="22 837 94 83",
                               phone_mobile="738 928 736", phone_work="938 728 738", fax="22 948 03 84",
                               email_1="email1@gmail.com", email_2="email2@gmail.com",
                               email_3="email3@gmail.com", homepage="www.testingpython.com",
                               birthday_day="13", birthday_month="September", birthday_year="1990",
                               anniversary_day="14", anniversary_month="November", anniversary_year="2020",
                               address_2="street 9/33, 03-254 Warsaw", phone_2="22 474 94 73", notes="notes"))
    app.logout()
