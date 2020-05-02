import random
from math import floor
from person import Person

class Ethnicity:
    empty_spots = []
    overload = 0
    def __init__(self, language, n, movement_rate, influence_rate,
                starting_x, starting_y, qd_size, color):
        self.language = language
        self.n = n
        self.movement_rate = movement_rate
        self.color = color
        self.qd_size = qd_size
        self.starting_x = starting_x
        self.starting_y = starting_y
        self.people = [Person(self.language, starting_x+(i%qd_size),
                                             starting_y+floor(i/qd_size),
                                             color, influence_rate)
                                            for i in range(n)]
        self.natives = self.people.copy()

    def calc_dialect(self):
        return self.language.most_used_dialect(self.people)

    def depart(self):
        grab_of_people = []
        for i in range(floor(self.n*self.movement_rate)):
            rperson = random.choice(self.people)
            grab_of_people.append(rperson)
            self.empty_spots.append((rperson.x, rperson.y))
            self.people.remove(rperson)
            rperson.x = 0
            rperson.y = 0
        return grab_of_people

    def arrival(self, travelers, rate):
        for traveler in travelers:
            for i in range(floor(self.n*rate)):
                random.choice(self.people).chitchat(traveler)
            if self.empty_spots == []:
                traveler.x = self.starting_x+(self.overload%self.qd_size)*0.5
                traveler.y = self.starting_y+floor(self.overload/self.qd_size)*0.5
            else:
                x, y = self.empty_spots.pop()
                traveler.x = x
                traveler.y = y
        self.people += travelers
