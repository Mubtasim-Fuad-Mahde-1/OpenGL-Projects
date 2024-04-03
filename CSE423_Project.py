#CSE423 Project
#----------------------------------------------------------------------------##----------------------------------------------------------------------------#
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import random

#Global Variables
#----------------------------------------------------------------------------##----------------------------------------------------------------------------#
global shooter_x,level,shooter_bullets,bots,bot_bullets,life
life = 3
shooter_x = 500
level = 1
bots = []
shooter_bullets = []
bot_bullets = []
pause = False



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

def top_bar():
    x = 0
    y = 1000
    glPointSize(5)
    color = (0,0,0)
    draw_line(x+10,y-10,x+990,y-10,color)
    draw_line(x+10,y-60,x+990,y-60,color)
    draw_line(x+10,y-10,x+10,y-60,color)
    draw_line(x+990,y-10,x+990,y-60,color)

def bottom_bar():
    x = 0
    y = 70
    glPointSize(5)
    color = (0,0,0)
    draw_line(x+10,y-10,x+990,y-10,color)
    draw_line(x+10,y-60,x+990,y-60,color)
    draw_line(x+10,y-10,x+10,y-60,color)
    draw_line(x+990,y-10,x+990,y-60,color)


def health():
    pass

def pause_title():
    if pause == True:
        color = (0,1,1)
        text("GAME PAUSE", (450,500), color)
        draw_line(400,450,400,570,color)
        draw_line(620,450,620,570,color)
        draw_line(400,570,620,570,color)
        draw_line(400,450,620,450,color)



def pause_resume():
    #global pause
    color = (1,1,0.1)
    glPointSize(2)
    if pause:
        draw_line(910,975,930,965,color)
        draw_line(910,955,930,965,color)
        draw_line(910,975,910,955,color)
    else:
        draw_line(910,975,910,955,color)
        draw_line(920,975,920,955,color)

def back():
    color = (0.2,0.7,1)
    glPointSize(2)
    draw_line(850, 965, 880, 965, color)
    draw_line(850, 965, 860, 975, color)
    draw_line(850, 965, 860, 955, color)

def cross():
    color = (1,0.2,0.2)
    glPointSize(2)
    draw_line(955,955,975,975,color)
    draw_line(955,975,975,955,color)


def shooter():
    global shooter_x
    x = shooter_x
    y = 130
    color = (0.3,0.3,0.3)
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
        color = (1,0.3,0.1)
        glPointSize(1)
        draw_line(x,y,x-6,y-20,color)
        draw_line(x,y,x+6,y-20,color)
        draw_line(x-6,y-20,x,y-12,color)
        draw_line(x+6,y-20,x,y-12,color)
    for i in shooter_bullets:
        x = i[0]-30
        y = i[1]-40
        color = (1,0.5,0.1)
        glPointSize(1)
        draw_line(x,y,x-6,y-20,color)
        draw_line(x,y,x+6,y-20,color)
        draw_line(x-6,y-20,x,y-12,color)
        draw_line(x+6,y-20,x,y-12,color)
    for i in shooter_bullets:
        x = i[0]+30
        y = i[1]-40
        color = (1,0.5,0.1)
        glPointSize(1)
        draw_line(x,y,x-6,y-20,color)
        draw_line(x,y,x+6,y-20,color)
        draw_line(x-6,y-20,x,y-12,color)
        draw_line(x+6,y-20,x,y-12,color)
        
def power_up():
    pass
    
def bot_range(i):
    i = 200*(i+1)
    x1 = i-170
    x2 = i-30
    y1 = 800
    y2 = 900
    x = random.randint(x1,x2)
    y = random.randint(y1,y2)
    return (x,y)

def bot_army():
    global bots
    for i in bots:
        x = i[0]
        y = i[1]
        r = 30
        color = (0.2,0.2,1)
        glPointSize(4)
        draw_circle(x,y,r,color)
        draw_circle(x,y,10,color)
        draw_line(x-7,y+7,x,y+30,color)
        draw_line(x-7,y+7,x-30,y,color)
        draw_line(x+7,y+7,x,y+30,color)
        draw_line(x+7,y+7,x+30,y,color)
        draw_line(x-7,y-7,x-30,y,color)
        draw_line(x-7,y-7,x,y-30,color)
        draw_line(x+7,y-7,x+30,y,color)
        draw_line(x+7,y-7,x,y-30,color)
        
def bullet_impact():
    global bots, shooter_bullets
    for i in shooter_bullets:
        x = i[0]
        y = i[1]
        count = 0
        for j in bots:
            X_min = j[0]-60
            X_max = j[0]+60
            Y_min = j[1]-60
            Y_max = j[1]+60
            if X_min <= x <= X_max: # if it hits destory the bubble and generate a new one
                if Y_min <= y <= Y_max:
                    shooter_bullets.remove(i)
                    idx = bots.index(j)
                    bots.remove(j)
                    bots.insert(idx,bot_range(idx))
                    return

