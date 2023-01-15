import numpy
from scipy import stats

speed = [99,86,87,88,111,86,103,87,94,78,77,85,86]

# The mean value is the average value.
v_mean = numpy.mean(speed)

# The median value is the value in the middle, after you have sorted all the values:
v_meadian = numpy.median(speed)

# The Mode value is the value that appears the most number of times:
v_mode = stats.mode(speed)

print(f"Mean: {v_mean}\nMedian: {v_meadian}\nMode: {v_mode}")


# Display graph
from matplotlib import pyplot as plt

# plot data
plt.scatter(numpy.array(range(len(speed))), numpy.array(speed))

# plot mean and meadian
plt.scatter(numpy.array([0]), numpy.array([v_mean]), c = numpy.array(["red"]), label="Mean: {}".format(v_mean) )
plt.scatter(numpy.array([0]), numpy.array([v_meadian]), c = numpy.array(["green"]), label="Median: {}".format(v_meadian) )

plt.legend(title="Mean/Median")
plt.grid(axis="y")


plt.show()

with open("tut01_plot01.jpg", "wb") as f:
    plt.savefig(f)
