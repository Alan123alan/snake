#!/usr/bin/env python
import pygame
from pygame import Rect

pygame.init()
screen = pygame.display.set_mode((300,300))
clock = pygame.time.Clock()

x_coordinate = 0
y_coordinate = 0
snake = Rect(x_coordinate,y_coordinate,10,10)
while True:
    # Process player inputs.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            raise SystemExit
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                snake = snake.move(x_coordinate, -1)
                print("snake going down",snake)
            if event.key == pygame.K_UP:
                snake = snake.move(x_coordinate, 1)
                print("snake going up",snake)

    # Do logical updates here.
    # ...

    screen.fill("black")  # Fill the display with a solid color

    # Render the graphics here.
    # ...
    #pygame.draw.rect(screen, "blue", snake)
    #snake = snake.move(x_coordinate+1, y_coordinate)
    pygame.draw.rect(screen, "blue", snake)
    pygame.display.flip()  # Refresh on-screen display
    clock.tick(60)         # wait until next frame (at 60 FPS)
