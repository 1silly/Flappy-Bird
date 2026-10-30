import pygame
from pygame.locals import *
import random

pygame.init()
clock = pygame.time.Clock()
FPS = 60
WIDTH = 864
HEIGHT = 936
CENTER_X = WIDTH/2
CENTER_Y = HEIGHT/2
SCREEN = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Flappy Bird")
font = pygame.font.SysFont("Verdana",60)
# game variables
ground_scroll = 0
scroll_speed = 4
flying = False
game_over = False
pipe_gap = 150
pipe_frequency = 1500
last_pipe = pygame.time.get_ticks()-pipe_frequency
score = 0
pass_pipe = False

# Load Images
bg = pygame.image.load("background.png")
ground_img = pygame.image.load("ground.png")
restart_img = pygame.image.load("restart.png")
# add text to the screen
def score_text(txt,font,clr,x,y):
    score_txt = font.render(txt,True,clr)
    SCREEN.blit(score_text,(x,y))

# Bird Sprite
class Bird(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.images = []
        self.index = 0
        self.counter = 0
        for num in range(1,4):
            img = pygame.image.load(f"bird{num}.png")
            self.images.append(img)
        self.image = self.images[self.index]
        self.rect = self.image.get_rect()
        self.rect.center = [x,y]
        self.vel = 0
        self.clicked = False
        
    def update(self):
        if flying == True:
            self.vel += 0.5
            if self.vel > 8:
                self.vel = 8
            
            if self.rect.bottom < 768:
                self.rect.y += self.vel
        if game_over == False:
            # jump
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                self.vel = -10 
            if pygame.mouse.get_pressed()[0] == 0:
                self.clicked = False

            # Animation handle
            flap_cooldown = 5
            self.counter == +1 
            if self.counter > flap_cooldown:
                self.counter = 0
                self.index +=1
                if self.index >= len(self.images):
                    self.index = 0
                self.image = self.images[self.index]
                
            self.image = pygame.transform.rotate(self.images[self.index],self.vel *-2)
        else:
            # point the bird towards the ground
            self.image = pygame.transform.rotate(self.image[self.index],-90)


# pipe class
class Pipe(pygame.sprite.Sprite):
    def __init__(self,x,y,position):
        pygame.sprite.Sprite.__init__()
        self.image = pygame.image.load("pole.png")
        self.rect = self.image.get_rect()
        if position == 1:
            self.image = pygame.transform.flip(self.image,False,True)
            self.rect.bottomleft = [x,y-int(pipe_gap / 2)]
        elif position == -1:
            self.rect.topleft = [x,y+int(pipe_gap / 2)]
    def update(self):
        self.rect.x -= scroll_speed
        if self.rect.right < 0:
            self.kill()
  
                
            