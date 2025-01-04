from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import random
from math import sin, cos, pi
global angle
global day
angle = 0
day = 0
speed = 0.01
def draw_house():
    #House
    glBegin(GL_QUADS)
    glColor3f(1.0,0,0)
    glVertex2f(370,500)
    glColor3f(1.0, 0, 0)
    glVertex2f(630, 500)
    glColor3f(1.0, 0, 0)
    glVertex2f(630, 300)
    glColor3f(1.0, 0, 0)
    glVertex2f(370, 300)
    glEnd()
    #Door
    glBegin(GL_QUADS)
    glColor3f(1.0, 1.0, 0)
    glVertex2f(400, 430)
    glColor3f(1.0, 1.0, 0)
    glVertex2f(500, 430)
    glColor3f(1.0, 1.0, 0)
    glVertex2f(500, 300)
    glColor3f(1.0, 1.0, 0)
    glVertex2f(400, 300)
    glEnd()
    glBegin(GL_LINES)
    glColor3f(0,0,0)
    glVertex2f(450,430)
    glColor3f(0, 0, 0)
    glVertex2f(450,300)
    glEnd()
    glPointSize(5)
    glBegin(GL_POINTS)
    glColor3f(1, 0, 1)
    glVertex2f(450, 365)
    glEnd()

    #Window
    glBegin(GL_QUADS)
    glColor3f(1.0, 1.0, 0)
    glVertex2f(550, 450)
    glColor3f(1.0, 1.0, 0)
    glVertex2f(600, 450)
    glColor3f(1.0, 1.0, 0)
    glVertex2f(600, 400)
    glColor3f(1.0, 1.0, 0)
    glVertex2f(550, 400)
    glEnd()
    glBegin(GL_LINES)
    glColor3f(0, 0, 0)
    glVertex2f(575, 450)
    glColor3f(0, 0, 0)
    glVertex2f(575, 400)
    glEnd()
    glBegin(GL_LINES)
    glColor3f(0, 0, 0)
    glVertex2f(550, 425)
    glColor3f(0, 0, 0)
    glVertex2f(600, 425)
    glEnd()
    #Roof
    glBegin(GL_TRIANGLES)
    glColor3f(0.5,0.3,0.1)
    glVertex2f(300, 500)
    glColor3f(0.706, 0.537, 0.302)
    glVertex2f(500, 600)
    glColor3f(0.706, 0.537, 0.302)
    glVertex2f(700, 500)
    glEnd()
    #Base
    glBegin(GL_QUADS)
    glColor3f(0.6,0.4,0.2)
    glVertex2f(370, 300)
    glColor3f(0.706, 0.537, 0.302)
    glVertex2f(630, 300)
    glColor3f(0.706, 0.537, 0.302)
    glVertex2f(680, 275)
    glColor3f(0.6,0.4,0.2)
    glVertex2f(320, 275)
    glEnd()

def Day():
    glutPostRedisplay()
    global day, speed
    if day != 1:
        day += speed
def Night():
    glutPostRedisplay()
    global day, speed
    if day != 0:
        day -= speed
def sky():
    global day
    day = abs(day)
    if day > 0.5:
        day = 0.5
    glBegin(GL_QUADS)
    glColor3f(day+0.1, day+0.1, day+0.4)
    glVertex2f(0, 1000)
    glVertex2f(1000, 1000)
    glVertex2f(1000, 0)
    glVertex2f(0, 0)
    glEnd()
def draw_land():
    #ground
    glBegin(GL_QUADS)
    glColor3f(0.8, 0.6, 0.4)
    glVertex2f(0, 350)
    glColor3f(0.8, 0.6, 0.4)
    glVertex2f(1000, 350)
    glColor3f(0.8, 0.6, 0.4)
    glVertex2f(1000, 0)
    glColor3f(0.8, 0.6, 0.4)
    glVertex2f(0, 0)
    glEnd()
    #grass
    for i in range(1,21):
        x = i*50
        y = [200,50,75,150,15,175,100,125,160,77,90,140,40,220,35]
        for j in range(6):
            glBegin(GL_TRIANGLES)
            glColor3f(0.01,0.02,0.01)
            glVertex2f(x, y[i%15])
            glColor3f(0,1,0)
            glVertex2f(x+random.randint(-30,30),y[i%15]+random.randint(25,50) )
            glColor3f(0.01,0.02,0.01)
            glVertex2f(x+15, y[i%15])
            glEnd()

def draw_rain():
    global angle
    for i in range(1,1000,20):
        for j in range(1,1000,40):
            glBegin(GL_LINES)
            glColor3f(0,0,0.8)
            glVertex2f(i + angle,j)
            glColor3f(0.3, 0.3, 1.0)
            glVertex2f(i , j + random.randint(20, 30))
            glEnd()

def draw_text(text):
    glRasterPos2f(10, 300)
    for char in text:
        glutBitmapCharacter(GLUT_BITMAP_HELVETICA_18, ord(char))



def iterate():
    glViewport(0, 0, 1000, 800)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 1000, 0.0, 800, 0.0, 1.0)
    glMatrixMode (GL_MODELVIEW)
    glLoadIdentity()

def keyboardListener(key, x, y):
    global day
    if key==b'd':
        day = 0
        glutIdleFunc(Day)
        print("Day Time")
    if key==b'n':
        day = 1
        glutIdleFunc(Night)
        print("Night Time")


def specialKeyListener(key, x, y):
    global angle
    if key==GLUT_KEY_RIGHT:
        angle += 1.5
        print("Rain Direction and Wind Speed Changed")
    if key== GLUT_KEY_LEFT:
        angle -= 1.5
        print("Rain Direction and Wind Speed Changed")
    glutPostRedisplay()
def showScreen():
    global angle
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    iterate()
    sky()
    draw_rain()
    draw_land()
    draw_house()
    glColor3f(0, 0, 1.0)
    if angle > 0:
        direction = "->"
    elif angle < 0:
        direction = "<-"
    else:
        direction = "!"
    draw_text("Direction = " + direction +", Speed = "+str(abs(angle))+" MPH")
    glutSwapBuffers()



glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(1000, 700)
glutInitWindowPosition(0, 0)
wind = glutCreateWindow(b"OpenGL Coding Practice")
glutDisplayFunc(showScreen)
glutKeyboardFunc(keyboardListener)
glutSpecialFunc(specialKeyListener)
glutMainLoop()