from requests_html import HTMLSession


# Init http session
session = HTMLSession()

### IMMOBILIENSCOUT24
# URL consists of base, location selector and search query
BASE_URL = 'https://www.immobilienscout24.de/Suche'
LOCATION_QUERY = '/de/bremen/bremen/wohnung-mieten'
SEARCH_QUERY = '?numberofrooms=2.0-&price=-550.0&livingspace=40.0-&enteredFrom=one_step_search'

# GET request
page = session.get(BASE_URL+LOCATION_QUERY+SEARCH_QUERY)

print(page.content)
