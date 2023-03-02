from matplotlib import animation
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


fig = plt.figure(figsize=(8,6))
axes = fig.add_subplot(1,1,1)
axes.set_ylim(0, 150)

lst1=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15 ]
lst2=[0, 5, 10, 15, 20, 25, 30, 35, 40, 50, 60, 70, 80, 90, 100]
print(len(lst1),len(lst2))
y1, y2, = [], []
def animate(i):
    y1=lst1[i]
    y2=lst2[i]
    
    plt.bar(["one", "two"], [y1,y2], color='red')

plt.title("Some Title, Year: {} ".format(5000), color=("blue"))
ani = FuncAnimation(fig, animate, interval=100, frames= len(lst1))

plt.show()