#CSE423 Project
#----------------------------------------------------------------------------##----------------------------------------------------------------------------#
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import random

#Global Variables
#----------------------------------------------------------------------------##----------------------------------------------------------------------------#
global shooter_x,level,shooter_bullets,bots,bot_bullets,life,health_cord,power_cord,power_i
power_i = 10
power_cord = []
health_cord = []
life = 3
shooter_x = 500
level = 1
bots = []
shooter_bullets = []
bot_bullets = []
pause = False
score = 0



#Display Objects on screen
#----------------------------------------------------------------------------##----------------------------------------------------------------------------#
def text(text, coordinate, color): #Naveya
    r = color[0]
    g = color[1]
    b = color[2]
    glColor3f(r,g,b)
    glRasterPos2f(coordinate[0], coordinate[1])
    for char in text:
        glutBitmapCharacter(GLUT_BITMAP_HELVETICA_18, ord(char))

def top_bar(): #Ramisa
    x = 0
    y = 1000
    glPointSize(5)
    color = (1, 0, 1)
    draw_line(x+10,y-10,x+990,y-10,color)
    draw_line(x+10,y-60,x+990,y-60,color)
    draw_line(x+10,y-10,x+10,y-60,color)
    draw_line(x+990,y-10,x+990,y-60,color)

def bottom_bar(): #Ramisa
    x = 0
    y = 70
    glPointSize(5)
    color = (1, 0, 1)
    color1 = (0,1,0)
    color2 = (0,1,1)
    draw_line(x+10,y-10,x+990,y-10,color)
    draw_line(x+10,y-60,x+990,y-60,color)
    draw_line(x+10,y-10,x+10,y-60,color)
    draw_line(x+990,y-10,x+990,y-60,color)
    text("* HEALTH GIVES YOU EXTRA LIFE", (20,40), color1)
    text("* POWER UP GIVES YOU EXTRA SPEED", (20,20), color2)

def health(): #Mahde
    global health_cord
    glPointSize(3)
    color = (0,1,0)
    for i in health_cord:
        x = i[0]
        y = i[1]
        draw_line(x-15,y-5,x-5,y-5,color)
        draw_line(x-15,y-5,x-15,y+5,color)
        draw_line(x-15,y+5,x-5,y+5,color)
        draw_line(x-5,y+5,x-5,y+15,color)
        draw_line(x-5,y+15,x+5,y+15,color)
        draw_line(x+5,y+15,x+5,y+5,color)
        draw_line(x+5,y+5,x+15,y+5,color)
        draw_line(x+15,y+5,x+15,y-5,color)
        draw_line(x+5,y-5,x+15,y-5,color)
        draw_line(x+5,y-5,x+5,y-15,color)
        draw_line(x-5,y-15,x+5,y-15,color)
        draw_line(x-5,y-5,x-5,y-15,color)

def pause_title(): #Naveya
    if pause == True:
        color = (0.75,0.75,0)
        text("GAME PAUSE", (450,500), color)
        draw_line(400,450,400,570,color)
        draw_line(620,450,620,570,color)
        draw_line(400,570,620,570,color)
        draw_line(400,450,620,450,color)

def pause_resume(): #Naveya
    #global pause
    color = (0.75,0.75,0)
    glPointSize(3)
    if pause:
        draw_line(910,975,930,965,color)
        draw_line(910,955,930,965,color)
        draw_line(910,975,910,955,color)
    else:
        draw_line(910,975,910,955,color)
        draw_line(920,975,920,955,color)

def back(): #Naveya
    color = (0.2,0.7,1)
    glPointSize(3)
    draw_line(850, 965, 880, 965, color)
    draw_line(850, 965, 860, 975, color)
    draw_line(850, 965, 860, 955, color)

def cross(): #Naveya
    color = (1,0.2,0.2)
    glPointSize(3)
    draw_line(955,955,975,975,color)
    draw_line(955,975,975,955,color)

