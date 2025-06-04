import pygame
import math
from config import settings

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        #samImage = pygame.image.load("./Assets/images/samurai.png")
        #self.surf = pygame.transform.scale(samImage, (35, 50))
        #self.rect = self.surf.get_rect()
        
        #self.surfLeft = pygame.transform.flip(self.surf, True, False) # facing left or right
        #self.surfRight = pygame.transform.scale(samImage, (35, 50))

        # Adding Sprites
        self.original_size = (96, 96)
        self.display_size = (96 * 2, 96 * 2) # Scale * 2

        self.sheet = pygame.image.load("./Assets/images/IDLE.png").convert_alpha()

        self.frames = [self.get_frame(i) for i in range(10)] #Range is frame count for sprite
        self.current_frame = 0
        self.animation_timer = 0
        self.animation_speed = 100

        #THIS IS THE SIZE OF THE RECT
        self.rect = pygame.Rect(0, 0, 44, 75)

        self.surf = pygame.transform.scale(self.frames[0], self.display_size)
        self.image = pygame.transform.scale(self.frames[0], self.display_size)
        #self.rect = self.image.get_rect()

        self.surfLeft = pygame.transform.flip(self.surf, True, False)
        self.surfRight = self.surf
        #####
        

        self.pos =  pygame.math.Vector2((30, 255)) #Start pos
        self.vel = pygame.math.Vector2(0, 0)
        self.acc = pygame.math.Vector2(0, 0)

        self.jumping = False


    def get_frame(self, index, row=0):
        frame = pygame.Surface(self.original_size, pygame.SRCALPHA)
        #THIS IS WHERE IMAGE IS SET ONTO THE RECT
        frame.blit(self.sheet, (-37, -45), (index * self.original_size[0], row * self.original_size[1], *self.original_size))
        return frame

    def idle_anim(self):
        now = pygame.time.get_ticks()
        if now - self.animation_timer > self.animation_speed:
            self.animation_timer = now
            self.current_frame = (self.current_frame + 1) % len(self.frames)
            raw_frame = self.frames[self.current_frame]
            self.image = pygame.transform.scale(raw_frame, self.display_size) #Resize for display

    def move(self):
        self.acc = pygame.math.Vector2(0,0.5) # second number is Gravity
        pressed_keys = pygame.key.get_pressed()

        if pressed_keys[pygame.K_LEFT]:
            self.acc.x = -settings.ACC
            #self.surf = self.surfLeft
            self.surf = pygame.transform.flip(self.surf, True, False)
        if pressed_keys[pygame.K_RIGHT]:
            self.acc.x = settings.ACC
            #self.surf = self.surfRight

        self.acc.x += self.vel.x * settings.FRIC
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc

        '''
        # This causes passthrough walls that return on opposite side

        if self.pos.x > settings.SCREEN_WIDTH:
            self.pos.x = 0
        if self.pos.x < 0:
            self.pos.x = settings.SCREEN_WIDTH
        '''

        # Stop when reaching wall
        if self.pos.x > settings.SCREEN_WIDTH - 10:
            self.pos.x = settings.SCREEN_WIDTH - 10
        if self.pos.x < 10:
            self.pos.x = 10 

        self.rect.midbottom = self.pos


    def update(self, player, platform):
        self.idle_anim()
        hits = pygame.sprite.spritecollide(player, platform, False)

        if self.vel.y > 0:
            if hits:
                if self.pos.y < hits[0].rect.bottom:
                    self.pos.y = hits[0].rect.top 
                    self.vel.y = 0
                    self.jumping = False

    def jump(self, platform):
        hits = pygame.sprite.spritecollide(self, platform, False)
        if hits and not self.jumping:
            self.jumping = True
            self.vel.y = -10 # Jump height
        
    def short_jump(self, platform):
        if self.jumping:
            if self.vel.y < -3:
                self.vel.y = -3
        