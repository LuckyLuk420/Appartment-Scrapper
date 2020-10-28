from requests_html import HTMLSession

# Init http session
session = HTMLSession()
# Get request for GEWOBA
URL = 'https://www.gewoba.de/mieten-verwalten-kaufen-verkaufen/wohnung-mieten'
page = session.get(URL)

# Render JavaScript to show filter options
page.html.render()


# Select filter options
options = [page.html.find('.options-basic'), page.html.find('.options-ranges')]


# Find relevant search filter nodes
filters = []
interests = {'city': {'id': 'ort', 'value': 'Bremen'},
             'district': {'id': 'stadtteil', 'value': ''},
             'rent': {'id': 'gesamt_miete', 'value': ''},
             'rooms': {'id': '_raeume_gesamt', 'value': ''}}
for interest in interests:
    for option in options:
        filters.append(options[option].find(f"#{interests[interest]['id']}"))

print(filters[0])

city = page.html.find(f'#{interests[0]}', first=True)
print(city)
"""
district = page.html.find('#stadtteil', first=True)
rent = page.html.find()

bremen = city.find('option[value=Bremen]')
"""
