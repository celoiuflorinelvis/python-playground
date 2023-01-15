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

