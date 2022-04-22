# LinePlot.py

import math
import numpy as np

import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from Utils import  *

pygame.init()

screen_width = 1000
screen_height = 800
# ortho_width = 640
# ortho_height = 480


ortho_left = 0
ortho_right = 4
ortho_bottom = 1
ortho_top = -1


screen = pygame.display.set_mode((screen_width, screen_height), DOUBLEBUF | OPENGL)
pygame.display.set_caption('Lines in PyOpenGL')


def init_ortho():
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    # gluOrtho2D(0, ortho_width, 0, ortho_height)
    gluOrtho2D(ortho_left, ortho_right, ortho_top , ortho_bottom)


def plot_point():
    glBegin(GL_POINTS)
    for p in points:
        glVertex2f(p[0], p[1])
    glEnd()


def plot_line():
    for l in lines:
        glBegin(GL_LINE_STRIP)
        for p in l:
            glVertex2f(p[0], p[1])
        glEnd()

def plot_graph():
    glBegin(GL_LINE_STRIP)
    px: GL_DOUBLE
    py: GL_DOUBLE
    for px in np.arange(0, 4, 0.005):
        py = math.exp(-px) * math.cos(2 * math.pi * px)
        glVertex2f(px, py)
    glEnd()

done = False
init_ortho()
glPointSize(5)
points = []
lines = []
mouse_down = False

while not done:
    p = None
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == MOUSEMOTION and mouse_down:
            p = pygame.mouse.get_pos()
            points.append((map_value(0, screen_width, ortho_left, ortho_right, p[0]),
                          map_value(0, screen_height, ortho_bottom, ortho_top, p[1])))
        elif event.type == MOUSEBUTTONDOWN:
            mouse_down = True
            points = []
            lines.append(points)
        elif event.type == MOUSEBUTTONUP:
            mouse_down = False



    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    plot_line()
    plot_graph()
    pygame.display.flip()
    #pygame.time.wait(100)
pygame.quit()