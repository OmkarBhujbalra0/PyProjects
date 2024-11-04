import random

stories = [
    '''A {noun1} lost at {noun2} followed the {noun3}, hoping for {noun4}. One {noun5}, he {verb1} a {adjective1} {noun6} guiding him {adverb}. Grateful, he {verb2} he’d {verb3} its {noun7} someday.''',

    '''In a {adjective1} {noun1}, a {noun2} bloomed only by {noun3}. One {noun4}, a {noun5} saw it {verb1} and {verb2} its {noun6}, feeling {adjective2} {noun7} of {adjective3} {noun8}.''',


    '''A {adjective1} {noun1} led a {adjective2} {noun2} through {adjective3} {noun3}. At the {noun4}, she {verb1} an {adjective4} {noun5}, now {pronoun1} {noun6} where {noun7} began to {verb2} again.'''
]

chosen = random.choice(stories)

noun1 = input("Enter first noun:(If not present in story then type space):")
noun2 = input("Enter second noun:(If not present in story then type space):")
noun3 = input("Enter third noun:(If not present in story then type space):")
noun4 = input("Enter fourth noun:(If not present in story then type space):")
noun5 = input("Enter fifth noun:(If not present in story then type space):")
noun6 = input("Enter sixth noun:(If not present in story then type space):")
noun7 = input("Enter seventh noun:(If not present in story then type space):")
noun8 = input("Enter eighth noun:(If not present in story then type space):")

verb1 = input("Enter first verb:(If not present in story then type space):")
verb2 = input("Enter second verb:(If not present in story then type space):")
verb3 = input("Enter third verb:(If not present in story then type space):")
verb4 = input("Enter fourth verb:(If not present in story then type space):")

pronoun1 = input("Enter first pronoun:(If not present in story then type space):")
pronoun2 = input("Enter second pronoun:(If not present in story then type space):")
pronoun3 = input("Enter third pronoun:(If not present in story then type space):")

adjective1 = input("Enter first adjective:(If not present in story then type space):")
adjective2 = input("Enter second adjective:(If not present in story then type space):")
adjective3 = input("Enter third adjective:(If not present in story then type space):")
adjective4 = input("Enter fourth adjective:(If not present in story then type space):")
adjective5 = input("Enter fifth adjective:(If not present in story then type space):")

adverb = input('enter adverb:')

update = chosen.format(
    verb1 = verb1,
    verb2 = verb2,
    verb3 = verb3,
    verb4 = verb4,
    noun1 = noun1,
    noun2 = noun2,
    noun3 = noun3,
    noun4 = noun4,
    noun5 = noun5,
    noun6 = noun6,
    noun7 = noun7,
    noun8 = noun8,
    adverb = adverb,
    adjective1 = adjective1,
    adjective2 = adjective2,
    adjective3 = adjective3,
    adjective4 = adjective4,
    adjective5 = adjective5,
    pronoun1 = pronoun1,
    pronoun2 = pronoun2,
    pronoun3 = pronoun3,
)

print(update)