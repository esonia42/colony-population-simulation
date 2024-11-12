import names
import random

from person import Person
from person import Colony
from person import Disease

start_year = 2397
current_year = start_year

colony1 = Colony(name='Ololo')
colony2 = Colony(name='Azaza')
colonies = [colony1, colony2]

disease1 = Disease('chickenpox', 0.8, 0.01)
disease2 = Disease('tuberculosis', 0.1, 0.7)

for colony in colonies:
    for i in range(10000):
        new_person = Person(colony)

while True:
    current_year += 1
    for colony in colonies:
        for i in range(int(len(colony.population) * colony.birth_rate)):
            new_person = Person(colony)
        people_to_delete = {}
        for person in colony.population.values():
            person.to_age()
            person.death_chance += 0.007
            if random.random() < person.death_chance:
                people_to_delete[person.id] = person
            if person.sex == 1 or person.sex == 2:
                if person.age > 20:
                    if random.random() < person.pregnancy_chance:
                        person.give_birth()
            if random.random() < disease1.contagiousness:
                person.infected = True
            if random.random() < disease2.contagiousness:
                person.infected = True
            if random.random() < disease1.death_rate:
                people_to_delete[person.id] = person
            if random.random() < disease2.death_rate:
                people_to_delete[person.id] = person
        for dead_man_id, dead_man in people_to_delete.items():
            dead_man.die()
        print(len(colony.population))
