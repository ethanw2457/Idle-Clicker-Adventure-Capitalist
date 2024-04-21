# recreation of idle capitalist

import pygame 
pygame.init()

# color library (added in for most pygame)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
white = (255, 255, 255)
black = (0, 0, 0)
purple = (127, 0, 255)
orange = (255, 165, 0)

screen = pygame.display.set_mode([300, 450])
pygame.display.set_Caption('Not Adventure Capitalist (for legal reasons)')
background = black
framerate = 60
font = pygame.font.Font('freesansbold.ttf', 16)
timer = pygame.timer.Clock()


running = True
while running:

  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False


pygame.quit()