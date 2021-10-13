from bs4 import BeautifulSoup
import requests
import os

# Create directory
try:
    os.mkdir('outFiles')
except FileExistsError:
    pass

# Grab request and all names in package
resp = requests.get('https://developer.android.com/reference/android/app/package-summary')
html = resp.text
soup = BeautifulSoup(html, features='html.parser')
hrefs = soup.find_all('td', class_='jd-linkcol')  # p class = 'note' or 'caution'
for a in hrefs:

    # Loop through names in package and find cautions and notes in fields, methods, and constants
    print(a.text)
    website = 'https://developer.android.com/reference/android/app/' + a.text
    resp_1 = requests.get(website)
    html_1 = resp_1.text
    soup_1 = BeautifulSoup(html_1, features='html.parser')
    hrefs_1 = soup_1.findAll('p', {"class": ["caution", "note"]})

    # Loop through notes and if it is in a field, method or constant, extract it and write it into the respective file
    write = True
    for i_1 in hrefs_1:
        if i_1.find_previous('h3') is not None and write:
            write = False
            f_1 = open("outFiles" + "/" + a.text, 'x')
            f_1.write(i_1.find_previous('h3').text + ":" + i_1.text.strip() + "\n")
        elif i_1.find_previous('h3'):
            f_1.write(i_1.find_previous('h3').text + ":" + i_1.text.strip() + "\n")
    if write is False:
        f_1.close()
