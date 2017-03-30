#!/usr/bin/python
"""
Visualizing Quick Sort.
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

def partition(A, p, q):
    x = A[p].get_height()
    i = p
 
    for j in range(p + 1, q + 1):
        yield 0, j, 0
        if A[j].get_height() <= x:
            i = i + 1
            yield 1, j, i
            #tmp = A[j].get_height()
            #A[j].set_height(A[i].get_height())
            #A[i].set_height(tmp)

    #A[p].set_height(A[i].get_height())
    #A[i].set_height(x)
    yield 2, p, i
    #return i

def quick_sort(A, p, r):
    if p < r:
        for i in partition(A, p, r):
            yield i
        q = i[2]
        for j in quick_sort(A, p, q - 1):
            yield j
        for k in quick_sort(A, q + 1, r):
            yield k

def index_gen():
    datas = quick_sort(rects, 0, samples - 1)
    for data in datas:
        yield data

def animate(data):
    print data
    flag, i, j = data

    if not i == j and flag > 0:
        tmp = rects[i].get_height()
        rects[i].set_height(rects[j].get_height())
        rects[j].set_height(tmp)

    if flag == 0:
        rects[i].set_color('y')
        if i > 0:
            rects[i - 1].set_color('b')
    if flag == 2:
        rects[j].set_color('b')

    return rects

class Counter():
    num = 0

def save_cnt_gen():
    #merge_sort_for_cnt(rects, 0, samples - 1)
    return Counter.num

if __name__ == '__main__':
    global samples, ypos, rects

    if len(sys.argv) < 2:
        sys.exit('missing operand\nTry \'python visual_quick_sort.py -h\' for more information.')

    outputfile = ''

    try:
        opts, args = getopt.getopt(sys.argv[1:], "hn:o:", ["help", "number=", "ofile=", "verbose-debug"])
    except getopt.GetoptError:
        print '''Usage: python visual_quick_sort.py -n <number>
 or: python visual_quick_sort.py -n <number> -o <outputfile>
Generate a <number> samples barchart to show how quick sort works. To directly
see the animation or save it into <outputfile>.gif file.'''
        sys.exit(2)

    for opt, arg in opts:
        if opt in ("-h", "--help"):
            print '''Usage: python visual_quick_sort.py -n <number>
 or: python visual_quick_sort.py -n <number> -o <outputfile>
Generate a <number> samples barchart to show how quick sort works. To directly
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
    tmp = []
    for i in range(0, samples):
        tmp.append(rects[i].get_height())
    print tmp
    
    ani = animation.FuncAnimation(fig, animate, frames=index_gen, repeat=False,
                                  init_func=init_animate, interval=500)
    if outputfile == '':
        plt.show()
    else:
        ani.save_count = save_cnt_gen()
        ani.save(outputfile + '.mp4', writer='ffmpeg', fps=30, dpi=50)
        #ani.save(outputfile + '.gif', writer='imagemagick', fps=30, dpi=50)
