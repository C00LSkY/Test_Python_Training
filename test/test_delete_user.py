__author__ = "C00LSkY"


def test_delete_first_user(app):
    app.user.delete_first_user()