def shooter(): #Ramisa
    global shooter_x
    x = shooter_x
    y = 130
    color = (0.4,0.2,1)
    color1 = (0.1,0.5,1)
    glPointSize(3)
    draw_line(x,y,x-25,y-50,color)
    draw_line(x,y,x+25,y-50,color)
    draw_line(x-25,y-50,x+25,y-50,color)
    draw_line(x-13,y-25,x-50,y-60,color)
    draw_line(x+13,y-25,x+50,y-60,color)
    draw_line(x-50,y-60,x-25,y-50,color)
    draw_line(x+50,y-60,x+25,y-50,color)
    glPointSize(2)
    draw_line(x,y+10,x-10,y-5,color1)
    draw_line(x,y+10,x+10,y-5,color1)
    draw_line(x-10,y-5,x,y,color1)
    draw_line(x+10,y-5,x,y,color1)
    glPointSize(4)
    draw_line(x-30,y-40,x-30,y-30,color1)
    draw_line(x+30,y-40,x+30,y-30,color1)

def shooter_bullet(): #Mahde
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
        
def power_up(): #Mahde
    global power_cord
    glPointSize(3)
    color = (0,1,1)
    for i in power_cord:
        x = i[0]
        y = i[1]
        draw_line(x-12,y-5,x,y,color)
        draw_line(x,y,x+12,y-5,color)
        y -= 7
        draw_line(x-12,y-5,x,y,color)
        draw_line(x,y,x+12,y-5,color)
        y -= 7
        draw_line(x-12,y-5,x,y,color)
        draw_line(x,y,x+12,y-5,color)
    
def bot_range(i): #Mahde
    i = 200*(i+1)
    x1 = i-170
    x2 = i-30
    y1 = 800
    y2 = 900
    x = random.randint(x1,x2)
    y = random.randint(y1,y2)
    return (x,y)

def bot_army(): #Ramisa
    global bots
    for i in bots:
        x = i[0]
        y = i[1]
        r = 30
        color = (0.7, 0.2, 0.0)
        glPointSize(4)
        draw_circle(x,y,r,color)
        draw_circle(x,y,10,color)
        color = (1,0,0)
        draw_line(x-7,y+7,x,y+30,color)
        draw_line(x-7,y+7,x-30,y,color)
        draw_line(x+7,y+7,x,y+30,color)
        draw_line(x+7,y+7,x+30,y,color)
        draw_line(x-7,y-7,x-30,y,color)
        draw_line(x-7,y-7,x,y-30,color)
        draw_line(x+7,y-7,x+30,y,color)
        draw_line(x+7,y-7,x,y-30,color)
        
def bullet_impact(): #Mahde
    global bots, shooter_bullets,health_cord,power_cord,score
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
                    score += 1
                    print(score)
                    shooter_bullets.remove(i)
                    idx = bots.index(j)
                    bots.remove(j)
                    bots.insert(idx,bot_range(idx))
                    r = random.random()
                    c = random.random()
                    if r <= 0.15:
                        health_cord.append((x,y))
                        return
                    if c <= 0.1:
                        power_cord.append((x,y))
                        return
                    return

def bot_bullets_(): #Ramisa
    global bot_bullets
    glPointSize(4)
    color = (1,0,0)
    for i in bot_bullets:
        x,y = i.cord()
        draw_circle(x,y,3,color)

def shooter_impact(): #mahde
    global bots,bot_bullets,shooter_x,life,power_i
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
    for k in health_cord:
        x,y = k[0],k[1]
        if x-20 < X < x+20:
            if y-20 < Y < y+20:
                life += 1
                if life > 5:
                    life -= 1
                health_cord.remove(k)
                del k
                glutPostRedisplay()
                break
    for l in power_cord:
        x,y = l[0],l[1]
        if x-20 < X < x+20:
            if y-20 < Y < y+20:
                power_i += 10
                if power_i > 40:
                    power_i -= 10
                power_cord.remove(l)
                del l
                glutPostRedisplay()
                break
    return

#Mid Point Line Drawing Algorithm
#----------------------------------------------------------------------------##----------------------------------------------------------------------------#
#Naveya
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
#Ramisa 
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
class nonplayer_bullet: #Mahde
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

