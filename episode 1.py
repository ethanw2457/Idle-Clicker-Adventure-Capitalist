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
draw_green = False
draw_red = False
draw_orange = False
draw_white = False
draw_purple = False
green_length = 0
red_length = 0
orange_length = 0
white_length = 0
purple_length = 0
green_speed = 5
red_speed = 4
orange_speed = 3
white_speed = 2
purple_speed = 1
score = 0


def draw_task(color, y_coord, value, draw, length, speed):
  global score
  if draw and length < 200:
    length += speed
  elif length >= 200:
    draw = False
    length = 0
    score += value
  task = pygame.draw.circle(screen, color, (30, y_coord), 20, 5)
  pygame.draw.rect(screen, color, [70, y_coord - 15, 200, 30])
  pygame.draw.rect(screen, black, [75, y_coord - 10, 190, 20])
  pygame.draw.rect(screen, color, [70, y_coord - 15, length, 30])
  value_text = font.render(str(value), True, white)
  screen.blit(value_text, (16, y_coord - 10))
  return task, length, draw
  

running = True
while running:
  timer.tick(framerate)
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False

  screen.fill(background)
  task1, green_length, draw_green = draw_task(green, 50, green_value, draw_green, green_length, green_speed)
  task2, red_length, draw_red = draw_task(red, 110, red_value, draw_red, red_length, red_speed)
  task3, orange_length, draw_orange = draw_task(orange, 170, orange_value, draw_orange, orange_length, orange_speed)
  task4, white_length, draw_white = draw_task(white, 230, white_value, draw_white, white_length, white_speed)
  task5, purple_length, draw_purple = draw_task(purple, 290, purple_value, draw_purple, purple_length, purple_speed)
  pygame.display.flip()
pygame.quit()