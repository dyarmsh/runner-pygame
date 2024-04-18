import pygame
from sys import exit

# necassary to run this before any other call; initialises all the pygame functions
pygame.init()

# "display surface" = what the player will see and interact with
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption("Runner")

# controlling the frame rate
clock = pygame.time.Clock()

# creating regular surfaces (which will be placed on the display surface)
test_surface = pygame.Surface((100,200))
test_surface.fill("Red")

# importing an img - putting it on a separate surface
sky_surface = pygame.image.load("graphics/Sky.png").convert()
ground_surface = pygame.image.load("graphics/ground.png").convert()

# adding text in pygame
test_font = pygame.font.Font("font/Pixeltype.ttf", 50) # arg 1: font type (file path), arg 2: font size
text_surface = test_font.render("My Game", False, "Black") # arg 1: text, arg 2: text smoothing (boolean), arg 3: colour

# snail surface
snail_surface = pygame.image.load("graphics/snail/snail1.png").convert_alpha()
snail_rect = snail_surface.get_rect(midbottom = (600, 300))


# player surface
player_surface = pygame.image.load("graphics/Player/player_walk_1.png").convert_alpha()
player_rect = player_surface.get_rect(midbottom = (80,300)) # takes a surface and draws a rectangle around it

while True:

    # event loop - check for the player's input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit() # escapes the while True loop
        # if event.type == pygame.MOUSEMOTION: # check if mouse collides with the player rectangle
        #     if player_rect.collidepoint(event.pos):
        #         print("COLLISION!")




    # draw all the elements
    # update everything

    # adding the test surface on the display surface
    # ORIGIN (0,0) is on the TOP LEFT
    screen.blit(sky_surface, (0,0)) # arg 1: surface to add, arg 2: (x,y) position on display surface
    screen.blit(ground_surface, (0,300))
    screen.blit(text_surface, (300, 50))
    
    snail_rect.x -= 4
    # animating the snail
    if snail_rect.right <= 0:
        snail_rect.left = 800
    screen.blit(snail_surface, snail_rect)

    player_rect.left += 1
    screen.blit(player_surface, player_rect)

    pygame.display.update()    # updates the display surface
    clock.tick(60)  # the while loop should not run faster than 60 fps
