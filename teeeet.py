import pygame
import colors as cc
pygame.init()

# Screen setup
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Text Input")

# Font setup
font = pygame.font.Font("assets\\fonts\\f4.ttf", 25)

class TextBox:
    def __init__(self, x, y, width, height, max_length=20, inactive_color=cc.colorlist[2], active_color=cc.colorlist[8], radius=10, placeholder='hello', textcolor=cc.colorlist[12], label=""):
        self.rect = pygame.Rect(x, y, width, height)
        self.inactive_color = pygame.Color(inactive_color)
        self.active_color = pygame.Color(active_color)
        self.color = self.inactive_color
        self.active = False
        self.text = placeholder
        self.textcolor = textcolor
        self.labelTextcolor = textcolor
        self.max_length = max_length
        self.radius = radius
        self.cursor_blink = True
        self.cursor_time = pygame.time.get_ticks()
        self.cursor_speed = 500  # Blinking speed in milliseconds
        self.label = label  # Add label attribute

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
                self.textcolor = cc.colorlist[2]
                if event.key == pygame.K_RETURN:
                    print(self.text)  # Print the entered text when Enter is pressed
                    self.text = ''  # Clear the text input after printing
                elif event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]  # Remove the last character
                elif len(self.text) < self.max_length:
                    self.text += event.unicode  # Add the typed character to the text

    def update(self):
        current_time = pygame.time.get_ticks()
        if current_time - self.cursor_time > self.cursor_speed:
            self.cursor_time = current_time
            self.cursor_blink = not self.cursor_blink

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect, border_radius=self.radius)
        
        
        label_surface = font.render(self.label, True, self.labelTextcolor)
        surface.blit(label_surface, (self.rect.x - label_surface.get_width() - 10, self.rect.y ))
        
     
        txt_surface = font.render(self.text, True, self.textcolor)
        
        width = max(200, txt_surface.get_width() + 10)
        self.rect.w = width
        
        if self.cursor_blink and self.active:
            cursor_x = self.rect.x + 5 + font.size(self.text)[0]
            cursor_y = self.rect.y + 2.5
            cursor_height = font.size(self.text)[1] - 5
            pygame.draw.line(surface, self.textcolor, (cursor_x, cursor_y), (cursor_x, cursor_y + cursor_height), 2)
            
        if self.active:
            self.textcolor = cc.colorlist[2]
        else:
            self.textcolor = cc.colorlist[10]
        surface.blit(txt_surface, (self.rect.x + 5, self.rect.y))

            

# Main loop
running = True


text_boxes = [TextBox(100,100, 140, 32, label="Name:"),
              TextBox(100, 150, 140, 32, label="Age:"),
              TextBox(100, 200, 140, 32, label="Email:")]

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

       
        for text_box in text_boxes:
            text_box.handle_event(event)

    # Fill the screen with white
    screen.fill((255, 255, 255))

    # Update and draw each text box
    for text_box in text_boxes:
        text_box.update()
        text_box.draw(screen)

    # Update the display
    pygame.display.flip()

pygame.quit()
