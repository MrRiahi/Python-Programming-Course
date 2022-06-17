# Data Structures - Set

number1 = set(['1','3','3','4'])
number2 = set(['1','5','7','4'])

print('Set of number1: ', number1, '\n')
print('Set of number2: ', number2, '\n')


## Return difference of sets
print(number1.difference(number2), '\n')

## Update a set with the difference of itself and another set
number1.difference_update(number2)
print('Set of number1: ', number1, '\n')

## Add an element to set
number1.add('4')
print('Set of number1: ', number1, '\n')

## Remove an element from set if it is in it
number2.discard('1')
print('Set of number2: ', number2, '\n')

## Return the intersection of two sets as a new set
number3 = number2.intersection(number1)
print('Set of number3: ', number3, '\n')

## Update a set with the intersection
number1.intersection_update(number2)
print('Set of number1: ', number1, '\n')

## Return True if two sets have a null intersection
print('Number2 isdisjoint number1 is: ', number2.isdisjoint(number1), '\n')

## Report whether another set contains this set
print('Number2 issubset number1 is: ', number2.issubset(number1))
print('Number1 issubset number2 is: ', number1.issubset(number2), '\n')

## Report whether this set contains another set
print('Number2 issuperset number1 is: ', number2.issuperset(number1))
print('Number1 issuperset number2 is: ', number1.issuperset(number2), '\n')

## Remove and return an arbitrary set element
print('Pop number2 is: ', number2.pop())
print('Set of number2: ', number2, '\n')

## Return the symmetric_difference of two sets as a new set
number4 = number2.symmetric_difference(number1)
print('Set of number4: ', number4, '\n')

## Update a set with the symmetric_difference of itself and another set
number2.symmetric_difference_update(number1)
print('Set of number2: ', number2, '\n')

## Return the union of sets as a new set
number5 = number2.union(number1)
print('Set of number5: ', number5, '\n')

## Update a set with the union of itself and another set
number2.update(set(['45']))
print('Set of number2: ', number2, '\n')




