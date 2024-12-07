import random


class Colony:
    def __init__(self, name, diseases=[]):
        self.name = name
        self.ducks = 20
        self.population = {}
        #percent of population
        self.birth_rate = random.random()
        self.mortality_rate = random.random()
        self.diseases = diseases

    def people_count(self):
        print(len(self.population))

    def process_diseases(self, person, grave_yard):
        for disease in self.diseases:
            # flow for already infected before
            if disease in person.carrying_diseases.keys():
                match person.carrying_diseases[disease]:
                    case 'infected':
                        if random.random() < disease.death_rate:
                            grave_yard[person.id] = person
                    case 'immune':
                        pass
            # flow for newcomers
            elif disease not in person.carrying_diseases.keys():
                # roll for contagiousness
                if random.random() < disease.contagiousness:
                    person.carrying_diseases[disease] = 'infected'
                    # roll for death rate
                    if disease in person.carrying_diseases.keys() and random.random() < disease.death_rate:
                        grave_yard[person.id] = person
                    # immunity for survivors
                    elif random.random() > disease.death_rate:
                        person.carrying_diseases[disease] = 'immune'