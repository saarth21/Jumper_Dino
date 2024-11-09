import pygame
import random
pygame.init()
screen_width = 900
screen_height = 800
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Dino Game')
# Animation functions -- different animation function
def animation():
    global dinoSurface, dinoIndex
    dinoIndex += 0.3
    if (dinoIndex >= len(dinoWalk)):
        dinoIndex = 0
    dinoSurface = dinoWalk[int(dinoIndex)]
#Lose
lose = False
# Pterodactyl Sprite
parySurface = pygame.image.load("Pterodactyl.png").convert_alpha()
parySurface = pygame.transform.scale(parySurface,(80,80))
pary=parySurface.get_rect()
#font
excoreFont = pygame.font.Font("Roboto-Regular.ttf",34)
textSurface = excoreFont.render("score",True,(0,0,0))
textRectangle = textSurface.get_rect()
#Game over
textLoseSurface = excoreFont.render("Game over",True,(0,0,0))
textLoseRectangle = textLoseSurface.get_rect()
textLoseRectangle.center = (screen_width/2,screen_height/2)
#Score
score = 0
# more cactus
cactus1Surface = pygame.image.load("Cactus1.png").convert_alpha()
cactus1Surface = pygame.transform.scale(cactus1Surface, (50,80))
cactus2Surface = pygame.image.load("Cactus2.png").convert_alpha()
cactus2Surface = pygame.transform.scale(cactus2Surface, (100,80))
cactus3Surface = pygame.image.load("Cactus3.png").convert_alpha()
cactus3Surface = pygame.transform.scale(cactus3Surface, (100,80))
cacti = [cactus1Surface,cactus2Surface,cactus3Surface]
# Animations
dinoWalkOne = pygame.image.load("Walkone.png").convert_alpha()
dinoWalkTwo = pygame.image.load("Walktwo.png").convert_alpha()
dinoWalkOne = pygame.transform.scale(dinoWalkOne,(70,80))
dinoWalkTwo = pygame.transform.scale(dinoWalkTwo,(70,80))
dinoWalk = [dinoWalkOne,dinoWalkTwo]
dinoIndex = 0
dinoSurface = dinoWalk[dinoIndex]
#dino player
dino=dinoSurface.get_rect(midbottom=(30,screen_height-100))
#cactus
cactusSurface = cactus1Surface
cactus=cactusSurface.get_rect(midbottom=(screen_width,screen_height-120))
cactus.y = screen_height-200  
floorY=600
jumpSpeed=16
gravity=13
jumpHeight=400
isJumping=False
run=True
#floor
floorSurrface=pygame.image.load('floor sprite.png')
floorSurrface=pygame.transform.scale(floorSurrface,(screen_width,397))
floor=floorSurrface.get_rect(midbottom=(450,800))
#backround
backroundSurface=pygame.image.load('pixel-art-sky.jpg')
backroundSurface=pygame.transform.scale(backroundSurface,(screen_width,screen_height))
backround=backroundSurface.get_rect()
#while code               
while run:
    if dino.colliderect(cactus):
        lose = True
    if lose == False:
        #Call function
        animation()
        #Player controls
        key = pygame.key.get_pressed()
        if ( key[pygame.K_SPACE]==True or key[pygame.K_UP]==True) and dino.y == floorY: 
            isJumping=True
        #Player movement:
        if isJumping==True:
            dino.y -= jumpSpeed
        else:
            dino.y += gravity
        if dino.y <= jumpHeight:
            isJumping = False
        if dino.y >= floorY:
            dino.y = floorY
        #Cactus movement:
        cactus.x -= 16
        if cactus.x <= -50:
            cactus.x = screen_width
            cactus.y = screen_height-200    
            cactusSurface = cacti[random.randint(0,2)]
        score += 1
    else:
        key = pygame.key.get_pressed()
        if ( key[pygame.K_SPACE]==True or key[pygame.K_UP]==True):
            lose = False
            score = 0
            dino.y = floorY
            cactus.x = screen_width
    textSurface = excoreFont.render("Score: "+ str(score),True,(0,0,0))
    #display sprite/backround
    screen.blit(backroundSurface,backround)
    screen.blit(dinoSurface,dino)
    screen.blit(floorSurrface,floor)
    screen.blit(cactusSurface,cactus)
    screen.blit(textSurface,textRectangle)
    if lose == True:
        screen.blit(textLoseSurface,textLoseRectangle)
    #screen.blit(textLoseSurface,textLoseRectangle)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
           run = False
           pygame.quit()
    #Updates the code
    pygame.display.update() 
    pygame.time.Clock().tick(60) 

pygame.quit()