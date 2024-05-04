import pygame
import sys
import classes as c
import design as d
import random as r
from settings import background_color,settingsaa
import colors as cc
pygame.init()

def statuser(var = None):
    return "Started"
def stopuser(var =None):
    return "Stopped"
def serverr(window):
    bgg = d.Background(window,70,1)
    tra = d.Trailsquare(7)
    chunk = (window.get_width()//10)
    backgroud = c.NormalBox(((window.get_width()//10),(window.get_height()//10)),window.get_width()-(chunk*2),window.get_height()-(chunk*2))
    status = "stopped"
    info = "Status: {}".format(status)
    heading = c.Text(((window.get_width()//10)+20,(window.get_height()//24)+70),60,cc.colorlist[12],"{Server}",3)
    information = c.Text(((window.get_width()//10)+500,(window.get_height()//24)+215),40,cc.colorlist[12],info,3)
    teext = [heading,information]
    
    offset = 20

    f1 = c.TextBox(heading.x+150,heading.y+60+offset,200,40,28,label='RoomName: ',placeholder='My Room')
    f2 = c.TextBox(heading.x+150,f1.rect.y+40+offset,200,40,15,label='Server_Ip: ',placeholder='0.0.0.0')
    f3 = c.TextBox(heading.x+150,f2.rect.y+40+offset,200,40,5,label='Port: ',placeholder='9999')
    
    fields = [f1,f2,f3]

    t1 = c.Text((0,0),25,(0,0,0),"Start Server",3)
    b1 = c.button((heading.x+150,f3.rect.y+40+offset),200,40,(0,0,0),(20,10),t1,statuser)
    t2 = c.Text((0,0),25,(0,0,0),"Stop Server",3)
    b2 = c.button((information.x,information.y+115),200,40,(0,0,0),(20,10),t2,stopuser)
    
    
    all_butts = [b1,b2]
    while True:
        clicked_buttons = []
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return
            for f in fields:
                f.handle_event(event)
            if event.type == pygame.MOUSEBUTTONDOWN:
                for a in all_butts:
                    if a.hover:
                        if not a.isClicked:
                            a.isClicked = True
                            clicked_buttons.append(a)
            if event.type == pygame.MOUSEBUTTONUP:
                for a in all_butts:
                    if a.hover:
                        a.isClicked = False
        m = pygame.mouse.get_pos()
        for a in all_butts:
            if a.disabled != True:
                if m[0] > a.x and m[1] > a.y:
                    if m[0] < (a.x + a.width) and m[1] < (a.y + a.height):
                        a.hover = True
                    else:
                        a.hover = False
                else:
                    a.hover = False
            else:
                a.hover = True
        for a in clicked_buttons:
            if a.disabled == False:
                status = a.action(window)
                information.update_text("Status: {}".format(status))
                bgg.reset_bg(window)
                tra.resetTrail()
        if status == "Started":
            b1.disabled = True
            b2.disabled = False
        else:
            b1.disabled = False
            b2.disabled = True
        tra.update(pygame.mouse.get_pos())
        
        bgg.draw(window)
        backgroud.draw(window)
        for a in all_butts:
            a.draw(window)
            
        for a in teext:
            a.draw(window)
        for a in fields:
            a.update()
            a.draw(window)
        tra.draw(window)
        pygame.display.flip()
