import random
from utils import *
from math import floor


class Language:

    def __init__(self, vocabulary, sides, chance_to_change):
        self.vocabulary = vocabulary
        self.sides = sides
        self.chance_to_change = chance_to_change

    def merge(self, another, rate):
        my_words = []
        their_words = []
        loc = []
        for i in range(floor(len(self.vocabulary)*rate)):
            chosen = random.choice(range(len(self.vocabulary)))
            my_words.append(self.vocabulary[chosen])
            their_words.append(another.vocabulary[chosen])
            loc.append(chosen)
        for my_word, their_word, i in zip(my_words, their_words, loc):
            if random.random() < self.chance_to_change:
                for j, letter in enumerate(my_word):
                    if random.random() < self.chance_to_change:
                        shifts = [(letter,x) for x in their_word if (letter, x) in self.sides]
                        if shifts: # TODO: use contagion rate
                            self.vocabulary[i] = self.vocabulary[i][:j] + random.choice(shifts)[1] + self.vocabulary[i][j+1:]

    def most_used_dialect(self, individuals):
        result = []
        for i, word in enumerate(self.vocabulary):
            modisms = [individual.language.vocabulary[i]
                                                for individual in individuals]
            result.append(most_common(modisms))
        return result
