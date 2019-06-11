import matplotlib.pyplot as plt

x = [1,2,3]
y = [5,7,4]

x2 = [5,9,11]
y2 = [10,14,12]

plt.bar(x, y, label='First Bar', color='red')
plt.bar(x2, y2, label='Second Bar', color='k')

plt.xlabel('X axis here')
plt.ylabel('Y axis here')
plt.title('Tutorial 2 Chart\nLooks Good!')
plt.legend()

plt.show()
