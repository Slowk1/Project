import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://en.wikipedia.org/wiki/List_of_countries_by_population'
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

# Find all tables on the page
tables = soup.find_all('table')

# Assume the first table is the one we want (you may need to adjust this based on the page structure)
table = tables[0]

# Extract table headers
headers = []
for th in table.find('tr').find_all('th'):
    headers.append(th.text.strip())

# Extract table rows
rows = []
for tr in table.find_all('tr')[1:]:
    row = []
    for td in tr.find_all('td'):
        row.append(td.text.strip())
    rows.append(row)

# Create DataFrame
df = pd.DataFrame(rows, columns=headers)

print(df)
