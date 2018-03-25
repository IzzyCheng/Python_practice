import dicom
import numpy
import pylab
import matplotlib.pyplot as plt
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys
from matplotlib.animation import adjusted_figsize
from operator import indexOf
from bdb import bar

ds = dicom.read_file("dicom20.dcm")
#ylab.imshow(ds.pixel_array, cmap=pylab.cm.bone)
#pylab.show()

#change ds from 2d-array to 1d-array
data = ds.pixel_array[0]
for i in range(1, 256, 1):
    data = numpy.hstack((data, ds.pixel_array[i]))

#count the number of pixel value at x=100~170, y=100~170
numb = numpy.zeros(1200)
for x in range(100, 161, 1):
    for y in range(100, 161, 1):
        numb[ds.pixel_array[y][x]] +=1

#count 10(1%) numb data into a bar
width = 10
length = 1200/width
bar = numpy.zeros(length)
for i in range(0, length, 1):
    for j in range(0, width, 1):
        bar[i] += numb[i*width+j]


volume = [1169, 1091, 1011, 903, 811, 747, 709, 705, 739, 859, 979, 1052, 1121, 1151, 1163, 1154, 1171, 1223, 1247, 1217]
volume = numpy.tile(volume, 3)
plt.plot(volume)
plt.show()

#print the two chart
'''
numb_x = 300
numb_y = 100
f, axarr = plt.subplots(2)
axarr[0].plot(numb, 'r-')
axarr[0].axis([0, numb_x, 0, numb_y])
axarr[0].set_title('Original counts of value(0~300)')
axarr[0].set_ylabel('count')
axarr[1].plot(bar)
axarr[1].axis([0, numb_x/width, 0, numb_y*width])
axarr[1].set_title('Sum every '+str(width)+' data')
axarr[1].set_ylabel('count')
plt.show()
'''

#find start and end of white range
start=0
end=0
top = max(bar)
for i in range(indexOf(bar, top), 119, 1):
    if bar[i] < bar[i+1]:
        start = i
        break
    else:
        start = -1
second_top = 0
index = 0
for i in range(15, 119, 1):    #find the max of rest bar
    if bar[i]>second_top:
        second_top=bar[i]
        index = i
min = bar[index]
for i in range(index, start-1, -1): #find the min between two peak
    if bar[i-1]<min:
        min = bar[i-1]
        end = i-1

if start >0 and end >0:
    print(start, end)
else:
    print(start, end)
    print("start & end not found")
    exit()

#draw to white(1000)
start = 4
end = 13
for y in range(0, 256, 1):
    for x in range(0, 256, 1):
        if ds.pixel_array[x][y] >= start*10 and ds.pixel_array[x][y]<= (end+1)*10:
            ds.pixel_array[x][y] = 1000
pylab.imshow(ds.pixel_array, cmap=pylab.cm.bone)
pylab.show()

#find edge and count volume
e=0
p=0
volume=0
edge_list = numpy.zeros((400, 2))
passed = numpy.zeros((3000, 2))
def getedge(x, y):
    global e, p, volume
    exist = 0
    for i in range(0, 3000, 1):
        if passed[i][0] == x and passed[i][1] == y:
            exist = 1
    if exist != 1:      #haven't pass
        passed[p][0] = x
        passed[p][1] = y
        p+=1
        volume+=1
        if (ds.pixel_array[x-1][y]<1000 and ds.pixel_array[x+1][y]<1000 and ds.pixel_array[x][y-1]<1000 and ds.pixel_array[x][y+1]<1000 and \
        ds.pixel_array[x-1][y-1]<1000 and ds.pixel_array[x-1][y+1]<1000 and ds.pixel_array[x+1][y-1]<1000 and ds.pixel_array[x+1][y+1]<1000):
            getedge(x-1, y)
            getedge(x+1, y)
            getedge(x, y-1)
            getedge(x, y+1)
            getedge(x-1, y-1)
            getedge(x-1, y+1)
            getedge(x+1, y-1)
            getedge(x+1, y+1)
        else:           #touch the edge
            exist = 0
            for i in range(0, 400, 1):      #double check edge
                if edge_list[i][0] == x and edge_list[i][1] == y:
                    exist = 1
            if exist != 1:
                edge_list[e][0] = x
                edge_list[e][1] = y
                e+=1


sys.setrecursionlimit(10000)
getedge(140, 130)


temp = "[[%d, %d]" %(edge_list[0][0], edge_list[0][1])
print(temp)
for i in range(1, 399, 1):
    temp = ",[%d, %d]" %(edge_list[i][0], edge_list[i][1])
    print(temp)
temp = ",[%d, %d]]" %(edge_list[399][0], edge_list[399][1])
print(temp)
print(volume)


