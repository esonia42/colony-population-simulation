import names
import random
import uuid

from sql_alchemy import add, delete


class Person:
    def __init__(self, colony, age=0):
        self.name = names.get_full_name()
        self.age = age
        self.sex = random.randint(0, 2)
        self.carrying_diseases = {}
        self.colony = colony
        self.id = uuid.uuid4()
        self.colony.population[self.id] = self
#        db_interface.insert_persons(self)
        add(self)
        self.death_chance = 0.0001
        self.pregnancy_chance = 0.5
#        self.likes_ducks = random.choices(['si', 'no'])

    def to_age(self):
        self.age+=1

    def marry(self, person):
        pass

    def kill(self, person):
        person.die(person)

    def give_birth(self):
        Person(self.colony)

    def process_birth(self, people_to_give_birth):
        if self.sex == 1 or self.sex == 2:
            if self.age > 20:
                if random.random() < self.pregnancy_chance:
                    people_to_give_birth.append(self)

    def die(self):
        self.colony.population.pop(self.id)
        delete(self)

    def process_death(self, grave_yard):
        self.death_chance += 0.0007
        if random.random() < self.death_chance:
            grave_yard[self.id] = self

