"""
Visualizing Bubble Sorting.
"""
import sys
import random
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def init_animate():
    i = 0
    for rect in rects:
        rect.set_height(ypos[i])
        i += 1

def index_gen():
    for i in range(0, (length - 1)):
        for j in range(1, (length - i)):
            yield j

        rects[length - i - 1].set_color('b')

    # A flag, represent the end of the sort.
    yield -1

def save_cnt_gen():
    k = 1

    for i in range(0, (length - 1)):
        for j in range(1, (length - i)):
            k += 1

    return k

def animate(i):
    if i > 0:
        if rects[i - 1].get_height() > rects[i].get_height():
            tmp = rects[i - 1].get_height()
            rects[i - 1].set_height(rects[i].get_height())
            rects[i].set_height(tmp)

        rects[i - 1].set_color('b')
        rects[i].set_color('y')

    return rects

if __name__ == '__main__':
    global length, ypos, rects

    if len(sys.argv) > 1 and sys.argv[1].isdigit():
        length = int(sys.argv[1])
    else:
        length = 20

    fig, ax = plt.subplots()
    xpos = np.arange(0, length)
    datalist = range(1, length + 1)
    random.shuffle(datalist)
    ypos = np.asarray(datalist)
    rects = ax.bar(xpos, ypos, alpha=0.4, color='b')
    
    ani = animation.FuncAnimation(fig, animate, frames=index_gen, repeat=False,
                                  init_func=init_animate, interval=50)

    if len(sys.argv) > 2 and sys.argv[2] == 'save':
        ani.save_count = save_cnt_gen()
        giffilename = "bubble_sort_" + str(length) + "samples_fps20_dpi50.gif"
        ani.save(giffilename, writer='imagemagick', fps=20, dpi=50)
    else:
        plt.show()
