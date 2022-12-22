from seleniumbase import BaseCase
# import pytest

from data.locators import *
from data.data_for_test import *
from selenium.common.exceptions import NoSuchElementException, TimeoutException

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
        self.scroll_to_bottom()
        self.type(TRACK_NUMBER, RANDOM_TRACK_NUMBER)
        self.click(CONTINUE_TO_ORDER_CREATION)
        # self.click(ADDRESS_SELECT)

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

# if __name__ == "__main__":
#     pytest.main()
