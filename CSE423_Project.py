#CSE423 Project
#----------------------------------------------------------------------------##----------------------------------------------------------------------------#
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import random

#Global Variables
#----------------------------------------------------------------------------##----------------------------------------------------------------------------#
global shooter_x,level
shooter_x = 500
level = 1
bots = []
shooter_bullets = []



#Display Objects on screen
#----------------------------------------------------------------------------##----------------------------------------------------------------------------#
def text(text, coordinate, color):
    r = color[0]
    g = color[1]
    b = color[2]
    glColor3f(r,g,b)
    glRasterPos2f(coordinate[0], coordinate[1])
    for char in text:
        glutBitmapCharacter(GLUT_BITMAP_HELVETICA_18, ord(char))

def cross():
    pass

def top_bar():
    x = 0
    y = 1000
    glPointSize(5)
    color = (1,1,1)
    draw_line(x+10,y-10,x+990,y-10,color)
    draw_line(x+10,y-60,x+990,y-60,color)
    draw_line(x+10,y-10,x+10,y-60,color)
    draw_line(x+990,y-10,x+990,y-60,color)

def bottom_bar():
    x = 0
    y = 70
    glPointSize(5)
    color = (1,1,1)
    draw_line(x+10,y-10,x+990,y-10,color)
    draw_line(x+10,y-60,x+990,y-60,color)
    draw_line(x+10,y-10,x+10,y-60,color)
    draw_line(x+990,y-10,x+990,y-60,color)

def shooter():
    pass

def health():
    pass

def pause_resume():
    pass

def restart():
    pass

def pause_title():
    pass

def shooter():
    global shooter_x
    x = shooter_x
    y = 130
    color = (1,1,1)
    glPointSize(3)
    draw_line(x,y,x-25,y-50,color)
    draw_line(x,y,x+25,y-50,color)
    draw_line(x-25,y-50,x+25,y-50,color)
    draw_line(x-13,y-25,x-50,y-60,color)
    draw_line(x+13,y-25,x+50,y-60,color)
    draw_line(x-50,y-60,x-25,y-50,color)
    draw_line(x+50,y-60,x+25,y-50,color)
    glPointSize(2)
    draw_line(x,y+10,x-10,y-5,color)
    draw_line(x,y+10,x+10,y-5,color)
    draw_line(x-10,y-5,x,y,color)
    draw_line(x+10,y-5,x,y,color)
    glPointSize(4)
    draw_line(x-30,y-40,x-30,y-30,color)
    draw_line(x+30,y-40,x+30,y-30,color)

def shooter_bullet():
    global shooter_bullets
    for i in shooter_bullets:
        x = i[0]
        y = i[1]
        color = (1,1,1)
        glPointSize(1)
        draw_line(x,y,x-6,y-20,color)
        draw_line(x,y,x+6,y-20,color)
        draw_line(x-6,y-20,x,y-12,color)
        draw_line(x+6,y-20,x,y-12,color)
    for i in shooter_bullets:
        x = i[0]-30
        y = i[1]-40
        color = (1,1,1)
        glPointSize(1)
        draw_line(x,y,x-6,y-20,color)
        draw_line(x,y,x+6,y-20,color)
        draw_line(x-6,y-20,x,y-12,color)
        draw_line(x+6,y-20,x,y-12,color)
    for i in shooter_bullets:
        x = i[0]+30
        y = i[1]-40
        color = (1,1,1)
        glPointSize(1)
        draw_line(x,y,x-6,y-20,color)
        draw_line(x,y,x+6,y-20,color)
        draw_line(x-6,y-20,x,y-12,color)
        draw_line(x+6,y-20,x,y-12,color)
        
    
    
#Mid Point Line Drawing Algorithm
#----------------------------------------------------------------------------##----------------------------------------------------------------------------#

def zone(x1, y1, x2, y2): 
    dy = y2-y1
    dx = x2-x1
    if abs(dx) >= abs(dy):
        if dx >= 0 and dy >= 0:
            return 0
        elif dx < 0 and dy > 0:
            return 3
        elif dx < 0 and dy < 0:
            return 4
        else:
            return 7
    else:
        if dx >= 0 and dy >= 0:
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


#Complex functions (dont touch these please!)
#----------------------------------------------------------------------------##----------------------------------------------------------------------------#


class nonplayer_bullet:
    def __init__(self):
        pass
    


#User input and actions
#----------------------------------------------------------------------------##----------------------------------------------------------------------------#

def convert_coordinate(x, y):
    return x, 600-y

def keyboardListener(key, x, y):
    global shooter_x, shooter_bullets
    if key == b' ':
        shooter_bullets.append((shooter_x,160))
    glutPostRedisplay()

def specialKeyListener(key, x, y):
    global shooter_x
    if key == GLUT_KEY_RIGHT:
        shooter_x+=10
        if shooter_x > 1000:
            shooter_x-=10
    elif key == GLUT_KEY_LEFT:
        shooter_x-=10
        if shooter_x < 0:
            shooter_x+=10

def mouseListener(button, state, x, y):
    pass



#Animation Functions
#----------------------------------------------------------------------------##----------------------------------------------------------------------------#

def animate(value):
    glutPostRedisplay()
    glutTimerFunc(1,animate,0)

def animate_shooter_bullets(value):
    global shooter_bullets
    for i in range(0,len(shooter_bullets)):
        if shooter_bullets[i][1]+5 > 940:
            shooter_bullets.pop(i)
            glutPostRedisplay()
            break
        else:
            shooter_bullets[i] = (shooter_bullets[i][0],shooter_bullets[i][1]+5)
            glutPostRedisplay()
    glutTimerFunc(1,animate_shooter_bullets,0)



#Screen Properties and Object display
#----------------------------------------------------------------------------##----------------------------------------------------------------------------#
def iterate():
    glViewport(0, 0, 1000, 1000)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 1000, 0.0, 1000, 0.0, 1.0)
    glMatrixMode (GL_MODELVIEW)
    glLoadIdentity()

def showScreen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glPointSize(2)
    color = (1,1,1)
    iterate()
    top_bar()
    bottom_bar()
    shooter()
    shooter_bullet()
    glutSwapBuffers()

glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(1000, 1000) #window size
glutInitWindowPosition(0, 0)
wind = glutCreateWindow(b"OpenGL Coding Practice") #window name
glutDisplayFunc(showScreen)
glutKeyboardFunc(keyboardListener)
glutSpecialFunc(specialKeyListener)
glutMouseFunc(mouseListener)
glutTimerFunc(1,animate_shooter_bullets,0)
glutTimerFunc(1,animate,0)
glutMainLoop()
