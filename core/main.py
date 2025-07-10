from threading import Thread
import random
import time
from flask import Flask


from person import Person
from colony import Colony
from disease import Disease

app = Flask(__name__)

current_year = 2397

disease1 = Disease('chickenpox', 0.8, 0.01, 'virus','permanent')
disease2 = Disease('tuberculosis', 0.02, 0.4, '',None)

colony1 = Colony(name='Ololo', diseases=[disease1, disease2])
colony2 = Colony(name='Azaza', diseases=[disease1, disease2])
colonies = [colony1, colony2]


def spawn_initial_population():
    for colony in colonies:
        for i in range(100):
            new_person = Person(colony, random.randint(20, 50))


spawn_initial_population()


def progress_time():
    while True:
        global current_year
        print(current_year)
        current_year += 1
        for colony in colonies:
            grave_yard = {}
            people_to_give_birth = []

            for person in colony.population.values():
                person.to_age()
                person.process_birth(people_to_give_birth)
                colony.process_diseases(person, grave_yard)
                person.process_death(grave_yard)

            for dead_man_id, dead_man in grave_yard.items():
                dead_man.die()

            for parent in people_to_give_birth:
                parent.give_birth()
        print("Colony 1: ", len(colony1.population))
        print("Colony 2: ", len(colony2.population))

@app.route('/people/<n>', methods=["GET"])
def people_count(n):
    if int(n) <= len(colonies):
        colony = colonies[int(n) - 1]
        return "Colony " + n + ": " + str(len(colony.population))
    else:
        return "No such colony"


if __name__ == "__main__":
   t = Thread(target=progress_time)
   t.start()
   app.run(debug=True)
