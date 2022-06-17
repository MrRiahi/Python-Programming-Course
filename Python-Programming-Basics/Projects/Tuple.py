# Data Structures - Tuple

''' Tuple like list but
    can not add or
    modify or
    delete elements '''


animals = ('Python', 'Elephant', 'Bird')
print('Animals tuple is: ', animals)
print(animals[-1], '\n')

NewAnimals = ('Monkey', 'Camel', animals)
print('NewAnimals tuple is: ', NewAnimals)
print(len(NewAnimals))
print(NewAnimals[2])
print(NewAnimals[2][1])


