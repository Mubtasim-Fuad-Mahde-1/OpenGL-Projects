from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

global animation_speed,pause,plate_x
plate_x = 200
pause = False
animation_speed = 25
def plate():
    global plate_x
    x = plate_x
    r,g,b = 1,0,0
    #line_algo(x,50,x+200,50,r,g,b)
    #line_algo(x+25,25,x+175,25,r,g,b)
    line_algo(x,50,x+25,25,r,g,b)
    #line_algo(x+175,25,x+200,50,r,g,b)

def diamond():
    pass

def back():
    pass

def pause_play():
    pass

def cross():
    pass

def convert_coordinate(x,y):
    return x, 600-y

def from_zone0(x, y, z):
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
        return -y, x
    elif z == 7:
        return x, -y

def to_zone0(x, y, z):
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

def determine_zone(x, y):
    if x >= 0:
        if y >= 0:
            if x >= y:
                return 0
            else:
                return 1
        else:
            if x >= -y:
                return 7
            else:
                return 6
    else:
        if y >= 0:
            if -x >= y:
                return 3
            else:
                return 2
        else:
            if x <= y:
                return 4
            else:
                return 5

def line_algo(x1,y1,x2,y2,r=1,g=1,b=1):
    z1 = determine_zone(x1,y1)
    x1,y1 = to_zone0(x1,y1,z1)
    z2 = determine_zone(x2,y2)
    x2,y2 = to_zone0(x2,y2,z2)
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    slope = dy > dx
    
    if slope:
        x1, y1 = y1, x1
        x2, y2 = y2, x2
    if x1 > x2:
        x1,x2 = x2,x1
        y1,y2 = y2,y1
          
    dx = x2 - x1  
    dy = -abs(y2 - y1)
    d = dy - (dx/2)  
    x = x1 
    y = y1  
    x1,y1 = from_zone0(x1,y1,z1)
    glBegin(GL_POINTS)
    glColor3f(r,g,b)
    glVertex2f(x1,y1)
    while (x < x2): 
        x=x+1
        if(d < 0): 
            d = d + dy    
        else: 
            d = d + (dy - dx)  
            y=y+1
        z = determine_zone(x,y)
        x,y = from_zone0(x,y,z)
        glVertex2f(x,y)
    glEnd()
def keyboardListener(key,x,y):
    global pause
    if key == b' ':
        if pause == False:
            pause == True
        else:
            pause == False
def restart():
    pass

def specialKeyListener():
    pass 

def mouseListener(button,state,x,y):
    global pause
    x,y = convert_coordinate(x,y)
    if button == GLUT_LEFT_BUTTON and state == GLUT_DOWN:
        if 25<=x<=75 and 525<=y<=575:
            restart()
            return
        elif 275<=x<=325 and 525<=y<=575:
            if pause == False:
                pause == True
            else:
                pause == False
        elif 525<=x<=575 and 525<=y<=575:
            glutLeaveMainLoop()

def animate(value):
    global animation_speed
    glutPostRedisplay()
    glutTimerFunc(animation_speed,animate,0)

def iterate():
    glViewport(0, 0, 600, 600)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 600, 0.0, 600, 0.0, 1.0)
    glMatrixMode (GL_MODELVIEW)
    glLoadIdentity()
    
def showScreen():
    global pause
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    iterate()
    plate()
    glutSwapBuffers()

glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(600, 600) #window size
glutInitWindowPosition(0, 0)
wind = glutCreateWindow(b"OpenGL Coding Practice") #window name
glutDisplayFunc(showScreen)
glutTimerFunc(animation_speed,animate,0)
glutKeyboardFunc(keyboardListener)
glutSpecialFunc(specialKeyListener)
glutMouseFunc(mouseListener)
glutMainLoop()