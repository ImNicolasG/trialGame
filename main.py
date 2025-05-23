# Example file showing a circle moving on screen
import pygame
import sys
import os
from config import settings
from entities import player

# Initialize Pygame
pygame.init()
pygame.font.init()
# Create Window
window = pygame.display.set_mode((settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT))
pygame.display.set_caption(f"{settings.WINDOW_TITLE}") # Title
FONT = pygame.font.Font(settings.FONT, 24)

# Colors
settings.BG_COLOR = (240, 242, 189) # background
orange = (202, 120, 66) # player1
green = (178, 205, 156) # player2


# # # #Character# # # #

# Standing and Jumping Sprite
STANDING_PIXEL = pygame.transform.scale(pygame.image.load("Assets/images/samurai2.png"), (50, 80))
JUMPING_PIXEL = pygame.transform.scale(pygame.image.load("Assets/images/jumping.png"), (60, 80))
STANDING_LEFT = pygame.transform.flip(STANDING_PIXEL, flip_x=1, flip_y=0)
JUMPING_LEFT = pygame.transform.flip(JUMPING_PIXEL, flip_x=1, flip_y=0)

char_x = 50 # x location
char_y = 540 # y location
CHAR_W = 50
CHAR_H = 80
CHAR_VEL_X = 5 # Velocity
JUMP = False
DIRECTION_RIGHT = True

Y_GRAVITY = 1
JUMP_HEIGHT = 15 
Y_VELOCITY = JUMP_HEIGHT

# # # #COINS# # # #

COINS = 0
coins_rects = [
    pygame.Rect(400, 240, 25, 25), # x, y, width, height
    pygame.Rect(450, 240, 25, 25),
    pygame.Rect(500, 240, 25, 25),
    pygame.Rect(550, 240, 25, 25)
]


player_rect = STANDING_PIXEL.get_rect(center=(char_x, char_y))

platform = pygame.Rect(470, 200, 70, 30)
floor = pygame.Rect(0, settings.SCREEN_HEIGHT-20, 1200, 50)


def get_background(name):
    image = pygame.image.load(os.path.join("Assets", "images", name))
    _,_, width, height = image.get_rect()
    tiles = []

    for i in range(settings.SCREEN_WIDTH// width + 1):
        for j in range(settings.SCREEN_HEIGHT // height + 1):
            pos = [i * width, j * height]
            tiles.append(pos)

    return tiles, image



def handle_move(player):
    keys = pygame.key.get_pressed()
    player.x_vel = 0
    if keys[pygame.K_LEFT]:
        player.move_left(5)
    if keys[pygame.K_RIGHT]:
         player.move_right(5)


def draw(window, char):

    char.draw(window)

    pygame.display.update()


bg_img = pygame.image.load("Assets/images/sBackground.png")
bg_imgStretch = pygame.transform.scale(bg_img, (settings.SCREEN_WIDTH + 10, settings.SCREEN_HEIGHT + 10))

def main(window):
    CLOCK = pygame.time.Clock()
    char = player.Player(100, 100, 50, 50)
    running = True

    while running:
        CLOCK.tick(settings.FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                break

        char.loop(settings.FPS)
        handle_move(char)
        draw(window, char)
        window.blit(bg_imgStretch, (-5,-5))
    pygame.quit()
    quit()

if __name__ == "__main__":
    main(window)


'''
# # MAIN GAME LOOP # #
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            break

    screen.fill(settings.BG_COLOR) # Resets screen with background color
    
    # # # COIN COLLECTION # # #
    

    for coin in coins_rects[:]:
        pygame.draw.ellipse(screen, (254, 186, 23), coin)
        if player_rect.colliderect(coin):
            COINS += 1
            coins_rects.remove(coin)

    coin_text = FONT.render(f"Coins: {COINS}", True, (0,0,0)) # Draw coin text
    screen.blit(coin_text, (10,10)) # Display text on screen

   
    # # # MOVEMENT # # #
        
    keys = pygame.key.get_pressed() # checks keypress
    if keys[pygame.K_LEFT] and char_x > 0 + (CHAR_W/2):
        char_x -= CHAR_VEL_X
        DIRECTION_RIGHT = False
    if keys[pygame.K_RIGHT] and char_x < settings.SCREEN_WIDTH - (CHAR_W/2):
        char_x += CHAR_VEL_X
        DIRECTION_RIGHT = True
    

    # if space is pressed, jump is true
    if not JUMP and keys[pygame.K_SPACE]:
        JUMP = True
    # When jump is true, y location is changed by amount of char velocity until the velocity reaches {value} which 
    # will go down to negative so it simulates a jump.
    if JUMP:
        # THIS IF/ELSE CHECKS FACING DIRECTION for jump
        if not DIRECTION_RIGHT:
            player_rect = STANDING_LEFT.get_rect(center=(char_x,char_y))
            screen.blit(JUMPING_LEFT, player_rect)
        else:
            player_rect = STANDING_PIXEL.get_rect(center=(char_x, char_y))
            screen.blit(JUMPING_PIXEL, player_rect)

        char_y -= Y_VELOCITY
        Y_VELOCITY -= Y_GRAVITY
        if Y_VELOCITY < -JUMP_HEIGHT:
            JUMP = False
            Y_VELOCITY = JUMP_HEIGHT        
            
    else:
        if not DIRECTION_RIGHT:  
            player_rect = STANDING_LEFT.get_rect(center=(char_x, char_y))
            screen.blit(STANDING_LEFT, player_rect)
        else:
            player_rect = STANDING_PIXEL.get_rect(center=(char_x, char_y))
            screen.blit(STANDING_PIXEL, player_rect)

    pygame.draw.rect(screen, (10, 10, 10), platform)

    
    #-#-#-#-#-#-#-#-#-#

    pygame.draw.rect(screen, (75,53,42), floor) # FLOOR
    
    pygame.display.flip() # Update display
    CLOCK.tick(settings.FPS)


pygame.quit()
'''


