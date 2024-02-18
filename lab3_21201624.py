from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import random
global pause,speed,origin
origin = []
speed = 25
pause = False

def draw_circle():
    global origin,pause
    for i in origin:
        glColor3f(random.random(),random.random(),random.random())
        x0,y0,r = i[0], i[1], i[2]
        x_min = x0 - r
        x_max = x0 + r
        y_min = y0 - r
        y_max = y0 + r
        if x_min > 0 and x_max < 600:
            if y_min > 0 and y_max < 600:
                circle_algo(x0,y0,r)
            
def circle_algo(x0,y0,r):
    d = 1 - r
    x = 0
    y = r
    while x < y:
        circle_zones(x, y, x0, y0)
        if d >= 0:
            d = d + 2*x - 2*y + 5
            x += 1
            y -= 1
        else:
            d = d + 2*x + 3
            x += 1
        
def convert_coordinate(x,y):
    return x, 600-y

def circle_zones(x, y, x0, y0): #x,y are points generated and x0,y0 is the origin of circle
    glVertex2f(x + x0, y + y0)
    glVertex2f(y + x0, x + y0)
    glVertex2f(y + x0, -x + y0)
    glVertex2f(x + x0, -y + y0)
    glVertex2f(-x + x0, -y + y0)
    glVertex2f(-y + x0, -x + y0)
    glVertex2f(-y + x0, x + y0)
    glVertex2f(-x + x0, y + y0)

def keyboardListener(key,x,y):
    global pause
    if key == b' ':
        if pause == True:
            pause = False
        else:
            pause = True
    glutPostRedisplay()

def specialKeyListener(key,x,y):
    global speed
    if key == GLUT_KEY_DOWN:
        speed += 1
    if key == GLUT_KEY_UP:
        speed -= 1
        if speed < 0:
            speed = 0
    print(speed)
    glutPostRedisplay()
    
def mouseListener(button,state,x,y):
    global origin
    if button == GLUT_RIGHT_BUTTON and state == GLUT_DOWN:
        x,y = convert_coordinate(x,y)
        origin.append((x,y,3))

def animate(value):
    global speed,pause,origin
    glutPostRedisplay()
    if pause == True:
        glutTimerFunc(speed,animate,0)
    else:
        for i in range(len(origin)):
            x,y,r = origin[i][0],origin[i][1],origin[i][2] + 1
            origin[i] = (x,y,r)
        glutTimerFunc(speed,animate,0)

def iterate():
    glViewport(0, 0, 600, 600)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 600, 0.0, 600, 0.0, 1.0)
    glMatrixMode (GL_MODELVIEW)
    glLoadIdentity()
    
def showScreen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    iterate()
    glBegin(GL_POINTS)
    glColor3f(random.random(),random.random(),random.random())
    draw_circle()
    glEnd()
    glutSwapBuffers()
    
glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(600, 600) #window size
glutInitWindowPosition(0, 0)
wind = glutCreateWindow(b"OpenGL Coding Practice") #window name
glutDisplayFunc(showScreen)
glutTimerFunc(speed,animate,0)
glutKeyboardFunc(keyboardListener)
glutSpecialFunc(specialKeyListener)
glutMouseFunc(mouseListener)
glutMainLoop()