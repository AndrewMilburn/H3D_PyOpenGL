# IFS.py

import pygame
import numpy as np
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from Utils import *

pygame.init()

screen_width = 800
screen_height = 800
ortho_left = -400
ortho_right = 400
ortho_top = -300
ortho_bottom = 500

screen = pygame.display.set_mode((screen_width, screen_height), DOUBLEBUF | OPENGL)
pygame.display.set_caption('Iterative Functions')
current_position = (0, 0)
current_direction = np.array([0, 1, 0])

axiom = 'X'
rules = {
        "F": "FF",
        "X": "F+[-F-XF-X][+FF][--XF[+X]][++F-X]"
        }
line_length = 5
angle = 25
stack = []
iterations = 5
instructions = ""
points = []
x_point = 0
y_point = 0


def run_rule(count):
    global instructions
    instructions = axiom
    for loops in range(count):
        old_system = instructions
        instructions = ""
        for c in range(0, len(old_system)):
            if old_system[c] in rules:
                instructions += rules[old_system[c]]
            else:
                instructions += old_system[c]
    print("Rule")
    print(instructions)


def init_ortho():
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(ortho_left, ortho_right, ortho_top, ortho_bottom)


def line_to(x_line, y_line):
    global current_position
    glBegin(GL_LINE_STRIP)
    glVertex2f(current_position[0], current_position[1])
    glVertex2f(x_line, y_line)
    current_position = (x_line, y_line)
    glEnd()


def move_to(pos):
    global current_position
    current_position = (pos[0], pos[1])


def reset_turtle():
    global current_position
    global current_direction
    current_position = (0, 0)
    current_direction = np.array([0, 1, 0])


def forward(draw_length):
    new_x = current_position[0] + current_direction[0] * draw_length
    new_y = current_position[1] + current_direction[1] * draw_length
    line_to(new_x, new_y)


def rotate(theta):
    global current_direction
    current_direction = z_rotation(current_direction, math.radians(theta))


def draw_turtle():
    global x_point, y_point
    points.append((x_point, y_point))
    r = np.random.rand()
    # if r < 0.1:
    #     x_point, y_point = 0.00 * x_point + 0.00 * y_point + 0.0, 0.00 * x_point + 0.16 * y_point + 0.0
    # elif r < 0.86:
    #     x_point, y_point = 0.85 * x_point + 0.04 * y_point + 0.0, -0.04 * x_point + 0.85 * y_point + 1.6
    # elif r < 0.93:
    #     x_point, y_point = 0.2 * x_point - 0.26 * y_point + 0.0, 0.23 * x_point + 0.22 * y_point + 0.44
    # else:
    #     x_point, y_point = -0.15 * x_point + 0.28 * y_point + 0.0, 0.26 * x_point + 0.24 * y_point + 0.44
    if r < 0.33:
        x_point, y_point = 0.50 * x_point + 0.00 * y_point + 0.0, 0.0 * x_point + 0.5 * y_point + 0.5
    elif r < 0.66:
        x_point, y_point = 0.5 * x_point + 0.0 * y_point + 0.5, -0.0 * x_point + 0.5 * y_point + 0
    else:
        x_point, y_point = 0.5 * x_point + 0.0 * y_point + 0.0, 0.0 * x_point + 0.5 * y_point + 0.00


def draw_points():
    glBegin(GL_POINTS)
    for p in points:
        glVertex2f(p[0], p[1])
    glEnd()


init_ortho()
done = False
glPointSize(2)
glColor3f(0, 1, 0)

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    glScaled(300, 300, 1)
    reset_turtle()
    draw_turtle()
    draw_points()
    pygame.display.flip()
    #pygame.time.wait(1)
pygame.quit()
