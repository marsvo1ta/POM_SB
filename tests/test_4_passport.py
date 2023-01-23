from seleniumbase import BaseCase
from seleniumbase.fixtures.base_case import NoSuchElementException
from time import sleep

from data.locators import *
from data.data_for_test import *
from data.handling_selectors import *

class TestHSCode(BaseCase):
    def test_passport(self):
        self.open(MAIN_URL)
        self.load_cookies()
        self.open(PASSPORT_URL)
        self.maximize_window()

        self.type(FIRST_NAME, RANDOM_NAME)
        self.type(LAST_NAME, RANDOM_SURNAME)
        self.type(MIDDLE_NAME, RANDOM_NAME)
        self.type(ISSUED_BY, ISSUED_BY_TEXT)
        self.type(REGISTRATION_ADDRESS, REGISTRATION_ADDRESS_TEXT)
        self.type(SERIAL_NUMBER, SERIAL_NUMBER_TEXT)
        self.type(IDENTICAL_NUMBER_INPUT, RANDOM_IDENTICAL_NUMBER)
        self.click(SAVE_PASSPORT_BUTTON)
        try:
            self.assert_element(ERROR_TITLE)
            self.assert_text('Значення недопустиме.', ERROR_TITLE)
        except NoSuchElementException:
            self.assert_text('ID картка', ID_CARD_TEXT)
        self.click(BIRTHDAY_MONTH_SELECT)
        self.click(SELECT_FEBRUARY)
        self.type(BIRTHDATE_DAY, '10')
        self.type(BIRTHDAY_YEAR, '1989')
        self.click(ISSUED_BY_MONTH)
        self.click(SELECT_MARCH)
        self.type(ISSUED_BY_DAY, '11')
        self.type(ISSUED_BY_YEAR, '1989')
        self.click(SAVE_PASSPORT_BUTTON)
        