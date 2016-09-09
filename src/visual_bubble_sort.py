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

def data_gen(i=0):
    # i = 100 + 99 + ... + 2
    i = (100 + 1) * 50 - 1
    k = 100

    while i > 0:
        for j in range(0, k):
            yield j
        i -= k    
        k -= 1

def animate(i):
    if i > 0:
        if rects[i - 1].get_height() > rects[i].get_height():
            tmp = rects[i - 1].get_height()
            rects[i - 1].set_height(rects[i].get_height())
            rects[i].set_height(tmp)

        rects[i - 1].set_color('b')
        rects[i].set_color('y')
    return ax,

ani = animation.FuncAnimation(fig, animate, data_gen, repeat=False, blit=True,
                              interval=1)

plt.show()
