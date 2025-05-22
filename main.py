# Example file showing a circle moving on screen
import pygame

# Initialize Pygame
pygame.init()


# Set width and height for window
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 300

# Create window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.display.set_caption("Sidescroller Game") # Title
CLOCK = pygame.time.Clock()


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
CHAR_VEL_X = 5 # Velocity
JUMP = False

Y_GRAVITY = 1
JUMP_HEIGHT = 15 
Y_VELOCITY = JUMP_HEIGHT


# # MAIN GAME LOOP # #
running = True

while running:
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
    
    # if space is pressed, jump is true
    if not JUMP and keys[pygame.K_SPACE]:
        JUMP = True
    # When jump is true, y location is changed by amount of char velocity until the velocity reaches {value} which 
    # will go down to negative so it simulates a jump.
    if JUMP:
        y -= Y_VELOCITY
        Y_VELOCITY -= Y_GRAVITY
        if Y_VELOCITY < -JUMP_HEIGHT:
            JUMP = False
            Y_VELOCITY = JUMP_HEIGHT

    pygame.time.delay(10)
    screen.fill(beige) # Resets screen with background color
    pygame.draw.rect(screen, orange,(x, y, CHAR_W, CHAR_H), border_radius=5) # screen/color/x-location/y-location/width-of-object/height-of-object/outline.
    pygame.draw.rect(screen, green,(700, 200, CHAR_W, CHAR_H), border_radius=5)
    
    # FLOOR
    pygame.draw.rect(screen, (75,53,42), (0, 280, 800, 100), 0)
    
    
    pygame.display.flip() # Update display
    CLOCK.tick(60)

pygame.quit()



