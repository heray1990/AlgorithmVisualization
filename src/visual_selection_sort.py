#!/usr/bin/python
"""
Visualizing Selection Sort.
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
    for i in range(0, samples - 1):
        idxOfMinElement = i
        yield i, idxOfMinElement, 0 
        for j in range(i + 1, samples):
            if rects[j].get_height() < rects[idxOfMinElement].get_height():
                yield j, idxOfMinElement, 1 
                idxOfMinElement = j
            yield j, idxOfMinElement, 2 
        yield i, idxOfMinElement, 3

    yield i, idxOfMinElement, -2

def save_cnt_gen():
    k = 1

    for j in range(1, samples):
        i = j - 1
        while i >= 0:
            k += 1
            i = i - 1
        k += 1

    return k

def animate(data):
    i, idxOfMin, flag = data

    if flag == 0:
        rects[i].set_color('y')
        rects[i].set_alpha(1)
    elif flag == 1:
        rects[idxOfMin].set_color('b')
        rects[idxOfMin].set_alpha(0.4)
        #rects[i].set_color('y')
        #rects[i].set_alpha(1)
    elif flag == 2:
        rects[i].set_color('y')
        rects[i].set_alpha(0.4)
        rects[idxOfMin].set_color('y')
        rects[idxOfMin].set_alpha(1)
        rects[i - 1].set_color('b')
        rects[i - 1].set_alpha(0.4)
    elif flag == 3:
        tmp = rects[idxOfMin].get_height()
        rects[idxOfMin].set_height(rects[i].get_height())
        rects[idxOfMin].set_color('b')
        rects[idxOfMin].set_alpha(0.4)
        rects[i].set_height(tmp)
        rects[i].set_color('b')
        rects[i].set_alpha(0.4)
        rects[samples - 1].set_color('b')

    return rects

if __name__ == '__main__':
    global samples, ypos, rects

    if len(sys.argv) < 2:
        sys.exit('missing operand\nTry \'python visual_selection_sort.py -h\' for more information.')

    outputfile = ''

    try:
        opts, args = getopt.getopt(sys.argv[1:], "hn:o:", ["help", "number=", "ofile="])
    except getopt.GetoptError:
        print '''Usage: python visual_selection_sort.py -n <number>
 or: python visual_selection_sort.py -n <number> -o <outputfile>
Generate a <number> samples barchart to show how selection sort works. To directly
see the animation or save it into <outputfile>.gif file.'''
        sys.exit(2)

    for opt, arg in opts:
        if opt in ("-h", "--help"):
            print '''Usage: python visual_selection_sort.py -n <number>
 or: python visual_selection_sort.py -n <number> -o <outputfile>
Generate a <number> samples barchart to show how selection sort works. To directly
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
                                  init_func=init_animate, interval=500)
    if outputfile == '':
        plt.show()
    else:
        ani.save_count = save_cnt_gen()
        ani.save(outputfile + '.gif', writer='imagemagick', fps=30, dpi=50)
