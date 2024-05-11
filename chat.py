from turtle import back
import pygame
import classes as c
import design as d
import random as r
import colors as cc

pygame.init()


def chat_room(window):
    bgg = d.Background(window,70,1)
    tra = d.Trailsquare(7)
    chunk = (window.get_width()//25)
    backgroud = c.NormalBox(((0+chunk),(0+chunk)),window.get_width()-(chunk*2),window.get_height()-(chunk*2))
    status = "Not Connected"
    info = "Status: {}".format(status)
    heading = c.Text((backgroud.x+20,backgroud.y+20),30,cc.colorlist[12],"{ROOM_NAME}",3)
    information = c.Text(((window.get_width()//10)+500,(window.get_height()//24)+215),40,cc.colorlist[12],info,3)
    teext = [heading]
    
    offset = 10

    f1 = c.TextBox(heading.x,heading.y+60+offset,200,40,28,placeholder='My Room')
    f2 = c.TextBox(heading.x,f1.rect.y+40+offset,200,40,15,placeholder='0.0.0.0')
    f3 = c.TextBox(heading.x,f2.rect.y+40+offset,200,40,5,placeholder='9999')
    
    input1 = c.TextBox(heading.x,window.get_height()-(chunk*2),window.get_width()-(chunk*6.3),40,85,placeholder='Enter message here')
    fields = [f1,f2,f3,input1]

    t1 = c.Text((0,0),25,(0,0,0),"Send",3)
    b1 = c.button((window.get_width()-(chunk*4.7),input1.rect.y),180,40,(0,0,0),(20,10),t1,)
    
    
    def exitt(var = None):
        global ret
        ret = 1
        return
    global ret 
    tback = c.Text((0,0),25,(0,0,0),"Disconnect",3)
    bback = c.button((window.get_width()-(chunk*4.7),heading.x),180,40,(0,0,0),(20,10),tback,exitt)
    
    all_butts = [b1,bback]
    ret = 0
    while True:
        clicked_buttons = []
        
        if ret == 1:
            return
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
                if a.text.text == "Join Room":
                    info = [f1.text,f2.text,f3.text]
                    print(info)
        
        tra.update(pygame.mouse.get_pos())
        
        bgg.draw(window)
        backgroud.draw(window)
        for a in teext:
            a.draw(window)
        for a in fields:
            a.update()
            a.draw(window)
        for a in all_butts:
            a.draw(window)
            
        tra.draw(window)
        pygame.display.flip()