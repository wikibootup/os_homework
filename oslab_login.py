import os

from selenium import webdriver


class OSLAB_login():

    def __init__(self):
        self.login_url = os.environ.get('LOGIN_URL')

    def login(self):
        browser = webdriver.Firefox()
        user_id = os.environ.get('USER_ID')
        password = os.environ.get('PASSWORD')

        browser.get(self.login_url)

        auth = browser.find_element_by_class_name("login")

        elem_user_id = auth.find_element_by_name("user_id")
        elem_password = auth.find_element_by_name("password")

        elem_user_id.send_keys(user_id)
        elem_password.send_keys(password)

        form = browser.find_element_by_id("fo_member_login")
        form.submit()

        return browser
