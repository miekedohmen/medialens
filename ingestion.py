# Hoe gebruik je dit?
# 1. installeer de benodigde bibliotheken:
# pip install feedparser pymongo
# 2. zorg dat MongoDB lokaal draait
# 3. voer het script uit: python ingestion.py

import feedparser
from pymongo import MongoClient
from datetime import datetime

# verbinding met MongoDB
# 'medialens' is de naam van de db - MongoDB maakt deze aan
# 'artikelen' is de naam van de collectie 

client = MongoClient("mongodb://localhotls:27017/")
db = client["medialens"]
collectie = db["artikelen"]

collectie.create_index("url", unique=True)

# feeds ophalen

FEEDS = [
    ("https://www.nu.nl/rss", "NU.nl")
    ("https://www.ad.nl/home/rss.xml", "AD")
    ("https://www.nrc.nl/rss/", "NRC")
    ("https://www.trouw.nl/nieuws/nederland/rss.xml", "Trouw")
    ("https://www.telegraaf.nl/rss/", "De Telegraaf")
    ("https://www.volkskrant.nl/voorpagina/rss.xml", "Volkskrant")
]

def haal_feed_op(feed_url, bron_naam):
    print(f"Feed ophalen: {bron_naam}...")
    feed = feedparser.parse(feed_url)
 
    nieuw = 0
 
    for artikel in feed.entries:
        titel = artikel.get("title", "").strip()
        url   = artikel.get("link",  "").strip()
 
        # Sla over als titel of URL ontbreekt — deze zijn verplicht
        if not titel or not url:
            continue
        