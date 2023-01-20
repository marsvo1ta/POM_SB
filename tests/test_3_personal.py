from seleniumbase import BaseCase
from time import sleep
from data.locators import *
from data.data_for_test import *
from data.handling_selectors import *

class TestHSCode(BaseCase):
    
    def test_personal(self):
        self.open(MAIN_URL)
        self.load_cookies()
        self.open(PERSONAL_DATA_URL)
        self.maximize_window()


        #Personal Data Text
        self.assert_text('Профіль', PROFILE_TAB)
        self.assert_text('Мої адреси', MY_ADDRESSES_TAB)
        self.assert_text('Паспортні дані', PASSPORT_DATA_TAB)
        self.assert_text('Кирилиця', CYRILLIC)
        self.assert_text('Латиниця', LATIN)
        self.assert_text('Зберегти', SAVE_PROFILE_BUTTON)
        self.assert_text('Змінити Email', CHANGE_EMAIL_BUTTON)
        self.assert_text('Змінити пароль', SAVE_PASSWORD_BUTTON)
        self.assert_text('Дата народження', DATE_PROFILE_LABEL)
        self.assert_text('Стать', GENDER_LABEL)
        self.assert_text('Чоловік', GENDER_RADIO_MALE)
        self.assert_text('Жінка', GENDER_RADIO_FEMALE)

        #My Addresses
        self.click(MY_ADDRESSES_TAB)
        self.assert_text('Додати адресу', ADD_ADDRESS_BUTTON)
        self.assert_element(MY_ADDRESSES_ITEMS)

        #Passport Data
        self.click(PASSPORT_DATA_TAB)
        self.assert_text('Паспорт України', PASSPORT_UKRAINE)
        self.assert_text('ID картка', ID_CARD)
        self.assert_text('Зберегти', SAVE_PASSPORT_BUTTON)
        self.assert_text('Ідентифікаційний номер', IDENTICAL_NUMBER)