from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import random
global speed,height,width,size,starlist,animation_speed,pause
animation_speed = 25
speed = 1
height = 500
width = 500
size = 10
starlist = []
pause = False
class Star:
    def __init__(self,x,y):
        self.r = random.random()
        self.g = random.random()
        self.b = random.random()
        self.x = x
        self.y = y
        self.dir_x = random.choice([-1,1])
        self.dir_y = random.choice([-1,1])
    def star(self):
        global speed
        global size
        global pause
        glPointSize(size)
        glBegin(GL_POINTS)
        glColor(self.r, self.g, self.b)
        if pause == True:
            glVertex2f((self.x), (self.y))
            glEnd()
        else:
            glVertex2f((self.x+speed*self.dir_x),(self.y+speed*self.dir_y))
            glEnd()
            self.x,self.y = (self.x+speed*self.dir_x),(self.y+speed*self.dir_y)
            if self.x > width/2 or self.x < -width/2:
                self.dir_x = -self.dir_x
            if self.y > height/2 or self.y < -height/2:
                self.dir_y = -self.dir_y

def keyboardListener(key,x,y):
    global pause
    if key == b' ' and pause == True:
        pause = False
        print("Unpaused")
    elif key == b' ' and pause == False:
        pause = True
        print("Paused")

def specialKeyListener(key,x,y):
    global speed
    global pause
    if key == GLUT_KEY_UP and pause == False:
        speed += 0.1
        print("speed = ",speed)
    if key == GLUT_KEY_DOWN and pause == False:
        speed -= 0.1
        if speed < 0:
            speed = 0
        print("speed = ",speed)
def sizedown(value):
    global size
    global animation_speed
    global pause
    t = int(animation_speed/5)
    if size == 10:
        return
    if size < 1:
        glutTimerFunc(t,sizeup,0)
    else:
        size -= 0.1
        if pause == True:
            size += 0.1
        glutTimerFunc(t,sizedown,0)
def sizeup(value):
    global size
    global animation_speed
    global pause
    t = int(animation_speed / 5)
    if size == 10:
        return
    if size == 9:
        glutTimerFunc(t,sizedown,0)
    else:
        size += 0.1
        if pause == True:
            size -= 0.1
        glutTimerFunc(t,sizeup,0)
def mouseListener(button,state,x,y):
    global size
    global pause
    if button == GLUT_RIGHT_BUTTON and state == GLUT_DOWN and pause == False:
        x,y = convert_coordinate(x,y)
        starlist.append(Star(x,y))
    if button == GLUT_LEFT_BUTTON and state == GLUT_DOWN:
        if size == 10:
            size = 9
            glutTimerFunc(animation_speed, sizedown, 0)
        else:
            size = 10
    glutPostRedisplay()

def convert_coordinate(x,y):
    global width, height
    a = x - (width/2)
    b = (height/2) - y
    return a,b
def animate(value):
    global animation_speed
    glutPostRedisplay()
    glutTimerFunc(animation_speed,animate,0)
def display():

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glClearColor(0, 0, 0, 0);
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    glMatrixMode(GL_MODELVIEW)

    glLoadIdentity()

    gluLookAt(0, 0, 200, 0, 0, 0, 0, 1, 0)
    glMatrixMode(GL_MODELVIEW)
    for star in starlist:
        star.star()
    glutSwapBuffers()
def init():
    #//clear the screen
    glClearColor(0,0,0,0)
    #//load the PROJECTION matrix
    glMatrixMode(GL_PROJECTION)
    #//initialize the matrix
    glLoadIdentity()
    #//give PERSPECTIVE parameters
    gluPerspective(104,	1,	1,	1000.0)
glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(500, 500)
glutInitWindowPosition(0, 0)
wind = glutCreateWindow(b"OpenGL Coding Practice")
init()
glutDisplayFunc(display)
glutTimerFunc(animation_speed,animate,0)
glutKeyboardFunc(keyboardListener)
glutSpecialFunc(specialKeyListener)
glutMouseFunc(mouseListener)
glutMainLoop()