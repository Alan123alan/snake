#!/usr/bin/env python
import pygame
from pygame import Rect
from pygame import Surface
from random import randint
from typing import Tuple
from collections import deque

class Point:
    def __init__(self, top:int, left:int):
        self.top = top
        self.left = left

class Square:
    def __init__(self, start:Point, side:int, next:Point=None, previous:Point=None):
        self.start = start
        self.side = side
        self.next = next
        self.previous = previous

class Snake:
    def __init__(self, head:Square=None, tail:Square=None, length:int=0):
        self.head = head
        self.tail = tail
        self.length = length 


def get_spawn_food_point(spawn_area_lower_limit:int, spawn_area_upper_limit:int)->Tuple:
    x = 10*randint(spawn_area_lower_limit/10,spawn_area_upper_limit/10) 
    y = 10*randint(spawn_area_lower_limit/10,spawn_area_upper_limit/10) 
    return (x,y)

my_start = Point(240,240)
print(my_start.top)
print(my_start.left)
my_square = Square(my_start,10)
print(my_square.start)
print(my_square.side)
print(my_square.next)
print(my_square.previous)
my_snake = Snake()
print(my_snake.tail)
print(my_snake.head)
print(my_snake.length)


# pygame.init()
# #game surface dimensions
# SURFACE_WIDTH = 500
# SURFACE_HEIGHT = 500
# SURFACE_CENTER_HEIGHT = SURFACE_HEIGHT/2
# SURFACE_CENTER_WIDTH = SURFACE_WIDTH/2
# #food spawn area
# SPAWN_AREA_L_LIMIT = 20;
# SPAWN_AREA_U_LIMIT = 470;
# #snake and food dimensions
# SNAKE_HEIGHT = FOOD_HEIGHT = 10
# SNAKE_WIDTH = FOOD_WIDTH = 10

# screen = pygame.display.set_mode((SURFACE_WIDTH,SURFACE_HEIGHT))
# clock = pygame.time.Clock()
# snake = [Rect(SURFACE_CENTER_HEIGHT-SNAKE_HEIGHT,SURFACE_CENTER_WIDTH-SNAKE_WIDTH, SNAKE_WIDTH, SNAKE_HEIGHT)]
# #initial position of food in the game surface
# #consider food will start being drawn at 280,280 from the top left corner
# #we are giving a 10 pixel margin between the game surface limit and the food bottom right corner
# (food_x,food_y) = get_spawn_food_point(SPAWN_AREA_L_LIMIT,SPAWN_AREA_U_LIMIT)
# food = Rect(food_x, food_y, FOOD_WIDTH, FOOD_HEIGHT)
# collisions = 0
# while True:
#     # Process player inputs.
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             pygame.quit()
#             raise SystemExit
#         if event.type == pygame.KEYDOWN:
#             if event.key == pygame.K_DOWN:
#                 if snake[0].top < SPAWN_AREA_U_LIMIT:
#                     snake = [snake[0].move(0, 10),*snake]
#                     print("snake going down",snake)
#                     print(snake)
#                     print(*snake)
#             if event.key == pygame.K_UP:
#                 if snake[0].top > SPAWN_AREA_L_LIMIT:
#                     snake = [snake[0].move(0, -10),*snake]
#                     print("snake going up",snake)
#                     print(snake)
#                     print(*snake)
#             if event.key == pygame.K_LEFT:
#                 if snake[0].left > SPAWN_AREA_L_LIMIT:
#                     snake = [snake[0].move(-10,0),*snake]
#                     print("snake going left",snake)
#             if event.key == pygame.K_RIGHT:
#                 if snake[0].left < SPAWN_AREA_U_LIMIT:
#                     snake = [snake[0].move(10,0),*snake]
#                     print("snake going right",snake)
#     # Do logical updates here.
#     # ...
#     if snake[0].colliderect(food):
#         collisions += 1
#         print(f"Collisions: {collisions}")
#         (food_x,food_y) = get_spawn_food_point(SPAWN_AREA_L_LIMIT,SPAWN_AREA_U_LIMIT)
#         food = Rect(food_x, food_y, FOOD_WIDTH, FOOD_HEIGHT)
#         snake.append(Rect(snake[0].left-10, snake[0].top-10, SNAKE_WIDTH, SNAKE_HEIGHT))

#     screen.fill("black")  # Fill the display with a solid color

#     # Render the graphics here.
#     # ...
#     #pygame.draw.rect(screen, "blue", snake)
#     #snake = snake.move(x_coordinate+1, y_coordinate)

#     for pixel in snake:
#         pygame.draw.rect(screen,"blue", pixel)
#     pygame.draw.rect(screen, "red", food)
#     pygame.display.flip()  # Refresh on-screen display
#     clock.tick(60)         # wait until next frame (at 60 FPS)
