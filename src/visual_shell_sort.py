#!/usr/bin/python
"""
Visualizing Shell Sort.
"""
import sys, getopt
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
    k = 0
    gap = samples / 2

    while gap >= 1:
        for i in range(0, gap):
            yield i, gap, 0, -1 
            for j in range(i + gap, samples, gap):  # Insertion Sort
                key = rects[j].get_height()
                yield j, gap, key, k + gap
                k = j - gap
                while k >= 0 and rects[k].get_height() > key:
                    yield k, gap, key, -2
                    k = k - gap
        gap = gap / 2

def save_cnt_gen():
    k = 0

    for j in range(1, samples):
        i = j - 1
        while i >= 0:
            k += 1
            i = i - 1
        k += 1

    return k

def animate(data):
    i, gap, key, flag = data
    #print(str(i) + ', ' + str(gap) + ', ' + str(key) + ', ' + str(flag))

    if flag == -1:
        for j in range(i, samples, gap):
            if gap > 1:
                rects[j].set_color('y')
                rects[j].set_alpha(0.4)
                if j > 0:
                    rects[j - 1].set_color('b')
                    rects[j - 1].set_alpha(0.4)
                if j == samples % gap:
                    rects[samples - 1].set_color('b')
                    rects[samples - 1].set_alpha(0.4)
            else:
                rects[j].set_color('b')
                rects[j].set_alpha(0.4)
    elif flag >= 0 and flag < samples:
        if i > gap:
            rects[flag].set_alpha(0.4)
        rects[i].set_alpha(1)

        if gap == 1:
            rects[flag].set_color('b')
            rects[i].set_color('y')
    elif flag == -2:
        if i >= 0:
            rects[i + gap].set_height(rects[i].get_height())
            rects[i + gap].set_alpha(0.4)
            rects[i].set_height(key)
            rects[i].set_alpha(1)

            if gap == 1:
                rects[i + gap].set_color('b')
                rects[i].set_color('y')

    return rects

if __name__ == '__main__':
    global samples, ypos, rects

    if len(sys.argv) < 2:
        sys.exit('missing operand\nTry \'python visual_shell_sort.py -h\' for more information.')

    outputfile = ''

    try:
        opts, args = getopt.getopt(sys.argv[1:], "hn:o:", ["help", "number=", "ofile="])
    except getopt.GetoptError:
        print '''Usage: python visual_shell_sort.py -n <number>
 or: python visual_shell_sort.py -n <number> -o <outputfile>
Generate a <number> samples barchart to show how shell sort works. To directly
see the animation or save it into <outputfile>.gif file.'''
        sys.exit(2)

    for opt, arg in opts:
        if opt in ("-h", "--help"):
            print '''Usage: python visual_shell_sort.py -n <number>
 or: python visual_shell_sort.py -n <number> -o <outputfile>
Generate a <number> samples barchart to show how shell sort works. To directly
see the animation or save it into <outputfile>.gif file.'''
            sys.exit()
        elif opt in ("-n", "--number"):
            samples = int(arg)
        elif opt in ("-o", "--ofile"):
            outputfile = arg

    fig, ax = plt.subplots()
    xpos = np.arange(0, samples)
    datalist = range(1, samples + 1)
    random.shuffle(datalist)
    ypos = np.asarray(datalist)
    rects = ax.bar(xpos, ypos, alpha=0.4, color='b')
    
    ani = animation.FuncAnimation(fig, animate, frames=index_gen, repeat=False,
                                  init_func=init_animate, interval=50)
    if outputfile == '':
        plt.show()
    else:
        ani.save_count = save_cnt_gen()
        ani.save(outputfile + '.gif', writer='imagemagick', fps=30, dpi=50)
