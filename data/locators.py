import os

MAIN_URL = str(os.environ.get('NPS_URL'))
ORDERS_URL = MAIN_URL + 'orders'
CATALOG_URL = MAIN_URL + 'catalog'

#Test Login
ALLOW_PRIVACY_POLICY = "button#accept-privacy-policy"
HAMBURGER = "a.header-right__login"
EMAIL_FIELD = "input#email"
PASSWORD_FIELD = "input#password"
REMEMBER_CHECKBOX = "div.checkbox-element"
LOGIN_BUTTON = "button.btn"
LK_TITLE = 'h1'

#Test Order
ADD_ORDER = "svg.btn__icon"
COUNTRY_SELECT = "div#vs1__combobox"
SELECT_USA = "li#vs1__option-1"
STORE_SELECT = "div#vs2__combobox"
SELECT_AMAZON = "li#vs2__option-1"
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
ADDRESS_SELECT = "div#vs4__combobox"

CATALOG_FROM_HEADER = 'a:contains("Магазини")'
ALL_STORES_SELECT = "div#vs1__combobox"
CLOTHES = "li#vs1__option-1"
ALL_COUNTRIES_SELECT = "div#vs2__combobox"
USA = "li#vs2__option-1"
SORTING_SELECT = "div#vs3__combobox"
ASC_SELECT = "ul#vs3__listbox"
TACTICAL_STORE = "div.catalog-item__title:contains('5.11 Tactical')"
TACTICAL_PAGE = "h2.h2"