#!/usr/bin/python3

import sys
import pygame
from pygame.locals import *
import OpenGL
from OpenGL.GL import *
from OpenGL.GLU import *

def triangle(l: list, c: list):
    glBegin(GL_TRIANGLE_STRIP)
    glColor3f(c[0], c[1], c[2])
    glVertex2f(l[0][0], l[0][1])
    glVertex2f(l[1][0], l[1][1])
    glVertex2f(l[2][0], l[2][1])
    glEnd()


def myPaint():
    glPushMatrix()
    for i in range(4):
        triangle([[0,0],[0,1],[1,0]], [0, 0, 1])
        triangle([[1,0],[1,1],[2,0]], [1, 0.5, 0])
        triangle([[2,0],[2,1],[3,0]], [1, 0.11, 0.81])
        triangle([[0,1],[0,2],[1,1]], [0.4, 1, 0])
        triangle([[1,1],[1,2],[2,1]], [1, 1, 0])
        triangle([[0,3],[1,2],[0,2]], [1, 0, 0])
        glRotated(-90, 0, 0, 1)
    glPopMatrix()

pygame.init()
display = (800,600)
pygame.display.set_mode(display, DOUBLEBUF|OPENGL)
# gluOrtho2D(45, (display[0]/display[1]), 0.0, 50.0)
gluPerspective(45, (display[0]/display[1]), 0.1, 50)
glTranslatef(0.0,0.0, -10)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_q:
            pygame.quit()
            sys.exit(0)
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)

    myPaint()
    pygame.display.flip()
    pygame.time.wait(10)