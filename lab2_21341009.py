from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import random

W_Width, W_Height = 500,500

points = []
move_x = 0
diamond_y = 0
diamond_x = 0
diamond_state = True
score = 0
plate_pos = ()
game_state = "playing"
play_hitbox = [(-14, 237), (34, 192)]
cross_hitbox = [(-14+200, 237), (34+200, 192)]
back_hitbox = [(-14-220, 237), (34-200, 192)]
#s

def convert_coordinate(x, y):
    global W_Width, W_Height
    a = x - (W_Width/2)
    b = (W_Height/2) - y
    return a,b


def specialKeyListener(key, x, y):
    global move_x, game_state
    if game_state == "playing":
        if key == GLUT_KEY_RIGHT:
            if move_x <= 166:
                move_x += 4

        elif key == GLUT_KEY_LEFT:
            if move_x >= -166:
                move_x -= 4

    glutPostRedisplay()


def mouseListener(button, state, x, y):  # /#/x, y is the x-y of the screen (2D)
    global play_hitbox, game_state
    if button == GLUT_RIGHT_BUTTON:
        if state == GLUT_DOWN:
            m, n = convert_coordinate(x, y)
            points.append([m, n])
            print(points)

    if button == GLUT_LEFT_BUTTON:
        if state == GLUT_DOWN:
            p, q = convert_coordinate(x, y)
            if p >= play_hitbox[0][0] and p <= play_hitbox[1][0] and q <= play_hitbox[0][1] and q >= play_hitbox[1][1]:
                if game_state == "playing":
                    game_state = "pause"
                elif game_state == "pause":
                    game_state = "playing"
                    glutTimerFunc(100, fall_diamond, 0)
                    glutTimerFunc(3000, spawn_diamond, 0)
                elif game_state == "over":
                    game_state = "playing"
                    glutTimerFunc(100, fall_diamond, 0)
                    glutTimerFunc(3000, spawn_diamond, 0)
            elif p >= cross_hitbox[0][0] and p <= cross_hitbox[1][0] and q <= cross_hitbox[0][1] and q >= cross_hitbox[1][1]:
                glutLeaveMainLoop()
            elif p >= back_hitbox[0][0] and p <= back_hitbox[1][0] and q <= back_hitbox[0][1] and q >= back_hitbox[1][1]:
                game_state = "restart"
                print("Restarting")


    glutPostRedisplay()


def findZone(x1, y1, x2, y2):
    dy = y2-y1
    dx = x2-x1
    if abs(dx) > abs(dy):
        if dx > 0 and dy > 0:
            return 0
        elif dx < 0 and dy > 0:
            return 3
        elif dx < 0 and dy < 0:
            return 4
        else:
            return 7
    else:
        if dx > 0 and dy > 0:
            return 1
        elif dx < 0 and dy > 0:
            return 2
        elif dx < 0 and dy < 0:
            return 5
        else:
            return 6


def convertzones(x1, y1, zone, to_zero):
    if zone == 0:
        return x1, y1
    elif zone == 1:
        return y1, x1
    elif zone == 2 and to_zero == True:
        return y1, -x1
    elif zone == 2 and to_zero == False:
        return -y1, x1
    elif zone == 3:
        return -x1, y1
    elif zone == 4:
        return -x1, -y1
    elif zone == 5:
        return -y1, -x1
    elif zone == 6 and to_zero == True:
        return -y1, x1
    elif zone == 6 and to_zero == False:
        return y1, -x1
    elif zone == 7:
        return x1, -y1


def midpointlinealgo(x1, x2, y1, y2):
    zone = findZone(x1, y1, x2, y2)

    glVertex2f(x1, y1)

    x1, y1 = convertzones(x1, y1, zone, True)
    x2, y2 = convertzones(x2, y2, zone, True)
    dy = y2 - y1
    dx = x2 - x1
    d = 2 * dy - dx
    while True:
        if x1 == x2 and y1 == y2:
            break
        if d > 0:
            d = d + 2 * dy - 2 * dx
            x1 += 1
            y1 += 1
            x1, y1 = convertzones(x1, y1, zone, False)

            glVertex2f(x1, y1)

            x1, y1 = convertzones(x1, y1, zone, True)
        else:
            d = d + 2 * dy
            x1 += 1
            x1, y1 = convertzones(x1, y1, zone, False)

            glVertex2f(x1, y1)

            x1, y1 = convertzones(x1, y1, zone, True)


