#! /usr/bin/env python
# https://www.pygame.org/project-Rect+Collision+Response-1061-.html

import random
import pygame
import sys

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


class Frog(object):
    def __init__(self, size):
        self.rect = pygame.Rect(SCREEN_WIDTH / 2, SCREEN_HEIGHT - size, size, size)
        self.color = pygame.Color("blue")
        self.vy = 0
        
    def draw(self):
        pygame.draw.rect(screen, self.color, self.rect)

    def move(self, vy):
        self.vy = vy
        self.rect.y += self.vy

        for car in cars:
            if self.rect.colliderect(car.rect):
                self.color = pygame.Color("red")
         

class Car(object):
    def __init__(self, x, y):
        cars.append(self)
        self.x = x
        self.y = y
        self.rect = pygame.Rect(x, y, 32, 32)
        self.vx = random.randrange(1, 3)
        self.color = pygame.Color("white")
               
    def move(self):
        self.rect = pygame.Rect(self.x + self.vx, self.y, 32, 32)
        self.x += self.vx

    def draw(self):
        pygame.draw.rect(screen, self.color, car.rect)


pygame.init()

pygame.display.set_caption("Get to the green square!")
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

clock = pygame.time.Clock()
cars = []
frog = Frog(32)


Car(0, SCREEN_HEIGHT / 2)
end_rect = pygame.Rect(SCREEN_WIDTH / 2, 0, 32, 32)


while True:
    clock.tick(60)
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    key = pygame.key.get_pressed()
    if key[pygame.K_UP]:
        frog.move(-2)

    if frog.rect.colliderect(end_rect):
        print("You Win!")

    # Draw the scene
    screen.fill((0, 0, 0))
    for car in cars:
        car.move()
        car.draw()
    pygame.draw.rect(screen, pygame.Color("green"), end_rect)
    frog.draw()
    pygame.display.flip()
