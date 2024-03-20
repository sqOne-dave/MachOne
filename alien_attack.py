import pgzrun
import time


WIDTH = 1000
HEIGHT = 500

ship = Actor('ship',(500,400))
rocket_fire = Actor('rocket_fire',(500,400))
alien = Actor('alien',center=(500,100))

def draw():
    screen.clear()
    screen.blit('space_back',(0,0))
    rocket_fire.draw()
    ship.draw()
    alien.draw()


def update():
    if alien.left > 0 and alien.right < 1000:
        alien.left += 1
    else: alien.left -=1
    
    if keyboard.left and ship.left > 0 :
        ship.x -= 3
    if keyboard.right and ship.right < 1000:
        ship.x += 3
    if keyboard.space:
        if rocket_fire.bottom >= 1:
            if rocket_fire.y == 500:
                rocket_fire.x = ship.x
            else:
                rocket_fire.y -= 5
        if rocket_fire.bottom <=0:
            rocket_fire.y = 500
            rocket_fire.y -= 5


    
pgzrun.go()
