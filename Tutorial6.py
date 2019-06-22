import matplotlib.pyplot as plt

#This shows information over a slice of time



my_data = [8,2,3,9]
my_labels = ['sleeping', 'eating', 'playing', 'working']
slice_cols = ['c','m','r','b']

plt.pie(my_data,
        labels=my_labels,
        colors=slice_cols,
        startangle=90,
        shadow=True,
        explode=(0,0,0,0.1),
        autopct='%1.1f%%')


#plt.xlabel('x')
#plt.ylabel('y')
plt.title('Tutorial 6\nPie Chart')
#plt.legend()

plt.show()
