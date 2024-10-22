import names
import random
# from person import Person

start_year = 2397
current_year = start_year

class Person:
    def __init__(self):
        self.name = names.get_full_name()
        self.age = 0
        self.sex = random.randint(0, 2)
        self.infected = False
        self.colony = 1

    def age(self):
        pass
    def give_birth(self):
        pass
    def marry(self, person):
        pass
    def kill(self, person):
        pass
    def get_infected(self):
        pass
    def die(self):
        pass


while True:
    current_year += 1
    for i in range(500):
        new_person = Person()
        print(new_person.name)

