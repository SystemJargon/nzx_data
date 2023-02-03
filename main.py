import requests
from bs4 import BeautifulSoup

# get the webpage
url = 'https://www.nzx.com/markets/NZSX/securities'
try:
    page = requests.get(url)
except:
    print("An error occurred while fetching the webpage")

# parse the webpage
try:
    soup = BeautifulSoup(page.content, 'html.parser')
except:
    print("An error occurred while parsing the webpage")

# find the table with the stock prices
try:
    table = soup.find('table', class_='responsive-table')
except:
    print("Could not find the table element in the webpage")

# find all rows in the table
try:
    rows = table.find_all('tr')
except:
    print("Could not find any rows in the table")

# Print Heading
print(f'Code,Company,Price,Change,Volume,Value,Captilisation')

# iterate over the rows and print the stock symbol and price
for row in rows:
    cells = row.find_all('td')
    if cells:
        code = cells[0].text.strip()
        company = cells[1].text.strip()
        price = cells[2].text.strip()
        change = cells[3].text.strip()
        volume = cells[4].text.strip()
        value = cells[5].text.strip()
        capitalisation = cells[6].text.strip()


# Print Results
        print(f'{code},{company},{price},{change},"{volume}","{value}","{capitalisation}"')
