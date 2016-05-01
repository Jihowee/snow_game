import pygame
import random
pygame.init()

black =(0,0,0)
white =(255,255,255)
green =(0,255,0)
red = (255,0,0)

size =(700,500)
screen = pygame.display.set_mode(size)

done = False

clock = pygame.time.Clock()
snows = []

for i in range(100):
    x = random.randrange(0,700)
    y = random.randrange(0,500)
    v_y = random.randrange(1,5)
    v_x = random.randrange(-3,3)

    snows.append([x, y, v_y, v_x])
count =0
while not done:
    screen.fill(black)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print("Quit!!")
            done = True
    for snow in snows:
        pygame.draw.circle(screen,white,[snow[0], snow[1]],2)
        snow[1] += snow[2]
        snow[0] += snow[3]
        if snow[1] >500:
            snow[1] = 0
            snow[0] = random.randrange(0,700)
        if count %60==0:
            snow[3] = -snow[3]


    pygame.display.flip()
    clock.tick(60)
    count +=1
