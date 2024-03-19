#Hello
#my name is mahde
#hi

#CSE423 Project
#----------------------------------------------------------------------------##----------------------------------------------------------------------------#
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import random




#Display Text on Screen
#----------------------------------------------------------------------------##----------------------------------------------------------------------------#
def draw_text(text, coordinate, color):
    r = color[0]
    g = color[1]
    b = color[2]
    glColor3f(r,g,b)
    glRasterPos2f(coordinate[0], coordinate[1])
    for char in text:
        glutBitmapCharacter(GLUT_BITMAP_HELVETICA_18, ord(char))




#Mid Point Line Drawing Algorithm
#----------------------------------------------------------------------------##----------------------------------------------------------------------------#

def zone(x1, y1, x2, y2): 
    dy = y2-y1
    dx = x2-x1
    if abs(dx) > abs(dy):
        if dx > 0 and dy >= 0:
            return 0
        elif dx < 0 and dy > 0:
            return 3
        elif dx < 0 and dy < 0:
            return 4
        else:
            return 7
    else:
        if dx > 0 and dy >= 0:
            return 1
        elif dx < 0 and dy > 0:
            return 2
        elif dx < 0 and dy < 0:
            return 5
        else:
            return 6

def zone02z(x, y, z): 
    if z == 0:
        return x, y
    elif z == 1:
        return y, x
    elif z == 2:
        return -y, x
    elif z == 3:
        return -x, y
    elif z == 4:
        return -x, -y
    elif z == 5:
        return -y, -x
    elif z == 6:
        return y, -x
    elif z == 7:
        return x, -y

def z2zone0(x, y, z):
    if z == 0:
        return x, y
    elif z == 1:
        return y, x
    elif z == 2:
        return y, -x
    elif z == 3:
        return -x, y
    elif z == 4:
        return -x, -y
    elif z == 5:
        return -y, -x
    elif z == 6:
        return -y, x
    elif z == 7:
        return x, -y

def draw_line(x1, y1, x2, y2, color): 
    z = zone(x1,y1,x2,y2)
    x1,y1 = z2zone0(x1,y1,z)
    x2,y2 = z2zone0(x2,y2,z)
    dy = y2 - y1 
    dx = x2 - x1 
    d = 2 * dy - dx 
    r = color[0]
    g = color[1]
    b = color[2]
    glBegin(GL_POINTS)
    glColor3f(r,g,b)
    glVertex2f(x1,y1)
    while True:
        if x1 == x2 and y1 == y2:
            break
        if d > 0: # for North East Pixel
            d = d + 2 * dy - 2 * dx
            x1 += 1
            y1 += 1
            x1,y1 = zone02z(x1,y1,z)
            glVertex2f(x1,y1)
            x1,y1 = z2zone0(x1,y1,z)
        else: # for East Pixel
            d = d + 2 * dy
            x1 += 1
            x1, y1 = zone02z(x1, y1,z)
            glVertex2f(x1, y1)
            x1, y1 = z2zone0(x1, y1,z)
    glEnd()





#Mid Point Circle Drawing Algorithm
#----------------------------------------------------------------------------##----------------------------------------------------------------------------#

def circle_zones(x, y, x0, y0, color): #x,y are points generated for each zone and x0,y0 is the origin of circle
    r = color[0]
    g = color[1]
    b = color[2]
    glBegin(GL_POINTS)
    glColor3f(r,g,b)
    glVertex2f(x + x0, y + y0)
    glVertex2f(y + x0, x + y0)
    glVertex2f(y + x0, -x + y0)
    glVertex2f(x + x0, -y + y0)
    glVertex2f(-x + x0, -y + y0)
    glVertex2f(-y + x0, -x + y0)
    glVertex2f(-y + x0, x + y0)
    glVertex2f(-x + x0, y + y0)
    glEnd()

def draw_circle(x0, y0, r, color): #midpoint circle drawing algorithm
    d = 1 - r
    x = 0
    y = r
    while x <= y: 
        circle_zones(x, y, x0, y0, color) # x0, y0 is the original center of the circle
        print(x,y)
        if d >= 0: # for South East Pixel
            d = d + 2*x - 2*y + 5
            x += 1
            y -= 1
        else: # for East Pixel
            d = d + 2*x + 3
            x += 1





#User input and actions
#----------------------------------------------------------------------------##----------------------------------------------------------------------------#

def convert_coordinate(x, y):
    return x, 600-y

def keyboardListener(key, x, y):
    pass

def specialKeyListener(key, x, y):
    pass

def mouseListener(button, state, x, y):
    pass






#Screen Properties and Object display
#----------------------------------------------------------------------------##----------------------------------------------------------------------------#

def showScreen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glPointSize(1)
    color = (1,1,1)
    iterate()
    #Objects
    
    glutSwapBuffers()

def iterate():
    glViewport(0, 0, 1000, 1000)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 1000, 0.0, 1000, 0.0, 1.0)
    glMatrixMode (GL_MODELVIEW)
    glLoadIdentity()

glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(1000, 1000) #window size
glutInitWindowPosition(0, 0)
wind = glutCreateWindow(b"OpenGL Coding Practice") #window name
glutDisplayFunc(showScreen)
glutKeyboardFunc(keyboardListener)
glutSpecialFunc(specialKeyListener)
glutMouseFunc(mouseListener)
glutMainLoop()
