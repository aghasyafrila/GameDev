import pygame
from pygame import rect
from pygame.locals import *
import time

BLACK = (0,0,0)
BLUE = (0,0, 255)
WHITE = (255,255,255)

pygame.init()
screen = pygame.display.set_mode((670,120))
pygame.display.set_caption('Smooth Movement')

text = "HAI AKU SYAFRILA DARI SEMARANG"
font = pygame.font.SysFont(None, 48)
img = font.render(text, True, BLUE)

rect = img.get_rect()
rect.topleft = (20,20)
cursor = Rect(rect.topright, (3, rect.height))

running = True
baground = WHITE

while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

        if event.type == KEYDOWN:
            if event.key == K_BACKSPACE:
                if len(text)>0:
                    text = text[:-1]

            else:
                text += event.unicode
            img = font.render(text, True, BLUE)
            rect.size = img.get_size()
            cursor.topleft = rect.topright

    screen.fill(baground)
    screen.blit(img,rect)
    if time.time() % 1 > 0.5:
        pygame.draw.rect(screen, BLUE, cursor)
    pygame.display.update()

pygame.quit()
