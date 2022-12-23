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

Brewery

Owner


#test
In de app zit ook een bestand genaamd test_app.py. Dit bestand gaat alle functies testen (get, post, delete). Omdat dit bestand gebruik maakt van vaste waarden gaan sommige test maar één keer kunnen uitgevoerd worden. Als u alle testen wilt uitvoeren moet u eerst de database verwijderen,

screen:

# Postman screenshots
# POSTS
# POST beer
# POST brewery
# POST owner
# POST token
# GETS
# GET
# GET
# GET
# GET
# GET
# GET
# DELETE
# OpenAPI docs screenshots
# LINKS
- Hosted API: https://beer-joppevdb.cloud.okteto.net
- Front-end repo: https://github.com/joppevdb/frontend-eindproject
- Hosted front-end: https://eindproject.netlify.app/
- Repo basisproject: https://github.com/joppevdb/basisproject





  

