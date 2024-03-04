import pgzrun
import time

WIDTH = 1000
HEIGHT = 500

points = 0
points_txt = "Points: " + str(points)

ship = Actor('ship',(500,400))
rocket_fire = Actor('before_rocket_fire',(500,400))
alien = Actor('alien',center=(100,100))

def draw():
    global points
    screen.clear()
    screen.blit('space_back',(0,0))
    ship.draw()
    rocket_fire.draw()
    alien.draw()
    screen.draw.text(points_txt, (5, 5), owidth=1, ocolor="black")

def move_rocket(ship):
    if keyboard.left and ship.left > 0:
        ship.x -= 5
        if rocket_fire.y == 400:
            rocket_fire.x -= 5
    if keyboard.right and ship.right < 1000:
        ship.x += 5
        if rocket_fire.y == 400:
            rocket_fire.x += 5

def rocket_flying(rocket_fire):
    if keyboard.space:
        rocket_fire.y -= 10
        rocket_fire.image = 'rocket_fire'
    elif rocket_fire.bottom > 1 and rocket_fire.bottom < 400:
        rocket_fire.y -= 10
    elif rocket_fire.bottom < 0:
        rocket_fire.image = 'rocket_fire'
        rocket_fire.y = 400
        rocket_fire.x = ship.x



def increase_points():
    global points
    points += 1
    print(points)
    
def move_alien(alien):
    global points
    if alien.left <= 999:
        alien.x += 3
    elif alien.left >= 1000:
        alien.x = 0   
    collide = rocket_fire.colliderect(alien)
    if collide == False:
        #print("You missed me!")
        alien.image = 'alien'
    elif collide == True:
        alien.image = 'pi'
        rocket_fire.image = 'before_rocket_fire'
        rocket_fire.y = 400
        rocket_fire.x = ship.x
        increase_points() 

def update():
    global points,points_txt
    draw()
    screen.draw.text(points_txt, (5, 5), owidth=1, ocolor="black")
    move_rocket(ship)
    rocket_flying(rocket_fire)
    move_alien(alien)
    
pgzrun.go()
