from bs4 import BeautifulSoup
import requests
import os

# Create directory
try:
    os.mkdir('outFiles')
except FileExistsError:
    pass

resp = requests.get('https://developer.android.com/reference/android/app/package-summary')
html = resp.text
soup = BeautifulSoup(html, features='html.parser')

print(soup.prettify())

hrefs = soup.find_all('td', class_='jd-linkcol')  # p class = 'note' or 'caution'
for i in hrefs:
    print(i.text)
