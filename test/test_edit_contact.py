from model.contact import Contact


def test_edit_contact_first_name(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(first_name="test"))
    old_contacts = app.contact.get_contact_list()
    app.contact.edit_first_contact(Contact(first_name="first name edit"))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)


def test_edit_contact_middle_name(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(middle_name="test"))
    old_contacts = app.contact.get_contact_list()
    app.contact.edit_first_contact(Contact(middle_name="middle name edit"))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)


def test_edit_contact_last_name(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(last_name="test"))
    old_contacts = app.contact.get_contact_list()
    app.contact.edit_first_contact(Contact(last_name="last name edit"))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
