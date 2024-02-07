from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import random

W_Width, W_Height = 500,500
rain_angle = 0
light = 0.2     # blue value of sky
day = 0         # green value of sky
animation_speed = 0.0006


def animate_today():
    glutPostRedisplay()
    global light, day
    # Increase light to 1 first then day
    if light < 1:
        light += animation_speed
    elif day < 0.8:
        day += animation_speed

def animate_tonight():
    glutPostRedisplay()
    global light, day
    # Decrease day to 0 first then light to 0
    if day > 0:
        day -= animation_speed
    elif light > 0:
        light -= animation_speed

def keyboardListener(key, x, y):
    if key==b'w':
        glutIdleFunc(animate_today)
    if key==b's':
        glutIdleFunc(animate_tonight)

    # glutPostRedisplay()

def specialKeyListener(key, x, y):
    global rain_angle
    if key==GLUT_KEY_RIGHT:
        rain_angle += 10
        print(rain_angle)
    elif key==GLUT_KEY_LEFT:
        rain_angle -= 10
        print(rain_angle)

    glutPostRedisplay()

def draw_bg():
    global light
    global day
    glBegin(GL_QUADS)
    # Land
    glColor3f(0, 0.5, 0)
    glVertex2d(-250, -30)
    glVertex2d(250, -30)
    glVertex2d(250, -250)
    glVertex2d(-250, -250)

    # Sky
    glColor3f(0, day, light)
    glVertex2d(-250, -30)
    glVertex2d(250, -30)
    glVertex2d(250, 250)
    glVertex2d(-250, 250)

    glEnd()



def draw_rain():
    global rain_angle
    for i in range(-250, 260, 20):
        for j in range(10, 260, 50):
            glBegin(GL_LINES)
            glColor3f(0.2, 0.4, 1)
            rain_len = random.randint(10, 20)
            # To make sure each rain drop starts and ends at random points
            glVertex2d(i + rain_angle, j - rain_len)
            glVertex2d(i, j + rain_len)
            glEnd()


