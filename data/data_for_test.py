import names
import random
import os

randomize = random.randrange(1, 11)
random_track_number = random.randrange(111111111, 999999999)

EMAIL = str(os.environ.get('NPS_EMAIL'))
PASSWORD = str(os.environ.get('NPS_PASS'))

RANDOM_NAME = names.get_first_name()
RANDOM_DIGIT = str(randomize)
SUM_RANDOM_DIGITS = randomize * 2
RANDOM_TRACK_NUMBER = str(random_track_number)

CABINET = 'Особистий кабінет'
FIVE_ELEVEN = '5.11 Tactical'

