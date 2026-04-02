# Dit script kijkt per artikel naar de bronnaam en voegt een politiek label toe.
# Ik gebruik een lookup table: een woordenboek waarbij de sleutel
# de bronnaam is en de waarde het label (links / midden / rechts).
# eerst ingestion.py uitvoeren, daarna classifier.py

from pymongo import MongoClient

# verbinding met MongoDB

client = MongoClient("mongodb://localhost:27017/")
db     = client["medialens"]
collectie = db["artikelen"]

# de lookup table 
# handmatige toewijzing van bronnamen naar politieke orientatie
# gebaseerd op gangbare mediaclassificatie in NL

POLITIEKE_LABELS = {
    "NOS":          "midden",
    "NU.nl":        "midden",
    "NRC":          "midden",
    "Trouw":        "links",
    "Volkskrant":   "links",
    "Telegraaf":    "rechts",
    "AD":           "rechts",
}

# als de bron niet in de lijst staat, geeft hij "onbekend" terug
def geef_label(bron):
    return POLITIEKE_LABELS.get(bron, "onbekend")

def classificeer_artikelen():
    artikelen = collectie.find({}) #haalt alle artikelen op/
    
    bijgewerkt = 0
    for artikel in artikelen:
        bron = artikel.get("bron", "")
        label = geef_label(bron)
        
        collectie.update_one(
            {"_id": artikel["_id"]}, #zoekt dit specifieke artikel
            {"$set": {"politiek_label": label}} #voegt het label toe.
        )
        
        bijgewerkt += 1
        
    print(f"{bijgewerkt} artikelen geclassificeerd.")
    
# overzicht om handig te controleren of classificatie goed gewerkt heeft

def toon_overzicht():
    print("\n=== Overzicht per bron ===")

    # Haal alle unieke bronnamen op
    bronnen = collectie.distinct("bron")

    for bron in sorted(bronnen):
        label  = geef_label(bron)
        aantal = collectie.count_documents({"bron": bron})
        print(f"  {bron:<15} → {label:<8}  ({aantal} artikelen)"
    )
    
    print("\n=== Drie voorbeeldartikelen ===")
    voorbeelden = collectie.find({}, {"titel": 1, "bron": 1, "politiek_label": 1}).limit(3)
    
    for artikel in voorbeelden:
        label = artikel.get("politiek_label", "onbekend")
        
        print(f"    [{label}] {artikel['bron']}: {artikel['titel']}")

# hoofdprogramma

if __name__ == "__main__":
    classificeer_artikelen()
    toon_overzicht()