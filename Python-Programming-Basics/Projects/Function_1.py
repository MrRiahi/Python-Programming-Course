# Function

def comp(x,y):
    if x > y:
        print('{}'.format(x)+' is greater than '+'{}'.format(y))
    elif x < y:
        print('{}'.format(y)+' is greater than '+'{}'.format(x))
    elif x == y:
        print('{}'.format(y)+' is equal to '+'{}'.format(x))


x = int(input('Insert a number (x): '))
y = int(input('Insert a number (y): '))

comp(x,y)