def bot_bullets_():
    global bot_bullets
    glPointSize(4)
    color = (1,0.2,0.2)
    for i in bot_bullets:
        x,y = i.cord()
        draw_circle(x,y,3,color)

def shooter_impact():
    global bots,bot_bullets,shooter_x,life
    X = shooter_x
    Y = 130
    for i in bots:
        x,y = i[0],i[1]
        if x-30 < X < x+30:
            if y-30 < Y < y+30:
                life -= 1
                idx = bots.index(i)
                bots.remove(i)
                bots.insert(idx,bot_range(idx))
                glutPostRedisplay()
                break
    for j in bot_bullets:
        x,y = j.cord()
        if x-20 < X < x+20:
            if y-20 < Y < y+20:
                life -= 1
                bot_bullets.remove(j)
                del j
                glutPostRedisplay()
                break
    return


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
    def __init__(self,x,y):
        global shooter_x
        self.x = x
        self.y = y
        x2 = shooter_x
        y2 = 100
        self.m = (y2-y)/(x2-x)
    def position(self):
        self.x = self.x-((1/self.m)*3)
        self.y = self.y -3
        return self.x, self.y
    def cord(self):
        return self.x, self.y

def restart():
    global shooter_x,level,shooter_bullets,bots,bot_bullets,life,pause
    pause = True
    life = 3
    shooter_x = 500
    level = 1
    bots = []
    shooter_bullets = []
    bot_bullets = []
    for i in range(5):
        bots.append(bot_range(i))
    glutPostRedisplay()

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
    global score,pause
    if button == GLUT_LEFT_BUTTON and state == GLUT_DOWN:
        y = 1000 - y
        print(x,y)

        if 910 <= x <= 930 and 955 <= y <= 975:  # pay_pause
            if pause == True:
                pause = False
            else:
                pause = True

        elif 955 <= x <= 975 and 955 <= y <= 975:  # Cross button
            print("Goodbye")
            print("Final Score:", score)
            glutLeaveMainLoop()

        elif 850 <= x <= 880 and 955 <= y <= 975:
            print("Starting Over")
            restart()


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

def animate_bot_movement(value):
    global bots,life
    for i in range(len(bots)):
        if bots[i][1]-2 < 90:
            life -= 1
            bots.pop(i)
            bots.insert(i,bot_range(i))
            glutPostRedisplay()
        bots[i] = (bots[i][0],bots[i][1]-2)
        glutPostRedisplay()
    glutTimerFunc(100,animate_bot_movement,0)

def bot_bullet_generation(value):
    global bots,bot_bullets,shooter_x
    X = shooter_x
    Y = 100
    r = random.randint(0,4)
    x = bots[r][0]
    y = bots[r][1]
    dx = abs(X-x)
    dy = abs(Y-y)
    if dx>=dy:
        pass
    else:
        obj = nonplayer_bullet(x,y)
        bot_bullets.append(obj)
    glutTimerFunc(2000,bot_bullet_generation,0)
    
def bot_bullet_animation(value):
    global bot_bullets
    for i in bot_bullets:
        x,y = i.position()
        if y < 60:
            bot_bullets.remove(i)
            del i
            break
    glutPostRedisplay()
    glutTimerFunc(1,bot_bullet_animation,0)

def life_checker(value):
    global life
    if life == 0:
        restart()
        return
    glutTimerFunc(1, life_checker, 0)

#Screen Properties and Object display
#----------------------------------------------------------------------------##----------------------------------------------------------------------------#
def iterate():
    glViewport(0, 0, 1000, 1000)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 1000, 0.0, 1000, 0.0, 1.0)
    glMatrixMode (GL_MODELVIEW)
    glLoadIdentity()

for i in range(5):
    bots.append(bot_range(i))

def showScreen():
    global life
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glPointSize(2)
    glClearColor(1.0, 1.0, 1.0, 1.0)
    color = (1,1,1)
    if pause == True:
        iterate()
        top_bar()
        bottom_bar()
        pause_resume()
        cross()
        back()
        pause_title()
        glutSwapBuffers()
    else:
        
        iterate()
        top_bar()
        bottom_bar()
        shooter()
        shooter_bullet()
        bot_army()
        bullet_impact()
        bot_bullets_()
        shooter_impact()
        pause_resume()
        cross()
        back()
        text(str(life), (100,950), color)
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
glutTimerFunc(100,animate_bot_movement,0)
glutTimerFunc(1,bot_bullet_animation,0)
glutTimerFunc(2000,bot_bullet_generation,0)
glutTimerFunc(1, life_checker, 0)
glutMainLoop()