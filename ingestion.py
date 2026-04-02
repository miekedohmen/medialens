# 1. Installeer de benodigde bibliotheken:
#    pip install feedparser pymongo
# 2. Zorg dat MongoDB lokaal draait (of gebruik MongoDB Atlas)
# 3. Voer het script uit: python ingestion.py

import feedparser
from pymongo import MongoClient
from datetime import datetime

# "medialens" is de naam van de database — MongoDB maakt die automatisch aan.
# "artikelen" is de naam van de collectie (vergelijkbaar met een tabel).

client = MongoClient("mongodb://localhost:27017/")
db = client["medialens"]
collectie = db["artikelen"]

collectie.create_index("url", unique=True)

# feeds ophalen

FEEDS = [
    ("https://www.nu.nl/rss", "NU.nl"),
    ("https://www.ad.nl/home/rss.xml", "AD"),
    ("https://www.nrc.nl/rss/", "NRC"),
    ("https://www.trouw.nl/nieuws/nederland/rss.xml", "Trouw"),
    ("https://www.telegraaf.nl/rss/", "De Telegraaf"),
    ("https://www.volkskrant.nl/voorpagina/rss.xml", "Volkskrant")
]

# feeds ophalen en opslaan.

def haal_feed_op(feed_url, bron_naam):
    print(f"Feed ophalen: {bron_naam}...")
    
    feed = feedparser.parse(
        feed_url,
        request_headers={"User-Agent": "Mozilla/5.0"}
    )

    print("Aantal items:", len(feed.entries))

    #  — foutmelding tonen
    if feed.bozo:
        print("Feed fout:", feed.bozo_exception)

    nieuw = 0

    for artikel in feed.entries:
        titel = artikel.get("title", "").strip()
        url   = artikel.get("link", "").strip()

        if not titel or not url:
            continue

        # document wat opgeslagen word in MongoDB
        document = {
            "titel": titel,
            "url": url,
            "samenvatting": artikel.get("summary", ""),
            "bron": bron_naam,
            "opgeslagen_op": datetime.now().isoformat(),
        }

        try:
            collectie.insert_one(document)
            print("Totaal in DB:", collectie.count_documents({}))
            nieuw += 1
        except Exception:
            pass

    print(f" -> {nieuw} nieuwe artikelen opgeslagen")

# hoofdprogramma

def run():
    print("=== Ingestie gestart ===")

    for feed_url, bron_naam in FEEDS:
        haal_feed_op(feed_url, bron_naam)

    totaal = collectie.count_documents({})
    print(f"\nKlaar: Totaal {totaal} artikelen in de database")

if __name__ == "__main__":
    run()