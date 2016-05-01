import pygame
import random
pygame.init()

black =(0,0,0)
white =(255,255,255)
green =(0,255,0)
red = (255,0,0)
light_red = (255,100,100)
yellow = (255,255,0)

size =(700,500)
screen = pygame.display.set_mode(size)

done = False

clock = pygame.time.Clock()
snows = []
stars = []
pygame.mouse.set_visible(0)

stop= False

def show_time(screen, time):
    font = pygame.font.Font(None, 30)
    text = font.render("{0:.2f}".format(time), 1, green)
    screen.blit(text, (500, 457))

def draw_stick_figure(screen,color, x, y):
    pygame.draw.rect(screen,color,[x,y,10,10])
x_speed = 0
y_speed = 0

# Current position
x_coord = 10
y_coord = 10

def draw_star(scree,color,x,y):
    pygame.draw.rect(screen,color,[x,y,10,10])

for i in range(100):
    x = random.randrange(0,700)
    y = random.randrange(0,500)
    v_y = 1
    v_x = random.randrange(-1,1)
    snows.append([x, y, v_y, v_x])

for y in range(10):
    x = random.randrange(0,700)
    y = random.randrange(0,500)
    v_y = 1
    v_x = 0
    stars.append([x, y, v_y, v_x])

count = 1
life = 2
transparent = False
hit_time=0
level_time= 600
level = 1
while not done:
    screen.fill(black)
    if count % level_time == 0:
        level += 1
        print("level: ", level)
        for snow in snows:
            v_y = level
            v_x = random.randrange(-1*level,1*level)
            snow[2] = v_y
            snow[3] = v_x
    if transparent:
        hit_time += 1
        if hit_time ==180:
            transparent = False
            hit_time = 0

    for i in range(0, life):
        pygame.draw.circle(screen,green,[600-25*i,40],10)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print("Quit!!")
            done = True
        elif event.type == pygame.KEYDOWN:
            # Figure out if it was an arrow key. If so
            # adjust speed.
            if event.key == pygame.K_LEFT:
                x_speed = -3
            elif event.key == pygame.K_RIGHT:
                x_speed = 3
            elif event.key == pygame.K_UP:
                y_speed = -3
            elif event.key == pygame.K_DOWN:
                y_speed = 3

        # User let up on a key
        elif event.type == pygame.KEYUP:
            # If it is an arrow key, reset vector back to zero
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                x_speed = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                y_speed = 0

    if not stop:
        for snow in snows:
            # 충돌을 체크 하는 부분
            if snow[0] >= x_coord and snow[0] < x_coord +10 and snow[1] >= y_coord and snow[1] < y_coord+27 and not transparent:
                transparent = True

                life -= 1
                if life < 0:
                    stop = True
                    break
            pygame.draw.circle(screen,white,[snow[0], snow[1]],2)
            snow[1] += snow[2]
            snow[0] += snow[3]
            if snow[1] >500:
                snow[1] = 0
                snow[0] = random.randrange(0,700)
        stars2 = stars[:]
        for star in stars2:
            if star[0] >= x_coord and star[0] < x_coord + 10 and star[1] >= y_coord and star[1] < y_coord+27:
                stars.remove(star)
                x = random.randrange(0,700)
                y = random.randrange(0,500)
                v_y = 1
                v_x = 0
                stars.append([x, y, v_y, v_x])

        for star in stars:
            draw_star(screen,yellow,star[0],star[1])
            star[1] += star[2]
            star[0] += star[3]
            if star[1] >500:
                star[1] = 0
                star[0] = random.randrange(0,700)
        x_coord = x_coord + x_speed
        y_coord = y_coord + y_speed

        # --- Drawing Code

        # First, clear the screen to WHITE. Don't put other drawing commands
        # above this, or they will be erased with this command.
        if transparent:
            draw_stick_figure(screen,light_red, x_coord, y_coord)

        else:
            draw_stick_figure(screen,red, x_coord, y_coord)

        show_time(screen, count/60.0)
        pygame.display.flip()

    clock.tick(60)
    count +=1