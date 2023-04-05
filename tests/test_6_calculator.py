import time
import pytest
from seleniumbase import BaseCase

from data.locators import *
from data.data_for_test import *
from data.handling_selectors import *

class TestCalculator(BaseCase):

    
    @pytest.mark.run(order=9)
    def test_calculator(self):
        self.open(CALCULATOR_URL)
        self.maximize_window()

        self.click(CALCULATOR_USA)
        self.get_text(USA_PAYMENT)
        self.click(BRITAIN_FROM_SELECT)
        self.get_text(BRITAIN_PAYMENT)
        self.click(CALCULATOR_BRITAIN)
        self.click(GERMANY_FROM_SELECT)
        assert '5.00' in self.get_text(GERMANY_PAYMENT)
        self.type('input.input.input-control__field', '1')
        assert '9.00' in self.get_text(IS_INCREASE)
        assert self.get_text('span.calc-form__label-text') == 'Оберіть країну'
        self.hover('i.icon-info')
        # self.assert_in('shipping', self.get_text('span.icon-help.tooltip'))
        # self.is_text_visible('Міжнародна експрес-доставка', 'div.calc-info__text')
        time.sleep(3)