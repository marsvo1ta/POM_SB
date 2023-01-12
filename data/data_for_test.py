import names
import random
import os

randomize = random.randrange(1, 11)
random_track_number = random.randrange(111111111, 999999999)

EMAIL = str(os.environ.get('NPS_EMAIL'))
PASSWORD = str(os.environ.get('NPS_PASS'))
PHONE = f'+38068{random.randrange(2111111, 9999999)}'

RANDOM_NAME = names.get_first_name()
RANDOM_DIGIT = str(randomize)
SUM_RANDOM_DIGITS = randomize * 2
RANDOM_TRACK_NUMBER = str(random_track_number)

CABINET = 'Особистий кабінет'
FIVE_ELEVEN = '5.11 Tactical'
SUCCESS_SCREEN_TITLE = 'Відправлення успішно додано'
ORDERS_TITLE = 'Мої відправлення'

HS_COOKIES = 'hs_cookies.txt'
DEVELOP_COOKIES = ['cookies.txt', 'develop_cookies.txt']