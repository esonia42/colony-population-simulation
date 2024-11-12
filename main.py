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

disease1 = Disease('chickenpox', 0.8, 0.01, 'permanent')
disease2 = Disease('tuberculosis', 0.02, 0.4, None)
disease_list = [disease1, disease2]


def process_diseases(person):
    for disease in disease_list:
        # flow for already infeced before
        if disease in person.infected_with.keys():
            if disease.immunity == None:
                # no immunity
                pass
            else:
                pass
                # disease has immunity

        # flow for newcomers

def process_death(person):
    person.death_chance += 0.0007
    if random.random() < person.death_chance:
        people_to_delete[person.id] = person


def process_birth(person):
    if person.sex == 1 or person.sex == 2:
        if person.age > 20:
            if random.random() < person.pregnancy_chance:
                people_to_get_birth.append(person)


for colony in colonies:
    for i in range(100):
        new_person = Person(colony, random.randint(20, 50))

while True:
    current_year += 1
    for colony in colonies:
        people_to_delete = {}
        people_to_get_birth = []
        for person in colony.population.values():
            person.to_age()
            process_birth(person)
            process_diseases(person)
            process_death(person)
        for dead_man_id, dead_man in people_to_delete.items():
            dead_man.die()
        for parent in people_to_get_birth:
            parent.give_birth()
        print(len(colony.population))
