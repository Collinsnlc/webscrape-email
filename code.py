import smtplib
import time
import requests
from bs4 import BeautifulSoup

url= requests.get('scrape site').text
soup = BeautifulSoup(url, 'lxml')
item = soup.find('a',class_="pi__title-link home-pi__title-link").text
itemprice = soup.find('span',class_='pi__price').text
iii = str(itemprice)


emailaddress = 'your email address'

while 0 == 0:
    with smtplib.SMTP('smtp.gmail.com',587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.ehlo()

        smtp.login('your email','yourpass')

        subject = 'Dinner this weekend?'
        body = 'star pallet price is: ' + iii

        msg = f'Subject: {subject}\n\n{body}'
        smtp.sendmail(emailaddress,'receiving email', msg)
        time.sleep(50)
