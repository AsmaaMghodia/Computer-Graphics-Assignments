from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from math import *
import numpy as np
x=0
angle=0
y=0
z=1
def init():
    glMatrixMode(GL_PROJECTION)
    gluPerspective(60,1,0.1,50)
    gluLookAt(10,10,10,0,0,0,0,1,0)
    glClearColor(1,1,1,1)

def trees(x,xx):
    glColor(0,1,0)
    glLoadIdentity()
    glTranslate(xx-x,4,-4)
    glutSolidSphere(1,10,10)

    glColor3f(.7,.4,.4)
    glLoadIdentity()
    glTranslate(xx-x,2,-4)
    glScale(.3,2,.3)
    glutSolidCube(1)

    glLoadIdentity()
    glColor3f(1,0,0)
    for i in range (4,6,1):
        glTranslate(xx-x,i,-4)
        glutSolidSphere(.2,10,10)

def sphere(x,z):
    glColor3f(z,z,0)
    glLoadIdentity()
    glTranslate(x+2,-2.9*.25,-0.05)
    glutWireSphere(.25,10,10)

    glLoadIdentity()
    glTranslate(x+2,-2.9*.25,-1.4)
    glutWireSphere(.25,10,10)

def draw():
    global z
    global y
    global angle
    global x
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    glClear(GL_COLOR_BUFFER_BIT)

    glColor3f(0,0,0)
    glBegin(GL_POLYGON)
    glVertex3d(50-x,0,4)
    glVertex3d(-50-x,0,4)
    glVertex3d(-50-x,0,-4)
    glVertex3d(50-x,0,-4)
    glEnd()

    glColor3f(1,1,1)
    glBegin(GL_POLYGON)
    glVertex3d(2-x,0,1)
    glVertex3d(-2-x,0,1)
    glVertex3d(-2-x,0,.1)
    glVertex3d(2-x,0,.1)
    glEnd()

    glColor3f(1,1,1)
    glBegin(GL_POLYGON)
    glVertex3d(7-x,0,1)
    glVertex3d(4-x,0,1)
    glVertex3d(4-x,0,.1)
    glVertex3d(7-x,0,.1)
    glEnd()

    glColor3f(1,1,1)
    glBegin(GL_POLYGON)
    glVertex3d(11-x,0,1)
    glVertex3d(8-x,0,1)
    glVertex3d(8-x,0,.1)
    glVertex3d(11-x,0,.1)
    glEnd()

    glColor3f(1,1,1)
    glBegin(GL_POLYGON)
    glVertex3d(-13-x,0,1)
    glVertex3d(-10-x,0,1)
    glVertex3d(-10-x,0,.1)
    glVertex3d(-13-x,0,.1)
    glEnd()

    glColor3f(1,1,1)
    glBegin(GL_POLYGON)
    glVertex3d(-17-x,0,1)
    glVertex3d(-14-x,0,1)
    glVertex3d(-14-x,0,.1)
    glVertex3d(-17-x,0,.1)
    glEnd()

    glColor3f(1, 1, 1)
    glBegin(GL_POLYGON)
    glVertex3d(-21-x, 0, 1)
    glVertex3d(-18-x, 0, 1)
    glVertex3d(-18-x, 0, .1)
    glVertex3d(-21-x, 0, .1)
    glEnd()

    glColor3f(1,1,1)
    glBegin(GL_POLYGON)
    glVertex3d(-7-x,0,1)
    glVertex3d(-4-x,0,1)
    glVertex3d(-4-x,0,.1)
    glVertex3d(-7-x,0,.1)
    glEnd()

    glColor3f(1,1,1)
    glBegin(GL_POLYGON)
    glVertex3d(-11-x,0,1)
    glVertex3d(-8-x,0,1)
    glVertex3d(-8-x,0,.1)
    glVertex3d(-11-x,0,.1)
    glEnd()



    glColor3f(1,0,0)
    glTranslate(x,0,0)
    glScale(1,0.25,0.5)
    glutWireCube(5)

    glLoadIdentity()
    glTranslate(x,5*.25,0)

    glScale(0.5,0.25,0.5)
    glutWireCube(5)

    glColor3f(0,0,1)
    glLoadIdentity()
    glTranslate(x+2.5,-2.5*.25,-2.5*.5)
    glRotate(angle,0,0,1)

    glutWireTorus(0.25*.5,.5,10,10)

    glLoadIdentity()
    glTranslate(x+2.5,-2.5*.25,2.5*.5)
    glRotate(angle,0,0,1)

    glutWireTorus(0.25*.5,.5,10,10)

    glLoadIdentity()
    glTranslate(x-2.5,-2.5*.25,-2.5*.5)
    glRotate(angle,0,0,1)

    glutWireTorus(0.25*.5,.5,10,10)

    glLoadIdentity()
    glTranslate(x-2.5,-2.5*.25,2.5*.5)
    glRotate(angle,0,0,1)

    glutWireTorus(0.25*.5,.5,10,10)

    sphere(x,z)

    if (x>6.5):
        y=1
        x-=.01
        angle+=.2
    elif(x>-15 and y!=0):
        x-=.01
        angle+=.2
    elif(x<-15 ):
        y=0
        x+=.01
        angle-=.2
    else:
        x+=.01
        angle-=.2
    for n in range(-40,20,2):
        trees(x,n)

    glFlush()

glutInit()
glutInitDisplayMode(GLUT_SINGLE|GLUT_RGB)
glutInitWindowSize(600,600)
glutCreateWindow(b"......")
glutDisplayFunc(draw)
glutIdleFunc(draw)
init()

glutMainLoop()