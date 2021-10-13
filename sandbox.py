from bs4 import BeautifulSoup
import requests
import os

try:
    os.mkdir('outFiles')
except FileExistsError:
    pass

resp = requests.get('https://developer.android.com/reference/android/app/Activity')
html = resp.text
soup = BeautifulSoup(html, features='html.parser')

filename = '/reference/android/app/Activity'
filename = filename[filename.rfind('/')+1:len(filename)]
f_1 = open("outFiles" + "/" + filename + ".txt", 'x')
hrefs_1 = soup.findAll('p', {"class": ["caution", "note"]})

for a in hrefs_1:
    print(a['href'])

for i_1 in hrefs_1:
    if i_1.find_previous('h3') is not None:
        f_1.write(i_1.find_previous('h3').text + ":" + i_1.text.strip() + "\n")
f_1.close()
