import matplotlib.pyplot as plt
import numpy as np

x = np.array(["A", "B", "C", "D"])
y = np.array([3, 8, 1, 10])


plt.subplot(2, 2, 1)
plt.bar(x, y, width = 0.1, color="green")


plt.subplot(2, 2, 2)
plt.barh(x, y, height=0.5, color="red")


plt.subplot(2, 2, 3)

data = np.random.normal(170, 10, 250)
plt.hist(data)

plt.show()

with open("plot01.jpg", "wb") as f:
    plt.savefig(f)

