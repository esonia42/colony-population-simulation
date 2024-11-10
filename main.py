import names
import random
from person import Person
from person import Colony

start_year = 2397
current_year = start_year

colony1 = Colony(name='Ololo')
colony2 = Colony(name='Azaza')
colonies = [colony1, colony2]

for colony in colonies:
    for i in range(100):
        new_person = Person(colony)

while True:
    current_year += 1
    for colony in colonies:
        for i in range(int(len(colony.population) * colony.birth_rate)):
            new_person = Person(colony)
        for person in colony.population:
            person.age()
        print(len(colony.population))
