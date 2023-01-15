import matplotlib.pyplot as plt
import numpy as np

y = np.array([35, 25, 25, 15])
mylabels = ["Apples", "Bananas", "Cherries", "Dates"]
myexplode = np.array([0.2, 0, 0, 0])


plt.subplot(2, 2, 1)
plt.pie(y, labels = mylabels, startangle=90)


plt.subplot(2, 2, 2)
plt.pie(y, labels = mylabels, startangle=180)


plt.subplot(2, 2, 3)
plt.pie(y, labels = mylabels, explode=myexplode, shadow=True)


plt.subplot(2, 2, 4)
plt.pie(y, labels = mylabels, explode=myexplode, shadow=True)
plt.legend(title = "Four Fruits:")


plt.show()

with open("plot01.jpg", "wb") as f:
    plt.savefig(f)
