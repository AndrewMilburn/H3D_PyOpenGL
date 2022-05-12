# Polygons
#
# import math
import numpy as np

import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from Utils import *

pygame.init()

screen_width = 800
screen_height = 800
ortho_left = -400
ortho_right = 400
ortho_top = -400
ortho_bottom = 400

screen = pygame.display.set_mode((screen_width, screen_height), DOUBLEBUF | OPENGL)
pygame.display.set_caption('Polygons in PyOpenGL')


def init_ortho():
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(ortho_left, ortho_right, ortho_top, ortho_bottom)


def plot_polygon():
    glBegin(GL_QUAD_STRIP)
    glColor(0, 0, 1)
    for xy in points:
        glVertex2f(xy[0], xy[1])
    glEnd()

    glLineWidth(5)
    glColor(1, 0, 0)
    for i in np.arange(0, len(points) - 3, 2):
        glBegin(GL_LINE_LOOP)
        glVertex2f(points[i][0], points[i][1])
        glVertex2f(points[i + 1][0], points[i + 1][1])
        glVertex2f(points[i + 2][0], points[i + 2][1])
        glVertex2f(points[i + 3][0], points[i + 3][1])
        glEnd()


def clear_drawing():
    points.clear()


done = False
init_ortho()

points = []
while not done:
    p = None
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == MOUSEBUTTONDOWN:
            p = pygame.mouse.get_pos()
            points.append((map_value(0, screen_width, ortho_left, ortho_right, p[0]),
                           map_value(0, screen_height, ortho_bottom, ortho_top, p[1])))
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                clear_drawing()

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    plot_polygon()
    pygame.display.flip()
pygame.quit()
