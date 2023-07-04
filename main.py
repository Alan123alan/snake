#!/usr/bin/env python
import pygame
from pygame import Rect
from pygame import Surface
from random import randint
from typing import Tuple
from collections import deque


def get_spawn_food_point(spawn_area_lower_limit:int, spawn_area_upper_limit:int)->Tuple:
    x = 10*randint(spawn_area_lower_limit/10,spawn_area_upper_limit/10) 
    y = 10*randint(spawn_area_lower_limit/10,spawn_area_upper_limit/10) 
    return (x,y)

def generate_upper_wall():
    return [Rect(point,10,WALL_BLOCK_WIDTH,WALL_BLOCK_HEIGHT) for point in range(10,481,10)]
    # upper_wall = []
    # TOP = 10
    # for x in range(10,481,10): 
    #     upper_wall.append(Rect(x,TOP,WALL_BLOCK_WIDTH,WALL_BLOCK_HEIGHT))
    # return upper_wall


def generate_lower_wall():
    return [Rect(point,480,WALL_BLOCK_WIDTH,WALL_BLOCK_HEIGHT) for point in range(10,481,10)]
    # lower_wall = []
    # TOP = 480
    # for x in range(10,481,10): 
    #     lower_wall.append(Rect(x,TOP,WALL_BLOCK_WIDTH,WALL_BLOCK_HEIGHT))
    # return lower_wall


def generate_left_wall():
    return [Rect(10,point,WALL_BLOCK_WIDTH,WALL_BLOCK_HEIGHT) for point in range(10,481,10)]
    # left_wall = []
    # LEFT = 10
    # for y in range(10,481,10): 
    #     left_wall.append(Rect(LEFT,y,WALL_BLOCK_WIDTH,WALL_BLOCK_HEIGHT))
    # return left_wall 

def generate_right_wall():
    return [Rect(480,point,WALL_BLOCK_WIDTH,WALL_BLOCK_HEIGHT) for point in range(10,481,10)]
    # right_wall = []
    # LEFT = 480
    # for y in range(10,481,10): 
    #     right_wall.append(Rect(LEFT,y,WALL_BLOCK_WIDTH,WALL_BLOCK_HEIGHT))
    # return right_wall 

def generate_walls():
    left_wall = generate_left_wall()
    right_wall = generate_right_wall()
    upper_wall = generate_upper_wall()
    lower_wall = generate_lower_wall()
    walls = [left_wall, right_wall, upper_wall, lower_wall]
    return walls

pygame.init()
#game surface dimensions
SURFACE_WIDTH = 500
SURFACE_HEIGHT = 500
SURFACE_CENTER_HEIGHT = SURFACE_HEIGHT/2
SURFACE_CENTER_WIDTH = SURFACE_WIDTH/2
#walls pixels
WALL_COLOR = "white" 
WALL_BLOCK_HEIGHT = 10
WALL_BLOCK_WIDTH = 10
#food spawn area
SPAWN_AREA_L_LIMIT = 20;
SPAWN_AREA_U_LIMIT = 470;
#snake and food dimensions
SNAKE_HEIGHT = FOOD_HEIGHT = 10
SNAKE_WIDTH = FOOD_WIDTH = 10
#snake movement directions
UP = (0,-10)
DOWN = (0,10)
LEFT = (-10,0)
RIGHT = (10,0)
START = (0,0)

screen = pygame.display.set_mode((SURFACE_WIDTH,SURFACE_HEIGHT))
clock = pygame.time.Clock()
snake = [Rect(SURFACE_CENTER_HEIGHT-SNAKE_HEIGHT,SURFACE_CENTER_WIDTH-SNAKE_WIDTH, SNAKE_WIDTH, SNAKE_HEIGHT)]
#initial position of food in the game surface
#consider food will start being drawn at 280,280 from the top left corner
#we are giving a 10 pixel margin between the game surface limit and the food bottom right corner
(food_x,food_y) = get_spawn_food_point(SPAWN_AREA_L_LIMIT,SPAWN_AREA_U_LIMIT)
food = Rect(food_x, food_y, FOOD_WIDTH, FOOD_HEIGHT)
collisions = 0
direction = START
while True:
    # Process player inputs.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            raise SystemExit
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                #if snake[0].top < SPAWN_AREA_U_LIMIT:
                direction = DOWN
                    # snake = [snake[0].move(0, 10),*snake]
                    # snake.pop()
            if event.key == pygame.K_UP:
                #if snake[0].top > SPAWN_AREA_L_LIMIT:
                direction = UP
                    # snake = [snake[0].move(0, -10),*snake]
                    # snake.pop()
            if event.key == pygame.K_LEFT:
                #if snake[0].left > SPAWN_AREA_L_LIMIT:
                direction = LEFT
                    # snake = [snake[0].move(-10,0),*snake]
                    # snake.pop()
            if event.key == pygame.K_RIGHT:
                #if snake[0].left < SPAWN_AREA_U_LIMIT:
                direction = RIGHT
                    #snake = [snake[0].move(10,0),*snake]
                    #snake.pop()
    # Do logical updates here.
    # ...
    #print(x_offset,y_offset)
    #print(snake[0].left,snake[0].top)
    tail = snake[-1]
    (x_offset,y_offset) = direction
    if (SPAWN_AREA_L_LIMIT < snake[0].left and direction == LEFT) or (snake[0].left < SPAWN_AREA_U_LIMIT and direction == RIGHT) or (SPAWN_AREA_L_LIMIT < snake[0].top and direction == UP) or (snake[0].top < SPAWN_AREA_U_LIMIT and direction == DOWN):
        snake = [snake[0].move(x_offset,y_offset),*snake]
        snake.pop()
    if snake[0].colliderect(food):
        collisions += 1
        print(f"Collisions: {collisions}")
        (food_x,food_y) = get_spawn_food_point(SPAWN_AREA_L_LIMIT,SPAWN_AREA_U_LIMIT)
        food = Rect(food_x, food_y, FOOD_WIDTH, FOOD_HEIGHT)
        snake.append(tail)
        #snake.append(Rect(snake[0].left-10, snake[0].top-10, SNAKE_WIDTH, SNAKE_HEIGHT))

    screen.fill("black")  # Fill the display with a solid color

    # Render the graphics here.
    # ...
    #pygame.draw.rect(screen, "blue", snake)
    #snake = snake.move(x_coordinate+1, y_coordinate)
    for wall in generate_walls():
        for wall_block in wall:
            pygame.draw.rect(screen,WALL_COLOR,wall_block)
    for pixel in snake:
        pygame.draw.rect(screen,"blue", pixel)
    pygame.draw.rect(screen, "red", food)
    pygame.display.flip()  # Refresh on-screen display
    clock.tick(10)         # wait until next frame (at 60 FPS)
