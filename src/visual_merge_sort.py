#!/usr/bin/python
"""
Visualizing Merge Sort.
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

def merge(A, p, q, r):
    L = []
    R = []
 
    for i in range(p, q + 1):
        L.append(A[i].get_height())
    for i in range(q + 1, r + 1):
        R.append(A[i].get_height())

    i = 0
    j = 0
    k = p

    while i < len(L) and j < len(R):
        if L[i] < R[j]:
            #A[k].set_height(L[i])
            yield k, L[i], r
            i = i + 1
            k = k + 1
        else:
            #A[k].set_height(R[j])
            yield k, R[j], r
            j = j + 1
            k = k + 1

    while i < len(L):
        #A[k].set_height(L[i])
        yield k, L[i], r
        i = i + 1
        k = k + 1

    while j < len(R):
        #A[k].set_height(R[j])
        yield k, R[j], r
        j = j + 1
        k = k + 1

def merge_sort(A, p, r):
    if p < r:
        q = (p + r) / 2
        for i in merge_sort(A, p, q):
            yield i
        for j in merge_sort(A, q + 1, r):
            yield j
        for k in merge(A, p, q, r):
            yield k

def index_gen():
    datas = merge_sort(rects, 0, samples - 1)
    for data in datas:
        yield data

def animate(data):
    #print data
    i, height, r = data
    rects[i].set_height(height)
    rects[i].set_color('y')
    if i > 0:
        rects[i - 1].set_color('b')
    if i == r:
        rects[i].set_color('b')

    return rects

class Counter():
    num = 0

def merge_for_cnt(A, p, q, r):
    L = []
    R = []

    for i in range(p, q + 1):
        L.append(A[i].get_height())
    for i in range(q + 1, r + 1):
        R.append(A[i].get_height())

    i = 0
    j = 0
    k = p

    while i < len(L) and j < len(R):
        if L[i] < R[j]:
            Counter.num += 1
            #A[k].set_height(L[i])
            i = i + 1
            k = k + 1
        else:
            Counter.num += 1
            #A[k].set_height(R[j])
            j = j + 1
            k = k + 1

    while i < len(L):
        Counter.num += 1
        #A[k].set_height(L[i])
        i = i + 1
        k = k + 1

    while j < len(R):
        Counter.num += 1
        #A[k].set_height(R[j])
        j = j + 1
        k = k + 1

def merge_sort_for_cnt(A, p, r):
    if p < r:
        q = (p + r) / 2
        merge_sort_for_cnt(A, p, q)
        merge_sort_for_cnt(A, q + 1, r)
        merge_for_cnt(A, p, q, r)

def save_cnt_gen():
    merge_sort_for_cnt(rects, 0, samples - 1)
    return Counter.num

if __name__ == '__main__':
    global samples, ypos, rects

    if len(sys.argv) < 2:
        sys.exit('missing operand\nTry \'python visual_merge_sort.py -h\' for more information.')

    outputfile = ''

    try:
        opts, args = getopt.getopt(sys.argv[1:], "hn:o:", ["help", "number=", "ofile=", "verbose-debug"])
    except getopt.GetoptError:
        print '''Usage: python visual_merge_sort.py -n <number>
 or: python visual_merge_sort.py -n <number> -o <outputfile>
Generate a <number> samples barchart to show how merge sort works. To directly
see the animation or save it into <outputfile>.gif file.'''
        sys.exit(2)

    for opt, arg in opts:
        if opt in ("-h", "--help"):
            print '''Usage: python visual_merge_sort.py -n <number>
 or: python visual_merge_sort.py -n <number> -o <outputfile>
Generate a <number> samples barchart to show how merge sort works. To directly
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
        ani.save(outputfile + '.mp4', writer='ffmpeg', fps=30, dpi=50)
        #ani.save(outputfile + '.gif', writer='imagemagick', fps=30, dpi=50)
