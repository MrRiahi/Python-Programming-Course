# Data Structures - Dictionary

''' in dictionary
    we have key
    and value'''

dic = {'mohammad' : 'mohammad@gmail.com',
       'ali' : 'ali@gmail.com',
       'javad' : 'javad@gmial.com',
       'hamid' : 'hamid@gmail.com'}

print('Dictionary is: ', dic)
print('''Ali's email is '''+dic['ali'], '\n')


del dic['hamid']
print('Dictionary is: ', dic, '\n')

print('There are {} contacts in the dic'.format(len(dic)), '\n')

for name, address in dic.items():
    tuple1 = (name, address)
    print('%s email is %s' % tuple1)
    print('{} email is {}'.format(name, address))

print('\n')

dic['hamid'] = 'hamid12@gmail.com'
print('Dictionary is: ', dic, '\n')

## Return keys and values
print(dic.keys())
print(dic.values())
print('Is mohammad in dic: ', 'mohammad' in dic.keys())
print('Is ali@gmail.com in dic: ', 'ali@gmail.com' in dic.values(), '\n')

## Get value of key, if it is not exist return None
print(dic.get('javad'))
print(dic.get('mohsen'))
print(dic.get('hamed', 'asghar@gmail.com'), '\n')

##Create set
print(dic.items(), '\n')

## Pop from end of dic
print(dic.popitem())
print('Dictionary is: ', dic, '\n')

## Get value of key, if the key is not exist create a key and value (default value is None
dic.setdefault('Mohsen')
dic.setdefault('Saman', 'Saman@gmail.com')
print('Dictionary is: ', dic, '\n')

## Attach two dictionary to each other
dic2 = {'Ahamad' : 'Ahmad@gmail.com'}
dic.update(dic2)
print('Dictionary is: ', dic, '\n')
