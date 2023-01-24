import pytest
from seleniumbase import BaseCase
from seleniumbase.fixtures.base_case import NoSuchElementException
from time import sleep

from data.locators import *
from data.data_for_test import *
from data.handling_selectors import *
from easy_contain.manage_contains import contains

class TestHSCode(BaseCase):


    @pytest.mark.run(order=5)
    def test_registration(self):
        self.open(REGISTRATION_PAGE)
        self.type(REGISTER_FIRST_NAME, NEW_FIRST_NAME)
        self.type(REGISTER_SECOND_NAME, NEW_SECOND_NAME)
        self.type(REGISTER_PHONE, '0')
        self.add_text(REGISTER_PHONE, PHONE)
        self.type(REGISTER_EMAIL, RANDOM_EMAIL)
        self.type(REGISTER_PASSWORD, RANDOM_PASSWORD)
        self.click(REGISTER_SUBMIT_BUTTON)
        find_email = self.get_text(REGISTER_SUCCESS_SCREEN).split(" ")[7][:-1]
        self.open(CATCHER_URL)
        self.click(contains('tr', find_email))
        self.switch_to_frame(0)
        self.click(OPEN_LETTER)
        self.switch_to_newest_tab()
        self.assert_text(CABINET, OWN_CABINET)
        self.hover_and_click(CABINET_MENU, LOGOUT_FROM_CABINET)
        self.click(HAMBURGER)
        self.type(EMAIL_FIELD, RANDOM_EMAIL)
        self.type(PASSWORD_FIELD, RANDOM_PASSWORD)
        self.click(REMEMBER_CHECKBOX)
        self.click(LOGIN_BUTTON)
        self.save_cookies('new_user.txt')
