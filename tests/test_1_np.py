from seleniumbase import BaseCase

from data.locators import *
from data.data_for_test import *
from data.handling_selectors import *

class TestNP(BaseCase):


    def test_login(self):
        self.get(MAIN_URL)
        self.maximize_window()
        self.click(ALLOW_PRIVACY_POLICY)    
        self.click(HAMBURGER)
        self.type(EMAIL_FIELD, EMAIL)
        self.type(PASSWORD_FIELD, PASSWORD)
        self.click(REMEMBER_CHECKBOX)
        self.click(LOGIN_BUTTON)
        self.assert_text(CABINET, LK_TITLE)
        self.save_cookies()
        

    def test_order(self):
        self.get(MAIN_URL)
        self.load_cookies()
        self.get(ORDERS_URL)
        self.maximize_window()
        self.click(ADD_ORDER)
        self.click(COUNTRY_SELECT)
        self.click(SELECT_USA)
        self.click(STORE_SELECT)
        self.click(SELECT_AMAZON)
        self.type(ORDER_NAME, RANDOM_NAME)
        self.type(ORDER_NAME_LAT, RANDOM_NAME)
        self.click(PLUS_COUNTER)
        self.assert_text('2', COUNTER_QUANTITY)
        self.type(UNIT_PRICE, RANDOM_DIGIT)
        self.assert_text(RANDOM_DIGIT, UNIT_PRICE)
        self.click(ONE_MORE_POSITION)
        self.type(SECOND_ORDER_NAME_LAT, RANDOM_NAME)
        self.type(SECOND_UNIT_PRICE, RANDOM_DIGIT)
        self.assert_text(SUM_RANDOM_DIGITS, FULL_ORDER_SUM)
        self.click(cargo_input_field(5))
        self.click(cargo_select_field(5))
        self.click(cargo_input_field(6))
        self.click(cargo_select_field(6))
        self.scroll_to_bottom()
        self.type(TRACK_NUMBER, RANDOM_TRACK_NUMBER)
        self.click(CONTINUE_TO_ORDER_CREATION)
        self.click(ADDRESS_SELECT)
        self.click(FIRST_ADDRESS)
        self.type(INPUT_PHONE, PHONE)
        self.click(SUBMIT_BUTTON)
        self.assert_text(SUCCESS_SCREEN_TITLE, SUCCESS_SCREEN)
        self.click(BACK_TO_LK_BUTTON)
        self.assert_text(ORDERS_TITLE, MY_ORDERS_TITLE)

    def test_catalog(self):
        self.open(CATALOG_URL)
        self.maximize_window()
        self.click(ALL_STORES_SELECT)
        self.click(CLOTHES)
        self.click(ALL_COUNTRIES_SELECT)
        self.click(USA)
        self.click(SORTING_SELECT)
        self.click(ASC_SELECT)
        self.click(TACTICAL_STORE)
        self.assert_text(FIVE_ELEVEN, TACTICAL_PAGE)


