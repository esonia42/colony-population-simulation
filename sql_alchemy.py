from sqlalchemy import create_engine, Column, Integer, String, Uuid
from sqlalchemy.orm import declarative_base, sessionmaker

engine = create_engine("postgresql+psycopg://postgres:postgres@localhost:5432/postgres")
Base = declarative_base()

Session = sessionmaker(bind=engine)
session = Session()

class Persona(Base):
    __tablename__ = 'people'

    id = Column(Uuid, primary_key=True)
    sex = Column(Integer)
    name = Column(String)
    age = Column(Integer)
    colony = Column(String)

def add(person):
    persona = Persona(id=person.id, sex=person.sex, age=person.age, name=person.name, colony=person.colony.name)
    session.add(persona)
    session.commit()

def delete(person):
    persona = session.query(Persona).filter_by(id=person.id).one_or_none()
    session.delete(persona)
    session.commit()