def restart(): #Naveya
    global shooter_x,level,shooter_bullets,bots,bot_bullets,life,pause,health_cord,power_cord,power_i,score
    power_i = 10
    power_cord = []
    health_cord = []
    pause = True
    life = 3
    score = 0
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

def keyboardListener(key, x, y): #Mahde
    global shooter_x, shooter_bullets
    if key == b' ':
        shooter_bullets.append((shooter_x,160))
    glutPostRedisplay()

def specialKeyListener(key, x, y): #Mahde
    global shooter_x,power_i
    if key == GLUT_KEY_RIGHT:
        shooter_x+=power_i
        if shooter_x > 1000:
            shooter_x-=power_i
    elif key == GLUT_KEY_LEFT:
        shooter_x-=power_i
        if shooter_x < 0:
            shooter_x+=power_i

def mouseListener(button, state, x, y):#Naveya
    global score,pause,life
    if button == GLUT_LEFT_BUTTON and state == GLUT_DOWN:
        y = 1000 - y
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

def animate(value): #Naveya
    glutPostRedisplay()
    glutTimerFunc(1,animate,0)

def animate_shooter_bullets(value): #Mahde
    global shooter_bullets,power_i
    for i in range(0,len(shooter_bullets)):
        if shooter_bullets[i][1]+5 > 940:
            shooter_bullets.pop(i)
            glutPostRedisplay()
            break
        else:
            shooter_bullets[i] = (shooter_bullets[i][0],shooter_bullets[i][1]+power_i/2)
            glutPostRedisplay()
    glutTimerFunc(1,animate_shooter_bullets,0)

def animate_bot_movement(value): #Mahde
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

def bot_bullet_generation(value): #Mahde
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
    
def bot_bullet_animation(value): #Mahde
    global bot_bullets
    for i in bot_bullets:
        x,y = i.position()
        if y < 60:
            bot_bullets.remove(i)
            del i
            break
    glutPostRedisplay()
    glutTimerFunc(1,bot_bullet_animation,0)

def life_checker(value): #Ramisa
    global life
    if life == 0:
        restart()
        return
    glutTimerFunc(1, life_checker, 0)

def animate_health(value): #Mahde
    global health_cord
    for i in range(len(health_cord)):
        x,y = health_cord[i][0],health_cord[i][1]
        if y < 90:
            health_cord.pop(i)
            glutPostRedisplay()
            break
        else:
            health_cord[i] = (x,y-3)
            glutPostRedisplay()
    glutTimerFunc(100,animate_health,0)
        
def animate_power_up(value): #Mahde
    global power_cord
    for i in range(len(power_cord)):
        x,y = power_cord[i][0],power_cord[i][1]
        if y < 90:
            power_cord.pop(i)
            glutPostRedisplay()
            break
        else:
            power_cord[i] = (x,y-3)
            glutPostRedisplay()
    glutTimerFunc(100,animate_power_up,0)

#Screen Properties and Object display
#----------------------------------------------------------------------------##----------------------------------------------------------------------------#
def iterate(): #Naveya
    glViewport(0, 0, 1000, 1000)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 1000, 0.0, 1000, 0.0, 1.0)
    glMatrixMode (GL_MODELVIEW)
    glLoadIdentity()

for i in range(5): #Mahde
    bots.append(bot_range(i))

def showScreen(): #All
    global life
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glPointSize(2)
    glClearColor(0,0,0, 1.0)
    color = (1,1,1)
    color1 = (0,1,0)
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
        health()
        power_up()
        text("LIFE REMAINING: "+str(life), (20,960), color)
        text("SCORE: "+str(score), (450,960), color1)
        glutSwapBuffers()

glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(1000, 1000) #window size
glutInitWindowPosition(0, 0)
wind = glutCreateWindow(b"Project: Space shooter") #window name
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
glutTimerFunc(100,animate_health,0)
glutTimerFunc(100,animate_power_up,0)
glutMainLoop()