import pygame
import sys
import classes as c
import design as d
import random as r
from settings import background_color,settingsaa
import colors as cc
pygame.init()


def serverr(window):
    bgg = d.Background(window,70,1)
    tra = d.Trailsquare(7)
    heading = c.Text(((window.get_width()//10)+20,(window.get_height()//24)+70),60,cc.colorlist[12],"{Server}",3)
    teext = [heading]
    chunk = (window.get_width()//10)
    backgroud = c.NormalBox(((window.get_width()//10),(window.get_height()//10)),window.get_width()-(chunk*2),window.get_height()-(chunk*2))
    
    
    offset = 20

    f1 = c.TextBox(heading.x+150,heading.y+60+offset,200,40,28,label='RoomName: ',placeholder='My Room')
    f2 = c.TextBox(heading.x+150,f1.rect.y+40+offset,200,40,15,label='Server_Ip: ',placeholder='0.0.0.0')
    f3 = c.TextBox(heading.x+150,f2.rect.y+40+offset,200,40,5,label='Port: ',placeholder='9999')
    

    fields = [f1,f2,f3]


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return
            for f in fields:
                f.handle_event(event)
        tra.update(pygame.mouse.get_pos())
        
        bgg.draw(window)
        backgroud.draw(window)
        for a in teext:
            a.draw(window)
        for a in fields:
            a.update()
            a.draw(window)
        tra.draw(window)
        pygame.display.flip()
