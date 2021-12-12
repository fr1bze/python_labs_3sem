import matplotlib.pyplot as plt
for num in range(1,6):
    f = open("/Users/mikhail/Desktop/python_3sem/laba/lab_1/episode_1 /00%d.dat" % num)
    n = int(f.readline())
    x = []
    y = []
    for i in range(n):
        r = f.readline().split()
        x.append(float(r[0]))
        y.append(float(r[1]))
    fig, axes = plt.subplots(figsize=[8.0, 6.4])
    plt.gca().set_aspect('equal', adjustable='box')
    axes.plot(x,y,'.C%d' % num, label = "00%d.dat" % num)
    plt.legend()
    plt.savefig('00%d.jpg' % num)
    plt.show()
