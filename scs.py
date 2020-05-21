import sys

from pygame import *
import pygame
from pygame.locals import *

import OpenGL
from OpenGL.GL import *
from OpenGL.GLU import *

m_transX=0
m_transY=0
m_angle1=0
m_angle2=0
ArmPart=0
verticies = (
    (1, -1, -1),
    (1, 1, -1),
    (-1, 1, -1),
    (-1, -1,-1),
    (1, -1, 1),
    (1, 1, 1),
    (-1, -1, 1),
    (-1, 1, 1)
    )

edges = (
    (0,1),
    (0,3),
    (0,4),
    (2,1),
    (2,3),
    (2,7),
    (6,3),
    (6,4),
    (6,7),
    (5,1),
    (5,4),
    (5,7)
    )


def myPaint():
    glPushMatrix()
    glTranslated( m_transX, m_transY, 0)
    glRotated( m_angle1, 0, 0, 1)
    glPushMatrix()
    glTranslated( 90, 0, 0)
    glRotated( m_angle2, 0, 0, 1)
    glColor4f(0.0, 1.0, 0.0, 1.0)
    glCallList(ArmPart)
    glPopMatrix()
    glColor4f(1.0, 0.0, 0.0, 1.0)
    glCallList(ArmPart)
    glPopMatrix()

#main code
pygame.init()
display = (800,600)
pygame.display.set_mode(display, DOUBLEBUF|OPENGL)

gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)
gluOrtho2D(0.0, 500.0*(display[0]/display[1]), 0.0, 500.0)
glTranslatef(200.0,200.0, 0)

m_RightDownPos=(0,0)
m_LeftDownPos=(0,0)
m_RightButtonDown=False
m_LeftButtonDown=False

def Cube():
    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(verticies[vertex])
    glEnd()

ArmPart=glGenLists(1)
glNewList(ArmPart, GL_COMPILE)
Cube()
glEndList()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_q:
            pygame.quit()
            sys.exit(0)
        elif event.type == pygame.MOUSEMOTION:
            if m_LeftButtonDown:
                m_angle1 += m_LeftDownPos[0] - event.pos[0]
                m_angle2 += m_LeftDownPos[1] - event.pos[1]
                m_LeftDownPos = event.pos
            elif m_RightButtonDown:
                m_transX -= m_RightDownPos[0] - event.pos[0]
                m_transY += m_RightDownPos[1] - event.pos[1]
                m_RightDownPos = event.pos
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                m_LeftButtonDown = True
                m_LeftDownPos=event.pos
            elif event.button == 3:
                m_RightButtonDown = True
                m_RightDownPos=event.pos
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                m_LeftButtonDown = False
            elif event.button == 3:
                m_RightButtonDown = False
    #glRotatef(1, 3, 1, 1)
    
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    #Cube()
    myPaint()
    pygame.display.flip()
    pygame.time.wait(10)