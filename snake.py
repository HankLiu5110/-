import pygame
import random
import time
import sys 

pygame.init()

width, height = 400, 400
game_screen = pygame.display.set_mode ((width, height))
pygame.display.set_caption("The Snake Game")

x, y = 200, 200
delta_x, delta_y = 10, 0

body_list = [(x, y)]

game_over = False

font = pygame.font.SysFont("AMGDT", 25)

clock = pygame.time.Clock()

food_x, food_y = random.randrange(0, width)//10*10, random.randrange(0, height)//10*10

def snake():
    global x, y, food_x, food_y, game_over
    x = (x + delta_x)%width
    y = (y + delta_y)%height
    
    if((x, y) in body_list):
        game_over = True
        return
    body_list.append((x, y))
    if(food_x == x and food_y == y):
        while((food_x, food_y) in body_list):
            food_x, food_y = random.randrange(0, width)//10*10, random.randrange(0, height)//10*10
    else:
        del body_list[0]

    
    game_screen.fill((0, 0, 0))
    pygame.draw.rect(game_screen, (255, 0, 0), [food_x, food_y, 10, 10])
    for (i, j) in body_list:
        pygame.draw.rect(game_screen, (255, 255, 255), [i, j, 10, 10])
    pygame.display.update()
    



while True:
    if game_over:
        game_screen.fill((0, 0, 0))
        msg = font.render("GAME OVER", True, (255, 255, 255))
        game_screen.blit(msg, [width//3, height//3])
        pygame.display.update()
        time.sleep(10)
        pygame.quit()
        sys.exit()
        
    events = pygame.event.get()
    for event in events:
        if(event.type == pygame.QUIT):
            pygame.quit()
            sys.exit()
        if(event.type == pygame.KEYDOWN):
            if(event.key == pygame.K_LEFT):
                if(delta_x != 10):
                    delta_x = -10
                delta_y = 0
            elif(event.key == pygame.K_RIGHT):
                if(delta_x != -10):
                    delta_x = 10
                delta_y = 0
            elif(event.key == pygame.K_UP):
                delta_x = 0
                if(delta_y != 10):
                    delta_y = -10
            elif(event.key == pygame.K_DOWN):
                delta_x = 0
                if(delta_y != -10):
                    delta_y = 10
            else:
                continue
            snake()
    if(not events):
        snake()
    clock.tick(10)


