import sys 
import pygame as pg
pg.init()
class Rectangle:
    def __init__(self,x=0,y=0,w=0,h=0):
        self.x = x # Position X
        self.y = y # Position Y
        self.w = w # Width
        self.h = h # Height
    def draw(self,screen):
        pg.draw.rect(screen,(255,142,199),(self.x,self.y,self.w,self.h))



run = True
win_x, win_y = 800, 480
screen = pg.display.set_mode((win_x, win_y))
firstObject = Rectangle(350,190,100,100)
keyboard =pg.key.get_pressed()
y=0
x=0
while(run):
    screen.fill((255, 255, 255))
    firstObject = Rectangle(350+x,190+y,100,100)
    keyboard =pg.key.get_pressed()
    if keyboard [pg.K_a]:
        x-= 0.1
    if keyboard [pg.K_d]:
        x+= 0.1
    if keyboard [pg.K_w]:
        y-= 0.1
    if keyboard [pg.K_s]:
        y+= 0.1
    firstObject.draw(screen) 
    pg.display.update()

    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            run = False

    # if event.type == pg.KEYDOWN and event.key == pg.K_d: #ปุ่มถูกกดลงและเป็นปุ่ม D
    #     x +=0.1
    # if event.type == pg.KEYDOWN and event.key == pg.K_a: #ปุ่มถูกปล่อยและเป็นปุ่ม A
    #     x -=0.1
    # if event.type == pg.KEYDOWN and event.key == pg.K_s: #ปุ่มถูกกดลงและเป็นปุ่ม S
    #     y -=0.1
    # if event.type == pg.KEYDOWN and event.key == pg.K_w: #ปุ่มถูกปล่อยและเป็นปุ่ม W
    #     y +=0.1
    
    

