import names
import random
import uuid

from sqlalchemy import create_engine, Column, Integer, String, Uuid, Float, ForeignKey
from sqlalchemy.orm import declarative_base, sessionmaker, Mapped, relationship

engine = create_engine("postgresql+psycopg://postgres:postgres@localhost:5432/postgres")
Base = declarative_base()

Session = sessionmaker(bind=engine)
session = Session()


class Disease(Base):
    __tablename__ = 'Diseases'

    name = Column(String, primary_key=True)
    contagiousness = Column(Float)
    death_rate = Column(Float)
    disease_type = Column(String)
    immunity = Column(String)


class Colony(Base):
    __tablename__ = 'colonies'

    name = Column(String, primary_key=True)
    birth_rate = Column(Float)
    mortality_rate = Column(Float)
    population: Mapped[list["Person"]] = relationship()


class Person(Base):
    __tablename__ = 'people'

    id = Column(Uuid, primary_key=True)
    sex = Column(Integer)
    name = Column(String)
    age = Column(Integer)
    colony_name = Column(String, ForeignKey("colonies.name"))
    death_chance = Column(Float)
    pregnancy_chance = Column(Float)
    colony: Mapped["Colony"] = relationship()

def add(colony):
    person = Person(
        id = uuid.uuid4(),
        sex=random.randint(0, 2),
        age=0,
        name=names.get_full_name(),
        colony=colony.name,
        death_chance = 0.0001,
        pregnancy_chance = 0.5)
    session.add(person)
    session.commit()

def delete(person):
    person_to_die = session.query(Person).filter_by(id=person.id).one_or_none()
    session.delete(person_to_die)
    session.commit()




'''    def __init__(self, person_id, sex, name, age, colony, death_chance, pregnancy_chance):
        self.person_id = person_id
        self.sex = sex
        self.name = name
        self.age = age
        self.colony = colony
        self.death_chance = death_chance
        self.pregnancy_chance = pregnancy_chance'''