"""
Visualizing Insertion Sort.
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
    i = 0
    #first frame
    yield -3, -3, -3
    for j in range(1, samples):
        key = rects[j].get_height()
        yield j, key, i + 1 
        i = j - 1
        while i >= 0 and rects[i].get_height() > key:
            yield i, key, -1 
            i = i - 1

    yield i, key, -2

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
    i, key, flag = data

    if flag == -1:
        if i >= 0:
            rects[i + 1].set_height(rects[i].get_height())
            rects[i + 1].set_color('b')
            rects[i + 1].set_alpha(0.4)
            rects[i].set_height(key)
            rects[i].set_color('y')
            rects[i].set_alpha(1)
    elif flag == -2:
        rects[i + 1].set_color('b')
        rects[i + 1].set_alpha(0.4)
    elif flag == -3:
        #first frame
        return rects
    else:
        if i > 1:
            rects[flag].set_color('b')
            rects[flag].set_alpha(0.4)
        rects[i].set_color('y')
        rects[i].set_alpha(1)

    return rects

if __name__ == '__main__':
    global samples, ypos, rects

    if len(sys.argv) < 2:
        sys.exit('missing operand\nTry \'python visual_insertion_sort.py -h\' for more information.')

    outputfile = ''

    try:
        opts, args = getopt.getopt(sys.argv[1:], "hn:o:", ["help", "number=", "ofile=", "verbose-debug"])
    except getopt.GetoptError:
        print '''Usage: python visual_insertion_sort.py -n <number>
 or: python visual_insertion_sort.py -n <number> -o <outputfile>
Generate a <number> samples barchart to show how insertion sort works. To directly
see the animation or save it into <outputfile>.gif file.'''
        sys.exit(2)

    for opt, arg in opts:
        if opt in ("-h", "--help"):
            print '''Usage: python visual_insertion_sort.py -n <number>
 or: python visual_insertion_sort.py -n <number> -o <outputfile>
Generate a <number> samples barchart to show how insertion sort works. To directly
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
        #ani.save(outputfile + '.gif', writer='imagemagickfile', fps=30, dpi=50)
        ani.save(outputfile + '.gif', writer='imagemagick', fps=30, dpi=50)
