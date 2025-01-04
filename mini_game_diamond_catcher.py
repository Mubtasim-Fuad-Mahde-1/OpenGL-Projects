from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import random
global animation_speed,pause,plate_x,speed,diamond_x,diamond_y,plate_speed
plate_speed = 3 
speed = 1
plate_x = 200 #for plate size and position change
pause = False #flag for pause or resume
animation_speed = 10
diamond_x,diamond_y = 300,500 #dimension of diamond 
def plate(): #draw the plate
    global plate_x
    x = plate_x
    r,g,b = 0,1,1
    line_algo(x,50,x+200,50,r,g,b)
    line_algo(x+25,25,x+175,25,r,g,b)
    line_algo(x,50,x+25,25,r,g,b)
    line_algo(x+175,25,x+200,50,r,g,b)

def diamond(): #draw the diamond and drop the diamond
    global diamond_x,diamond_y,speed,plate_x,pause,plate_speed
    if diamond_y < 110 and plate_x<=diamond_x<=plate_x+200:
        diamond_y = 500
        print('Score=',plate_speed-2)
        plate_speed+=1
        speed+=plate_speed*0.01
        diamond_x = random.randint(25,575)
    if diamond_y < 110 and (diamond_x>(plate_x+200) or diamond_x<plate_x):
        restart()
        return
    diamond_y-=speed
    if pause == True:
        diamond_y+=speed
    x = diamond_x
    y = diamond_y
    r,g,b = 1,1,0
    line_algo(x,y,x-20,y-30,r,g,b)
    line_algo(x,y,x+20,y-30,r,g,b)
    line_algo(x-20,y-30,x,y-60,r,g,b)
    line_algo(x+20,y-30,x,y-60,r,g,b)
    glutPostRedisplay()

def back(): #draw the restart button
    r,g,b = 0,1,0
    x = 25
    y = 550
    line_algo(x,y,x+50,y,r,g,b)
    line_algo(x,y,x+25,y+25,r,g,b)
    line_algo(x,y,x+25,y-25,r,g,b)

def pause_play(): # draw the pause and resume button based on pause condition
    global pause 
    r,g,b = 1,0.2,1
    if pause == True:
        x = 275
        y = 575
        line_algo(x,y,x+50,y-25,r,g,b)
        line_algo(x,y-50,x+50,y-25,r,g,b)
        line_algo(x,y,x,y-50,r,g,b)
    else:
        x = 275
        y = 575
        line_algo(x+10,y,x+10,y-50,r,g,b)
        line_algo(x+40,y,x+40,y-50,r,g,b)

def cross(): #draw the cross to close the game
    r,g,b = 1,0,0
    x = 525
    y = 575
    line_algo(x,y,x+50,y-50,r,g,b)
    line_algo(x,y-50,x+50,y,r,g,b)

def convert_coordinate(x,y): #convert mouse coordinates to screen coordinates
    return x, 600-y

def zone(x1, y1, x2, y2): #determine zone of a line
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

def zone02z(x,y,z): # convert from zone 0 to zone z (z can be found from function zone())
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

def z2zone0(x,y,z): #convert from any zone to zone 0
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
    
def line_algo(x1,y1,x2,y2,r=1,g=1,b=1): #midpoint line drawing algorithm with zone determiniation and convertion
    z = zone(x1,y1,x2,y2)
    x1,y1 = z2zone0(x1,y1,z)
    x2,y2 = z2zone0(x2,y2,z)
    dy = y2 - y1 
    dx = x2 - x1 
    d = 2 * dy - dx 
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

def restart(): # restart function that initializes everything to original state
    global plate_x,diamond_x,diamond_y,speed,pause,temp_speed,plate_speed
    pause = True
    plate_x = 200
    diamond_x,diamond_y = 300,500
    speed = 0
    plate_speed = 3
    print('Restart!')
    glutPostRedisplay()

def keyboardListener(key,x,y): # pause keyboard space button to control pause and resume
    global temp_speed,speed,pause
    if key == b' ':
        if pause == False:
            pause = True
            speed = 0
        elif pause == True:
            pause = False
            speed = 1
        glutPostRedisplay()

def specialKeyListener(key,x,y): # arrow keys to control the position of plate, also implement a system so speed of plate inscreses after every socre
    global pause,plate_x,speed,plate_speed
    if pause == True:
        return
    if key == GLUT_KEY_RIGHT:
        plate_x+=plate_speed*2
        if plate_x > 400:
            plate_x-=plate_speed*2
    elif key == GLUT_KEY_LEFT:
        plate_x-=plate_speed*2
        if plate_x < 0:
            plate_x+=plate_speed*2

def mouseListener(button,state,x,y): # use mouse to press 3 positions of the screen, back pause and close
    global speed,temp_speed,pause
    x1,x2,x3 = 0,250,500
    x,y = convert_coordinate(x,y)
    if button == GLUT_LEFT_BUTTON and state == GLUT_DOWN:
        if x1<=x<=(x1+100) and 500<=y<=600: #for restart button
            restart()
        elif x3<=x<=(x3+100) and 500<=y<=600: #for close button
            glutLeaveMainLoop()
        elif x2<=x<=(x2+100) and 500<=y<=600: #for pause button
            if pause == False:
                pause = True
                speed = 0
                glutPostRedisplay()
            else:
                pause = False
                speed = 1
                glutPostRedisplay()

def iterate(): # for screen frame rate
    glViewport(0, 0, 600, 600)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 600, 0.0, 600, 0.0, 1.0)
    glMatrixMode (GL_MODELVIEW)
    glLoadIdentity()
    
def showScreen(): # display everything
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glPointSize(1)
    iterate()
    plate()
    diamond()
    back()
    pause_play()
    cross()
    glutSwapBuffers()

glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(600, 600) #window size
glutInitWindowPosition(0, 0)
wind = glutCreateWindow(b"OpenGL Coding Practice") #window name
glutDisplayFunc(showScreen)
glutKeyboardFunc(keyboardListener)
glutSpecialFunc(specialKeyListener)
glutMouseFunc(mouseListener)
glutMainLoop()