def draw_points():
    global move_x
    if len(points) < 2:
        pass
    else:
        for i in range(0, len(points)-1, 2):
            x1 = points[i][0]
            x2 = points[i+1][0]
            y1 = points[i][1]
            y2 = points[i+1][1]
            midpointlinealgo(x1, x2, y1, y2)


def spawn_diamond(_):
    global diamond_x, diamond_y, game_state, score
    if game_state == "over":
        score = 0
    elif game_state == "playing":
        if diamond_y == -290:
            diamond_y = 0
            diamond_x = random.randint(-240, 240)
    elif game_state == "restart":
        game_state = "playing"
        score = 0
        diamond_y = 0
        diamond_x = random.randint(-240, 240)
        glutTimerFunc(1000, fall_diamond, 0)

    glutPostRedisplay()
    glutTimerFunc(10, spawn_diamond, 0)


def fall_diamond(_):
    global diamond_y
    if game_state == "playing":
        if diamond_y > -291:
            diamond_y -= 1
        glutPostRedisplay()
        glutTimerFunc(10, fall_diamond, 0)


def diamond():
    global diamond_y, plate_pos, diamond_x
    glBegin(GL_POINTS)
    glColor3f(0, 1, 1)
    midpointlinealgo(0 + diamond_x, -12 + diamond_x, 150+diamond_y, 125+diamond_y)
    midpointlinealgo(-12 + diamond_x, 0 + diamond_x, 125+diamond_y, 100+diamond_y)
    midpointlinealgo(0 + diamond_x, 12 + diamond_x, 100+diamond_y, 125+diamond_y)
    midpointlinealgo(12 + diamond_x, 0 + diamond_x, 125+diamond_y, 150+diamond_y)
    glEnd()


def game():
    global plate_pos, score, diamond_y, game_state, diamond_x
    if plate_pos[0]<diamond_x and plate_pos[1]>diamond_x and diamond_y == -289:
        score += 1
        print("Score:", score)
    elif (plate_pos[0]>diamond_x or plate_pos[1]<diamond_x) and diamond_y == -289:
        game_state = "over"
        diamond_y -= 1
        print("Game over! Score:", score)
        score = 1


def pause_button():
    glBegin(GL_POINTS)
    glColor3f(0, 0, 1)
    midpointlinealgo(-14, -14, 237, 202)
    midpointlinealgo(14, 14, 237, 202)
    glEnd()


def cross_button():
    glBegin(GL_POINTS)
    glColor3f(0, 1, 0)
    midpointlinealgo(195, 231, 237, 202)
    midpointlinealgo(231, 195, 237, 202)
    glEnd()


def back_button():
    glBegin(GL_POINTS)
    glColor3f(1, 0, 0)
    midpointlinealgo(-216, -241, 237, 215)
    midpointlinealgo(-241, -216, 215, 193)
    midpointlinealgo(-241, -200, 215, 215)
    glEnd()


def play_button():
    glBegin(GL_POINTS)
    glColor3f(0, 0, 1)
    midpointlinealgo(-10, -10, 237, 193)
    midpointlinealgo(-10, 34, 193, 214)
    midpointlinealgo(34, -10, 214, 237)
    glEnd()


def plate():
    global move_x, plate_pos
    glBegin(GL_POINTS)
    glColor3f(1, 1, 0)
    plate_pos = (-84 + move_x, 84+ move_x)
    midpointlinealgo(-84 + move_x, 84+ move_x, -191, -191)
    midpointlinealgo(-84+ move_x, -70+ move_x, -191, -210)
    midpointlinealgo(-70+ move_x, 70+ move_x, -210, -210)
    midpointlinealgo(70+ move_x, 84+ move_x, -210, -191)
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
    # midpointlinealgo(x1, x2, y1, y2)

    glBegin(GL_POINTS)
    glColor3f(1, 0, 0)
    draw_points()
    glEnd()
    diamond()

    if game_state == "playing":
        pause_button()
    else:
        play_button()

    plate()
    cross_button()
    back_button()
    game()
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
wind = glutCreateWindow(b"Game") #window name
init()
glutDisplayFunc(display)
# glutIdleFunc(animate)
# glutTimerFunc(speed, animate, 0)

glutTimerFunc(100, fall_diamond, 0)
glutTimerFunc(30, spawn_diamond, 0)

# glutKeyboardFunc(keyboardListener)
glutSpecialFunc(specialKeyListener)
glutMouseFunc(mouseListener)
glutMainLoop()