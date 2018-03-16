

def test_phones_on_home_page(app):
    contact_from_home_page = app.user.get_user_list()[0]
    contact_from_edit_page = app.user.get_user_info_from_edit_page(0)
    assert contact_from_home_page.home_tel == contact_from_edit_page.home_tel
    assert contact_from_home_page.mobile_tel == contact_from_edit_page.mobile_tel
    assert contact_from_home_page.work_tel == contact_from_edit_page.work_tel
