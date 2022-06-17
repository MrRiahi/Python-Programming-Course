# Data Structures - Dictionary


dic = {'mohammad' : 'mohammad@gmail.com',
       'ali' : 'ali@gmail.com',
       'javad' : 'javad@gmial.com',
       'hamid' : 'hamid@gmail.com'}

print('Dictionary is: ', dic)
print('''Ali's email is '''+dic['ali'], '\n')


del dic['hamid']
print('Dictionary is: ', dic, '\n')

print('There are {} contacts in the dic'.format(len(dic)), '\n')


dic['hamid'] = 'hamid12@gmail.com'
print('Dictionary is: ', dic, '\n')

## Return keys and values
print(dic.keys())
print(dic.values(), '\n')

## Pop from end of dic
print(dic.popitem())
print('Dictionary is: ', dic, '\n')

