import os

from easy_contain.manage_contains import contains


MAIN_URL = str(os.environ.get('NPS_URL'))
REGISTRATION_PAGE = f'{MAIN_URL}register'
ORDERS_URL = f'{MAIN_URL}orders'
CATALOG_URL = f'{MAIN_URL}catalog'
PERSONAL_DATA_URL = f'{MAIN_URL}profile'
NEW_ORDER = f'{MAIN_URL}forwarding/declaration'
PASSPORT_URL = f'{PERSONAL_DATA_URL}/passport'
CATCHER_CRED = os.environ.get('CATCHER')
CATCHER_URL = f'https://{CATCHER_CRED}@npshopping-stag-mail.c1.npshopping.com/'
CALCULATOR_URL = f'{MAIN_URL}calculator'


# Test Start Deploy
START_DEPLOY_BUTTON = 'button#start-btn'
DEPLOY_LOADER = 'img#progress-animation'
DEPLOY_TEXT = 'h1#in-progress'

# Test Registration
REGISTER_FIRST_NAME = "input#registration_form_lastNameCyr"
REGISTER_SECOND_NAME = "input#registration_form_firstNameCyr"
REGISTER_PHONE = "input#registration_form_phone"
REGISTER_EMAIL = "input#registration_form_email"
REGISTER_PASSWORD = "input#registration_form_plainPassword"
REGISTER_SUBMIT_BUTTON = "button.btn"
REGISTER_SUCCESS_SCREEN = "p.alert__text"
FIND_EMAIL = 'div.ng-binding.ng-scope'
OPEN_LETTER = "div.button.letter__button"
OWN_CABINET = contains("a", "Особистий кабінет")
CABINET_MENU = "a.header-right__login"
LOGOUT_FROM_CABINET = contains("a.profile-link", "Вихід")

# Test Login
ALLOW_PRIVACY_POLICY = "button#accept-privacy-policy"
HAMBURGER = "a.header-right__login"
EMAIL_FIELD = "input#email"
PASSWORD_FIELD = "input#password"
REMEMBER_CHECKBOX = "div.checkbox-element"
LOGIN_BUTTON = "button.btn"
LK_TITLE = 'h1'

#Test Order
ADD_ORDER = "a.cabinet-link"
COUNTRY_SELECT = "div#vs1__combobox"
SELECT_USA = "li#vs1__option-0"
SELECT_POLAND = contains("li", "Польща")
SELECT_BRITAIN = contains("li", "Велика Британія")
STORE_SELECT = "div#vs2__combobox"
SELECT_AMAZON = contains("li", "Amazon")
ORDER_NAME = "input#forward_order_name"
ORDER_NAME_LAT = "input#forward_order_items_0_name"
PLUS_COUNTER = "span.input-number__btn.input-number__plus"
COUNTER_QUANTITY = "input#forward_order_items_0_quantity"
UNIT_PRICE = "input#forward_order_items_0_unitPrice_tbbc_amount"
ONE_MORE_POSITION = "a#forwarding-add-position"
SECOND_ORDER_NAME_LAT = "input#forward_order_items_1_name"
SECOND_UNIT_PRICE = "input#forward_order_items_1_unitPrice_tbbc_amount"
FULL_ORDER_SUM = "span#order_sum"
TRACK_NUMBER = "input#forward_order_trackNo"
CONTINUE_TO_ORDER_CREATION = "button#declaration.btn.btn_outline"
ADDRESS_SELECT = "div#vs7__combobox"
FIRST_ADDRESS = "li#vs7__option-0"
INPUT_PHONE = "input#input-phone-number"
ERROR_VALIDATION_PHONE = 'div.form__field-6.form__field-xs-12.form__field.has-error.focused'
SUBMIT_BUTTON = "button.btn_outline"
SUCCESS_SCREEN = "h1"
BACK_TO_LK_BUTTON = "a.btn"
MY_ORDERS_TITLE = "h3"

#Test Catalog
CATALOG_FROM_HEADER = 'a:contains("Магазини")'
ALL_STORES_SELECT = "div#vs1__combobox"
CLOTHES = "li#vs1__option-1"
ALL_COUNTRIES_SELECT = "div#vs2__combobox"
USA = "li#vs2__option-1"
SORTING_SELECT = "div#vs3__combobox"
ASC_SELECT = "ul#vs3__listbox"
TACTICAL_STORE = "div.catalog-item__title:contains('5.11 Tactical')"
TACTICAL_PAGE = "h2.h2"

#Test Countries in Header
COUNTRY_LINK = "div.menu-link__text:contains('Країни')"
US_COUNTRY = "a.countries-link:contains('США')"
IT_COUNTRY = "a.countries-link:contains('Італія')"
ES_COUNTRY = "a.countries-link:contains('Іспанія')"
GB_COUNTRY = "a.countries-link:contains('Британія')"
PL_COUNTRY = "a.countries-link:contains('Польща')"
TU_COUNTRY = "a.countries-link:contains('Туреччина')"
GE_COUNTRY = "a.countries-link:contains('Німеччина')"
FR_COUTRY = "a.countries-link:contains('Франція')"
CZ_COUTRY = "a.countries-link:contains('Чехія')"


