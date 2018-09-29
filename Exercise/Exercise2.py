## Compute nearest distance
from math import sqrt

def comp(distance1, distance2):
    
    if distance2 > distance1:
        MyDic.setdefault(tuple(MyData[i]), 'Class1')
    elif distance2 < distance1:
        MyDic.setdefault(tuple(MyData[i]), 'Class2')
        
    


MyClass = ((0, 0),
           (5, 5))

MyData = []

MyDic = {}

number = int(input('How many points you want: '))

for i in range(number):
    x = float(input('Insert a number (x): '))
    y = float(input('Insert a number (y): '))
    MyData.insert(i, [x, y])

print('MyData is: ', MyData)

for i in range(number):
    ## for first label 
    EuclideanDistance1 = sqrt((MyClass[0][0] - MyData[i][0])**2 +
                                  (MyClass[0][1] - MyData[i][1])**2)
    ## for second label 
    EuclideanDistance2 = sqrt((MyClass[1][0] - MyData[i][0])**2 +
                                  (MyClass[1][1] - MyData[i][1])**2)

    result = comp(EuclideanDistance1, EuclideanDistance2)
    
    
print('MyDic is: ', MyDic)  


