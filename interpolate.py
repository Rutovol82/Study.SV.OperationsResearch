import itertools

from scipy.interpolate import LinearNDInterpolator
from plotting import *
import matplotlib.pyplot as plt
import numpy as np

wind = [0, 6, 8, 10, 12, 14, 16, 20]

angles = [0, 52, 60, 75, 90, 110, 120, 135, 150]

src_ = [[0, 0, 0, 0, 0, 0, 0, 0],
        [0, 5.03, 5.89, 6.49, 6.77, 6.92, 7.01, 7.07],
        [0, 5.28, 6.16, 6.66, 6.91, 7.07, 7.19, 7.28],
        [0, 5.45, 6.33, 6.77, 7.02, 7.22, 7.39, 7.65],
        [0, 5.39, 6.35, 6.88, 7.09, 7.27, 7.48, 7.85],
        [0, 5.43, 6.51, 7.01, 7.33, 7.62, 7.79, 8.06],
        [0, 5.31, 6.39, 6.95, 7.3, 7.63, 7.95, 8.33],
        [0, 4.88, 5.93, 6.69, 7.09, 7.42, 7.78, 8.41],
        [0, 4.21, 5.21, 6.12, 6.75, 7.11, 7.42, 8.07]]

points_source_1 = list(itertools.chain(*([(x, y) for y in wind] for x in map(np.radians, angles))))
points_source_2 = [(np.pi * 2 - x, y) for (x, y) in points_source_1]

data_source = list(itertools.chain(*src_))

points = np.array(points_source_1 + points_source_2)
data = np.array(data_source + data_source)

interp = LinearNDInterpolator(points=points, values=data)
#print(interp(60, 10))

ax = plt.subplot(projection='polar')

degrees = np.linspace(0, np.pi * 2)

for (v, c) in zip(range(0, 21), rnd_colors()):
    knots = interp(degrees, v)
    ax.plot(degrees, knots, color=c, label=f'{v} knots')

ax.set_theta_zero_location("N")
ax.legend()
plt.show()
