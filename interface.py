import pygame, sys
from pygame.locals import *



# setup
pygame.init()
clock = pygame.time.Clock()

# display
screen = pygame.display.set_mode((1920,1080))
board = pygame.image.load("IMAGE/piste.jpg")
board_rect = board.get_rect(topleft = [0,0])

moving = False


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == MOUSEBUTTONDOWN:
          if board_rect.collidepoint(event.pos):
              moving = True 
        elif event.type == MOUSEBUTTONUP:          
           moving = False
        elif event.type == MOUSEMOTION and moving:
           board_rect.move_ip(event.rel) 

    pygame.display.flip()
    screen.fill((0,0,0))
    board_rect.top = 0
    if board_rect.left > 0:
       board_rect.left = 0
    elif board_rect.right < 1920:
       board_rect.right = 1920
    screen.blit(board,board_rect)
    clock.tick(244)


pygame.quit()