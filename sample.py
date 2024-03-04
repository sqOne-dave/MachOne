import pgzrun
import pygame
import time 

game_hero = Actor('mbros')
game_hero.pos = 500,500

WIDTH = 1000
HEIGHT = game_hero.height + 500


def draw(): 
    screen.clear()
    game_hero.draw()
    screen.blit('space')

def update():
    
    if keyboard.left:
        game_hero.x -= 2
    elif keyboard.right: 
        game_hero.x += 2
    elif keyboard.up:
        game_hero.y -= 2
    elif keyboard.down:
        game_hero.y +=2

pgzrun.go()
