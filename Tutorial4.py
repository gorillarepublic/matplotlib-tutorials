import matplotlib.pyplot as plt


x = [1,2,3,4,5,6,7,8]
y = [5,2,4,2,1,4,5,2]

x2 = [8,7,6,5,4,3,2,1]
y2 = [4,8,6,7,2,1,4,6]

plt.scatter(x,y, label='skitscat', color='k', marker="d")
plt.scatter(x2,y2, label='skitscat', color='k', marker="d")

plt.xlabel('x')
plt.ylabel('y')
plt.title('Tutorial 2 Chart\nLooks Good!')
plt.legend()

plt.show()
