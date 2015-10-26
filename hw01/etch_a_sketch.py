import pygame

pygame.init()

white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
lime = (0,255,0)
yellow = (255, 255, 0)


gameDisplay = pygame.display.set_mode((800,600))
pygame.display.set_caption('BeagleBone')


pygame.display.update()

gameExit = False

lead_x = 300
lead_y = 300

gameDisplay.fill(white)
while not gameExit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameExit = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                lead_x -= 10
                print "LEFT"
            if event.key == pygame.K_RIGHT:
                    lead_x += 10
                    print "RIGHT"
            if event.key == pygame.K_UP:
                lead_y -= 10
                print "UP"
            if event.key == pygame.K_DOWN:
                    lead_y += 10
                    print "DOWN"
            if event.key == pygame.K_ESCAPE:
                gameDisplay.fill(white)
                    
                
        
        
    #gameDisplay.fill(white)
    pygame.draw.rect(gameDisplay, black, [lead_x,lead_y,10,10],2)
    pygame.display.update()
    
        
pygame.quit()
quit()
