import os

from fastapi import Depends, FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
from sqlalchemy.orm import Session

import auth
import crud
import models
import schemas
from database import SessionLocal, engine

if not os.path.exists('.\sqlitedb'):
    os.makedirs('.\sqlitedb')

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
origins = [
    "http://localhost",
    "http://localhost:8080",
    "https://localhost.tiangolo.com",
    "http://127.0.0.1:5500",
    "http://localhost:63342",
    "https://eindproject.netlify.app"

]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# posts
@app.post("/brewery/", response_model=schemas.Brewery)
def create_brewery(brewery: schemas.BreweryCreate, db: Session = Depends(get_db)):
    db_brewery = crud.get_brewery(db, brewery_name=brewery.name)
    if db_brewery:
        raise HTTPException(status_code=400, detail="Brewery already exist!")
    return crud.create_brewery(db=db, brewery=brewery)


@app.post("/brewery/{brewery_id}/beers/", response_model=schemas.Beer)
def create_beer_for_brewery(brewery_id: int, beer: schemas.BeerCreate, db: Session = Depends(get_db)):
    db_beer = crud.get_beer(db, beer_name=beer.name)
    if db_beer:
        raise HTTPException(status_code=400, detail="Beer already exist!")
    return crud.create_beer(db=db, beer=beer, brewery_id=brewery_id)


@app.post("/owner/", response_model=schemas.Owner)
def create_owner(owner: schemas.OwnerCreate, db: Session = Depends(get_db)):
    db_owner = crud.get_owner_name(db, name=owner.name)
    if db_owner:
        raise HTTPException(status_code=400, detail="Name already exist!")
    return crud.create_owner(db, owner=owner)


@app.post("/token")
def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    owner = auth.authenticate_owner(db, form_data.username, form_data.password)
    if not owner:
        raise HTTPException(status_code=401, detail="Incorrect name or password",
                            headers={"WWW-Authenticate": "bearer"})
    access_token = auth.create_acces_token(data={"sub": owner.id})

    return {"access_token": access_token, "token_type": "bearer"}


# gets
@app.get("/brewery/", response_model=list[schemas.Brewery])
def get_breweries(skip: int = 0, limit: int = 20, db: Session = Depends(get_db)):
    return crud.get_breweries(db, skip=skip, limit=limit)


@app.get("/brewery/{name}", response_model=schemas.Brewery)
def get_brewery(name: str, db: Session = Depends(get_db)):
    db_brewery = crud.get_brewery(db, brewery_name=name)
    if db_brewery is None:
        raise HTTPException(status_code=404, detail="Brewery not found!")
    return db_brewery


@app.get("/beer/", response_model=list[schemas.Beer])
def get_beers(skip: int = 0, limit: int = 20, db: Session = Depends(get_db)):
    return crud.get_beers(db, skip=skip, limit=limit)


@app.get("/beer/{naam}", response_model=schemas.Beer)
def get_beer(name: str, db: Session = Depends(get_db)):
    db_beer = crud.get_beer(db, beer_name=name)
    if db_beer is None:
        raise HTTPException(status_code=404, detail="Beer not found!")
    return db_beer


@app.get("/beer/type/{type}", response_model=list[schemas.Beer])
def get_type(beer_type: str, db: Session = Depends(get_db)):
    db_type = crud.get_beer_by_type(db, beer_type=beer_type)
    if db_type is None:
        raise HTTPException(status_code=404, detail="Type not found!")
    return db_type


@app.get("/beer/brewery/{brewery_id}", response_model=list[schemas.Beer])
def get_beer_by_brewery(brewery_id: int, db: Session = Depends(get_db)):
    db_beer_brewery = crud.get_beer_by_brewery(db, brewery_id=brewery_id)
    if db_beer_brewery is None:
        raise HTTPException(status_code=404, detail="ID not found!")
    return db_beer_brewery


# delete
@app.delete("/beer/{id}")
def delete_bier(beer_id: int, db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)):
    db_delete_beer = crud.get_beer_by_id(db, beer_id=beer_id)
    if db_delete_beer is None:
        raise HTTPException(status_code=404, detail="ID not found!")
    return crud.delete_beer(db=db, beer_id=beer_id)
