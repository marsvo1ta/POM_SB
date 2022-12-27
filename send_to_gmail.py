import os
from datetime import datetime as d

from bs4 import BeautifulSoup
from send_gmail import SendGMail


txt = 'Pytest Result'
subject = 'Pytest Result '
date = d.utcnow().strftime("%A, %d. %B %Y %I:%M%p") + 'in UTC +0'

smtpsrv = SendGMail(id=os.environ.get('RECEIVE_FROM_GMAIL'),pwd=os.environ.get('GMAIL_PYTEST_CODE'))
with open('dashboard.html', 'r',) as report:
    S = BeautifulSoup(report,features="html.parser")
    smtpsrv.send(None, os.environ.get('SEND_TO_GMAIL'), subject=subject+date, text=txt, html=S)
print(date)