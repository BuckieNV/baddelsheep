
#Libraries:

import pygame
import random
import time
import math

#Initation of PyGame:

pygame.init()

#Screen config:

display_width = 800
display_height = 600
screen = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption("Baddelsheep")

#Colours:

BLACK    = (   0,   0,   0)
WHITE    = ( 255, 255, 255)
GREEN    = (   0, 255,   0)
RED      = ( 255,   0,   0)
BLUE     = (   0,   0, 255)

global rectColour
global m_x, m_y # Mouse x and y positions
global circ1_x, circ1_y  # x and y positions for circle 1
global follower_x, follower_y  # x and y position offsets for "follower" rectangle
global displayImage
displayImage = False # No image stuff unless user presses I key.

#Crusor Coordinates:
m_x, m_y = pygame.mouse.get_pos()


#Battleship Sprite:
bb = pygame.image.load("yamato.png")
bb_rect = bb.get_rect()
bb_prex = display_width/2
bb_prey = display_height/2
bb_x = bb_prex - 0.5 * bb_rect.width
bb_y = bb_prey - 0.5 * bb_rect.height


 
def yamato(bb_x,bb_y):
    screen.blit(bb, (bb_x, bb_y))

    #Turret I:
def turret1(bb_x, bb_y):
    screen.blit(turret_1, (bb_x - 300, bb_x + 10))    

turret_1 = pygame.image.load("turret_bb1.png")


    #Turret II:
def turret2(bb_x, bb_y):

    screen.blit(turret_2, (bb_x + 100, bb_y + 10))
turret_2 = pygame.image.load("turret_bb2.png")


    
keepgoing = True
 
clock = pygame.time.Clock()

# Set initial position for circle 1
circ1_x = 200
circ1_y = 100




while keepgoing:

    #Background:
    screen.fill(WHITE)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            keepgoing = False
            
    

        #if event.type == pygame.MOUSEMOTION:
            #x1, y1 = pygame.mouse.get_pos()
            #x2, y2 = bb_rect.centerx, bb_rect.centery #added
            #dx, dy = x2 - x1, y2 - y1
            #rads = math.atan2(dx, dy)
            #degs = math.degrees(rads)
            #print (degs)
            #pygame.transform.rotate(bb, degs)
 
    # --- Drawing code should go here

    

    keys = pygame.key.get_pressed()
    if (keys[pygame.K_RIGHT] == True):
        bb_x += 5
    if (keys[pygame.K_LEFT] == True):
        bb_x -= 5
    if (keys[pygame.K_UP] == True):
        bb_y -= 5
    if (keys[pygame.K_DOWN] == True):
        bb_y += 5
    pygame.draw.circle(screen, GREEN, [circ1_x, circ1_y], 25, 3)

    m_x, m_y = pygame.mouse.get_pos()

    if (keys[pygame.K_x] == True):
        print (bb_rect.center)
        print (m_x, m_y)


        
    turret1(bb_x, bb_y)
    turret2(bb_x, bb_y)
    yamato(bb_x,bb_y)


    

    pygame.display.flip()
    
    clock.tick(60)

pygame.quit()
