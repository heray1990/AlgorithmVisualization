"""
Visualizing Bubble Sorting.
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
    #first frame
    yield -1, -1

    for i in range(0, (samples - 1)):
        yield i, 0
        for j in range((samples - 1), i, -1):
            yield j, 1

    yield i, 2
    #last frame 
    yield i, 3

def save_cnt_gen():
    k = 3

    for i in range(0, (samples - 1)):
        k += 1
        for j in range((samples - 1), i, -1):
            k += 1

    return k

def animate(data):
    i, flag = data

    if flag == 1:
        if rects[i - 1].get_height() > rects[i].get_height():
            tmp = rects[i - 1].get_height()
            rects[i - 1].set_height(rects[i].get_height())
            rects[i].set_height(tmp)

        rects[i].set_color('b')
        rects[i].set_alpha(0.4)
        rects[i - 1].set_color('y')
        rects[i - 1].set_alpha(1)
    elif flag == 0:
        rects[samples - 1].set_color('y')
        rects[samples - 1].set_alpha(1)
        if i > 0:
            rects[i - 1].set_color('b')
            rects[i - 1].set_alpha(0.4)
    elif flag == 2:
        rects[samples - 2].set_color('b')
        rects[samples - 2].set_alpha(0.4)
        rects[samples - 1].set_color('y')
        rects[samples - 1].set_alpha(1)
    elif flag == 3:
        rects[samples - 1].set_color('b')
        rects[samples - 1].set_alpha(0.4)

    return rects

if __name__ == '__main__':
    global samples, ypos, rects

    if len(sys.argv) < 2:
        sys.exit('missing operand\nTry \'python visual_bubble_sort.py -h\' for more information.')

    outputfile = ''

    try:
        opts, args = getopt.getopt(sys.argv[1:], "hn:o:", ["help", "number=", "ofile=", "verbose-debug"])
    except getopt.GetoptError:
        print '''Usage: python visual_bubble_sort.py -n <number>
 or: python visual_bubble_sort.py -n <number> -o <outputfile>
Generate a <number> samples barchart to show how bubble sort works. To directly
see the animation or save it into <outputfile>.gif file.'''
        sys.exit(2)

    for opt, arg in opts:
        if opt in ("-h", "--help"):
            print '''Usage: python visual_bubble_sort.py -n <number>
 or: python visual_bubble_sort.py -n <number> -o <outputfile>
Generate a <number> samples barchart to show how bubble sort works. To directly
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
        ani.save(outputfile + '.gif', writer='imagemagickfile', fps=30, dpi=50)
        #ani.save(outputfile + '.gif', writer='imagemagick', fps=30, dpi=50)
