from seleniumbase import BaseCase



class TestNP(BaseCase):
    def test_reg(self):
        self.open('https://mint.intuit.com/')
        self.click('a.btn.btn-mint-plum02-outline.beacon-this   ')
        self.type('input#ius-email', 'euromobilco@gmail.com')
        self.type('input#ius-mobile-phone', '3134048290')
        self.type('input#ius-password', 'Password1@')
        self.type('input#ius-confirm-password', 'Password1@')
        self.click('button#ius-sign-up-submit-btn')
        self.assert_text("The feature you've requested is temporarily unavailable", 'span#ius-create-account-disabled-high-risk-header')




