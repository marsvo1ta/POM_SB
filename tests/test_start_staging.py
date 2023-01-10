from seleniumbase import BaseCase

from data.locators import *


class TestNP(BaseCase):

    def test_start_staging(self):
        self.open(MAIN_URL)
        if self.is_element_present(START_DEPLOY_BUTTON):
            self.click(START_DEPLOY_BUTTON)
            self.assert_elements_visible(DEPLOY_LOADER)
        