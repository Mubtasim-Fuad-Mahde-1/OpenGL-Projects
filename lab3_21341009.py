from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *


W_Width, W_Height = 500,500

points = []
freeze = False
speed = 50

radius = 3

def toggle_freeze():
    global freeze
    freeze = not(freeze)


def convert_coordinate(x, y):
    global W_Width, W_Height
    a = x - (W_Width/2)
    b = (W_Height/2) - y
    return a,b


def keyboardListener(key, x, y):
    global freeze, speed
    if key==b' ':
        toggle_freeze()
        if freeze == False:
            print(speed)
            glutTimerFunc(speed, animate, 0)


def specialKeyListener(key, x, y):
    global speed, freeze
    if not freeze:
        if key==GLUT_KEY_DOWN:
            speed = round(speed/ 2)

            print(speed)
        elif key==GLUT_KEY_UP:
            speed *= 2
            print(speed)


def mouseListener(button, state, x, y):  # /#/x, y is the x-y of the screen (2D)
    if button == GLUT_RIGHT_BUTTON:
        if state == GLUT_DOWN:
            m, n = convert_coordinate(x, y)
            points.append([m, n, 0])
            print(points)

    glutPostRedisplay()


def all_circle_zones(x, y, x0, y0):
    glVertex2f(x + x0, y + y0)
    glVertex2f(y + x0, x + y0)
    glVertex2f(y + x0, -x + y0)
    glVertex2f(x + x0, -y + y0)
    glVertex2f(-x + x0, -y + y0)
    glVertex2f(-y + x0, -x + y0)
    glVertex2f(-y + x0, x + y0)
    glVertex2f(-x + x0, y + y0)


def midpointcirclealgo(x1, y1, r = 30):
    d_init = 1 - r
    d = d_init

    x = 0
    y = r
    while x < y:
        all_circle_zones(x, y, x1, y1)
        if d >= 0:
            d = d + 2*x - 2*y + 5
            x += 1
            y -= 1
        else:
            d = d + 2*x + 3
            x += 1


def draw_points():
    for i in range(0, len(points)):
        x1 = points[i][0]
        y1 = points[i][1]
        radius = points[i][2]
        # midpointlinealgo(x1, x2, y1, y2)
        min_x = x1 - radius
        max_x = x1 + radius
        min_y = y1 - radius
        max_y = y1 + radius

        if min_x > -250 and max_x < 250:
            if min_y > -250 and max_y < 250:
                midpointcirclealgo(x1, y1, radius)


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
    # midpointlinealgo(x1, x2, y1, y2)
    global radius, create_new
    glBegin(GL_POINTS)
    glColor3f(1, 0, 0)
    draw_points()
    # grow_points()
    glEnd()

    glutSwapBuffers()


def animate(_):
    glutPostRedisplay()
    global points, freeze, speed
    if not(freeze):
        for i in range(len(points)):
            points[i][2] += 1
        print(speed)
        glutTimerFunc(speed, animate, 0)



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
wind = glutCreateWindow(b"Bubbles") #window name
init()
glutDisplayFunc(display)
# glutIdleFunc(animate)
glutTimerFunc(speed, animate, 0)

# glutTimerFunc(100, fall_diamond, 0)
# glutTimerFunc(30, draw_points(), 0)

glutKeyboardFunc(keyboardListener)
glutSpecialFunc(specialKeyListener)
glutMouseFunc(mouseListener)
glutMainLoop()