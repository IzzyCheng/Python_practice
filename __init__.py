from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import math
import sys

def init():
    glClearColor(1,1,1,1)
    gluOrtho2D(-5,5,-5,5)       #(-x, x, -y, y)

def plotpoints():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(0,0,0)
    glBegin(GL_LINES)
    glVertex2f(-3, 0)
    glVertex2f(3, 0)
    glVertex2f(0, -3)
    glVertex2f(0, 3)
    glEnd()
    x = 0.0
    while x <= 1.0:
        y = x**2
        glBegin(GL_POINTS)
        glVertex2f(x, y)
        glVertex2f(-x, y)
        glVertex2f(x, -y)
        glVertex2f(-x, -y)
        glEnd()
        x += 0.001
        
    x = 0.0
    while x <= 1.0:
        y = math.sqrt(x)
        glBegin(GL_POINTS)
        glVertex2f(x, y)
        glVertex2f(-x, y)
        glVertex2f(x, -y)
        glVertex2f(-x, -y)
        glEnd()
        x += 0.001

    glFlush()

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(500,500)
    glutInitWindowPosition(50,50)
    glutCreateWindow("Plot Points")
    glutDisplayFunc(plotpoints)
    init()
    glutMainLoop()

main()
