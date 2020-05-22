import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *


def myPaint():
    glPushMatrix()
    #dodanie światła 
    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT2)
    glEnable(GL_DEPTH_TEST)
    glDrawBuffer(GL_BACK)
    glClear(GL_DEPTH_BUFFER_BIT)
    glPopMatrix()


verticies = (
    (1, -1, -1),
    (1, 1, -1),
    (-1, 1, -1),
    (-1, -1, -1),
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
    (5,7))

surfaces = (
    (0,1,2,3),
    (3,2,7,6),
    (6,7,5,4),
    (4,5,1,0),
    (1,5,7,2),
    (4,0,3,6)
    )
#kolory 
colors_serf = (( 1.0, 0.0, 0.0, 1.0), #czerwony 
( 1.0, 1.0, 0.0, 1.0), #żółty
( 1.0, 1.0, 1.0, 1.0), #biały
( 0.0, 1.0, 0.0, 1.0), #zielony
( 0.0, 1.0, 1.0, 1.0), #niebieski
( 1.0, 0.0, 0.0, 1.0)) #czerowny 

#stworzenie sześcianu
def Cube():
    glBegin(GL_QUADS)
    
    for surface in surfaces:
        x = 0
        for vertex in surface:
            #nałożenie kolorów
            glMaterialfv(GL_FRONT_AND_BACK, GL_AMBIENT,colors_serf[x])
            x+=1
            glVertex3fv(verticies[vertex])

    glEnd()

    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(verticies[vertex])
    glEnd()

def main():
    pygame.init()
    display = (800,600)
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)

    gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)

    glTranslatef(0.0,0.0, -5)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        glRotatef(1, 3, 1, 1)
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        myPaint()
        Cube()
        pygame.display.flip()
        pygame.time.wait(10)

main()