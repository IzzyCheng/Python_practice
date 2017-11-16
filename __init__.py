from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys

edge_list = [[129, 105]
,[129, 106]
,[128, 107]
,[129, 107]
,[121, 108]
,[129, 108]
,[107, 109]
,[137, 109]
,[107, 110]
,[138, 110]
,[107, 111]
,[135, 111]
,[106, 112]
,[139, 112]
,[106, 113]
,[137, 113]
,[106, 114]
,[137, 114]
,[106, 115]
,[138, 115]
,[105, 116]
,[139, 116]
,[105, 117]
,[138, 117]
,[105, 118]
,[138, 118]
,[105, 119]
,[139, 119]
,[105, 120]
,[139, 120]
,[105, 121]
,[139, 121]
,[105, 122]
,[139, 122]
,[105, 123]
,[139, 123]
,[105, 124]
,[138, 124]
,[105, 125]
,[139, 125]
,[105, 126]
,[137, 126]
,[105, 127]
,[139, 127]
,[105, 128]
,[139, 128]
,[105, 129]
,[138, 129]
,[106, 130]
,[139, 130]
,[105, 131]
,[139, 131]
,[105, 132]
,[139, 132]
,[105, 133]
,[139, 133]
,[105, 134]
,[139, 134]
,[105, 135]
,[139, 135]
,[105, 136]
,[139, 136]
,[105, 137]
,[139, 137]
,[105, 138]
,[139, 138]
,[105, 139]
,[139, 139]
,[105, 140]
,[138, 140]
,[108, 141]
,[138, 141]
,[108, 142]
,[138, 142]
,[108, 143]
,[137, 143]
,[109, 144]
,[135, 144]
,[110, 145]
,[136, 145]
,[111, 146]
,[136, 146]
,[112, 147]
,[134, 147]
,[112, 148]
,[133, 148]
,[117, 149]
,[131, 149]
,[0, 0]
,[0, 0]
,[0, 0]
,[0, 0]
,[0, 0]
,[0, 0]
,[0, 0]
,[0, 0]
,[0, 0]
,[0, 0]
,[0, 0]
,[0, 0]]



def init():
    glClearColor(1,1,1,1)
    gluOrtho2D(90,160,95,150)       #(-x, x, -y, y)

def plotpoints():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(0,0,0)
    glBegin(GL_LINE_LOOP)
    for i in range(0, 100, 1):
        if edge_list[i][0] <= 128 and edge_list[i][0] >= 105:   #if 105 <= y <= 128 then draw
            glVertex2f(edge_list[i][1], edge_list[i][0])
    for i in range(99, -1, -1):
        if edge_list[i][0] >= 129:
            glVertex2f(edge_list[i][1], edge_list[i][0])        #if y >= 129 then draw
    glEnd()
    glFlush()

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(500,350)
    glutInitWindowPosition(50,50)
    glutCreateWindow("Plot Points")
    glutDisplayFunc(plotpoints)
    init()
    glutMainLoop()

main()

"""
    x = 0.0
    while x <= 1.0:
        y = x**2            #y = x^2
        glBegin(GL_POINTS)
        glVertex2f(x, y)
        glVertex2f(-x, y)
        glVertex2f(x, -y)
        glVertex2f(-x, -y)
        glEnd()
        x += 0.001
        
    x = 0.0
    while x <= 1.0:
        y = math.sqrt(x)    #y = x^1/2
        glBegin(GL_POINTS)
        glVertex2f(x, y)
        glVertex2f(-x, y)
        glVertex2f(x, -y)
        glVertex2f(-x, -y)
        glEnd()
        x += 0.001
"""