#Test HS Code
CARGO_CATEGORY = "div#vs4__combobox"
STARLINK_FROM_SELECT = contains("li", "Starlink")
NEEDLE_FROM_SELECT = contains("div.select-option", "Голка")
LABEL = "i.icon-info"
CUSTOMS_DEFAULT_STATE = "span#order_customs_clearance"
CUSTOMS_PRICE = CUSTOMS_DEFAULT_STATE
CUSTOMS_ELEMENT = "div.delivery-information"
ORDER_SUM = 'span#order_sum'
BONUSES = 'div.delivery-information'
DELETE_ONE_POSITION = "i:contains('close')"
ALLOW_POP_UP = '//*[@id="add-order"]/div/div/div[3]/div/div/div[4]/span'
NOT_IN_LIST_CHECKBOX = "label.label-checkbox:contains(' Немає в переліку')"


#Test Personal
PROFILE_TAB = "li.tabs-nav__item:contains('Профіль')"
MY_ADDRESSES_TAB = "li.tabs-nav__item:contains('Мої адреси')"
PASSPORT_DATA_TAB = "li.tabs-nav__item:contains('Паспортні дані')"
CYRILLIC = "div.form__box-title:contains('Кирилиця')"
LATIN = "div.form__box-title:contains('Латиниця')"
SAVE_PROFILE_BUTTON = "button.btn:contains('Зберегти')"
CHANGE_EMAIL_BUTTON = "div.bottom-panel:contains('Змінити Email')"
SAVE_PASSWORD_BUTTON = "div.bottom-panel:contains('Змінити пароль')"
GENDER_LABEL = "label.float-label:contains('Стать')"
DATE_PROFILE_LABEL = "label.float-label:contains('Дата народження')"
GENDER_RADIO_MALE = "div.radio-element__item:contains('Чоловік')"
GENDER_RADIO_FEMALE = "div.radio-element__item:contains('Жінка')"
ADD_ADDRESS_BUTTON = "a#add-address"
MY_ADDRESSES_ITEMS = "div.my-addresses"
PASSPORT_UKRAINE = "a.form-office__tab:contains('Паспорт України')"
ID_CARD = "a.form-office__tab:contains('ID картка')"
SAVE_PASSPORT_BUTTON = "div.bottom-panel"
IDENTICAL_NUMBER = "div.form__field:contains('Ідентифікаційний номер')"


#Test Passport
FIRST_NAME = "input#user_passport_verification_firstName"
LAST_NAME = "input#user_passport_verification_lastName"
MIDDLE_NAME = "input#user_passport_verification_middleName"
SERIAL_NUMBER = "input#user_passport_verification_serialNumber"
ISSUED_BY = "input#user_passport_verification_issuedBy"
REGISTRATION_ADDRESS = "input#user_passport_verification_registration"
IDENTICAL_NUMBER_INPUT = "input#user_passport_verification_taxNumber"
ERROR_TITLE = "span.text-error"
ID_CARD_TEXT = contains('a.form-office__tab','ID картка')
BIRTHDATE_DAY = "input#user_passport_verification_birthDate_day"
BIRTHDAY_YEAR = "input#user_passport_verification_birthDate_year"
BIRTHDAY_MONTH_SELECT = "span#select2-user_passport_verification_birthDate_month-container"
SELECT_FEBRUARY = contains('li', 'лютого')
ISSUED_BY_MONTH = "span#select2-user_passport_verification_date_month-container"
SELECT_MARCH = contains('li', 'березня')
ISSUED_BY_DAY = "input#user_passport_verification_date_day"
ISSUED_BY_YEAR = "input#user_passport_verification_date_year"


#Test ID Card
ID_FIRST_NAME = "input#user_identity_card_verification_firstName"
ID_SECOND_NAME = "input#user_identity_card_verification_lastName"
ID_MIDDLE_NAME = "input#user_identity_card_verification_middleName"
ID_CARD_NUMBER = "input#user_identity_card_verification_identityCardNumber"
ID_ISSUED_BY = "input#user_identity_card_verification_issuedBy"
ID_ADDRESS_REGISTRATION = "input#user_identity_card_verification_registration"
ID_IDENTITY_NUMBER = "input#user_identity_card_verification_taxNumber"
ID_BIRTHDATE_DAY = "input#user_identity_card_verification_birthDate_day"
ID_BIRTHDATE_YEAR = "input#user_identity_card_verification_birthDate_year"
ID_BIRTHDATE_MONTH = "span#select2-user_identity_card_verification_birthDate_month-container"
ID_SELECT_APRIL = contains("li", "квітня")
ID_ISSUED_BY_DAY = "input#user_identity_card_verification_date_day"
ID_ISSUED_BY_YEAR = "input#user_identity_card_verification_date_year"
ID_ISSUED_BY_MONTH = "span#select2-user_identity_card_verification_date_month-container"
ID_SELECT_MAY = contains("li", "травня")
ID_SAVE_CARD = contains('button', 'Зберегти ID картку')


#Test Currency
CURRENCY_ICON = "span.price-symbol"
CUSTOMS_CURRENCY_ICON = contains("span.delivery-information__right", "zł")

#Test Calculator
CALCULATOR_USA = contains('div.select-option', 'США')
BRITAIN_FROM_SELECT = contains('li', 'Велика Британія')
CALCULATOR_BRITAIN = contains('div.select-option', 'Велика Британія')
GERMANY_FROM_SELECT = contains('li', 'Німеччина')
USA_PAYMENT = contains('div.calc-info__row', '7.00')
BRITAIN_PAYMENT = contains('div.calc-info__row', '7.00')
GERMANY_PAYMENT = contains('div.calc-info__row', '5.00')
IS_INCREASE = contains('div.calc-info__row', '9.00')