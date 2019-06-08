import matplotlib.pyplot as plt

x = [1,2,3]
y = [5,7,4]

x2 = [1,2,3]
y2 = [10,14,12]

plt.plot(x, y, label='First Line')
plt.plot(x2, y2, label='Second Line')

plt.xlabel('X axis here')
plt.ylabel('Y axis here')
plt.title('Tutorial 2 Chart\nLooks Good!')
plt.legend()

plt.show()
