# Data Structures - List

fruits = ['apple', 'bannana', 'orange', 'straberry', 'lemon']

print('I have', len(fruits), 'fruits', '\n')

print('These items are: ')
for item in fruits:
    print(item)

print('\n')

for index in range(len(fruits)):
    print(fruits[index])

print('\n')

print('is cucumber in fruits: ', 'cucumber' in fruits)
print('is apple in fruits: ', 'apple' in fruits, '\n')

fruits.append('rice')
print('New fruits list is:',fruits, '\n')

fruits.append('apple')
print('New fruits list is:',fruits)
print('Number of apple: ', fruits.count('apple'))
print('Number of {}: '.format(fruits[3]), fruits.count(fruits[3]), '\n')

print(fruits.remove('lemon'))
print('New fruits list is:', fruits)
print(fruits.pop(2))
print('New fruits list is:', fruits, '\n')

print('Apple index is: ', fruits.index('apple'))
print('Second apple index is: ', fruits.index('apple',2), '\n')

fruits.insert(3, 'orange')
print('New fruits list is:', fruits, '\n')

fruits.reverse()
print('New fruits list is:', fruits, '\n')

CopyFruits = fruits.copy()
print('CopyFruits list is:', CopyFruits, '\n')

fruits.sort()
print('Sorted fruits is: ', fruits, '\n')

NewList = ['a', 'b', 2]
fruits.extend(NewList)
print('Extend fruits list is: ', fruits, '\n')


del fruits[1]
print('New fruits list is:', fruits, '\n')

print('My favorite fruits is: ', fruits[2:5])

fruits.clear()
print('New fruits list is:', fruits, '\n')



##brothers = ['Alireza ', ', Mohammadreza ', ', Amirreza ']
##glue = 'Riahi'
##print(glue.join(brothers))

