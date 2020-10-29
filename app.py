import requests
from bs4 import BeautifulSoup

### IMMOBILIENSCOUT24
# URL consists of base, location selector and search query
BASE_URL = 'https://www.immobilienscout24.de/Suche'
LOCATION_QUERY = '/de/{}/{}/wohnung-mieten'
SEARCH_QUERY = '?numberofrooms={}-&price=-{}&livingspace={}-&enteredFrom=one_step_search'

# Get query input from user
FILTERS = ['city', 'numberofrooms', 'price', 'livingspace']
RELEVANT_FILTERS = {}
for Filter in FILTERS:
    if Filter == 'city':
        RELEVANT_FILTERS[Filter] = input(Filter + ': ').lower()
    else:
        RELEVANT_FILTERS[Filter] = float(input(Filter + ': '))

# Create user agent
user_agent = {'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                            'Chrome/85.0.4183.102 Safari/537.36 Edg/85.0.564.51'}

# Make URL and GET request
URL = BASE_URL + LOCATION_QUERY.format(RELEVANT_FILTERS['city'], RELEVANT_FILTERS['city']) + SEARCH_QUERY.format(RELEVANT_FILTERS['numberofrooms'], RELEVANT_FILTERS['price'], RELEVANT_FILTERS['livingspace'])
page = requests.get(URL, headers=user_agent)

soup = BeautifulSoup(page.content, 'html.parser')

print(soup.text)


# Select search results
results = soup.find(id='resultListItems')





# print(results.find('div.result-list-entry__address'))
# print(soup)