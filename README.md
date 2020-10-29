# Appartment Scrapper


## [Gewoba](https://www.gewoba.de/mieten-verwalten-kaufen-verkaufen/wohnung-mieten)

- A few hours in I noticed i was following a tutorial for static websites, trying to srap dynamic content.

- Checked XHR requests, but only requests made where for the map view


## [ImmoScout24](https://www.immobilienscout24.de/wohnen/mietwohnungen.html)

- The most important search filters can be made over the url	`/Suche/de/bremen/bremen/wohnung-mieten?numberofrooms=2.0-&price=-550.0&livingspace=40.0-&enteredFrom=one_step_search`

- Requesting the site via formatted url returns captcha check

- Created dictionary containing my user agent and got the search results

- Successfully copied and used a Microsoft Edge 85.0 User Agent from [user-agents.net](https://user-agents.net/browsers/edge)

- While searching and selecting the nodes with the relevent data i encountered a captcha again. I made probably too many (about 5) requests per minute
