import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

f =  open("/Users/mikhail/Desktop/python_3sem/laba/lab_1/episode_2 /frames.dat", 'r')
fig, ax = plt.subplots(nrows=2, ncols=3, sharey = 'all')
for i in range(6):
    x = [float(j) for j in f.readline().split()]
    y = [float(j) for j in f.readline().split()]
    #print(x)
    #print(y)
    ax[int(i / 3)][i % 3].plot(x,y)
    ax[int(i / 3)][i % 3].set_title("frame: " + str(int(i+1)))
    ax[int(i / 3)][i % 3].xaxis.set_major_locator(ticker.MultipleLocator(3))
    ax[int(i / 3)][i % 3].yaxis.set_major_locator(ticker.MultipleLocator(3))
    ax[int(i / 3)][i % 3].grid(which='major', color = 'gray')
plt.subplots_adjust(wspace = 0.2, hspace = 0.4)
plt.suptitle("Episode 2")
plt.savefig('lab_2.png', dpi = 1500)
plt.show()

        





