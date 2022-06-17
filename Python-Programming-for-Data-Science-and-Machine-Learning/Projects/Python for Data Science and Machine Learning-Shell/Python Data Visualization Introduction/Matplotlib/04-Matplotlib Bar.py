import matplotlib.pyplot as plt

## Define variable
x1 = [2, 4, 6, 8, 10]
y1 = [6, 7, 8, 2, 4]

x2 = [1, 3, 5, 7, 9]
y2 = [7, 8, 2, 4, 2]

## Bar Plot
plt.bar(x1, y1, label = 'Bar1', color = 'r')
plt.bar(x2, y2, label = 'Bar2', color = 'c')

plt.xlabel('x number')
plt.ylabel('y number')
plt.title('Bar Graph')
plt.legend()

plt.show()
