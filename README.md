# Eindproject
Voor het eindproject van het vak API development wordt er gevraagd om een API te maken die verbonden is met een databank (SQL). Deze API moet volledig automatisch worden opgebouwd  met GitHub actions. Hierna wordt de API gehost op Okteto en gekoppeld aan een front-end dat gehost wordt op Netlify.

# Thema
Het gekozen is hetzelfde als bij de basisproject. Omdat ik persoonlijk het een interessant thema vind. Het gekozen thema is bier. De API is gebouwd rond het bijhouden van welke brouwerij heeft welke bieren gebrouwen. 

# API
De API is complexer voor een overzicht te behouden is de API opgedeeld in drie onderdelen (bieren, brouwerijen, eigenaars). Per onderdeel wordt er een tabel aangemaakt in de database. Vervolgens wordt er per onderdeel een post aangemaakt zodat er snel gegevens toegevoegd kunnen worden. Tot slotte zijn er per onderdeel ook verschillende gets om de gegevens op te halen. Voor het onderdeel bieren is er ook een delete toegevoegd.

# Models.py
In dit bestand wordt de lay-out van de verschillende tabellen opgesteld. Hieronder vind u de gegevens per tabel.

Tabel Beers:
  - ID (int, primary key)
  - Name (string)
  - Volume (float)
  - Alcohol percentage (float)
  - type (string)
  - Brewery ID (int, foreign key from tabel brewery)

Tabel Breweries
  - ID (int, primary key)
  - Name (string)
  - Address (string)
  - Owner ID (int, foreign key from tabel owners)
 
 Tabel Owners
  - ID (int, primary key)
  - name (string)
  - Hased password (string)
  
Relaties:
  - Een eigenaar kan meerdere brouwerijen hebben. Maar een brouwerij kan maar één eigenaar hebben.
  - Een brouwerij kan meerdere bieren hebben. Maar een bier kan meer één brouwerij hebben.

# schemas.py
In dit bestand wordt opgegeven hoe een nieuw item kan gecreëerd worden voor een bepaalde tabel.

Bij owner is er een opvallend gegeven er wordt gevraagd om een paswoord mee te geven. Maar het is een string dus een plain text paswoord. Dit paswoord wordt later omgezet naar een uniek gehashed paswoord.

# crud.py
In dit bestand worden de functies aangemaakt om gegevens toe te voegen (CREATE), op te vragen (READ) of te verwijderen (DELETE).
Om gegevens toe te voegen wordt er eerst een session gestart. Samen met de session wordt er ook een schema gegeven van het bijpassend item. Vervolgens wordt er een model gemaakt van het item en dit wordt dan toegevoegd in de database

Om gegevens op te vragen word er een query uitgevoerd met of zonder een filter.

Om gegevens te verwijderen uit de database wordt er eerst een query gemaakt die de gegevens gaat ophalen. De opgehaalde gegevens worden vervolgens verwijderd uit de database.

# database.py
In dit bestand wordt de database gecreëerd via een URL. Vervolgens worden de nodige onderdelen aangemaakt: een engine, een lokale session, een base.

# auth.py
In dit bestand wordt alles afgehandeld van paswoorden en authenticatie. Eerst worden de nodig libraries geïmporteerd.  Hierna worden de nodige variabelen aangemaakt.
def get_password_hash(password)
  - Het plain text paswoord dat eerder werd meegegeven bij het aanmaken van een nieuwe eigenaar wordt hier omgezet naar een gehashed paswoord.
  
def verify_password(plain_password, hashed_password)
  - Het gegeven paswoord wordt vergeleken met de het gehashed paswoord.

def authenticate_owner(db: Session, name: str, password:str)
  - Er wordt eerst gecontroleerd of de naam voorkomt in de database. Zo niet wordt de functie afgebroken.
  - Hierna wordt het paswoord gecontroleerd met de functie die hierboven wordt beschreven.

def create_acces_token(data:dict)
  - Expires data bepaald wanneer de token vervalt.
  - Controle of expire data een waarde bevat.
  - Tot slotte wordt de token gecreëerd en teruggeven.

# main.py
In dit bestand vindt zich het “hoofdprogramma” terug. Hieruit worden de verschillende delen gekoppeld. De main.py bevat de vier post functies die nodig zijn om items te kunnen creëren. Ook bevat de main.py zes get functies om deze gegevens op te halen. Tot slotte is er nog een delete om een specifiek bier te kunnen verwijderen.
Overzicht van het bestand:
  - Alle nodige imports worden uitgevoerd.
  - Controle op het bestaan van de map '.\sqlitedb'.
  - De tabellen worden aangemaakt.
  - De app wordt opgestart.
  - Bearer wordt aangemaakt
  - De nodige CORS worden opgesteld. Er wordt ook voorzien dat de commando’s kunnen worden uitgevoerd in een lokale omgeving. Maar ook dat er commando’s kunnen worden uitgevoerd vanuit de gehoste site.
  - De database connectie wordt getest.
  - De post functies
  - De get functies
  - De delete functie (enkel toegangkelijk met de nodig authenticatie)


