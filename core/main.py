import random

from person import Person
from colony import Colony
from disease import Disease

start_year = 2397
current_year = start_year

disease1 = Disease('chickenpox', 0.8, 0.01, 'virus','permanent')
disease2 = Disease('tuberculosis', 0.02, 0.4, '',None)

colony1 = Colony(name='Ololo', diseases=[disease1, disease2])
colony2 = Colony(name='Azaza', diseases=[disease1, disease2])
colonies = [colony1, colony2]

for colony in colonies:
    for i in range(100):
        new_person = Person(colony, random.randint(20, 50))

while True:
    current_year += 1
    for colony in colonies:
        grave_yard = {}
        people_to_give_birth = []

        for person in colony.population.values():
            person.to_age()
            person.feed_ducks()
            person.process_birth(people_to_give_birth)
            colony.process_diseases(person, grave_yard)
            person.process_death(grave_yard)

        for dead_man_id, dead_man in grave_yard.items():
            dead_man.die()

        for parent in people_to_give_birth:
            parent.give_birth()

        print(len(colony.population))
        print(colony.ducks)
