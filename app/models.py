from sqlalchemy import Column, ForeignKey, Integer, String, Float
from sqlalchemy.orm import relationship

from database import Base


class Brewery(Base):
    __tablename__ = "brewerys"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    address = Column(String, index=True)
    owner_id = Column(Integer, ForeignKey("owners.id"))

    beers = relationship("Beer", back_populates="brewery")
    owner = relationship("Owner", back_populates="breweries")


class Beer(Base):
    __tablename__ = "bieren"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    volume = Column(Float)
    alcohol_perc = Column(Float)
    type = Column(String)
    brewery_id = Column(Integer, ForeignKey("brewerys.id"))

    brewery = relationship("Brewery", back_populates="beers")


class Owner(Base):
    __tablename__ = "owners"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    hashed_password = Column(String)

    breweries = relationship("Brewery", back_populates="owner")
