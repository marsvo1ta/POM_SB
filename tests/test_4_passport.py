from seleniumbase import BaseCase
from seleniumbase.fixtures.base_case import NoSuchElementException
from time import sleep
import pytest

from data.locators import *
from data.data_for_test import *
from data.handling_selectors import *

class TestHSCode(BaseCase):


    @pytest.mark.run(order=8)
    def test_passport(self):
        self.open(MAIN_URL)
        self.load_cookies('new_user.txt')
        self.open(PASSPORT_URL)
        self.maximize_window()

        #Test Password
        self.type(FIRST_NAME, RANDOM_NAME)
        self.type(LAST_NAME, RANDOM_SURNAME)
        self.type(MIDDLE_NAME, RANDOM_NAME)
        self.type(ISSUED_BY, ISSUED_BY_TEXT)
        self.type(REGISTRATION_ADDRESS, REGISTRATION_ADDRESS_TEXT)
        self.type(SERIAL_NUMBER, SERIAL_NUMBER_TEXT)
        self.type(IDENTICAL_NUMBER_INPUT, RANDOM_IDENTICAL_NUMBER)
        self.click(SAVE_PASSPORT_BUTTON)
        try:
            self.assert_element(ERROR_TITLE, timeout=2)
            self.assert_text('Значення недопустиме.', ERROR_TITLE, timeout=2)
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
        

        #Test ID_Card
        self.click(ID_CARD_TEXT)
        self.type(ID_FIRST_NAME, RANDOM_NAME, timeout=20)
        self.type(ID_SECOND_NAME, RANDOM_SURNAME)
        self.type(ID_MIDDLE_NAME, RANDOM_NAME)
        self.type(ID_CARD_NUMBER, RANDOM_IDENTICAL_NUMBER)
        self.type(ID_ISSUED_BY, ISSUED_BY_TEXT)
        self.type(ID_ADDRESS_REGISTRATION, REGISTRATION_ADDRESS_TEXT)
        self.type(ID_IDENTITY_NUMBER, RANDOM_IDENTICAL_NUMBER)
        self.type(ID_BIRTHDATE_DAY, '2')
        self.type(ID_BIRTHDATE_YEAR, '2000')
        self.click(ID_BIRTHDATE_MONTH)
        self.click(ID_SELECT_APRIL)
        self.type(ID_ISSUED_BY_DAY, '3')
        self.type(ID_ISSUED_BY_YEAR, '2001')
        self.click(ID_ISSUED_BY_MONTH)
        self.click(ID_SELECT_MAY)
        self.click(ID_SAVE_CARD)
