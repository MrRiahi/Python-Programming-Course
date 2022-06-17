# String

name = 'MohammadReza Riahi'

print(len(name), '\n')

print('is R in name: ', 'R' in name)
print('is Mohammadreza in name: ', 'Mohammadreza' in name, '\n')

print(name.find('Riahi'))
print('Riahi'[2], '\n')


SortedName = sorted(name)
print('Sorted name is: ', SortedName, '\n')


message = 'My name Is MohamMadrEza'
print(message)
print(message.lower())
print(message.upper())
print(message.replace('MohamMadrEza','alireza'), '\n')



name = 'MohammadReza'
NameList = list(name)
NameTuple = tuple(name)
print(NameList)
print(NameTuple, '\n')