# Extra's
Hier onder vindt u alle extra's die in het project zitten.
# Front-end
In de front-end worden alle get en post functies opgeroepen. De front-end word gemaakt op basis van alpine. Bovenaan bevindt zich een navigatie menu waar u mee kan navigeren naar de verschillende onderdelen (beer, brewery, owner). Bij elk onderdeel vindt u de bijhorende get en post functies.

Beer

![image](https://user-images.githubusercontent.com/71765408/209341540-a9ee1ab6-b78f-4dbe-9fd9-fea5c22699e4.png)
![image](https://user-images.githubusercontent.com/71765408/209347871-54b8a962-e5d8-405f-b10c-182d13b6c8f2.png)
![image](https://user-images.githubusercontent.com/71765408/209341642-a4e421eb-7e6c-44e4-ad1f-8d61e4113685.png)
![image](https://user-images.githubusercontent.com/71765408/209341691-23dcb7af-de0d-4a59-b061-1775916df739.png)

Brewery

![image](https://user-images.githubusercontent.com/71765408/209349539-4d33a130-1b29-43d8-b076-3b9e72d657e3.png)
![image](https://user-images.githubusercontent.com/71765408/209349695-3a717e7f-dad1-42e6-879b-6e12a7d8672e.png)

Owner

![image](https://user-images.githubusercontent.com/71765408/209349776-cd249510-ba97-441b-8e0f-30e3922bf00f.png)

# test_app.py
In de app zit ook een bestand genaamd test_app.py. Dit bestand gaat alle functies testen (get, post, delete). Omdat dit bestand gebruik maakt van vaste waarden gaan sommige test maar één keer kunnen uitgevoerd worden. Als u alle testen wilt uitvoeren moet u eerst de database verwijderen,

screen:
![image](https://user-images.githubusercontent.com/71765408/209358759-a29ee9a4-5728-4dd0-91e8-dc04e23ad326.png)

# Postman screenshots
# POSTS
# POST beer
![image](https://user-images.githubusercontent.com/71765408/209359424-88d047e2-1ac1-42fd-8725-e46e7a36b259.png)
# POST brewery
![image](https://user-images.githubusercontent.com/71765408/209359161-fb3da1b5-0e09-406e-880d-7aecd575749e.png)
# POST owner
![image](https://user-images.githubusercontent.com/71765408/209360348-14a8d5e9-dec2-4edf-9a21-3c95e815b328.png)
# POST token
![image](https://user-images.githubusercontent.com/71765408/209361181-d24c9396-5e34-445b-a806-7b95a0d31a09.png)
# GETS
# GET BREWERIES
![image](https://user-images.githubusercontent.com/71765408/209361405-3575e592-130c-49d4-9278-dc760b709a5e.png)
# GET BREWERY BY NAME
![image](https://user-images.githubusercontent.com/71765408/209361620-f6e2abea-9027-49a8-ae86-3be6a370acb8.png)
# GET BEERS
![image](https://user-images.githubusercontent.com/71765408/209361331-50621e78-250e-477b-9152-09313f947807.png)
# GET BEER BY NAME
![image](https://user-images.githubusercontent.com/71765408/209361663-807e3973-d78f-4d2f-98a3-c4ac768c2f52.png)
# GET BEERS WITH SPECIFIC TYPE
![image](https://user-images.githubusercontent.com/71765408/209361961-cb663ea7-9888-4df4-b8e0-5ab3e3876cde.png)
# GET BEERS MADE BY BREWERY
![image](https://user-images.githubusercontent.com/71765408/209362105-a70d2ab4-ce98-4099-b215-6e61f23cf7cb.png)
# DELETE
# DELETE WITHOUT AUTH
![image](https://user-images.githubusercontent.com/71765408/209362239-5de2b5fb-b5e4-4185-aec3-b75fd2e1c41d.png)
# DELETE WITH AUTH
![image](https://user-images.githubusercontent.com/71765408/209362492-7c793ed6-8101-4f03-8e6c-c76b65712865.png)
# OpenAPI docs screenshots
![image](https://user-images.githubusercontent.com/71765408/209362539-3e0666cf-a695-4a5b-abdc-2a152d8a3925.png)
![image](https://user-images.githubusercontent.com/71765408/209362566-9888cdc4-0f0b-449a-967d-50f4d62420f4.png)
![image](https://user-images.githubusercontent.com/71765408/209362649-c735a090-fc1c-42af-a403-d4f8c9fc2bda.png)
![image](https://user-images.githubusercontent.com/71765408/209362696-ce347b1f-0324-41d2-ab44-868a38398d01.png)
![image](https://user-images.githubusercontent.com/71765408/209362718-62d0b35c-9bd5-4f9c-831e-fc76ab28b962.png)
![image](https://user-images.githubusercontent.com/71765408/209362749-ef63016e-607d-405c-a196-6f12155be4b1.png)
# LINKS
- Hosted API: https://beer-joppevdb.cloud.okteto.net
- Front-end repo: https://github.com/joppevdb/frontend-eindproject
- Hosted front-end: https://eindproject.netlify.app/
- Repo basisproject: https://github.com/joppevdb/basisproject





  

