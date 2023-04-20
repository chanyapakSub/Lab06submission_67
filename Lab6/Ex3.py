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


class InputBox:

    def __init__(self, x, y, w, h,Num , text='' ):
        self.rect = pg.Rect(x, y, w, h)
        self.color = COLOR_INACTIVE
        self.text = text
        self.txt_surface = FONT.render(text, True, self.color)
        self.active = False
        self.num = Num

    def handle_event(self, event):
        
        if event.type == pg.MOUSEBUTTONDOWN:# ทำการเช็คว่ามีการคลิก Mouse หรือไม่
            if self.rect.collidepoint(event.pos): #ทำการเช็คว่าตำแหน่งของ Mouse อยู่บน InputBox นี้หรือไม่
                # Toggle the active variable.
                self.active = not self.active
            else:
                self.active = False
            self.color = COLOR_ACTIVE if self.active else COLOR_INACTIVE # เปลี่ยนสีของ InputBox
            
        if event.type == pg.KEYDOWN:
            if self.active:
                if event.key == pg.K_RETURN:
                    show =True
                elif event.key == pg.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    if not self.num:
                        self.text += event.unicode
                    else: 
                        if chr(event.key).isnumeric():
                            self.text += event.unicode
                # Re-render the text.
                self.txt_surface = FONT.render(self.text, True, self.color)

    def update(self):
        # Resize the box if the text is too long.
        width = max(200, self.txt_surface.get_width()+10)
        self.rect.w = width

    def draw(self, Screen):
        # Blit the text.
        Screen.blit(self.txt_surface, (self.rect.x+5, self.rect.y+5))
        # Blit the rect.
        pg.draw.rect(Screen, self.color, self.rect, 2)
    

run = True

win_x, win_y = 800, 480
screen = pg.display.set_mode((win_x, win_y))
COLOR_INACTIVE = pg.Color(153,0,153) # ตั้งตัวแปรให้เก็บค่าสี เพื่อนำไปใช้เติมสีให้กับกล่องข้อความตอนที่คลิกที่กล่องนั้นๆอยู่
COLOR_ACTIVE = pg.Color(193,129,236)     # ^^^
FONT = pg.font.Font(None, 32)


input_box1 = InputBox(200, 80, 250, 40,False) # สร้าง InputBox1
input_box2 = InputBox(200, 180, 250, 40,False) # สร้าง InputBox2
input_box3 = InputBox(200, 280, 250, 40,True)
input_boxes = [input_box1, input_box2, input_box3] # เก็บ InputBox ไว้ใน list เพื่อที่จะสามารถนำไปเรียกใช้ได้ง่าย
btn = Button(460,315,110,50)

font = pg.font.Font('freesansbold.ttf', 25) # font and fontsize
fontrect = pg.font.Font('freesansbold.ttf', 15)
# text = font.render('', True, (255,142,199), (229,204,255)) # (text,is smooth?,letter color,background color)
# textRect = text.get_rect() # text size
#ใส่ชื่อเล่น
nickname = font.render('nikname :', True, (153,0,153),None)
nicknameRect = nickname.get_rect()
#ใส่ชื่อจริง
name = font.render('name :', True, (153,0,153),None)
nameRect = name.get_rect()
#ใส่อายุ
age = font.render('age :', True, (153,0,153),None)
ageRect = age.get_rect()
#submit
submit = font.render('submit', True, (153,0,153),None)
submitRect = submit.get_rect()




nicknameRect.bottomleft = (200,70)
nameRect.bottomleft =(200,170)
ageRect.bottomleft = (200,270)
submitRect.bottomleft = (470,350)
error = False
show = False

red = (255,90,90)
grey = (139,139,139)
purple = (193,129,236)


system = pg.cursors.Cursor(pg.SYSTEM_CURSOR_HAND)

while run:
    screen.fill((255, 255, 255))

    screen.blit(nickname, nicknameRect)
    screen.blit(name, nameRect)
    screen.blit(age, ageRect)

    for box in input_boxes: # ทำการเรียก InputBox ทุกๆตัว โดยการ Loop เข้าไปยัง list ที่เราเก็บค่า InputBox ไว้
        box.update() # เรียกใช้ฟังก์ชัน update() ของ InputBox
        box.draw(screen) # เรียกใช้ฟังก์ชัน draw() ของ InputBox เพื่อทำการสร้างรูปบน Screen
    
    if btn.isMouseOn() and btn.isMousePress():
        if input_box1.text != '' and input_box2.text != '' and input_box3.text != '':
            text = fontrect.render('Hello ' + input_box1.text + ' ' + input_box2.text + '! You are ' + input_box3.text + ' years old.', True, (255,142,199),None)
            textRect = text.get_rect()
            textRect.bottomleft= (200,450)
            show = True
            color = purple
        
        else :
            text = fontrect.render('please write all box!!!!!!! right now', True, (255,142,199),None)
            textRect = text.get_rect()
            textRect.bottomleft= (200,450)
            show = True
            color = purple


    elif btn.isMouseOn():
        system =pg.cursors.Cursor(pg.SYSTEM_CURSOR_HAND)
        color = grey
    
    else:
       color = red
    
    btn.draw(screen)
    screen.blit(submit, submitRect)

    if show:
        screen.blit(text, textRect)
  



    for event in pg.event.get():
        for box in input_boxes:
            box.handle_event(event)
        if event.type == pg.QUIT:
            pg.quit()
            run = False

    pg.time.delay(1)
    pg.display.update()