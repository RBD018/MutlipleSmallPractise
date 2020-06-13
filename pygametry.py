import pygame

pygame.init()

screen = pygame.display.set_mode((800,600))

pygame.display.set_caption("TIC TAC")
#icon = pygame.image.load('traffic-sign.png')
pygame.display.set_icon(icon)

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run =False
    screen.fill((204,255,0))
    
    pygame.draw.rect(screen,(255,0,0),(266,0,10,600))
    pygame.draw.rect(screen,(255,0,0),(532,0,10,600))
    pygame.draw.rect(screen,(255,0,0),(0,200,800,10))
    pygame.draw.rect(screen,(255,0,0),(0,400,800,10))

    pygame.display.update()

