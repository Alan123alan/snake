#!/usr/bin/env python
import pygame
from pygame import Rect
from pygame import Surface
from random import randint
from typing import Tuple

def get_spawn_food_point(spawn_area_lower_limit:int, spawn_area_upper_limit:int)->Tuple:
    x = 10*randint(spawn_area_lower_limit/10,spawn_area_upper_limit/10) 
    y = 10*randint(spawn_area_lower_limit/10,spawn_area_upper_limit/10) 
    return (x,y)


pygame.init()
#game surface dimensions
SURFACE_WIDTH = 500
SURFACE_HEIGHT = 500
#food spawn area
SPAWN_AREA_L_LIMIT = 20;
SPAWN_AREA_U_LIMIT = 480;
#snake and food dimensions
SNAKE_HEIGHT = FOOD_HEIGHT = 10
SNAKE_WIDTH = FOOD_WIDTH = 10

screen = pygame.display.set_mode((SURFACE_WIDTH,SURFACE_HEIGHT))
clock = pygame.time.Clock()
# directions = {
#     up: {"x":-height,}
# }
snake = Rect(0,0, SNAKE_WIDTH, SNAKE_HEIGHT)
#initial position of food in the game surface
#consider food will start being drawn at 280,280 from the top left corner
#we are giving a 20 pixel margin between the game surface limit and the food bottom right corner
(x,y) = get_spawn_food_point(SPAWN_AREA_L_LIMIT,SPAWN_AREA_U_LIMIT)
food = Rect(x, y, FOOD_WIDTH, FOOD_HEIGHT)
collisions = 0
while True:
    # Process player inputs.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            raise SystemExit
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                snake = snake.move(0, 10)
                print("snake going down",snake)
            if event.key == pygame.K_UP:
                snake = snake.move(0, -10)
                print("snake going up",snake)
            if event.key == pygame.K_LEFT:
                snake = snake.move(-10,0)
                pass
            if event.key == pygame.K_RIGHT:
                snake = snake.move(10,0)
                pass
    # Do logical updates here.
    # ...
    # pressed_key = pygame.key.get_pressed()
    # if pressed_key[pygame.K_UP]:
    #     snake = snake.move(x_coordinate, -10)
    # if pressed_key[pygame.K_DOWN]:
    #     snake = snake.move(x_coordinate, 10)
    # if pressed_key[pygame.K_LEFT]:
    #     snake = snake.move(-10,y_coordinate)
    # if pressed_key[pygame.K_RIGHT]:
    #     snake = snake.move(10,y_coordinate)

    if snake.colliderect(food):
        collisions += 1
        print(f"Collisions: {collisions}")
        (x,y) = get_spawn_food_point(SPAWN_AREA_L_LIMIT,SPAWN_AREA_U_LIMIT)
        food = Rect(x, y, FOOD_WIDTH, FOOD_HEIGHT)

    screen.fill("black")  # Fill the display with a solid color

    # Render the graphics here.
    # ...
    #pygame.draw.rect(screen, "blue", snake)
    #snake = snake.move(x_coordinate+1, y_coordinate)
    pygame.draw.rect(screen,"red", food)
    pygame.draw.rect(screen, "blue", snake)
    pygame.display.flip()  # Refresh on-screen display
    clock.tick(60)         # wait until next frame (at 60 FPS)
