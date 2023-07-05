class Flower:
    def __init__(self, type):
        self.type = type
        self.basket = 0

    def pick(self):
        self.basket += 1
        return self.basket

class Person:
    def __init__(self, name):
        self.name = name
        self.feeling = None
        self.memories = []

    def think_of(self, other_person):
        self.memories.append(other_person)
        self.feeling = 'longing'

    def drink_to_forget(self, vessel):
        self.memories = []
        self.feeling = None

class Vessel:
    def __init__(self, type):
        self.type = type

class Mountain:
    def __init__(self, height):
        self.height = height

class Horse:
    def __init__(self, color):
        self.color = color

class Journey:
    def __init__(self, person, horse, flower, mountain, vessel):
        self.person = person
        self.horse = horse
        self.flower = flower
        self.mountain = mountain
        self.vessel = vessel

    def start(self):
        while self.flower.pick() < 10:
            self.person.think_of('Someone')
            self.person.drink_to_forget(self.vessel)

# Example instantiation
person = Person('Poet')
horse = Horse('Yellow')
flower = Flower('Juan Ear')
mountain = Mountain('High')
vessel = Vessel('Jug')

journey = Journey(person, horse, flower, mountain, vessel)
journey.start()
