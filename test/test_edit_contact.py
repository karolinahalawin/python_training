from model.contact import Contact


def test_edit_contact_first_name(app):
    app.session.login(username="admin", password="secret")
    app.contact.edit_first_contact(
        Contact(first_name="first name edit"))
    app.session.logout()


def test_edit_contact_middle_name(app):
    app.session.login(username="admin", password="secret")
    app.contact.edit_first_contact(
        Contact(middle_name="middle name edit"))
    app.session.logout()


def test_edit_contact_last_name(app):
    app.session.login(username="admin", password="secret")
    app.contact.edit_first_contact(
        Contact(last_name="last name edit"))
    app.session.logout()
