import pygame

# pygame setup
pygame.init()
Screen_Width, Screen_Height = 500, 600
screen = pygame.display.set_mode((Screen_Width, Screen_Height))
pygame.display.set_caption('Space Shooter')
running = True

background = pygame.image.load('src/SpaceBg.png')
surf = pygame.Surface((100,200))

while running:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.blit(background, (0, 0))

    pygame.display.update()

pygame.quit()
