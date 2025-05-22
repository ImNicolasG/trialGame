# Example file showing a circle moving on screen
import pygame
import sys

# Initialize Pygame
pygame.init()

# Create Window
# Set width and height for window
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 300
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.display.set_caption("Sidescroller Game") # Title
CLOCK = pygame.time.Clock()


# Colors
beige = (240, 242, 189) # background
orange = (202, 120, 66) # player1
green = (178, 205, 156) # player2


# Standing and Jumping Sprite
STANDING_PIXEL = pygame.transform.scale(pygame.image.load("Assets/sprites/standing.png"), (50, 80))
JUMPING_PIXEL = pygame.transform.scale(pygame.image.load("Assets/sprites/jumping.png"), (50, 80))

# # # #Character# # # #
# Start Location
x = 50
y = 240
CHAR_W = 50
CHAR_H = 80
CHAR_VEL_X = 5 # Velocity
JUMP = False

Y_GRAVITY = 1
JUMP_HEIGHT = 15 
Y_VELOCITY = JUMP_HEIGHT


player_rect = STANDING_PIXEL.get_rect(center=(x, y))

# # MAIN GAME LOOP # #
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(beige) # Resets screen with background color
   
   # # # MOVEMENT # # #
    keys = pygame.key.get_pressed() # checks keypress
    if keys[pygame.K_LEFT] and x > 0 + (CHAR_W/2):
        x -= CHAR_VEL_X
    if keys[pygame.K_RIGHT] and x < 800 - (CHAR_W/2):
        x += CHAR_VEL_X

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
        player_rect = STANDING_PIXEL.get_rect(center=(x, y))
        screen.blit(JUMPING_PIXEL, player_rect)
    else:
        player_rect = STANDING_PIXEL.get_rect(center=(x, y))
        screen.blit(STANDING_PIXEL, player_rect)

    #-#-#-#-#-#-#-#-#-#

    pygame.time.delay(10)

    #pygame.draw.rect(screen, orange,(x, y, CHAR_W, CHAR_H), border_radius=5) # screen/color/x-location/y-location/width-of-object/height-of-object/outline.
    pygame.draw.rect(screen, green,(700, 200, CHAR_W, CHAR_H), border_radius=5) # PLAYER 2
    
    pygame.draw.rect(screen, (75,53,42), (0, 280, 800, 100), 0) # FLOOR
    
    
    pygame.display.flip() # Update display
    CLOCK.tick(60)

pygame.quit()



