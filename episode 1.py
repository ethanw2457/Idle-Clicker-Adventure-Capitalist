# recreation of idle capitalist

import pygame 
pygame.init()

screen = pygame.display.set_mode([300, 450])
pygame.display.set_Caption('Not Adventure Capitalist (for legal reasons)')


running = True
while running:

  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False


pygame.quit()