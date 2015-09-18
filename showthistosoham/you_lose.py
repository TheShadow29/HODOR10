import pygame, Buttons , sys
from pygame.locals import *

pygame.init()
overImg= pygame.image.load('ben10.jpg')

class Button_Example:
    def __init__(self):
        self.main()
    
    #Create a display
    def display(self):
        self.screen = pygame.display.set_mode((750,600),0,32)
        pygame.display.set_caption("Game Over")

    #Update the display and show the button
    def update_display(self):
        self.screen.fill((30,144,255))
        self.screen.blit(overImg, (0, 0))
        #Parameters:               surface,      color,       x,   y,   length, height, width,    text,      text_color
        self.Button1.create_button(self.screen, (9,9,255), 100, 235, 200,    50,    0,    "Play Again", (255,255,255))
        self.Button2.create_button(self.screen, (255,5,5), 100, 335, 200,    50,    0,    "Quit", (255,255,255))
        pygame.display.flip()


    #Run the loop
    def main(self):
        self.Button1 = Buttons.Button()
        self.Button2 = Buttons.Button()
        self.display()
        while True:
            self.update_display()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                elif event.type == MOUSEBUTTONDOWN:
                    if self.Button1.pressed(pygame.mouse.get_pos()):
                        print "Play Again"
                    elif self.Button2.pressed(pygame.mouse.get_pos()):
                        print "Quit"
                        pygame.quit()   
                        sys.exit()

if __name__ == '__main__':
    obj = Button_Example()
