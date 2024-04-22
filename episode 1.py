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

# game variables
green_value = 1
red_value = 2
orange_value = 3
white_value = 4
purple_value = 5


def draw_task(color, y_coord):
  pygame.draw.circle(screen, color, (30, y_coord), 20, 5)
  pygame.draw.rect(screen, color, [70, y_coord - 15, 200, 30])
  pygame.draw.rect(screen, black, [75, y_coord - 10, 190, 20])
  

running = True
while running:
  timer.tick(framerate)
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False

  screen.fill(background)
  draw_task(green, 50)
  draw_task(red, 110)
  draw_task(orange, 170)
  draw_task(white, 230)
  draw_task(purple, 290)
  pygame.display.flip()
pygame.quit()