def draw_house():
    draw_bg()
    draw_rain()


    glBegin(GL_TRIANGLES)
    shift_tr1_x = 120
    shift_tr2_x = -120
    shift_tr3_y = 40

    shift_tr4_y = 50

    # Small triangle 1
    glColor3f(1, 0, 0.0)
    glVertex2d(-35+shift_tr1_x, 0)
    glColor3f(1, 0, 0.0)
    glVertex2d(0+shift_tr1_x, 50)
    glColor3f(1, 1, 0.0)
    glVertex2d(35+shift_tr1_x, 0)

    # Small triangle 2
    glColor3f(1, 0, 0.0)
    glVertex2d(-35+shift_tr2_x, 0)
    glColor3f(1, 0, 0.0)
    glVertex2d(0+shift_tr2_x, 50)
    glColor3f(1, 1, 0.0)
    glVertex2d(35+shift_tr2_x, 0)

    # Big triangle 1
    glColor3f(1, 0, 0.0)
    glVertex2d(-95, 0+shift_tr3_y)
    glColor3f(1, 0, 0.0)
    glVertex2d(0 , 50+shift_tr3_y)
    glColor3f(1, 1, 0.0)
    glVertex2d(95, 0+shift_tr3_y)

    # Big triangle 2
    glColor3f(1, 0, 0.0)
    glVertex2d(-85, 0 + shift_tr4_y)
    glColor3f(1, 0, 0.0)
    glVertex2d(0, 50 + shift_tr4_y)
    glColor3f(1, 1, 0.0)
    glVertex2d(85, 0 + shift_tr4_y)
    glEnd()

    glBegin(GL_LINES)

    glEnd()



    glBegin(GL_QUADS)
    glColor3f(128 / 256, 0, 0)

    # Whole Building BG

    glVertex2d(-20 + shift_tr2_x, -20)
    glVertex2d(-20 + shift_tr2_x, -75)

    glVertex2d(20 + shift_tr1_x, -75)
    glVertex2d(20 + shift_tr1_x, -20)

    # Main Building BG


    glVertex2d(-50 + shift_tr1_x, -75)
    glVertex2d(-50 + shift_tr1_x, 40)

    glVertex2d(50 + shift_tr2_x, 40)
    glVertex2d(50 + shift_tr2_x, -75)

    # Left Building BG

    glVertex2d(-20 + shift_tr2_x, 0)
    glVertex2d(-20 + shift_tr2_x, -75)

    glVertex2d(20 + shift_tr2_x, -75)
    glVertex2d(20 + shift_tr2_x, 0)

    # Right Building BG

    glVertex2d(-20 + shift_tr1_x, 0)
    glVertex2d(-20 + shift_tr1_x, -75)

    glColor3f(1, 0.2, 0.0)
    glVertex2d(20 + shift_tr1_x, -75)
    glVertex2d(20 + shift_tr1_x, 0)

    glEnd()

    # Windows

    glBegin(GL_QUADS)
    glColor3f(1, 0, 0)
    shift_q1_x = -40
    shift_q1_y = 10

    glVertex2d(-15+shift_q1_x, 15+shift_q1_y)
    glVertex2d(15+shift_q1_x, 15+shift_q1_y)
    glVertex2d(15+shift_q1_x, -15+shift_q1_y)
    glVertex2d(-15+shift_q1_x, -15+shift_q1_y)

    shift_q2_x = 40
    shift_q2_y = 10

    glVertex2d(-15 + shift_q2_x, 15 + shift_q2_y)
    glVertex2d(15 + shift_q2_x, 15 + shift_q2_y)
    glVertex2d(15 + shift_q2_x, -15 + shift_q2_y)
    glVertex2d(-15 + shift_q2_x, -15 + shift_q2_y)

    glEnd()


    glBegin(GL_LINES)

    # Window lines

    glColor3f(0, 0, 0.0)
    glVertex2d(shift_q1_x, 15+shift_q1_y)
    glVertex2d(shift_q1_x, -15 + shift_q1_y)

    glVertex2d(-15+shift_q1_x, shift_q1_y)
    glVertex2d(15 + shift_q1_x, shift_q1_y)

    glVertex2d(shift_q2_x, 15 + shift_q2_y)
    glVertex2d(shift_q2_x, -15 + shift_q2_y)

    glVertex2d(-15 + shift_q2_x, shift_q2_y)
    glVertex2d(15 + shift_q2_x, shift_q2_y)

    # Door

    glColor3f(1, 0, 0.0)
    glVertex2d(-15, -30)
    glVertex2d(15, -30)

    glVertex2d(-15, -30)
    glVertex2d(-15, -75)

    glVertex2d(15, -30)
    glVertex2d(15, -75)


    glEnd()

    # Doorknob

    glBegin(GL_POINTS)

    glVertex2d(10, -50)

    glEnd()






def display():
    #//clear the display
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glClearColor(0,0,0,0);	#//color black
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    #//load the correct matrix -- MODEL-VIEW matrix
    glMatrixMode(GL_MODELVIEW)
    #//initialize the matrix
    glLoadIdentity()
    #//now give three info
    #//1. where is the camera (viewer)?
    #//2. where is the camera looking?
    #//3. Which direction is the camera's UP direction?
    gluLookAt(0,0,200,	0,0,0,	0,1,0)
    glMatrixMode(GL_MODELVIEW)

    draw_house()
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
glutInitDisplayMode(GLUT_DEPTH | GLUT_DOUBLE | GLUT_RGB)
glutInitWindowSize(500, 500) #window size
glutInitWindowPosition(0, 0)
wind = glutCreateWindow(b"Rainy House") #window name
init()
glutDisplayFunc(display)

glutKeyboardFunc(keyboardListener)
glutSpecialFunc(specialKeyListener)
glutMainLoop()