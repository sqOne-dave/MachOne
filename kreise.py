import pgzrun
import random

WIDTH = 3840
HEIGHT = 1080

x_kor = [WIDTH // 4, (WIDTH // 4) * 2, (WIDTH // 4) * 3]
y_kor = [HEIGHT / 2, HEIGHT / 2, HEIGHT / 2]

red = [255, 0, 0]
green = [0, 255, 0]
blue = [0, 0, 255]
c_kor = [(x_kor[0], y_kor[0]), (x_kor[1], y_kor[1]), (x_kor[2], y_kor[2])]
c_farbe = [[red[0], green[0], blue[0]], [red[1], green[1], blue[1]], [red[2], green[2], blue[2]]]
got_direction = [False, False, False]
radius = 20

change_x_kor = [0, 0, 0]
change_y_kor = [0, 0, 0]

def draw():
    global c_kor, c_farbe, radius
    for i in range(3):
        screen.draw.filled_circle(c_kor[i], radius, c_farbe[i])

def update():
    c = 0
    i = 0
    x = 0
    while c <= 2:
        check_for_bounce(c)
        c += 1
    while i <= 2:
        reise_c(i)
        i += 1
    while x <= 2:
        farbwechsel(x)
        x += 1

def reise_c(i):
    global c_kor, x_kor, y_kor, got_direction, change_x_kor, change_y_kor
    if got_direction[i] == False:
        change_x_kor[i] = random.randint(-5, 5)
        change_y_kor[i] = random.randint(-5, 5)
        got_direction[i] = True

    x_kor[i] = x_kor[i] + change_x_kor[i]
    y_kor[i] = y_kor[i] + change_y_kor[i]
    c_kor[i] = (x_kor[i], y_kor[i])

def check_for_bounce(c):
    global x_kor, y_kor, radius, got_direction, WIDTH, HEIGHT
    if x_kor[c] - radius <= 0:
        bounce = True
        where = ('left')
    elif x_kor[c] + radius >= WIDTH:
        bounce = True
        where = ('right')
    elif y_kor[c] - radius <= 0:
        bounce = True
        where = ('top')
    elif y_kor[c] + radius >= HEIGHT:
        bounce = True
        where = ('bottom')
    else:
        bounce = False
        got_direction[c] = False
    if bounce == True:
        got_direction[c] = True
        change_direction(where, c)

def change_direction(where, c):
    global change_x_kor, change_y_kor
    if where == 'left' or 'right':
        change_x_kor[c] = change_x_kor[c] * -1
    if where == 'top' or 'bottom':
        change_y_kor[c] = change_y_kor[c] * -1
    bounce = False
    print(change_x_kor[c], change_y_kor[c])

def farbwechsel(x):
    global c_farbe
    m_o_w = random.randint(0, 1)
    number = c_farbe[x][x]
    if m_o_w == 0 and number <= 254:
        number += 1
    elif number >= 1:
        number -= 1
    if m_o_w == 1 and number >= 1:
        number -= 1
    elif number <= 254:
        number += 1
    c_farbe[x][x] = number
    mix_colors()

def mix_colors():
    global c_farbe, c_kor, radius, screen
    for i in range(3):
        for j in range(i + 1, 3):
            if c_kor[i][0] + radius >= c_kor[j][0] - radius and c_kor[i][0] - radius <= c_kor[j][0] + radius and \
               c_kor[i][1] + radius >= c_kor[j][1] - radius and c_kor[i][1] - radius <= c_kor[j][1] + radius:
                mixed_color = [
                    (c_farbe[i][0] + c_farbe[j][0]) // 2,
                    (c_farbe[i][1] + c_farbe[j][1]) // 2,
                    (c_farbe[i][2] + c_farbe[j][2]) // 2
                ]
                screen.surface.set_at((int((c_kor[i][0] + c_kor[j][0]) / 2), int((c_kor[i][1] + c_kor[j][1]) / 2)), mixed_color)

pgzrun.go()
