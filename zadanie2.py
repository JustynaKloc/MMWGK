import sys
import pygame
from pygame.locals import *
import OpenGL
from OpenGL.GL import *
from OpenGL.GLU import *

def t_blue():
    glBegin(GL_TRIANGLE_STRIP)   
    glColor3f(0, 0, 1)
    glVertex2f(0,0)
    glVertex2f(0,1)
    glVertex2f(1,0)
    glEnd()

def t_orange():
    glBegin(GL_TRIANGLE_STRIP)
    glColor3f(1, 0.5, 0)
    glVertex2f(1,0)
    glVertex2f(1,1)
    glVertex2f(2,0)
    glEnd()

def t_pink():
    glBegin(GL_TRIANGLE_STRIP)
    glColor3f(1, 0.11, 0.81)
    glVertex2f(2,0)
    glVertex2f(2,1)
    glVertex2f(3,0)
    glEnd()

def t_green():
    glBegin(GL_TRIANGLE_STRIP)
    glColor3f(0.4, 1, 0)
    glVertex2f(0,1)
    glVertex2f(0,2)
    glVertex2f(1,1)
    glEnd()

def t_yellow():
    glBegin(GL_TRIANGLE_STRIP)
    glColor3f(1, 1, 0)
    glVertex2f(1,1)
    glVertex2f(1,2)
    glVertex2f(2,1)
    glEnd()

def t_red():
    glBegin(GL_TRIANGLE_STRIP)
    glColor3f(1, 0, 0)
    glVertex2f(0,3)
    glVertex2f(1,2)
    glVertex2f(0,2)
    glEnd()

m1 = [[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]]
m2 = [[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]]
m3 = [[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]]

def myPaint():
    global m1
    global m2
    glPushMatrix()
    glLoadMatrixf(m1)
    glRotatef(-1.5,0,0,1)
    m1 = glGetFloatv(GL_MODELVIEW_MATRIX)
    glPopMatrix()

    glPushMatrix()
    glLoadMatrixf(m2)
    #(1*3)/(360*10) - w tym wypadku 1 oznacza długość przyprostokątnej, 360 - pełen obrót, 10 - ilość obrotów zadana w zadaniu
    glTranslatef((1*3)/(360*10), (1*3)/(360*10), 0)
    m2 = glGetFloatv(GL_MODELVIEW_MATRIX)
    glPopMatrix()

    glMatrixMode(GL_MODELVIEW)
    for i in range(4):
        glPushMatrix()
        glMultMatrixf(m1)
        glPushMatrix()
        glMultMatrixf(m2)
        t_blue() 
        t_orange() 
        t_green()
        glPopMatrix()
        glPopMatrix()
        glRotated(-90, 0, 0, 1)
    
    glPushMatrix()
    for i in range(4):
        t_yellow()
        t_red()
        t_pink()
        glRotated(-90, 0, 0, 1)
    glPopMatrix()

pygame.init()
display = (800,600)
pygame.display.set_mode(display, DOUBLEBUF|OPENGL)
gluPerspective(45, (display[0]/display[1]), 0.1, 50)
glTranslatef(0.0,0.0, -10)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_q:
            pygame.quit()
            sys.exit(0)
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    glMatrixMode(GL_MODELVIEW)
    glPushMatrix()
    glLoadMatrixf(m3)
    glRotatef(0.5,0,0,1)
    m3 = glGetFloatv(GL_MODELVIEW_MATRIX)
    glPopMatrix()
    glPushMatrix()
    glMultMatrixf(m3)
    myPaint()
    glPopMatrix()
    pygame.display.flip()
    pygame.time.wait(10)