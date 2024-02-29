from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import random

global pause, shooter, circles, bullet, life, score
pause = False
shooter = 300
circles = []
bullet = []
life = 3
score = 0

def random_origin_x(i):
    return random.randint((120 * i)+20,120 * (i+1)-20)
    
def random_origin_y():
    return random.randint(400,500)

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
        line_algo(x,y,x,y-50,r,g,b)
        line_algo(x+30,y,x+30,y-50,r,g,b)

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
    if abs(dx) >= abs(dy):
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
    
def iterate(): # for screen frame rate
    glViewport(0, 0, 600, 600)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 600, 0.0, 600, 0.0, 1.0)
    glMatrixMode (GL_MODELVIEW)
    glLoadIdentity()
    
def circle_zones(x, y, x0, y0): #x,y are points generated for each zone and x0,y0 is the origin of circle
    glBegin(GL_POINTS)
    glColor3f(1,0,0)
    glVertex2f(x + x0, y + y0)
    glVertex2f(y + x0, x + y0)
    glVertex2f(y + x0, -x + y0)
    glVertex2f(x + x0, -y + y0)
    glVertex2f(-x + x0, -y + y0)
    glVertex2f(-y + x0, -x + y0)
    glVertex2f(-y + x0, x + y0)
    glVertex2f(-x + x0, y + y0)
    glEnd()

def circle_algo(x0,y0,r): #midpoint circle drawing algorithm
    d = 1 - r
    x = 0
    y = r
    while x <= y: 
        circle_zones(x, y, x0, y0) # x0, y0 is the original center of the circle
        if d >= 0: # for South East Pixel
            d = d + 2*x - 2*y + 5
            x += 1
            y -= 1
        else: # for East Pixel
            d = d + 2*x + 3
            x += 1

def draw_shooter():
    global pasue, shooter
    x = shooter
    y = 25
    r = 15
    circle_algo(x,y,r)

def draw_circle():
    global pause, circles
    if pause == True:
        j = 0
    else:
        j = 2
    for i in range(len(circles)):
        x = circles[i][0]
        y = circles[i][1]
        circles[i][1]-=j
        circle_algo(x,y,20)
    
def draw_bullet():
    global pause, bullet
    if pause == True:
        j = 0
    else:
        j = 10
    for i in range(len(bullet)):
        x = bullet[i][0]
        y = bullet[i][1]
        bullet[i][1]+=j
        circle_algo(x,y,10)  

def shot_checker():
    global circles, bullet, life, score
    for i in bullet:
        x = i[0]
        y = i[1]
        count = 0
        for j in circles:
            X_min = j[0]-30
            X_max = j[0]+30
            Y_min = j[1]-30
            Y_max = j[1]+30
            if X_min <= x <= X_max:
                if Y_min <= y <= Y_max:
                    bullet.remove(i)
                    circles.remove(j)
                    circles.insert(count,[random_origin_x(count),random_origin_y()])
                    score+=1
                    print('Score =', score)
                    return
            elif j[1] < 50:
                life-=1
                print('Life Left =',life)
                circles.remove(j)
                circles.insert(count,[random_origin_x(count),random_origin_y()])
                if life == 0:
                    print('Game Over!')
                    restart()
                return
            count+=1
            #my_list.remove(value_to_remove)

def draw_text(text):
    glColor3f(1,1,1)
    glRasterPos2f(10, 580)
    for char in text:
        glutBitmapCharacter(GLUT_BITMAP_HELVETICA_18, ord(char))

def generate_circle():
    global cicles
    for i in range(5):
        circles.append([random_origin_x(i),random_origin_y()])

def restart():
    global pause, circles, bullet, shooter, life, score
    shooter = 300
    pause = True
    circles.clear()
    bullet.clear()
    generate_circle()
    life = 3
    score = 0

def keyboardListener(key,x,y):
    global pause, bullet, shooter
    if pause == True:
        return
    if key == b' ':
        bullet.append([shooter,50])

def specialKeyListener(key,x,y):
    global pause, shooter
    if pause == True:
        return
    if key == GLUT_KEY_RIGHT:
        shooter+=7
        if shooter > 600:
            shooter-=7
    elif key == GLUT_KEY_LEFT:
        shooter-=7
        if shooter < 0:
            shooter+=7

def mouseListener(button,state,x,y): # use mouse to press 3 positions of the screen, back pause and close
    global pause
    x1,x2,x3 = 0,250,500
    x,y = convert_coordinate(x,y)
    if button == GLUT_LEFT_BUTTON and state == GLUT_DOWN:
        if x1<=x<=(x1+100) and 500<=y<=600: #for restart button
            restart()
            print('Restart')
        elif x3<=x<=(x3+100) and 500<=y<=600: #for close button
            glutLeaveMainLoop()
        elif x2<=x<=(x2+100) and 500<=y<=600: #for pause button
            if pause == False:
                pause = True
                glutPostRedisplay()
            else:
                pause = False
                glutPostRedisplay()

def animate(value):
    glutPostRedisplay()
    glutTimerFunc(50,animate,0)   

def showScreen(): # display everything
    global circles, pause
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glEnable(GL_POINT_SMOOTH)  # Enable point antialiasing
    glPointSize(1)
    iterate()
    if pause == False:
        draw_circle()
    draw_shooter()
    draw_bullet()
    back()
    pause_play()
    cross()
    shot_checker()
    draw_text(f'''Score = {str(score)} Life = {str(life)}''')
    glutSwapBuffers()

glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(600, 600) #window size
glutInitWindowPosition(0, 0)
wind = glutCreateWindow(b"OpenGL Coding Practice") #window name
generate_circle()
glutTimerFunc(50,animate,0)
glutDisplayFunc(showScreen)
glutKeyboardFunc(keyboardListener)
glutSpecialFunc(specialKeyListener)
glutMouseFunc(mouseListener)
glutMainLoop()