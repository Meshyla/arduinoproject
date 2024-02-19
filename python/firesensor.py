import serial as sr
import pygame
pygame.init()
surface = pygame.display.set_mode((500, 500))
color = (255, 0, 0)
surface.fill(color)
pygame.display.flip()


serialArd = sr.Serial('COM3', baudrate=9600)

fire_win = pygame.display.set_mode((500, 500))

fontzz = pygame.font.SysFont('algerian', 50)

run = True
while run == True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    

    if serialArd.readline().decode().strip() == 'YES':
        result = fontzz.render("There is fire!", 1 ,(255,185,205))
        fire_win.fill((255,0,0))
        fire_win.blit(result, (0,0))
        pygame.display.update()
       
           

    else:
        result = fontzz.render("There's no fire!", 1 ,(215,255,255))
        pygame.display.update()
        fire_win.fill((0,0,255))
        fire_win.blit(result, (0,0))
        
       
    
    
pygame.quit()
