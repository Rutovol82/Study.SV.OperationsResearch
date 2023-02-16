import csv

import matplotlib.pyplot as plt
import pysailing as psl
import numpy as np

from plotting import *


#BOAT = 'Norlin 36 A (SD)'
#BOAT = "VOLVO OPEN 70"
#BOAT = "Maxi One 80"
#BOAT = "Maxi 72"
#BOAT = "WILKE 49"
BOAT = "Avance 24"

MIN_ANGLE = 0.1

WIND_COURSE_ANGLE = 8
WIND_KNOTS_SPEED = 11

DISPLAY_LEVELS = 50


def plot_polar_velocities(axis, parameters: psl.VelocityParameters):

    degrees = np.linspace(0, np.pi * 2)

    for (v, c) in zip(range(0, 21, 2), rnd_colors()):
        knots = parameters.getv(degrees, v)
        axis.plot(degrees, knots, color=c, label=f'{v} knots')

    axis.set_theta_zero_location("N")
    axis.legend(ncol=3).set_draggable(True)

    axis.set_title(f"BOAT: {BOAT}\n")


def plot_angeling_contourf(figure, axis, angleler: psl.AnglesComputer, entrance):

    d, r, t, best = angleler.scores(WIND_COURSE_ANGLE, WIND_KNOTS_SPEED, min_angle=MIN_ANGLE, entrance=entrance)

    levels = [best[-1] * num / 10 for num in range(10, DISPLAY_LEVELS)]
    cf = axis.contourf(d, r, t, levels=levels, cmap='YlGnBu')

    axis.set_xlabel("dep")
    axis.set_ylabel("ret")

    if entrance == 'right':
        figure.colorbar(cf, ax=axis, location='right')
    else:
        axis.yaxis.set_label_position('right')
        axis.yaxis.tick_right()
        figure.colorbar(cf, ax=axis, location='left')

    axis.set_title(f"CONDITIONS\n"
                   f"Wind: {WIND_COURSE_ANGLE} deg, {WIND_KNOTS_SPEED} knots\n"
                   f"BEST AT {entrance.upper()} ENTRANCE\n"
                   f"Entrance: {round(best[0], 3)} deg, Angle: {round(best[1], 3)}, Score: {round(best[-1], 3)}")


def main():

    params: psl.VelocityParameters

    with open(f"sailboats/{BOAT}.csv") as file:
        measurements = psl.VelocityMeasurements.from_csv(csv.reader(file, delimiter=';'))
        params = psl.VelocityParameters(measurements)
        computer = psl.AnglesComputer(params)

    fig = plt.figure()
    gs = plt.GridSpec(1, 3)

    ax1 = fig.add_subplot(gs[0, 0])
    ax2 = fig.add_subplot(gs[0, 1], projection='polar')
    ax3 = fig.add_subplot(gs[0, 2])

    plot_polar_velocities(ax2, params)
    plot_angeling_contourf(fig, ax1, computer, 'left')
    plot_angeling_contourf(fig, ax3, computer, 'right')

    fig.subplots_adjust(left=0.03, right=0.97, wspace=0.25)
    plt.show()


if __name__ == '__main__':
    main()
