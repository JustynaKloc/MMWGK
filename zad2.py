
import sys
import pygame
from pygame.locals import *
import OpenGL
from OpenGL.GL import *
from OpenGL.GLU import *

def myPaint():
    glPushMatrix()
    for i in range(4):
        glBegin(GL_TRIANGLE_STRIP)
        glColor3f(0, 0, 1)
        glVertex2f(0,0)
        glVertex2f(0,1)
        glVertex2f(1,0)
        glEnd()
        glBegin(GL_TRIANGLE_STRIP)
        glColor3f(1, 0.5, 0)
        glVertex2f(1,0)
        glVertex2f(1,1)
        glVertex2f(2,0)
        glEnd()
        glBegin(GL_TRIANGLE_STRIP)
        glColor3f(1, 0.11, 0.81)
        glVertex2f(2,0)
        glVertex2f(2,1)
        glVertex2f(3,0)
        glEnd()
        glBegin(GL_TRIANGLE_STRIP)
        glColor3f(0.4, 1, 0)
        glVertex2f(0,1)
        glVertex2f(0,2)
        glVertex2f(1,1)
        glEnd()
        glBegin(GL_TRIANGLE_STRIP)
        glColor3f(1, 1, 0)
        glVertex2f(1,1)
        glVertex2f(1,2)
        glVertex2f(2,1)
        glEnd()
        glBegin(GL_TRIANGLE_STRIP)
        glColor3f(1, 0, 0)
        glVertex2f(0,3)
        glVertex2f(1,2)
        glVertex2f(0,2)
        glEnd()
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