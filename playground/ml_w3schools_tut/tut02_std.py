import numpy as np

"""
Standard deviation is a number that describes how spread out the values are.
A low standard deviation means that most of the numbers are close to the mean (average) value.
A high standard deviation means that the values are spread out over a wider range.
"""

speed_std_small = [86,87,88,86,87,85,86]
std_small = np.std(speed_std_small)
print(f"Std. for {speed_std_small} -> {std_small}")

speed_std_big = [32,111,138,28,59,77,97]
std_big = np.std(speed_std_big)
print(f"Std. for {speed_std_big} -> {std_big}")


# plot data
from matplotlib import pyplot as plt

plt.subplot(2, 2, 1)
plt.hist(speed_std_small)

plt.subplot(2, 2, 2)
plt.hist(speed_std_big)

plt.subplot(2, 2, 3)
plt.scatter(range(len(speed_std_big)), speed_std_big)
plt.scatter(range(len(speed_std_small)), speed_std_small)


plt.grid(axis="y")
plt.show()

with open("tut02_plot01.jpg", "wb") as f:
    plt.savefig(f)


# Variance

"""
Variance is another number that indicates how spread out the values are.
In fact, if you take the square root of the variance, you get the standard deviation!
Or the other way around, if you multiply the standard deviation by itself, you get the variance!

E.g.:
1. Find the mean:
(32+111+138+28+59+77+97) / 7 = 77.4

2. For each value: find the difference from the mean:
32 - 77.4 = -45.4
111 - 77.4 =  33.6
138 - 77.4 =  60.6
 28 - 77.4 = -49.4
 59 - 77.4 = -18.4
 77 - 77.4 = - 0.4
 97 - 77.4 =  19.6

 3. For each difference: find the square value:
(-45.4)2 = 2061.16
 (33.6)2 = 1128.96
 (60.6)2 = 3672.36
(-49.4)2 = 2440.36
(-18.4)2 =  338.56
(- 0.4)2 =    0.16
 (19.6)2 =  384.16

 4. The variance is the average number of these squared differences:
(2061.16+1128.96+3672.36+2440.36+338.56+0.16+384.16) / 7 = 1432.2
"""

var_big = np.var(speed_std_big)
var_small = np.var(speed_std_small)

print(f"variance for {speed_std_small} -> {var_small}")
print(f"variance for {speed_std_big} -> {var_big}")
