import random
from matplotlib import pyplot as plt
from matplotlib import animation
from language import Language
from ethnicity import Ethnicity
from utils import *
from math import sqrt, ceil
from threading import *

N = 1000
movement_rate = 0.001
influence_rate = 0.1
propagation_rate = 0.01
chance_to_change = 0.75
languages_n = 4


# TODO: study vowel shifts and other shifts to create sides table

sides = [
    ('a', 'e'),
    ('e', 'i'),
    ('o', 'u'),
    ('u', 'i'),
    ('i', 'e'),
]

f = open("languages/spanish", 'r')
spanish_voc = [i.replace("\n", "") for i in f.readlines()]
f.close()
f = open("languages/english", 'r')
english_voc = [i.replace("\n", "") for i in f.readlines()]
f.close()
f = open("languages/french", 'r')
french_voc = [i.replace("\n", "") for i in f.readlines()]
f.close()
f = open("languages/italian", 'r')
italian_voc = [i.replace("\n", "") for i in f.readlines()]
f.close()

spanish_lang = Language(spanish_voc, sides, chance_to_change)
english_lang = Language(english_voc, sides, chance_to_change)
french_lang = Language(french_voc, sides, chance_to_change)
italian_lang = Language(italian_voc, sides, chance_to_change)


# We give form to our graph, in quadrants
fig = plt.figure()
quadrant_lenght = ceil(sqrt(N))
size = quadrant_lenght * languages_n


spaniards = Ethnicity(spanish_lang, N, movement_rate, influence_rate,
                                                    1, 1, quadrant_lenght, 'ro')
english = Ethnicity(english_lang, N, movement_rate, influence_rate,
                                    quadrant_lenght+1, 1, quadrant_lenght, 'bo')
frenchs = Ethnicity(french_lang, N, movement_rate, influence_rate,
                                    1, quadrant_lenght+1, quadrant_lenght, 'go')
italians = Ethnicity(italian_lang, N, movement_rate, influence_rate,
                    quadrant_lenght+1, quadrant_lenght+1, quadrant_lenght, 'yo')

ethnicities = []
ethnicities.append(spaniards)
ethnicities.append(english)
ethnicities.append(frenchs)
ethnicities.append(italians)


ax = plt.axes(xlim=(0, quadrant_lenght*2 + 1), ylim=(0, quadrant_lenght*2 + 1))
for ethnicity in ethnicities:
    ethnicity.ax = ax.plot([person.x for person in ethnicity.people],
            [person.y for person in ethnicity.people], ethnicity.color)

def movement():
    travelers = []
    for ethnicity in ethnicities:
        travelers += ethnicity.depart()
    random.shuffle(travelers)
    travel_groups = list(split(travelers, len(ethnicities)))
    for ethnicity, arrivers in zip(ethnicities, travel_groups):
        ethnicity.arrival(arrivers, propagation_rate)

def animate(i):
    movement()
    ax.clear()
    for ethnicity in ethnicities:
        ethnicity.ax = ax.plot([person.x for person in ethnicity.natives],
                    [person.y for person in ethnicity.natives], ethnicity.color)


anim = animation.FuncAnimation(fig, animate, frames=20, interval=200)
plt.show()
print("Spaniards:")
print(spaniards.calc_dialect())
print("English:")
print(english.calc_dialect())
print("Franch:")
print(frenchs.calc_dialect())
print("Italians:")
print(italians.calc_dialect())
