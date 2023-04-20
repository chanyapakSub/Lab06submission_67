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
        pg.draw.rect(screen,(color),(self.x,self.y,self.w,self.h))


  
class Button(Rectangle):
    def __init__(self, x=0, y=0, w=0, h=0):
        Rectangle.__init__(self, x, y, w, h)
    
    def isMouseOn(self):
        mx,my = pg.mouse.get_pos()
        if my>=self.y and mx>=self.x and my<= self.y + self.h and mx<= self.x+self.w:
            return True
        else :
            return False
    def isMousePress(self):
        if pg.mouse.get_pressed()[0]:
            return True
        else:
            return False

run = True
win_x, win_y = 800, 480
screen = pg.display.set_mode((win_x, win_y))
btn = Button(20,20,100,100) # สร้าง Object จากคลาส Button ขึ้นมา
red = (255,90,90)
grey = (139,139,139)
purple = (193,129,236)
while(run):
    screen.fill((255, 255, 255))
    if btn.isMouseOn() and btn.isMousePress():
        color = purple

    elif btn.isMouseOn():
        color = grey
    
    else:
       color = red
    
    btn.draw(screen)
    pg.display.update()
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            run = False




