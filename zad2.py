import sys

from pygame import *
import pygame
from pygame.locals import *
import numpy as np
import OpenGL
from OpenGL.GL import *
from OpenGL.GLU import *

def myPaint():
    glBegin(GL_POLYGON)
    glColor4f(0.0,0.0,1.0,1.0)
    glVertex2f(50.0,25.0)
    glColor4f(0.0,0.0,1.0,1.0)
    glVertex2f(225.0,225.0)
    glColor4f(0.0,0.0,1.0,1.0)
    glVertex2f(225.0,25.0)
    glEnd()

pygame.init()
display = (800,600)
pygame.display.set_mode(display,DOUBLEBUF|OPENGL)

gluOrtho2D(0.0, 500.0*(display[0]/display[1]), 0.0, 500.0);

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    myPaint()
    pygame.display.flip()
    pygame.time.wait(10)

