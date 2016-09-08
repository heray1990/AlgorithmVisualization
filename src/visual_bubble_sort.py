"""
Visualizing Bubble Sorting.
"""
import random
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

fig, ax = plt.subplots()

xpos = np.arange(0,100)
datalist = range(1,101)
random.shuffle(datalist)
ypos = np.asarray(datalist)

rects = ax.bar(xpos, ypos, alpha=0.4)

def animate(i):
    if i > 0:
        if rects[i - 1].get_height() > rects[i].get_height():
            tmp = rects[i - 1].get_height()
            rects[i - 1].set_height(rects[i].get_height())
            rects[i].set_height(tmp)

        rects[i - 1].set_color('b')
        rects[i].set_color('y')
    return ax,

ani = animation.FuncAnimation(fig, animate, 100, repeat=False, blit=True)

plt.show()
