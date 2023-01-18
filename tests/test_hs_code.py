from seleniumbase import BaseCase
from time import sleep
from data.locators import *
from data.data_for_test import *
from data.handling_selectors import *

class TestHSCode(BaseCase):
    
    def test_hs_code(self):
        self.open(MAIN_URL)
        self.load_cookies()
        self.open(NEW_ORDER)
        self.maximize_window()
        self.click(COUNTRY_SELECT)
        self.click(SELECT_USA)
        self.click(STORE_SELECT)
        self.click(SELECT_AMAZON)
        self.click(CARGO_CATEGORY)

        #Starlink
        self.click(STARLINK_FROM_SELECT)
        self.type(UNIT_PRICE, '1')
        self.click(LABEL)
        self.assert_text('1', ORDER_SUM)
        self.assert_text('0.00', CUSTOMS_DEFAULT_STATE)
        self.type(UNIT_PRICE, '1000')
        self.click(LABEL)
        self.scroll_to_element(BONUSES)
        self.assert_text_not_visible(CUSTOMS_ELEMENT, '1000')

        #Needle
        self.type(cargo_input_field(4), NEEDLE)
        self.assert_text(NEEDLE, NEEDLE_FROM_SELECT)
        self.click(NEEDLE_FROM_SELECT)
        self.scroll_to_element(BONUSES)
        self.type(UNIT_PRICE, '1000')
        self.click(LABEL)
        self.scroll_to_element(BONUSES)
        self.assert_text('292.95', CUSTOMS_PRICE)
        self.assert_text('1000', ORDER_SUM)
        self.type(UNIT_PRICE, '1')
        self.click(LABEL)
        self.scroll_to_element(BONUSES)
        self.assert_text('0.00', CUSTOMS_DEFAULT_STATE)
        self.assert_text('1', ORDER_SUM)

        #Needle - 10$; Starlink - 1000$
        self.type(UNIT_PRICE, '10')
        self.click(ONE_MORE_POSITION)
        self.scroll_to_element(BONUSES)
        self.assert_text('0.00', CUSTOMS_DEFAULT_STATE)
        self.type(cargo_input_field(6), f'{STARLINK}\n')
        self.type(SECOND_UNIT_PRICE, '1000')
        self.click_if_visible(LABEL)
        self.scroll_to_element(BONUSES)
        self.assert_text(EMPTY_CUSTOMS_TEXT, CUSTOMS_ELEMENT)

        #Needle - 1000$; Starlink - 10$
        self.type(UNIT_PRICE, '1000')
        self.type(SECOND_UNIT_PRICE, '10')
        self.click(LABEL)
        self.scroll_to_element(BONUSES)
        self.assert_text('1010', FULL_ORDER_SUM)
        self.assert_text('292.95', CUSTOMS_PRICE)

        #Not in List - 555$
        self.click(DELETE_ONE_POSITION)
        self.click(NOT_IN_LIST_CHECKBOX)
        self.click(ALLOW_POP_UP)
        self.type(UNIT_PRICE, '555')
        self.click(LABEL)
        self.scroll_to_element(CUSTOMS_PRICE)
        self.assert_text('137.20', CUSTOMS_PRICE)
        self.scroll_to_element(FULL_ORDER_SUM)
        self.assert_text('555.00', FULL_ORDER_SUM)

        #Not in list - 555$; Needle 10$
        self.click(ONE_MORE_POSITION)
        self.scroll_to_top()
        self.add_text(UNIT_PRICE, '555')
        self.scroll_to_element(BONUSES)
        self.type(cargo_input_field(8), NEEDLE)
        self.click(cargo_select_field(8))
        self.type(SECOND_UNIT_PRICE, '10')
        self.click(LABEL)
        self.scroll_to_bottom()
        self.assert_text('565.00', FULL_ORDER_SUM)
        self.assert_text('137.20', CUSTOMS_PRICE)