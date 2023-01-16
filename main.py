import csv

import matplotlib.pyplot as plt
import pysailing as psl
import numpy as np

from plotting import *


#BOAT = 'Norlin 36 A (SD)'
#BOAT = "VOLVO OPEN 70"
BOAT = "Maxi One 80"

MIN_ANGLE = 0.1

WIND_COURSE_ANGLE = 360
WIND_KNOTS_SPEED = 11

DISPLAY_LEVELS = 50


def plot_polar_velocities(axis, parameters: psl.VelocityParameters):
    degrees = np.linspace(0, np.pi * 2)

    for (v, c) in zip(range(0, 21, 2), rnd_colors()):
        knots = parameters.getv(degrees, v)
        axis.plot(degrees, knots, color=c, label=f'{v} knots')

    axis.set_theta_zero_location("N")
    axis.legend(ncol=1).set_draggable(True)

    axis.set_title(f"BOAT: {BOAT}\n")


def plot_angeling_contourf(figure, axis, angleler: psl.AnglesComputer):

    d, r, t, best = angleler.scores(WIND_COURSE_ANGLE, WIND_KNOTS_SPEED, min_angle=MIN_ANGLE)

    levels = [best[-1] * num / 10 for num in range(10, DISPLAY_LEVELS)]
    cf = axis.contourf(d, r, t, levels=levels, cmap='YlGnBu')

    axis.set_xlabel("dep")
    axis.set_ylabel("ret")

    figure.colorbar(cf, ax=axis)

    axis.set_title(f"CONDITIONS\n"
                   f"Wind: {WIND_COURSE_ANGLE} deg, {WIND_KNOTS_SPEED} knots\n"
                   f"BEST\n"
                   f"Entrance: {round(best[0], 3)} deg, Angle: {round(best[1], 3)}, Score: {round(best[-1], 3)}")


if __name__ == '__main__':

    params: psl.VelocityParameters

    with open(f"sailboats/{BOAT}.csv") as file:
        measurements = psl.VelocityMeasurements.from_csv(csv.reader(file, delimiter=';'))
        params = psl.VelocityParameters(measurements)
        computer = psl.AnglesComputer(params)

    fig = plt.figure()
    gs = plt.GridSpec(1, 2)

    ax1 = fig.add_subplot(gs[0, 0], projection='polar')
    ax2 = fig.add_subplot(gs[0, 1])

    plot_polar_velocities(ax1, params)
    plot_angeling_contourf(fig, ax2, computer)

    plt.show()
