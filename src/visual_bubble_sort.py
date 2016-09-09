"""
Visualizing Bubble Sorting.
"""
import random
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

length = 10 
fig, ax = plt.subplots()

xpos = np.arange(0, length)
datalist = range(1, length + 1)
random.shuffle(datalist)
ypos = np.asarray(datalist)

rects = ax.bar(xpos, ypos, alpha=0.4)

def data_gen():
    for i in range(0, (length - 1)):
        for j in range(1, (length - i)):
            yield j

def animate(i):
    if i > 0:
        if rects[i - 1].get_height() > rects[i].get_height():
            tmp = rects[i - 1].get_height()
            rects[i - 1].set_height(rects[i].get_height())
            rects[i].set_height(tmp)

        rects[i - 1].set_color('b')
        rects[i].set_color('y')

    return ax,

ani = animation.FuncAnimation(fig, animate, data_gen, repeat=False, blit=True)

plt.show()
