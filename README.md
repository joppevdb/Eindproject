# Eindproject
Voor het tweede en laatste deel van het project moest er een API gemaakt worden die verbonden was aan een databank. De API moet volledig automatisch worden opgebouwd door github actions. Tot slotten moet de API gehost worden op Okteto.

# Thema
Ik heb besloten om verder te bouwen op mijn vorige API. Omdat ik het een intressant thema vond. Het gekozen thema is bieren. De API is gebouwt rond het bijhouden van de geproduceerde bieren per brouwerij.

# API
De API is complexer er zijn drie hoofdonderdelen (bieren, brouwerijen, eigenaars). Per onderdeel is een tabel aangemaakt. Hierna is er ook een post per onderdeel aangemaakt zodat er snel gegevens kunnen toegevoegd worden. Tot slotte zijn er ook verschillende gets aangemaakt om gegevens op te vragen.

# Models.py
In dit bestand worden de verschillende tabellen opgesteld samen met hun relaties.

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
In dit bestand wordt opgegeven hoe een item voor een tabel gecreed kan worden.

Een opvallend gegeven bij owner wordt er een plain text password meegegeven. Dit word later pas omgezet naar een hashed password.

# crud.py
In dit bestand worden de functies aangemaakt om gegevens toe te voegen (create), om gegevense op te vragen (read) en om gegevens te verwijderen (delete).

Om gegevens toe te voegen moet eer een session worden gestart. Ook wordt er een schema meegegeven om het item aan te maken.
Vervolgens wordt er een item toegevoegd volgens het model. Hierna wordt het item toegevoegd aan de database.

Om gegevens op te vragen word er een query uitgevoerd met of zonder een filter.

Om gegevens te verwijderen wordt er eerste een query gemaakt die de gegevens gaat opvragen. Vervolgens worden de gegevens verwijderd uit de database.

# database.py
Hier wordt de database gecreerd via een URL. Vervolgens wordt er een engine, een lokale sessie en een base aangemaakt.

# auth.py
Dit bestand handelt alles af van passworden en authenticatie. Eerst worden de nodige libraries geimporteerd. Vervolgens worden de nodige varaibles aangemaakt.

def get_password_hash(password)
  -Deze functie gaat het plain text password omzetten naar een gehashed password aan de hand van de hashing methodes.
  
def verify_password(plain_password, hashed_password)
  -Deze functie gaat vergelijken of dat het gegeven password overeen komt met gehashed password

def authenticate_owner(db: Session, name: str, password:str)
  - Eerst word er gezien of de naam in de database staat
  - Hierna word het password gecontroleerd met de funcite die hierboven beschreven staat.

def create_acces_token(data:dict)
  - expire date wordt bepaald aan de hand van een vooraf gedeclareerd variable
  - Vervolgens wordt er een jwt key aangemaakt
 
# main.py
Dit bestand is het hoofdprogramma hier worden alle delen in samen gebracht. De main bevat 4 post functies om de gegevens aan te maken. Ook bevat de main 6 get functies om de gegevens te kunnen opvragen.

Overzicht van het bestand
  -Alle nodige imports worden uitgevoerd.
  -Controle op het bestaan van de map '.\sqlitedb'.
  -De tabellen worden aangemaakt.
  -De app wordt opgestart.
  -Bearer wordt aangemaakt
  -De nodige cors worden opgesteld. Er wordt ook voorzien dat de commands in een lokale omgeving kunnenn uitgevoerd worden.
  -De database wordt getest
  -De posts
  -De gets
  -De delete (enkel toegangkelijk met de nodig authenticatie)

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





  

