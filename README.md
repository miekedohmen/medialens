# Opdracht 1

## 1.   Wat de opdracht inhoudt

De opdracht is het bouwen van een werkend prototype voor MediaLens, een systeem dat nieuws vanuit verschillende hoeken belicht. Het doel is om artikelen van ten minste dire verschillende bronnen te verzamelen die over dezelfde gebeurtenis gaan. Het systeem moet de politieke kleur (links, midden, rechts) van de bron herkennen en een neutrale samenvatting genereren met behulp van AI. Hiermee help ik lezers om 'framing' en informatie-bias beter te begrijpen.

## 2.   Stappenplan 

Om dit project overzichtelijk te houden, onderneem ik de volgende stappen:
1. Projectinrichting: Een GitHub repository aanmaken om mijn voortgang bij te houden.
2. Data verzamelen: Gebruikmaken van bestaande RSS-feeds van bijvoorbeeld de NOS, Telegraaf en NU.nl om makkelijk tekst en titels op te halen.
3. Classificeren: Voor de haalbaarheid begin ik met een handmatige toewijzing (een "lookup table") waarbij ik bekende bronnen vooraf label als links, midden of rechts.
4. Groeperen (Clustering): Artikelen die over hetzelfde onderwerp gaan bij elkaar brengen door te zoeken naar overeenkomstige trefwoorden of titels.
5. AI samenvatting: De teksten van de verschillende bronnen naar een AI-model (LLM) sturen met een specifieke instructie om een feitelijk en neutraal overzicht te maken.
6. Presentatie: Een eenvoudige interface bouwen waarin de clusters en samenvatting zichtbaar zijn.

## 3.    Tools en technologieën

- Programmeertaal: Python, omdat dit de standaard is voor AI en dataverwerking in deze case.
- Bibliotheken: feedparser voor het uitlezen van RSS-feeds en eenvoudige tekstverwerkings-tools voor Python.
- AI: Een Large Language Model (zoals GPT of een open-source variant) voor het maken van de samenvattingen.
- Documentatie & planning: Obsidian voor mijn eigen aantekeningen en Github voor versiebeheer en taakbeheer.

## 4.    Implementatie van onderdelen

Het systeem wordt modulair opgebouwd, zodat elk deel part getest kn worden.

- Ingestion: Een script dat de RSS-links uitleest en de artikelen opslaat.
- Classifier: Een eenvoudige functie die de bronnaam checkt en de bijbehorende politieke kleur teruggeeft.
- Clusteraar: Een onderdeel dat kijkt of artikelen dezelfde woorden in de titel hebben om ze aan elkaar te koppelen.
- Summarizer: Een onderdeel dat kijkt of artikelen dezelfde woorden in de titel hebben om ze aan elkaar te koppelen.

## 5.      Evaluatie van de presentaties

Ik controleer of het systeem goed werkt aan de hand van deze punten.
- Bron-check: Haalt het systeem inderdaad artikelen op van minimaal 3 verschillende bronnen?
- Neutraliteit: Is de gegenereerde samenvatting echt neutraal en worden de verschillende kanten van het verhaal benoemd?
- Gebruiksgemak: Is de output voor een normale nieuwslezer goed te begrijpen?
- Betrouwbaarheid: Werkt het proces van ophalen tot samenvatten zonder foutmeldingen?





