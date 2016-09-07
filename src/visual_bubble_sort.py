import random
import numpy as np
import matplotlib.pyplot as plt

plt.subplots()

xpos = np.arange(0,100)
mylist = range(1,101)
random.shuffle(mylist)
ypos = np.asarray(mylist)

plt.bar(xpos, ypos, alpha=0.4)

plt.show()
