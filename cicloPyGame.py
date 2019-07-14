import pygame, sys

#pintamos la pantalla
width = 640
height = 480

screen = pygame.display.set_mode((width, height))
screen.fill((246, 147, 48))
pygame.display.set_caption("Ciclo básico de pygame")

pygame.font.init()

#escuchador de eventos
gameOver = False
while not gameOver:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:#evento de cerrar en el aspa la pantalla
            gameOver = True
            
    #repintamos la pantalla
    pygame.display.flip()
            
pyGame.quit()
sys.exit()