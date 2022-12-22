from pydantic import BaseModel


class BeerBase(BaseModel):
    name: str
    volume: float
    alcohol_perc: float
    type: str


class BeerCreate(BeerBase):
    pass


class Beer(BeerBase):
    id: int
    brewery_id: int

    class Config:
        orm_mode = True


class BreweryBase(BaseModel):
    name: str
    address: str
    owner_id: int

class BreweryCreate(BreweryBase):
    pass


class Brewery(BreweryBase):
    id: int
    beers: list[Beer] = []

    class Config:
        orm_mode = True


class OwnerBase(BaseModel):
    name: str


class OwnerCreate(OwnerBase):
    password: str


class Owner(OwnerBase):
    id: int
    hashed_password: str
    breweries: list[Brewery] = []

    class Config:
        orm_mode = True
