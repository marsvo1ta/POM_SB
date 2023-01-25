import names
import random
import os
from fake_email import Email
from password_generator import PasswordGenerator


randomize = random.randrange(1, 11)
random_track_number = random.randrange(111111111, 999999999)
random_identical_number = random.randrange(1111111111, 9999999999)

EMAIL = str(os.environ.get('NPS_EMAIL'))
PASSWORD = str(os.environ.get('NPS_PASS'))
PHONE = f'68{random.randrange(2111111, 3333333)}'

NEW_FIRST_NAME = 'Тестовий'
NEW_SECOND_NAME = 'Тестовий'
RANDOM_NAME = names.get_first_name()
RANDOM_SURNAME = names.get_last_name()
RANDOM_EMAIL = Email().Mail()['mail']
RANDOM_PASSWORD = PasswordGenerator().generate()
RANDOM_DIGIT = str(randomize)
SUM_RANDOM_DIGITS = randomize * 2
RANDOM_TRACK_NUMBER = str(random_track_number)
RANDOM_IDENTICAL_NUMBER = str(random_identical_number)
ISSUED_BY_TEXT = 'МВУМВС'
REGISTRATION_ADDRESS_TEXT = 'Старкон 5'
SERIAL_NUMBER_TEXT = 'НВ404529'

CABINET = 'Особистий кабінет'
FIVE_ELEVEN = '5.11 Tactical'
SUCCESS_SCREEN_TITLE = 'Відправлення успішно додано'
ORDERS_TITLE = 'Мої відправлення'
NEEDLE = 'Голка'
STARLINK = 'Starlink'
EMPTY_CUSTOMS_TEXT = 'Я згоден з оплатою послуги розмитнення (митний збір, податки та митно-брокерські послуги)'

HS_COOKIES = 'hs_cookies.txt'
DEVELOP_COOKIES = ['cookies.txt', 'develop_cookies.txt']