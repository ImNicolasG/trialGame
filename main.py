# Example file showing a circle moving on screen
import pygame

# Initialize Pygame
pygame.init()


# Set width and height for window
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 300

# Create window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.display.set_caption("Sidescroller Game") # Title



# Colors
beige = (240, 242, 189) # background

orange = (202, 120, 66) # player1
green = (178, 205, 156) # player2


# # # #Character# # # #

CHAR_SIZE = 50

# Start Location
x = 50
y = 200
CHAR_W = 30
CHAR_H = 80
CHAR_VEL_X = 3 # Velocity
CHAR_VEL_Y = 3
JUMP = False


# # MAIN GAME LOOP # #
running = True

while running:
    pygame.time.delay(10)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed() # checks keypress
    if keys[pygame.K_LEFT] and x > 0:
        x -= CHAR_VEL_X
    if keys[pygame.K_RIGHT] and x < 800 - CHAR_W:
        x += CHAR_VEL_X
    #if keys[pygame.K_UP] and y > 0:
    #    y -= CHAR_VEL_Y
    #if keys[pygame.K_DOWN] and y < 300 - CHAR_H:
    #    y +=CHAR_VEL_Y
    
    if not JUMP and keys[pygame.K_SPACE]:
        JUMP = True
    if JUMP:
        y -= CHAR_VEL_Y
        CHAR_VEL_Y -= 1
        if CHAR_VEL_Y < -10:
            JUMP = False
            CHAR_VEL_Y = 10


    screen.fill(beige) # Resets screen with background color
    pygame.draw.rect(screen, orange,(x, y, CHAR_W, CHAR_H), border_radius=5) # screen/color/x-location/y-location/width-of-object/height-of-object/outline.
    pygame.draw.rect(screen, green,(700, 200, CHAR_W, CHAR_H), border_radius=5)
    
    
    pygame.display.flip() # Update display

pygame.quit()



