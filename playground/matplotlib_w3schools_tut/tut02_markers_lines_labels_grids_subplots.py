import numpy as np
import matplotlib 

matplotlib.use("agg")

from matplotlib import pyplot as plt

yp = np.array([3, 8, 1, 10])

"""
Markers:
'o'	Circle	
'*'	Star	
'.'	Point	
','	Pixel	
'x'	X	
'X'	X (filled)	
'+'	Plus	
'P'	Plus (filled)	
's'	Square	
'D'	Diamond	
'd'	Diamond (thin)	
'p'	Pentagon	
'H'	Hexagon	
'h'	Hexagon	
'v'	Triangle Down	
'^'	Triangle Up	
'<'	Triangle Left	
'>'	Triangle Right	
'1'	Tri Down	
'2'	Tri Up	
'3'	Tri Left	
'4'	Tri Right	
'|'	Vline	
'_'	Hline

Line Syntax :
'-'	Solid line	
':'	Dotted line	
'--'	Dashed line	
'-.'	Dashed/dotted line
'solid' (default)	'-'	
'dotted'	':'	
'dashed'	'--'	
'dashdot'	'-.'	
'None'	'' or ' '

Color Syntax:
'r'	Red	
'g'	Green	
'b'	Blue	
'c'	Cyan	
'm'	Magenta	
'y'	Yellow	
'k'	Black	
'w'	White
"""

plt.subplot(2, 2, 1)
plt.plot(yp, marker="*", mfc="r", mec="g", ms="20", ls=":", c="#FF0000")

plt.subplot(2, 2, 2)
plt.plot(yp, marker="*", mfc="r", mec="g", ms="20", linestyle="dashed", color="m", linewidth="10.5")

plt.subplot(2, 2, 3)
# marker|line|color
plt.plot(yp, "D--g")

x1 = np.array([0, 1, 2, 3])
y1 = np.array([3, 8, 1, 10])
x2 = np.array([0, 1, 2, 3])
y2 = np.array([6, 2, 7, 11])

#plt.subplot(2, 2, 4)
#plt.plot(x1, y1, x2, y2)

plt.subplot(2, 2, 4)
plt.plot(x1, y1, color="g", marker="D", ls="--")
plt.plot(x2, y2, c="r", marker="*", linestyle=":")

plt.title("Markers, Lines, Labels, Grids, Subplots", loc="center")
plt.xlabel("Average Pulse")
plt.ylabel("Calorie Burnage")

#plt.grid()
#plt.grid(axis="x")
#plt.grid(axis="y")
plt.grid(color="green", linestyle="--", linewidth="0.5")

plt.show()

with (open("plot01.jpg", "wb")) as f:
    plt.savefig(f)

