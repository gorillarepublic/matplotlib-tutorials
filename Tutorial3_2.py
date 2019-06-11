import matplotlib.pyplot as plt



population_ages = [3,45,63,63,93,6,29,33,53,9,57,15,36,19,99,103,129,34,89,24]

bin = [0,10,20,30,40,50,60,70,80,90,100,120,130]

plt.hist(population_ages, bin, histtype='bar', rwidth=0.8)

plt.xlabel('X axis here')
plt.ylabel('Y axis here')
plt.title('Tutorial 2 Chart\nLooks Good!')
plt.legend()

plt.show()
