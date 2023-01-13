import csv

import matplotlib.pyplot as plt
import pysailing as psl
import numpy as np

from plotting import *


if __name__ == '__main__':

    params: psl.VelocityParameters

    with open("sailboats/Norlin_36_A_(SD).csv") as file:
        measurements = psl.VelocityMeasurements.from_csv(csv.reader(file, delimiter=';'))
        params = psl.VelocityParameters(measurements)

    ax = plt.subplot(projection='polar')

    degrees = np.linspace(0, 360)

    for (v, c) in zip(range(0, 21), rnd_colors()):
        knots = params[degrees, v]
        ax.plot(np.radians(degrees), knots, color=c, label=f'{v} knots')

    ax.set_theta_zero_location("N")

    ax.legend().set_draggable(True)

    plt.show()
