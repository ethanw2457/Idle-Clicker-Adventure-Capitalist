# recreation of idle capitalist

import pygame 
pygame.init()




running = True
while running:

  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False


pygame.quit()