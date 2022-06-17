import matplotlib.pyplot as plt

## Define variable
x = [1, 2, 3, 4, 5, 6, 7, 8]
y = [5, 2, 4, 2, 1, 4, 5, 2]

## Scatter Plot
plt.figure()
plt.scatter(x, y, color = 'k', linewidths = 5, marker = 'o')


plt.xlabel('x number')
plt.ylabel('y number')
plt.title('Scatter Graph')

plt.show()
