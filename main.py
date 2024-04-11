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
sky_surface = pygame.image.load("graphics/Sky.png")
ground_surface = pygame.image.load("graphics/ground.png")

# adding text in pygame
test_font = pygame.font.Font("font/Pixeltype.ttf", 50) # arg 1: font type (file path), arg 2: font size
text_surface = test_font.render("My Game", False, "Green") # arg 1: text, arg 2: text smoothing (boolean), arg 3: colour

while True:

    # event loop - check for the player's input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit() # escapes the while True loop


    # draw all the elements
    # update everything

    # adding the test surface on the display surface
    # ORIGIN (0,0) is on the TOP LEFT
    screen.blit(sky_surface, (0,0)) # arg 1: surface to add, arg 2: (x,y) position on display surface
    screen.blit(ground_surface, (0,300))
    screen.blit(text_surface, (300, 50))

    pygame.display.update()    # updates the display surface
    clock.tick(60)  # the while loop should not run faster than 60 fps
