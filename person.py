import names
import random
import uuid

class Person:
    def __init__(self, colony):
        self.name = names.get_full_name()
        self.age = 0
        self.sex = random.randint(0, 2)
        self.infected = False
        self.colony = colony
        self.id = uuid.uuid4()
        self.colony.population[self.id] = self.name

    def age(self):
        self.age+=1

    def marry(self, person):
        pass

    def kill(self, person):
        person.die(person)

    def get_infected(self):
        self.infected = True

    def give_birth(self):
        pass

    def die(self):
        self.colony.population.popitem(self)

class Colony:
    def __init__(self, name):
        self.name = name
        self.ducks = 20
        self.population = {}
        #percent of population
        self.birth_rate = random.random()
        self.mortality_rate = random.random()

    def people_count(self):
        pass

    def ducks_count(self):
        print(self.ducks)

class Disease:
    def __init__(self, name, contagiousness):
        self.name = name
        self.contagiousness = contagiousness