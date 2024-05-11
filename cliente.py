
import pygame
import classes as c
import design as d
import random as r
import colors as cc
import chat 
pygame.init()


def clientt(window):
    bgg = d.Background(window,70,1)
    tra = d.Trailsquare(7)
    chunk = (window.get_width()//10)
    backgroud = c.NormalBox(((window.get_width()//10),(window.get_height()//10)),window.get_width()-(chunk*2),window.get_height()-(chunk*2))
    status = "Not Connected"
    info = "Status: {}".format(status)
    heading = c.Text(((window.get_width()//10)+20,(window.get_height()//24)+70),60,cc.colorlist[12],"{Join Room}",3)
    information = c.Text(((window.get_width()//10)+500,(window.get_height()//24)+215),40,cc.colorlist[12],info,3)
    teext = [heading,information]
    
    offset = 20

    f1 = c.TextBox(heading.x+150,heading.y+60+offset,200,40,28,label='RoomName: ',placeholder='My Room')
    f2 = c.TextBox(heading.x+150,f1.rect.y+40+offset,200,40,15,label='Server_Ip: ',placeholder='127.0.0.1')
    f3 = c.TextBox(heading.x+150,f2.rect.y+40+offset,200,40,5,label='Port: ',placeholder='9999')
    
    fields = [f1,f2,f3]

    t1 = c.Text((0,0),25,(0,0,0),"Join Room",3)
    b1 = c.button((heading.x+150,f3.rect.y+40+offset),200,40,(0,0,0),(20,10),t1,)
    
    
    def exitt(var = None):
        global ret
        ret = 1
        return
    tback = c.Text((0,0),25,(0,0,0),"Back",3)
    bback = c.button(((window.get_width()//2)-100,600),100,40,(0,0,0),(20,10),tback,exitt)
    
    all_butts = [b1,bback]
    global ret 
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
                    chat.connect(info)
        
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