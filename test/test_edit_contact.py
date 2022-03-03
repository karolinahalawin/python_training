from model.contact import Contact


def test_edit_first_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.edit_first_contact(
        Contact(first_name="first name edit", middle_name="middle name edit", last_name="last name edit",
                nickname="nickname edit", title="title edit", company="company edit",
                address="street 1/10, 01-059 Warsaw edit", phone_home="22 837 94 83 11",
                phone_mobile="738 928 736 11", phone_work="938 728 738 11", fax="22 948 03 84 11",
                email_1="emailedit1@gmail.com", email_2="emailedit2@gmail.com",
                email_3="emailedit3@gmail.com", homepage="www.testingpythonedit.com",
                birthday_day="11", birthday_month="December", birthday_year="1991",
                anniversary_day="18", anniversary_month="January", anniversary_year="2021",
                address_2="street 9/33, 03-254 Warsaw edit", phone_2="22 474 94 73 11",
                notes="notes edit"))
    app.session.logout()
