import pygame 
import random
import time

SCREEN_HEIGHT = 800
SCREEN_WIDTH = 1200
length_of_array = 50

def createPos():
    '''randomly generates height of multiple of 10 (visual diffrence) and appends in pos'''
    pos = []
    for x in range(length_of_array):
        y = int(random.randint(0,SCREEN_HEIGHT)//10)*10
        pos.append(y)
    return pos

def animate(pos,j):
    '''animates the lines , the jth line is colored green'''
    screen.fill("black")
    rf = SCREEN_WIDTH/len(pos)
    for x in range(len(pos)):
        if x == j:
            pygame.draw.line(screen,"green",(x*rf , SCREEN_HEIGHT),(x*rf,SCREEN_HEIGHT-pos[x]),width=int(rf)-1)
            #cause for some reason the origin in pygame is in top left

        else:
            pygame.draw.line(screen,"red",(x*rf , SCREEN_HEIGHT),(x*rf,SCREEN_HEIGHT-pos[x]),width=int(rf)-1)

def bubble_sort(pos):
    '''sorts, calls animate() and returns False if the sort is completed'''
    n = len(pos)
    for i in range(n):
        for j in range(0, n-i-1):
            if pos[j] > pos[j+1]:
                pos[j], pos[j+1] = pos[j+1], pos[j]

            pygame.display.flip()
            animate(pos,j+1) #passed j to  visualize current highest value

            clock.tick(120)     #limits the fps to 120 Hz
            for event in pygame.event.get():
                if event.type == pygame.QUIT:      #exit when 'x' icon is pressed
                    return False 
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        time.sleep(1)  #wacky pause mechanics  
    return False


screen = pygame.display.set_mode((SCREEN_WIDTH , SCREEN_HEIGHT))
clock = pygame.time.Clock()
screen.fill("black")
pos = createPos()
running = True

pygame.init()
while running:
    running = bubble_sort(pos)
pygame.quit()