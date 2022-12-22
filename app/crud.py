from sqlalchemy.orm import Session

import auth
import models
import schemas


# eigenaar
def create_owner(db: Session, owner: schemas.OwnerCreate):
    hashed_password = auth.get_password_hash(owner.password)
    db_owner = models.Owner(name=owner.name, hashed_password=hashed_password)
    db.add(db_owner)
    db.commit()
    db.refresh(db_owner)
    return db_owner


def get_owner_name(db: Session, name: str):
    return db.query(models.Owner).filter(models.Owner.name == name).first()


# brouwerij
def get_brewery(db: Session, brewery_name: str):
    return db.query(models.Brewery).filter(models.Brewery.name == brewery_name).first()


def get_breweries(db: Session, skip: int = 0, limit: int = 20):
    return db.query(models.Brewery).offset(skip).limit(limit).all()


def create_brewery(db: Session, brewery: schemas.BreweryCreate):
    db_brewery = models.Brewery(name=brewery.name, address=brewery.address, owner_id=brewery.owner_id)
    db.add(db_brewery)
    db.commit()
    db.refresh(db_brewery)
    return db_brewery


# Bieren
def get_beer(db: Session, beer_name: str):
    return db.query(models.Beer).filter(models.Beer.name == beer_name).first()


def get_beer_by_id(db: Session, beer_id: int):
    return db.query(models.Beer).filter(models.Beer.id == beer_id).first()


def get_beer_by_type(db: Session, beer_type: str):
    return db.query(models.Beer).filter(models.Beer.type == beer_type).all()


def get_beer_by_brewery(db: Session, brewery_id: int):
    return db.query(models.Beer).filter(models.Beer.brewery_id == brewery_id).all()


def get_beers(db: Session, skip: int = 0, limit: int = 20):
    return db.query(models.Beer).offset(skip).limit(limit).all()


def create_beer(db: Session, beer: schemas.BeerCreate, brewery_id: int):
    db_beer = models.Beer(**beer.dict(), brewery_id=brewery_id)
    db.add(db_beer)
    db.commit()
    db.refresh(db_beer)
    return db_beer


def delete_beer(db: Session, beer_id: int):
    db_beer_to_delete = db.query(models.Beer).filter(models.Beer.id == beer_id).first()
    db.delete(db_beer_to_delete)
    db.commit()
    return db_beer_to_delete
