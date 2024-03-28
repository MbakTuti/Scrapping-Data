import requests
from bs4 import BeautifulSoup
import csv

wagon='8'
van='7'
coupe='6'
truk='5'
mpv='3'
hatchback='2'
sedan='1'
suv='4'

jenis= "suv",
merk= "honda",
tahun= '2019'

url = 'https://www.carsome.id/beli-mobil-bekas/{}?bodyType={}&year={}'.format(merk, jenis, tahun)

req = requests.post(url)
soup = BeautifulSoup(req.text, 'html.parser')
items= soup.findAll('div', 'mod-b-card__footer')
for it in items:
    name= it.find('a', 'mod-b-card__title').text
    print(name)