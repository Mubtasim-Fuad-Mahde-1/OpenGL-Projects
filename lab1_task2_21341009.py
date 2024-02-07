from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import random

W_Width, W_Height = 500,500
create_new = False
points = []
move_x, move_y = 0, 0
speed = 750
blink = False
blink_flag = True
freeze = False

def toggle_freeze():
    global freeze
    freeze = not freeze

def keyboardListener(key, x, y):
    if key==b' ':
        toggle_freeze()

def toggle_blink(value):
    global blink, freeze
    if not freeze and blink_flag:
        blink = not blink
        glutTimerFunc(100, toggle_blink, 0)

def convert_coordinate(x,y):
    global W_Width, W_Height
    a = x - (W_Width/2)
    b = (W_Height/2) - y
    return a,b

def specialKeyListener(key, x, y):
    global speed, freeze
    if not freeze:
        if key==GLUT_KEY_UP:
            speed = round(speed/ 2)

            print(speed)
        elif key==GLUT_KEY_DOWN:
            speed *= 2
            print(speed)


    glutPostRedisplay()

def mouseListener(button, state, x, y):  # /#/x, y is the x-y of the screen (2D)
    global create_new, freeze, blink_flag, blink
    if not freeze:
        if button == GLUT_RIGHT_BUTTON:
            if state == GLUT_DOWN:
                create_new = convert_coordinate(x, y)
        if button == GLUT_LEFT_BUTTON:
            if state == GLUT_DOWN:
                toggle_blink(0)

        # Acts as a blink lock, when clicked it locks the blink and when clicked again
        # it unlocks the blink, so we can press left click to start blink again
        if button == GLUT_MIDDLE_BUTTON:
            if state == GLUT_DOWN:
                blink_flag = not blink_flag
                blink = False

    glutPostRedisplay()

def animate(value):
    glutPostRedisplay()
    global speed, freeze
    global move_x, move_y, points
    # move_x, move_y = 0, 0
    if not freeze:
        move_x = random.choice([-6, 6])
        move_y = random.choice([-6, 6])

    glutTimerFunc(speed, animate, 0)




def draw_points():
    global move_x, move_y
    for i in range(len(points)):
        if blink:
            pass
        else:
            glPointSize(10)
            glBegin(GL_POINTS)
            # Random colors for each points
            if points[i][2] == 0:
                glColor3f(1, 0, 0)
            elif points[i][2] == 1:
                glColor3f(0, 1, 0)
            elif points[i][2] == 2:
                glColor3f(0, 0, 1)
            glVertex2f((points[i][0]+move_x), (points[i][1] + move_y))
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

    # Stores the points from the right click to a list, and its movement is stored in move_x and move_y
    if (create_new):
        m, n = create_new
        r = m % 3
        points.append([m, n, r])

    draw_points()
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
wind = glutCreateWindow(b"Starry Night") #window name
init()
glutDisplayFunc(display)
# glutIdleFunc(animate)
glutTimerFunc(speed, animate, 0)



glutKeyboardFunc(keyboardListener)
glutSpecialFunc(specialKeyListener)
glutMouseFunc(mouseListener)
glutMainLoop()