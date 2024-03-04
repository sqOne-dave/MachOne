import pgzrun
import pygame
import time

game_hero = Actor('mbros')
game_hero.pos = 0,300
game_hero2 = Actor('alien')
game_hero2.pos = 1000,400

WIDTH = 1000
HEIGHT = game_hero.height + 200



def draw():
    screen.clear()
    screen.blit('space',(0,0))
    game_hero.draw()
    game_hero2.draw()
    
    

def update():
    game_hero.left += 5
    if game_hero.left > WIDTH:
        game_hero.right = 0
    elif game_hero2.left - game_hero.right <= 200:
        if game_hero2.left - game_hero.right >= 0:
            game_hero.y -= 5
        elif game_hero2.right - game_hero.left <= -1 and game_hero.y < 300 :
            game_hero.y += 5
    
    game_hero2.left -= 5
    if game_hero2.right < 0:
        game_hero2.left = 1000
    print("Hero",game_hero2.right - game_hero.left)

def on_mouse_down(pos):
    if game_hero.collidepoint(pos):
        game_hero.image = 'pi'
        """screen.draw.text("You got me!",(game_hero.x,game_hero.y + 50),color="white")"""
        print("You got me!")    
    else:
        print("Missed you looser!")
        game_hero.image = 'mbros'
        sounds.eep.play()
    



pgzrun.go()

