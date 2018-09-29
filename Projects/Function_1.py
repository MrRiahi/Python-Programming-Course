# Function_1

def comp(x,y):
    if x > y:
        print('{}'.format(x)+' is greater than '+'{}'.format(y))
        return x
    elif x < y:
        print('{}'.format(y)+' is greater than '+'{}'.format(x))
        return y
    elif x == y:
        print('{}'.format(y)+' is equal to '+'{}'.format(x))
        return y


x = int(input('Insert a number (x): '))
y = int(input('Insert a number (y): '))

a = comp(x,y)
print(a)

input()
