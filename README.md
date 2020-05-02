Runs on Python3
# The idea
I want, in a ludicrous manner, show moving dots to represent moving people from different ethnicity.
Each ethnicity has its original language, and each individual has its own copy.
The individuals will randomly move depending on the looseness of the ethnicity (just thinking of the Hungarians)
and suffer contagions in its own dialect.
There are 4 main rates to fiddle:
`movement_rate`: how many individuals of an ethnicity move each clock (how many people)
`propagation_rate`: how much individuals does a single individual impact (how many people)
`influence_rate`: how much do they influence (how many words)
`chance_to_change`: for each language how susceptible is to change (how likely is for a word to change in a contact, and how likely is for each letter of the word to change)

## Simulation:
Generate ethnicity and possible shifts, and the 4 rates selected
Each ethnicity starts with different language but __equal__ in size. Each vocabulary has an array
of semantically equivalents words (position is meaning here)
It holds a state, and its responsible for the moving of pieces

## Language:
A language consist of a list of words (vocabulary), and an array sides of n
tuples. Sides represent the sides of a oriented graph, for the flow of shifts.

## Ethnicity and persons:
Ethnicity receives and let people of, stores a natives array and a current population array.
