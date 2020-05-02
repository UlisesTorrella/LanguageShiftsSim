

class Person:

    def __init__(self, language, x, y, color, influence_rate):
        self.language = language
        self.x = x
        self.y = y
        self.color = color
        self.influence_rate = influence_rate

    def chitchat(self, pal):
        self.language.merge(pal.language, self.influence_rate)
