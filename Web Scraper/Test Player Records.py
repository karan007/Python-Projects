#Python program to scrape website 
#and save records for various test players from cricinfo.com

import requests
from bs4 import BeautifulSoup
import csv
 
URL = "http://stats.espncricinfo.com/ci/content/records/283683.html"
r = requests.get(URL)

soup = BeautifulSoup(r.content, 'html5lib')
 
test_records = []  # a list to store test records
 
table = soup.find('table', attrs = {'class':'engineTable'})

fields = {}
fieldvalues = []
for row in table.findAll('tr', attrs = {'class':'head'}):
    for i in range(1, 14):
        fields[i] = row.contents[2*i-1].text
        fieldvalues.append(row.contents[2*i-1].text)

for row in table.findAll('tr', attrs = {'class':'data1'}):
    test_record = {}
    for i in range(1,14):
        test_record[fields[i]] = row.contents[2*i-1].text
    test_records.append(test_record)


filename = 'Test Player Records.csv'
with open(filename, 'wb') as f:
    w = csv.DictWriter(f,fieldvalues)
    w.writeheader()
    for test_record in test_records:
        w.writerow(test_record)
