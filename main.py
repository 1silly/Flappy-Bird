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