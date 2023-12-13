# Khansa Farras Callista
# 1306621067
#

import pygame
from pygame.locals import *

# Initialize Pygame
pygame.init()

# fungsi tampilan layar
def Layar():
    layar.fill(cokelat)
    layar.blit(text,[310,30])
    return

# fungsi tampilan bola
def Bola(x,y,grey1):
    pygame.draw.circle(layar,grey1,[x,y],40)
    pygame.draw.circle(layar,grey2,[x+5,y-5],35)
    pygame.draw.circle(layar, black, [x+15,y-3],7)
    pygame.draw.circle(layar, black, [x+5,y-20],6)
    pygame.draw.circle(layar, black, [x+19,y-22],6)
    return x,y,grey1

# fungsi untuk gerak jatuh
def jatuhbebas(a,b,z):
    while True:
        z = z + d
        b = b + z
        Layar()
        Bola(a,b,grey1)
        pygame.display.flip()
        waktu.tick(cti)
        if b >= 570:
            break
    return a,b,z

# fungsi untuk gerak atas
def memantul(a,b,z):
    while True:
        z = z - d
        b = b - z
        Layar()
        Bola(a,b,grey1)
        pygame.display.flip()
        waktu.tick(cti)
        if z<=0:
            break
    return a,b,z

# fungsi untuk gerak bola
def GerakBola(x,y,z):
    while True:
        if z <= 0:
            x,y,z = jatuhbebas(x,y,z)
        elif y >= 570:
            x,y,z = memantul(x,y,z)
            if y >=570:
                break
    return x,y,z
    
#Warna
cokelat=(95,66,66)
grey1=(52,70,74)
grey2=(56,76,80)
white=(250,250,250)
black=(0,0,0)

#Layar
layar = pygame.display.set_mode((1000,700))
pygame.display.set_caption('SC-Modul-7-1306621067-KF')
layar.fill(cokelat)

# Inisiasi suara
click_sound = pygame.mixer.Sound("click.wav")

#Text
font = pygame.font.Font(None,30)
text = font.render('Simulasi Benda Jatuh Bebas & Memantul',True,white)
layar.blit(text,[310,30])

#Nilai Awal
x = 500
y = 100
z = 0
d = 3
cti = 35
waktu = pygame.time.Clock()

#Program utama pygame
while True: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            click_sound.play()
            x,y,z = GerakBola(x,y,z)
    Bola(x,y,grey1)
    pygame.display.flip()
    waktu.tick(cti)