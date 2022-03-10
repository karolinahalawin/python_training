from model.contact import Contact


def test_edit_contact_first_name(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(first_name="test"))
    app.contact.edit_first_contact(Contact(first_name="first name edit"))


def test_edit_contact_middle_name(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(middle_name="test"))
    app.contact.edit_first_contact(Contact(middle_name="middle name edit"))


def test_edit_contact_last_name(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(last_name="test"))
    app.contact.edit_first_contact(Contact(last_name="last name edit"))
