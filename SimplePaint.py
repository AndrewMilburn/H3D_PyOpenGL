# Simple Paint.py

import math
import numpy as np

import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from Utils import  *

pygame.init()

screen_width= 1080
screen_height = 720

ortho_left = 0
ortho_right = 1080
ortho_bottom = 720
ortho_top = 0

points = []
lines = []

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
    print("Graphing")
    glBegin(GL_LINE_STRIP)
    px: GL_DOUBLE
    py: GL_DOUBLE
    for px in np.arange(0, 4, 0.005):
        py = math.exp(-px) * math.cos(2 * math.pi * px)
        glVertex2f(px, py)
    glEnd()

def save_drawing():
    f = open("drawing.txt", "w")
    f.write(str(screen_width) + " " + str(screen_height) + "\n")
    f.write(str(ortho_top) + " " + str(ortho_left) + " " +
            str(ortho_bottom) + " " + str(ortho_right) + "\n")
    f.write(str(len(lines)) + "\n")
    for l in lines:
        f.write(str(len(l)) + "\n")
        for p in l:
            f.write(str(p[0]) + " " + str(p[1]) + "\n")
    f.close()
    print("Drawing Saved")

def load_drawing():
    f = open("drawing.txt", "r")
    screen_width, screen_height = [int(entries) for entries in f.readline().split()]
    pygame.display.set_mode((screen_width, screen_height), DOUBLEBUF | OPENGL)
    print(str(screen_width) + " " + str(screen_height))
    ortho_top, ortho_left, ortho_bottom, ortho_right = [int(entries) for entries in next(f).split()]
    gluOrtho2D(ortho_left, ortho_right, ortho_top, ortho_bottom)
    print(str(ortho_top) + " " + str(ortho_left) + " " +
          str(ortho_bottom) + " " + str(ortho_right))
    num_lines = int(f.readline())
    global points
    global lines
    print(num_lines)
    lines = []
    for l in range(num_lines):
        points = []
        lines.append(points)
        num_points = int(f.readline())
        for point in range(num_points):
            x, y = [float(entry) for entry in next(f).split()]
            points.append((x, y))
            print(str(x) + ", " + str(y))


def clear_drawing():
    lines.clear()
    points.clear()

done = False
init_ortho()
glPointSize(5)

mouse_down = False

while not done:
    p = None
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s:
                save_drawing()
            elif event.key == pygame.K_l:
                load_drawing()
            elif event.key == pygame.K_SPACE:
                clear_drawing()
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
    #plot_graph()
    pygame.display.flip()
    #pygame.time.wait(100)
pygame.quit()
