import matplotlib.pyplot as plt
for num in range(1,6):
    f = open("00%d.dat" % num)
    n = int(f.readline())
    x = []
    y = []
    for i in range(n):
        r = f.readline().split()
        x.append(float(r[0]))
        y.append(float(r[1]))

    plt.plot(x,y,'.C%d' % num, label = "00%d.dat" % num)
    plt.legend()
    plt.savefig('00%d.jpg' % num)
    plt.show()

