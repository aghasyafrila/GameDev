import pygame, sys
from pygame import rect
from pygame.locals import *
import time

#mengatur besar layar dan menampilkan judul layar
WIDTH, HEIGHT = 400, 400
pygame.display.set_caption('Agha Syafrila TID')

pygame.init()#sebagai inisialisasi
win = pygame.display.set_mode((WIDTH, HEIGHT)) 
clock = pygame.time.Clock()#clock Mengetahui Waktu yang di perlukan untuk benda bergerak

#Set Warna Menggunakan RGB Colors
BLACK = (0,0,0)

#membuat sebuah objek. Di setiap metode class harus selalu ada self sebagai 
class Player:
    def __init__(self, x, y):
        self.x = int(x)
        self.y = int(y)
        self.rect = pygame.Rect(self.x, self.y, 32, 32)
        self.color = (250, 120, 60)
        self.velX = 0
        self.velY = 0
        self.left_pressed = False
        self.right_pressed = False
        self.up_pressed = False
        self.down_pressed = False
        self.speed = 4

    def draw(self, win):
        pygame.draw.rect(win, self.color, self.rect)

    def update(self): #mengupdate properti-properti pada object
        self.velX = 0 #memberikan arah gerak pada object yaitu secara horizontal, dimulai dari titik 0
        self.velY = 0 #memberikan arah gerak pada object yaitu secara vertical, dimulai dari titik 0
        if self.left_pressed and not self.right_pressed:
            self.velX = -self.speed
        if self.right_pressed and not self.left_pressed:
            self.velX = -self.speed
        if self.up_pressed and not self.down_pressed:
            self.velY = -self.speed
        if self.down_pressed and not self.up_pressed:
            self.velY = -self.speed
            
        self.x += self.velX
        self.y += self.velY
        
        self.rect = pygame.Rect(int(self.x), int(self.y), 32, 32)

#Hegiht dan Widht tadi yaitu 400 dan 400 di bagi menjadi 2         
player = Player(WIDTH/2, HEIGHT/2)
#untuk merubah Warna Huruf
font_color = (200, 200,200)
#Untuk mendefinisikan Font apa dan besar fontnya
font_obj = pygame.font.Font("C:\Windows\Fonts\Humnst777 Blk BT Black Italic.TTF",25)
#Tulisan akan muncul di layar
text = "saya sedang belajar pygame"
img = font_obj.render(text, True, (0,0,0))

rect = img.get_rect()
rect.topleft = (20,20)
cursor = Rect(rect.topright, (3, rect.height))

#untuk membuat keyboard down dan keybord up, Keyboard left dan right
while  True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.left_pressed = True
            if event.key == pygame.K_RIGHT:
                player.right_pressed = True
            if event.key == pygame.K_UP:
                player.up_pressed = True
            if event.key == pygame.K_DOWN:
                player.down_pressed = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                player.left_pressed = False
            if event.key == pygame.K_RIGHT:
                player.right_pressed = False
            if event.key == pygame.K_UP:
                player.up_pressed = False
            if event.key == pygame.K_DOWN:
                player.down_pressed = False
    
            if event.type == QUIT:
                    running = False

            if event.type == KEYDOWN:
                if event.key == K_BACKSPACE:
                    if len(text)>0:
                        text = text[:-1]

                else:
                    text += event.unicode
                    img = font_obj.render(text, True, BLACK)
                    rect.size = img.get_size()
                    cursor.topleft = rect.topright

    #Mengatur warna background
    win.fill((255, 255, 255))
    pygame.draw.rect(win, (255, 165, 0), player)

    win.blit(img,rect)
    if time.time() % 1 > 0.5:
        pygame.draw.rect(win, BLACK, cursor)
    pygame.display.update()

    #Menampilkan keseluruhan hasil 
    player.update()
    pygame.display.flip()

    clock.tick(120)
    pygame.display.update()
     
pygame.quit()
