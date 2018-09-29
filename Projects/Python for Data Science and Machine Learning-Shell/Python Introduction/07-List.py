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

print('is apple in fruits: ', 'apple' in fruits, '\n')



fruits.append('apple')
print('New fruits list is:',fruits)
print('Number of apple: ', fruits.count('apple'))
print('Number of {}: '.format(fruits[3]), fruits.count(fruits[3]), '\n')

print(fruits.remove('lemon'))
print('New fruits list is:', fruits)


print('Apple index is: ', fruits.index('apple'), '\n')


fruits.insert(3, 'orange')
print('New fruits list is:', fruits, '\n')


fruits.clear()
print('New fruits list is:', fruits, '\n')




