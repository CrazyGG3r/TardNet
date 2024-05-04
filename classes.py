from re import A
import pygame
import random
import colors as c

font = ['assets\\fonts\\f1.ttf','assets\\fonts\\f2.ttf','assets\\fonts\\f3.ttf','assets\\fonts\\f4.ttf']

class Text:
    def __init__(self, coords, font_size, color, text, fonts=0):
        self.text = text
        self.font_size = font_size
        self.color = color
        self.color2 = color
        self.x = coords[0]
        self.y = coords[1]
        self.font = pygame.font.Font(font[fonts], font_size)
        self.surface = self.font.render(text, True, color)

    def update_text(self, new_text):
        self.text = new_text
        self.surface = self.font.render(new_text, True, self.color)
        
    def update_coords(self, coords):
        self.x = coords[0]
        self.y = coords[1]
    def draw(self, screen):
        screen.blit(self.surface, (self.x, self.y))
    def updateColor(self):
        self.changecolor(c.colorlist[12])

    def changecolor(self, color):
        self.surface = self.font.render(self.text, True, color)
        


def dummy(ac = "None"):
    print("Clicked somehting",random.randint(0,10))


class button:
    def __init__(self, coords, w, h, color,padding, butt_text, function = dummy):
        self.x = coords[0]
        self.y = coords[1]
        self.pad_x = self.x + padding[0]
        self.pad_y = self.y + padding[1]
        self.width = w
        self.height = h
        self.NotHovercolor = c.colorlist[9]
        self.Hovercolor = c.colorlist[4]

        self.disabled = False
        self.text = None
        self.hover = False
        self.text = butt_text
        self.text.update_coords((self.pad_x,self.pad_y))
        self.action = function
        self.isClicked = False

    def draw(self, screen,):
        self.updateColor()
        self.text.updateColor()
        if self.hover:
            pygame.draw.rect(screen, self.Hovercolor, (self.x, self.y, self.width, self.height),border_radius=10)
            self.text.color2 = c.colorlist[12]
            self.text.changecolor(self.text.color2)
            self.text.draw(screen)
        else:
            pygame.draw.rect(screen, self.NotHovercolor, (self.x, self.y, self.width, self.height),border_radius=10)
            self.text.changecolor(c.colorlist[2])
            self.text.draw(screen)
            self.text.draw(screen)
    def updateColor(self):
        self.NotHovercolor = c.colorlist[9]
        self.Hovercolor = c.colorlist[4]
class CreateDrone:
    def __init__(self, radius, position, speed, destination, name, color):
        self.radius = radius
        self.position = position
        self.speed = speed
        self.des = destination
        self.name = str(name)
        self.color = color
        self.fontColor = (0,190,190)
    def draw(self, window):
        pygame.draw.circle(window, self.color, self.position, self.radius)
       
        name_surface = pygame.font.SysFont(None, 20).render(self.name, True, self.fontColor)
        window.blit(name_surface, (self.position[0] - self.radius, self.position[1] + self.radius + 10))
class NormalBox:
    def __init__(self,coords,wdith,height,color = c.colorlist[0],boundaryColor = c.colorlist[12]):
        self.x = coords[0]
        self.y =coords[1]
        self.height = height
        self.width = wdith
        self.color = color
        self.bcolor = boundaryColor
        self.update()
        self.borderthick = 10
        self.surfacebound = pygame.rect.Rect(self.x,self.y,self.width+self.borderthick,self.height+self.borderthick)
        self.surfacemain = pygame.rect.Rect(self.x+5,self.y+5,self.width,self.height)
        
    def update(self):
        self.color = c.colorlist[0]
        self.bcolor = c.colorlist[12]
    def draw(self,screen):
        pygame.draw.rect(screen,self.bcolor,self.surfacebound,border_radius=10)
        pygame.draw.rect(screen,self.color,self.surfacemain,border_radius=10)




class TextBox:
    def __init__(self, x, y, width, height, max_length=20, inactive_color=c.colorlist[2], active_color=c.colorlist[8], radius=10, placeholder='hello', textcolor=c.colorlist[12], label="",fontt = 3):
        self.rect = pygame.Rect(x, y, width, height)
        self.inactive_color = pygame.Color(inactive_color)
        self.active_color = pygame.Color(active_color)
        self.color = self.inactive_color
        self.active = False
        self.text = placeholder
        self.textcolor = textcolor
        self.notactivetextcolor = c.colorlist[0]
        self.labelTextcolor = textcolor
        self.max_length = max_length
        self.radius = radius
        self.cursor_blink = True
        self.cursor_time = pygame.time.get_ticks()
        self.cursor_speed = 500  # Blinking speed in milliseconds
        self.label = label  # Add label attribute
        self.ffont = pygame.font.Font(font[fontt], 25)
    def handle_event(self, event):
        
        self.color = self.active_color if self.active else self.inactive_color
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.active = not self.active
            else:
                self.active = False
            self.color = self.active_color if self.active else self.inactive_color
        
        if event.type == pygame.KEYDOWN:
            if self.active:
                self.textcolor = c.colorlist[2]
                if event.key == pygame.K_RETURN:
                    print(self.text)  # Print the entered text when Enter is pressed
                    self.text = ''  # Clear the text input after printing
                elif event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]  # Remove the last character
                elif len(self.text) < self.max_length:
                    self.text += event.unicode  # Add the typed character to the text

    def update(self):
        current_time = pygame.time.get_ticks()
        self.labelTextcolor = c.colorlist[12]
        self.textcolor = c.colorlist[12]
        if current_time - self.cursor_time > self.cursor_speed:
            self.cursor_time = current_time
            self.cursor_blink = not self.cursor_blink

    def draw(self, surface):
        if self.active:
            self.textcolor = c.colorlist[2]
            self.color = c.colorlist[10]
        else:
            self.color = c.colorlist[2]
            self.textcolor = c.colorlist[10]
        pygame.draw.rect(surface, self.color, self.rect, border_radius=self.radius)
        
        
        label_surface = self.ffont.render(self.label, True, self.labelTextcolor)
        surface.blit(label_surface, (self.rect.x - label_surface.get_width() - 10, self.rect.y + 10 ))
        
     
        txt_surface = self.ffont.render(self.text, True, self.textcolor)
        
        width = max(200, txt_surface.get_width() + 10)
        self.rect.w = width
        
        if self.cursor_blink and self.active:
            cursor_x = self.rect.x + 5 + self.ffont.size(self.text)[0]
            cursor_y = self.rect.y + 7
            cursor_height = self.ffont.size(self.text)[1] 
            pygame.draw.line(surface, self.textcolor, (cursor_x, cursor_y), (cursor_x, cursor_y + cursor_height), 2)
            
        
            
        surface.blit(txt_surface, (self.rect.x + 5, self.rect.y+10))
def limit_value(value, min_value, max_value):
    return max(min_value, min(max_value, value))