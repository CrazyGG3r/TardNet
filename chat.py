from http import server
import pygame
import classes as c
import design as d
import random as r
import colors as cc
import socket
import threading
import queue
import socket
import select

global clientsideMSG
clientsideMSG = c.message('_you have entered the chat_',10)

connected = 0

pygame.init()

buffer_queue = queue.Queue()
buffer_lock = threading.Lock()
print(buffer_queue)

server_socket = socket.socket()   
def connect(somethinghere):
    username = somethinghere[0]
    host = somethinghere[1]
    port = int(somethinghere[2])
    global connected
    server_socket = socket.socket()   
    try:
        connected = 2
        server_socket.connect((host, port))
        connected = 1
        print("Connected to: {}:{}".format(host, port))
    except Exception as e:
        print("Error connecting:", e)
        connected = 3
        return
  
    while True:
        ready_to_read, _, _ = select.select([server_socket], [], [], 0.1)
        for sock in ready_to_read:
            m = sock.recv(2048).decode()
            if m:
                print("server: {}".format(m))
                clientsideMSG.addMsg(m)
        try:
                buffer = buffer_queue.get_nowait()
                server_socket.send(bytes(buffer, "utf-8"))
                print("Sent:", buffer)
        except queue.Empty:
            pass
        
chattext = []
def chat_room(window,roomname):
    bgg = d.Background(window,70,1)
    tra = d.Trailsquare(7)
    chunk = (window.get_width()//25)
    backgroud = c.NormalBox(((0+chunk),(0+chunk)),window.get_width()-(chunk*2),window.get_height()-(chunk*2))

    heading = c.Text((backgroud.x+20,backgroud.y+20),30,cc.colorlist[5],f"{roomname}",3)
    teext = [heading]
    
    offset = 10
  
    input1 = c.TextBox(heading.x,window.get_height()-(chunk*2),window.get_width()-(chunk*6.3),40,85,placeholder='Enter message here')
    fields = [input1]

    t1 = c.Text((0,0),25,(0,0,0),"Send",3)
    b1 = c.button((window.get_width()-(chunk*4.7),input1.rect.y),180,40,(0,0,0),(20,10),t1,)
    
    global ret 
    tback = c.Text((0,0),25,(0,0,0),"Disconnect",3)
    bback = c.button((window.get_width()-(chunk*4.7),heading.x),180,40,(0,0,0),(20,10),tback,)
    
    all_butts = [b1,bback]
    ret = 0
    buffer = ''
    
    def update_texts(input1,clientsideMSG):
            try:
                clientsideMSG
                coutner = 60
                global chattext
                chattext = []
                clientsideMSG.text.reverse()
                texxt = clientsideMSG.text
                clientsideMSG.text.reverse()
                if texxt:
                    for a in texxt:
                        chattext.append(c.Text((input1.rect.x+10,input1.rect.y - coutner),25,cc.colorlist[12],a,3))
                        coutner += 30
                    return chattext
            except:
                pass
    
    chattext  = update_texts(input1,clientsideMSG)
    print(chattext)        
    while True:
        global buffer_queue
        
        clicked_buttons = []
        if ret == 1:
            return
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return
                if event.key == pygame.K_RETURN:
                    if input1.text:
                        with buffer_lock:
                            buffer = ''
                            buffer = input1.text 
                            input1.text = ''
                            buffer_queue.put(buffer)
                            print(buffer_queue)
                    
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
                if a.text.text == "Disconnect":
                    server_socket.close()
                    return
                    
                if a.text.text == "Send":
                    pass
                   
                    
        
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
            
        # chattext  = update_texts(input1,clientsideMSG)
        chattext  = update_texts(input1,clientsideMSG)
        try:
            for a in chattext:
                a.draw(window)
        except:
            pass
        tra.draw(window)
        pygame.display.flip()