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
 
    yield 0, p + 1, i, p, q
    for j in range(p + 1, q + 1):
        yield 0, j, i, p, q
        if A[j].get_height() <= x:
            i = i + 1
            yield 1, j, i, p, q
    yield 2, p, i, p, q

def quick_sort(A, p, r):
    if p < r:
        #print('p = %d, r = %d' % (p, r))
        for data0 in partition(A, p, r):
            yield data0
        q = data0[2]
        #print('p = %d, q = %d, r = %d' % (p, q, r))
        for data1 in quick_sort(A, p, q - 1):
            yield data1
        for data2 in quick_sort(A, q + 1, r):
            yield data2

def index_gen():
    datas = quick_sort(rects, 0, samples - 1)
    for data in datas:
        yield data

def animate(data):
    # flag = 
    #   0: scan and compare
    #   1: exchange
    #   2: exchange and finish current partition
    flag, j, i, p, q = data
    #print(data)

    rects[p].set_color('y')

    if flag == 0:
        if j == p + 1:
            for idx in range(p, q + 1):
                rects[idx].set_color('g')
                rects[p].set_color('y')
        else:
            if j > i + 1:
                rects[j - 1].set_color('r')
        rects[j].set_color('c')
    elif flag > 0:
        if i != j:
            # Exchange rects[j] and rects[i]
            rects[j].set_color('r')
            rects[i].set_color('slateblue')
            tmp = rects[j].get_height()
            rects[j].set_height(rects[i].get_height())
            rects[i].set_height(tmp)
        else:
            rects[i].set_color('slateblue')

        if flag == 2:
            for rect in rects:
                rect.set_color('b')

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
        print('''Usage: python visual_quick_sort.py -n <number>
 or: python visual_quick_sort.py -n <number> -o <outputfile>
Generate a <number> samples barchart to show how quick sort works. To directly
see the animation or save it into <outputfile>.gif file.''')
        sys.exit(2)

    for opt, arg in opts:
        if opt in ("-h", "--help"):
            print('''Usage: python visual_quick_sort.py -n <number>
 or: python visual_quick_sort.py -n <number> -o <outputfile>
Generate a <number> samples barchart to show how quick sort works. To directly
see the animation or save it into <outputfile>.gif file.''')
            sys.exit()
        elif opt in ("-n", "--number"):
            samples = int(arg)
        elif opt in ("-o", "--ofile"):
            outputfile = arg

    fig, ax = plt.subplots()
    xpos = np.arange(0, samples)
    datalist = list(range(1, samples + 1))
    random.shuffle(datalist)
    ypos = np.asarray(datalist)
    rects = ax.bar(xpos, ypos, alpha=0.4, color='b')
    #tmp = []
    #for i in range(0, samples):
    #    tmp.append(rects[i].get_height())
    #print(tmp)

    ani = animation.FuncAnimation(fig, animate, frames=index_gen, repeat=False,
                                  init_func=init_animate, interval=500)
    if outputfile == '':
        plt.show()
    else:
        ani.save_count = save_cnt_gen()
        ani.save(outputfile + '.mp4', writer='ffmpeg', fps=30, dpi=50)
        #ani.save(outputfile + '.gif', writer='imagemagick', fps=30, dpi=50)
