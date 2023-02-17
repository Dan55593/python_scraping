from scrap import *
for page in range(1, 11):
    url = Url(page)
    scrap = ScrapData(url.url())
    scrap.display_voiture()
