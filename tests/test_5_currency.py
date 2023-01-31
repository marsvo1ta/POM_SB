from seleniumbase import BaseCase
from data.locators import *
from data.data_for_test import *
from time import sleep

class TestCurrency(BaseCase):
    def test_currency(self):
        self.open(MAIN_URL)
        self.load_cookies()
        self.open(NEW_ORDER)
        self.maximize_window()
        self.click(COUNTRY_SELECT)
        self.click(SELECT_POLAND)
        self.click(STORE_SELECT)
        self.click(SELECT_AMAZON)
        self.click(CARGO_CATEGORY)
        self.click(NEEDLE_FROM_SELECT)
        self.type(ORDER_NAME_LAT, NEEDLE)
        self.type(UNIT_PRICE, '10')
        self.click(LABEL)
        self.assert_text('zł', CURRENCY_ICON)
        self.assert_element(CUSTOMS_CURRENCY_ICON)
        self.scroll_to_bottom()
        self.click(SUBMIT_BUTTON)
        self.assert_text(CABINET, SUCCESS_SCREEN)