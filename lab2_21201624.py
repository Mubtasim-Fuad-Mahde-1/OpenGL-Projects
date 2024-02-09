from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import random
global plate_x,diamond_x_y,speed,hitbox_x,pause,animation_speed,temp_speed
temp_speed = 0
animation_speed = 25
pause = False
hitbox_x = {'play':250,'back':0,'cross':500}
plate_x = 200
diamond_x_y = (300,500)
speed = 3
def plate():
    global plate_x
    x,y = plate_x,60
    glBegin(GL_LINES)
    glColor3f(1,1,0)
    glVertex2f(x,y)
    glVertex2f(x+200,y)
    glVertex2f(x+200,y)
    glVertex2f(x+175,y-25)
    glVertex2f(x+175,y-25)
    glVertex2f(x+25,y-25)
    glVertex2f(x+25,y-25)
    glVertex2f(x,y)
    glEnd()
def diamond():
    global diamond_x_y,speed,plate_x,pause
    x,y = diamond_x_y[0],diamond_x_y[1]-speed
    if y < 120 :
        if plate_x<=x<=(plate_x+200):
            speed+=1
            print('Score',speed-3)
            y = 500
            x = random.randint(50,550)
        else:
            restart()
            return
    glBegin(GL_LINES)
    glColor3f(0,1,1)
    glVertex2f(x,y)
    glVertex2f(x+20,y-30)
    glVertex2f(x+20,y-30)
    glVertex2f(x,y-60)
    glVertex2f(x,y-60)
    glVertex2f(x-20,y-30)
    glVertex2f(x-20,y-30)
    glVertex2f(x,y)
    glEnd()
    diamond_x_y = (x,y)
def convert_coordinate(x,y):
    a = x
    b = 600 - y
    return a,b
def play():
    global pause
    glBegin(GL_LINES)
    glColor3f(1,0,0)
    if pause == False:
        glVertex2f(280,575)
        glVertex2f(280,525)
        glVertex2f(320,575)
        glVertex2f(320,525)
    else:
        glVertex2f(280,575)
        glVertex2f(320,550)
        glVertex2f(320,550)
        glVertex2f(280,525)
        glVertex2f(280,525)
        glVertex2f(280,575)
    glEnd()
def animate(value):
    global animation_speed
    glutPostRedisplay()
    glutTimerFunc(animation_speed,animate,0)
def cross():
    glBegin(GL_LINES)
    glColor3f(1,0,0)
    glVertex2f(525,575)
    glVertex2f(575,525)
    glVertex2f(525,525)
    glVertex2f(575,575)
    glEnd()
def back():
    glBegin(GL_LINES)
    glColor3f(0,1,0)
    glVertex2f(10,550)
    glVertex2f(50,575)
    glVertex2f(10,550)
    glVertex2f(50,525)
    glVertex2f(10,550)
    glVertex2f(75,550)
    glEnd()
def restart():
    global plate_x,diamond_x_y,speed,pause,temp_speed
    pause = True
    plate_x = 200
    diamond_x_y = (300,500)
    speed = 0
    temp_speed = 3
    print('Restart')
    glutPostRedisplay()
def keyboardListener(key,x,y):
    pass  
def specialKeyListener(key,x,y):
    global pause,plate_x,speed
    if pause == True:
        return
    if key == GLUT_KEY_RIGHT:
        plate_x+=speed*2
        if plate_x > 400:
            plate_x-=speed*2
    elif key == GLUT_KEY_LEFT:
        plate_x-=speed*2
        if plate_x < 0:
            plate_x+=speed*2
def mouseListener(button,state,x,y):
    global hitbox_x,speed,temp_speed,pause
    x1,x2,x3 = hitbox_x['back'],hitbox_x['play'],hitbox_x['cross']
    x,y = convert_coordinate(x,y)
    if button == GLUT_LEFT_BUTTON and state == GLUT_DOWN:
        if x1<=x<=(x1+100) and 500<=y<=600:
            restart()
        elif x3<=x<=(x3+100) and 500<=y<=600:
            glutLeaveMainLoop()
        elif x2<=x<=(x2+100) and 500<=y<=600:
            if pause == False:
                pause = True
                temp_speed = speed
                speed = 0
                glutPostRedisplay()
            elif pause == True:
                pause = False
                speed = temp_speed
                temp_speed = 0
                glutPostRedisplay()
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
    print(pause)
    plate()
    diamond()
    back()
    cross()
    play()
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