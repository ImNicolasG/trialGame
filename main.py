# Example file showing a circle moving on screen
import pygame
import sys

# Initialize Pygame
pygame.init()
pygame.font.init()

# Create Window
# Set width and height for window
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 300
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.display.set_caption("Sidescroller Game") # Title
CLOCK = pygame.time.Clock()
FONT = pygame.font.SysFont("Arial", 24)

# Colors
beige = (240, 242, 189) # background
orange = (202, 120, 66) # player1
green = (178, 205, 156) # player2


# # # #Character# # # #

# Standing and Jumping Sprite
STANDING_PIXEL = pygame.transform.scale(pygame.image.load("Assets/sprites/standing.png"), (50, 80))
JUMPING_PIXEL = pygame.transform.scale(pygame.image.load("Assets/sprites/jumping.png"), (60, 80))
STANDING_LEFT = pygame.transform.flip(STANDING_PIXEL, flip_x=1, flip_y=0)
JUMPING_LEFT = pygame.transform.flip(JUMPING_PIXEL, flip_x=1, flip_y=0)

char_x = 50 # x location
char_y = 240 # y location
CHAR_W = 50
CHAR_H = 80
CHAR_VEL_X = 5 # Velocity
JUMP = False
DIRECTION_RIGHT = True

FALLING = False
FALL_VEL = 0
Y_GRAVITY = 1
JUMP_HEIGHT = 15 
Y_VELOCITY = JUMP_HEIGHT

# # # #COINS# # # #
#    pygame.draw.circle(screen, (254, 186, 23), (600, 240), 15) # coin!

COINS = 0
coins_rects = [
    pygame.Rect(400, 240, 25, 25), # x, y, width, height
    pygame.Rect(450, 240, 25, 25),
    pygame.Rect(500, 240, 25, 25),
    pygame.Rect(550, 240, 25, 25)
]


player_rect = STANDING_PIXEL.get_rect(center=(char_x, char_y))

platform = pygame.Rect(470, 200, 70, 30)
floor = pygame.Rect(0, SCREEN_HEIGHT-20, 800, 50)



# # MAIN GAME LOOP # #
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(beige) # Resets screen with background color
    
    # # # COIN COLLECTION # # #
    

    for coin in coins_rects[:]:
        pygame.draw.ellipse(screen, (254, 186, 23), coin)
        if player_rect.colliderect(coin):
            COINS += 1
            coins_rects.remove(coin)

    coin_text = FONT.render(f"Coins: {COINS}", True, (0,0,0)) # Draw coin text
    screen.blit(coin_text, (10,10)) # Display text on screen

   
    # # # MOVEMENT # # #
    future_y = char_y + 2
    future_rect = STANDING_PIXEL.get_rect(center=(char_x, future_y))
    if not future_rect.colliderect(floor): # not colliding
        
        FALL_VEL += Y_GRAVITY
        char_y += FALL_VEL
        FALLING = True
    else:
        char_y = floor.top + CHAR_H // 2
        FALLING = False
        FALL_VEL = 0
        
    if not future_rect.colliderect(platform) and FALLING == True:
        char_y += Y_GRAVITY
    else:
        char_y = platform.top - CHAR_H // 2
        FALLING = False
    
        
        


    keys = pygame.key.get_pressed() # checks keypress
    if keys[pygame.K_LEFT] and char_x > 0 + (CHAR_W/2):
        char_x -= CHAR_VEL_X
        DIRECTION_RIGHT = False
    if keys[pygame.K_RIGHT] and char_x < 800 - (CHAR_W/2):
        char_x += CHAR_VEL_X
        DIRECTION_RIGHT = True
    
    # if space is pressed, jump is true
    if not JUMP and keys[pygame.K_SPACE]:
        JUMP = True
    # When jump is true, y location is changed by amount of char velocity until the velocity reaches {value} which 
    # will go down to negative so it simulates a jump.
    if JUMP:
        # THIS IF/ELSE CHECKS FACING DIRECTION
        if not DIRECTION_RIGHT:
            player_rect = STANDING_LEFT.get_rect(center=(char_x,char_y))
            screen.blit(JUMPING_LEFT, player_rect)
        else:
            player_rect = STANDING_PIXEL.get_rect(center=(char_x, char_y))
            screen.blit(JUMPING_PIXEL, player_rect)

        char_y -= Y_VELOCITY
        Y_VELOCITY -= Y_GRAVITY
        if Y_VELOCITY <= -JUMP_HEIGHT:
            JUMP = False
            FALLING = False
            Y_VELOCITY = JUMP_HEIGHT
            
    else:
        if not DIRECTION_RIGHT:  
            player_rect = STANDING_LEFT.get_rect(center=(char_x, char_y))
            screen.blit(STANDING_LEFT, player_rect)
        else:
            player_rect = STANDING_PIXEL.get_rect(center=(char_x, char_y))
            screen.blit(STANDING_PIXEL, player_rect)

    collide = player_rect.colliderect(platform)
    pygame.draw.rect(screen, (10, 10, 10), platform)

    
    #-#-#-#-#-#-#-#-#-#

    pygame.draw.rect(screen, green,(700, 200, CHAR_W, CHAR_H), border_radius=5) # PLAYER 2

    pygame.draw.rect(screen, (75,53,42), floor) # FLOOR
    
    
    pygame.display.flip() # Update display
    CLOCK.tick(60)

pygame.quit()



