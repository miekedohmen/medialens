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

# Opdracht 2 - Technisch Ontwerp.

Dit technische ontwerp beschrijft de architectuur, de datastromen en de vereisten voor het MediaLens-prototype. 

## 1.    Requirements Document

Functionele Eisen
- Data-acquisitie: Het systeem moet artikelen ophalen van minmaal drie verschillende nieuwsbronnen.
- Classificatie: Elke bron moet worden gelabeld met een politieke oriëntatie: links, midden of rechts. 
- Clustering: Artikelen die over dezelfde gebeurtenis gaan (gebaseerd op gedeelde entiteiten, locaties en tijdstippen), moeten worden gegroepeerd.
- Analyse: Het systeem moet verschillen in framing en taalgebruik tussen de bronnen identificeren. 
- Summarization: Er moet een neutrale, gebalanceerde samenvatting worden gegenereerd die kernfeiten en verschillen in perspectief belicht zonder ideologisch geladen taal.
- User Interface: De app moet clusters tonen met een visuele weergave van de politieke spreiding en de neutrale samenvatting.

Niet-functionele Eisen
- Transparantie: Het systeem moet uitlegbaar zijn over de AI-beslissingen en de classificaties tot stand komen.
- Design: De UI moet voldoen aan de MediaLens-huisstijl, inclusief het gebruik van het Helvetica Neue font en de kleuren #**CDCCFE** en #**8DC4FB**
- Betrouwbaarheid: Het proces van ophalen tot het samenvatten moet consistent en zonder fouten verlopen.

Technologieën
- Programmeertaal: Python. 
- Data: RSS-feeds en Web Scraping
- AI: Large Language Models (LLM) voor samenvattingen en embeddings voor clustering.

## 2.    Procesflow

De data stroomt als volgt door het systeem:
1. Ingestion: RSS-feeds worden periodiek uitgelezen. De titels, URL's en volledige teksten van artikelen worden opgehaald.
2. Classificatie: Aan elk artikel wordt de politieke kleur van de bron gekoppeld (bijv. Volkskrant = Links, NOS = midden, Telegraaf = Rechts)
3. Clustering: Het systeem vergelijkt artikelen. Als ze dezelfde gebeurtenis beschrijven, krijgen ze dezelfde `Cluster_ID`
4. Analyse: De AI vergelijkt de teksten binnen een cluster op verschillende claims en sentiment.
5. Synthese. De AI genereert een samenvatting op basis van de verzamelde claims.
6. Presentatie: De samenvatting en de bijbehorende artikelen worden getoond in de UI.

## 3.    Applicatie Structuur Diagram (ASCD) & Componenten

Het systeem is modulair opgebouwd uit de volgende componenten:
- Ingestion Service: Verantwoordelijk voor de communicatie met externe RSS-feeds en het scrapen va de volledige artikeltekst.
- Source Classification Module: Bevat de logica om bronnen te matchen aan hun politieke oriëntatie.
- Topic Clustering Module: Gebruikt vector-similarity of keyword-extractie om artikelen te groeperen.
- Bias & Framing Analyzer: Analyseert de verschillen in 





