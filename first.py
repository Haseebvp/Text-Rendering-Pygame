import pygame, sys
from pygame.locals import *

pygame.init()

import json

# pprint(data['Academic projects and Seminars']['Mini Project : Implementation of map in Android using Bayesian Network'])
#   set up the window
black = (0,0,0)
screen_width = 1200
screen_height = 800
screen = pygame.display.set_mode((screen_width, screen_height), 0, 32)
pygame.display.set_caption('Curriculum Vitae')
myfont = pygame.font.SysFont("freesansbold.ttf", 20)
main_Head_font = pygame.font.SysFont("freesansbold.ttf", 40)
sub_Head_font = pygame.font.SysFont("freesansbold.ttf", 30)




def draw_text(text, x, y):
    label = myfont.render(text, 1, (255,255,255))
    screen.blit(label, (x, y))    

def draw_head(text, x, y):
    label = main_Head_font.render(text, 1, (255,255,255))
    screen.blit(label, (x, y))

def draw_sub(text, x, y):
    label = sub_Head_font.render(text, 1, (255,255,255))
    screen.blit(label, (x, y))        


with open('data0.json') as data_file:    
    data = json.load(data_file)
x = 50
y = 50
ydif = 40
head_ydif = 100
head_x = 500
head_y = 10

def page1(x=50,y=50,ydif=40,head_ydif=100,head_x=500,head_y=10):
    draw_head(('Curriculum Vitae'), head_x, head_y)
    y += head_ydif
    draw_sub((data['name']), x, y)
    y += ydif
    draw_text((data['Address']), x, y)
    y += ydif
    draw_text((data['Email']), x, y)
    y += ydif
    draw_text((data['Phone']), x, y)
    y += ydif
    draw_sub(('Education'), x, y)
    y += ydif
    for key,value in data['Education'].items():
        draw_text((key + ':' + value), x, y)
        y += ydif
    draw_sub(('TechnicalSkills'), x, y)
    y += ydif    
    for key,value in data['TechnicalSkills'].items():
        draw_text((key + ':' + value), x, y)
        y += ydif

def page2(x=50,y=50,ydif=25,sub_ydif=25,head_ydif=100,head_x=500,head_y=10):
    draw_sub(('HobbyProjects'), x, y)
    y += sub_ydif
    for key,value in data['HobbyProjects'].items():
        draw_sub((key), x, y)
        y += ydif
        for i in value:
            draw_text((i), x, y)
            y += ydif

def page3(x=50,y=50,ydif=20,sub_ydif=25,head_ydif=100,head_x=500,head_y=10):
    draw_sub(('Academic projects and Seminars'), x, y)
    y += sub_ydif
    for key,value in data['Academic projects and Seminars'].items():
        draw_sub((key), x, y)
        y += ydif
        for i in value:
            draw_text((i), x, y)
            y += ydif 

def page4(x=50,y=50,ydif=30,sub_ydif=50,head_ydif=100,head_x=500,head_y=10):
    draw_sub(('Experience'), x, y)
    y += sub_ydif
    for key,value in data['Experience'].items():
        draw_sub((key), x, y)
        y += ydif
        for i in value:
            draw_text((i), x, y)
            y += ydif
    draw_sub(('Languages'), x, y)
    y += sub_ydif            
    for j in data['Languages']:
        draw_text((j), x, y)
        y += ydif
    draw_sub(('Extra- Curricular activities'), x, y)
    y += sub_ydif            
    for j in data['Extra- Curricular activities']:
        draw_text((j), x, y)
        y += ydif 

def page5(x=50,y=50,ydif=30,sub_ydif=50,head_ydif=100,head_x=500,head_y=10):
    draw_sub(('Interests'), x, y)
    y += sub_ydif
    for j in data['Interests']:
        draw_text((j), x, y)
        y += ydif
    draw_sub(('My Github Repository'), x, y)
    y += sub_ydif
    draw_text((data['My Github Repository']), x, y)
    y += ydif     
    draw_sub(('My Blog Address'), x, y)
    y += sub_ydif
    draw_text((data['My Blog Address']), x, y)
    y += ydif  
    draw_sub(('Declaration'), x, y)
    y += sub_ydif
    draw_text((data['Declaration']), x, y)
    y += ydif 
                     

now = page1()

# def key_down_events(now=now):
#     if now == '':
#         now = page1()
#     elif now == page1():
#         print "now == page1()"
#         screen.fill(black)
#         now = page2()
#     elif now == page2():
#         screen.fill(black)
#         now = page3()
#     elif now == page3():
#         screen.fill(black)
#         now = page4()
#     else:
#         screen.fill(black)
#         now = page5()




# current = "page1"
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            pygame.quit()
            sys.exit()
        #for i in range(5):    
        if event.type == pygame.KEYDOWN and event.key == pygame.K_KP1:
            screen.fill(black)
            page2()

        if event.type == pygame.KEYDOWN and event.key == pygame.K_KP2:
            screen.fill(black)
            page3()

        if event.type == pygame.KEYDOWN and event.key == pygame.K_KP3:
            screen.fill(black)
            page4()

        if event.type == pygame.KEYDOWN and event.key == pygame.K_KP4:
            screen.fill(black)
            page5()

        if event.type == pygame.KEYDOWN and event.key == pygame.K_KP0:
            screen.fill(black)
            page1()
            
 
    pygame.display.update()
    