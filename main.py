import csv

import matplotlib.pyplot as plt
import pysailing as psl
import numpy as np

from plotting import *


BOAT = 'Norlin_36_A_(SD)'
WIND_COURSE_ANGLE = 90
WIND_KNOTS_SPEED = 6


def plot_polar_velocities(axis, parameters: psl.VelocityParameters):
    degrees = np.linspace(0, 360)

    for (v, c) in zip(range(0, 21), rnd_colors()):
        knots = parameters[degrees, v]
        axis.plot(np.radians(degrees), knots, color=c, label=f'{v} knots')

    axis.set_theta_zero_location("N")
    axis.legend(ncol=7).set_draggable(True)

    axis.set_title(BOAT)


def plot_angeling_contourf(figure, axis, angleler: psl.AnglesComputer):
    d, a, t, best = angleler.scores(WIND_COURSE_ANGLE, WIND_KNOTS_SPEED)

    cf = axis.contourf(d, a, t, levels=[best[2] * num / 10 for num in range(10, 30)], cmap='YlGnBu')

    axis.set_xlabel("dep")
    axis.set_ylabel("ret")

    figure.colorbar(cf, ax=axis)

    axis.set_title(f"Angel(course, wind) = {WIND_COURSE_ANGLE} deg, Wind speed = {WIND_KNOTS_SPEED} knots")


if __name__ == '__main__':

    params: psl.VelocityParameters

    with open('sailboats/' + BOAT + '.csv') as file:
        measurements = psl.VelocityMeasurements.from_csv(csv.reader(file, delimiter=';'))
        params = psl.VelocityParameters(measurements)
        computer = psl.AnglesComputer(params)

    fig = plt.figure()
    gs = plt.GridSpec(1, 2)

    ax1 = fig.add_subplot(gs[0, 0])
    ax2 = fig.add_subplot(gs[0, 1], projection='polar')

    plot_polar_velocities(ax2, params)
    plot_angeling_contourf(fig, ax1, computer)

    plt.show()
