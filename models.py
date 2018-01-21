# coding: utf-8
from sqlalchemy import Column, Numeric, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata

class Market(Base):
    __tablename__ = 'markets'

    fmid = Column(String, primary_key=True)
    market_name = Column(String, nullable=False)
    website = Column(String)
    facebook = Column(String)
    twitter = Column(String)
    youtube = Column(String)
    other_media = Column(String)
    street = Column(String)
    city = Column(String)
    county = Column(String)
    state = Column(String)
    zipcode = Column(String)
    season_1_date = Column(String)
    season_1_time = Column(String)
    season_2_date = Column(String)
    season_2_time = Column(String)
    season_3_date = Column(String)
    season_3_time = Column(String)
    season_4_date = Column(String)
    season_4_time = Column(String)
    x = Column(Numeric)
    y = Column(Numeric)
    location = Column(String)
    credit = Column(String)
    wic = Column(String)
    wic_cash = Column(String)
    sfmnp = Column(String)
    snap = Column(String)
    organic = Column(String)
    baked_goods = Column(String)
    cheese = Column(String)
    crafts = Column(String)
    flowers = Column(String)
    eggs = Column(String)
    seafood = Column(String)
    herbs = Column(String)
    vegetables = Column(String)
    honey = Column(String)
    jams = Column(String)
    maple = Column(String)
    meat = Column(String)
    nursery = Column(String)
    nuts = Column(String)
    plants = Column(String)
    poultry = Column(String)
    prepared = Column(String)
    soap = Column(String)
    trees = Column(String)
    wine = Column(String)
    coffee = Column(String)
    beans = Column(String)
    fruits = Column(String)
    grains = Column(String)
    juices = Column(String)
    mushrooms = Column(String)
    pet_food = Column(String)
    tofu = Column(String)
    wild_harvested = Column(String)
    update_time = Column(String)

    def json(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}
