# Example file showing a circle moving on screen
import pygame

# Initialize Pygame
pygame.init()

# Colors
beige = (240, 242, 189) # background

orange = (202, 120, 66) # player


# # # #Character# # # #

object_size = 50

# Start Location
x = 50
y = 200
charW = 30
charH = 80
vel = 5 # Velocity

# Set width and height for window
width, height = 800, 300

# Create window
screen = pygame.display.set_mode((width, height))
screen.fill(beige) # Screen color

pygame.display.set_caption("Sidescroller Game") # Title



# # MAIN GAME LOOP # #
running = True

while running:
    pygame.time.delay(10)
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed() # checks keypress
    # for each key pressed, check if it is at the edge of window. If so, stop
    if keys[pygame.K_LEFT] and x > 0:
        x -= vel
    if keys[pygame.K_RIGHT] and x < 800 - charW:
        x += vel
    if keys[pygame.K_UP] and y > 0:
        y -= vel
    if keys[pygame.K_DOWN] and y < 300 -charH:
        y +=vel

    screen.fill(beige) # Resets screen with background color
    pygame.draw.rect(screen, orange,(x, y, charW, charH), border_radius=5) # screen/color/x-location/y-location/width-of-object/height-of-object/outline.
    pygame.display.update()
    #pygame.display.flip() # Update display

pygame.quit()



