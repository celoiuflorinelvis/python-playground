from matplotlib import pyplot as plt
import matplotlib
import numpy

matplotlib.use('Agg')

xp = numpy.array([0, 6])
yp = numpy.array([0, 250])

plt.plot(xp, yp)
plt.show()

#Two  lines to make our compiler able to draw:
with (open("plot01.jpg", "wb")) as f:
    plt.savefig(f)
    f.close()

plt.clf()
plt.plot(xp, yp, 'o')
plt.show()

#Two  lines to make our compiler able to draw:
with (open("plot02.jpg", "wb")) as f:
    plt.savefig(f)
    f.close()


xp = numpy.array([1, 2, 6, 8])
yp = numpy.array([3, 8, 1, 10])

plt.clf()
plt.plot(xp, yp)
plt.show()

#Two  lines to make our compiler able to draw:
with (open("plot03.jpg", "wb")) as f:
    plt.savefig(f)
    f.close()

