import dicom
import numpy
import pylab
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys

"""Get edges"""
ds = dicom.read_file("dicom1.dcm")
for y in range(100, 150, 1):       #for y>105 and y<140, x>100 and x<155, pixel 180~70
    for x in range(105, 140, 1):
        if ds.pixel_array[x][y] >=70 and ds.pixel_array[x][y] <=180:
            ds.pixel_array[x][y] = 1000

def fill(x, y):
    ds.pixel_array[x][y] = 1000
    if ds.pixel_array[x-1][y] != 1000:
        fill(x-1, y)
    if ds.pixel_array[x+1][y] != 1000:
        fill(x+1, y)
    if ds.pixel_array[x][y-1] != 1000:
        fill(x, y-1)
    if ds.pixel_array[x][y+1] != 1000:
        fill(x, y+1)

fill(128, 128)
pylab.imshow(ds.pixel_array, cmap=pylab.cm.bone)
pylab.show()

i = 0
edge_list = numpy.zeros((100, 2))
for y in range(100, 150, 1):
    x = 128
    if ds.pixel_array[x][y] == 1000:            #if (x,y)is white find higher pixel
        while ds.pixel_array[x-1][y] == 1000:   #find the highest pixel
            x -= 1
        edge_list[i][0] = x                     #record in edge_list
        edge_list[i][1] = y
        i += 1
    x = 129
    if ds.pixel_array[x][y] == 1000:            #if (x,y)is white find lower pixel
        while ds.pixel_array[x+1][y] == 1000:   #find the lowest pixel
            x += 1
        edge_list[i][0] = x                     #record in edge_list
        edge_list[i][1] = y
        i += 1
temp = "[[%d, %d]" %(edge_list[0][0], edge_list[0][1])
print(temp)
for i in range(1, 99, 1):
    temp = ",[%d, %d]" %(edge_list[i][0], edge_list[i][1])
    print(temp)
temp = ",[%d, %d]]" %(edge_list[99][0], edge_list[99][1])
print(temp)
#rint(edge_list)

"""Draw edges"""
"""
def init():
    glClearColor(1,1,1,1)
    gluOrtho2D(80, 170, 85, 160)       #(-x, x, -y, y)
    
def plotpoints():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(0,0,0)
    glBegin(GL_LINE_LOOP)
    glVertex2f(100, 105)
    glVertex2f(150, 105)
    glVertex2f(100, 140)
    glVertex2f(150, 140)
    for i in range(0, 99, 1):
        if edge_list[i][0] <= 128 and edge_list[i][0] >= 105:   #if 105 <= y <= 128 then draw
            glVertex2f(edge_list[i][1], edge_list[i][0])
    for i in range(99, 0, -1):
        if edge_list[i][0] >= 129:
            glVertex2f(edge_list[i][1], edge_list[i][0])        #if y >= 129 then draw
    glEnd()
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
"""