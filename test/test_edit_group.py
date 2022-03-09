from model.group import Group


def test_edit_group_name(app):
    app.session.login(username="admin", password="secret")
    app.group.edit_first_group(Group(name="group name edit"))
    app.session.logout()


def test_edit_group_header(app):
    app.session.login(username="admin", password="secret")
    app.group.edit_first_group(Group(header="header edit"))
    app.session.logout()


def test_edit_group_footer(app):
    app.session.login(username="admin", password="secret")
    app.group.edit_first_group(Group(footer="footer edit"))
    app.session.logout()
