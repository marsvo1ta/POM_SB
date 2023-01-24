import pytest
from seleniumbase import BaseCase

from data.locators import *


class TestNPStart(BaseCase):


    @pytest.mark.run(order=1)
    def test_start_staging(self):
        self.open(MAIN_URL)
        if self.is_element_present(START_DEPLOY_BUTTON) or \
            self.is_element_present('img#progress-animation'):
            
            self.click(START_DEPLOY_BUTTON, timeout=10)
            self.assert_elements_visible(DEPLOY_LOADER)
        