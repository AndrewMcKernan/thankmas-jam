import pygame
import os
from constants import *



class MenuItem(pygame.sprite.Sprite):
    def __init__(self, rect, name, description):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((1, 1))
        self.rect = rect
        self.name = name
        self.description = description

    def __str__(self):
        return self.name + " " + str(self.rect.x) + "," + str(self.rect.y) + " - " + str(self.rect.width) + ',' + str(
            self.rect.height)


class Terrain(pygame.sprite.Sprite):
    def __init__(self, image, width, height, start_x=0, start_y=0):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(image, (width, height))
        self.rect = self.image.get_rect()
        self.rect.x = start_x
        self.rect.y = start_y


class MouseSprite(pygame.sprite.Sprite):
    def __init__(self, xy_position_tuple):
        pygame.sprite.Sprite.__init__(self)

        self.image = None
        self.rect = pygame.rect.Rect(xy_position_tuple, (1, 1))


class Player(pygame.sprite.Sprite):

    def __setup_sprites(self):
        PLAYER_IMAGES = dict()
        PLAYER_IMAGES[PLAYER_IDLE] = []
        IMAGE = pygame.image.load(os.path.join('assets', 'idle-1.png')).convert()
        IMAGE.set_colorkey(TRANSPARENT)
        PLAYER_IMAGES[PLAYER_IDLE].append(IMAGE)
        IMAGE = pygame.image.load(os.path.join('assets', 'idle-2.png')).convert()
        IMAGE.set_colorkey(TRANSPARENT)
        PLAYER_IMAGES[PLAYER_IDLE].append(IMAGE)
        IMAGE = pygame.image.load(os.path.join('assets', 'idle-3.png')).convert()
        IMAGE.set_colorkey(TRANSPARENT)
        PLAYER_IMAGES[PLAYER_IDLE].append(IMAGE)
        IMAGE = pygame.image.load(os.path.join('assets', 'idle-4.png')).convert()
        IMAGE.set_colorkey(TRANSPARENT)
        PLAYER_IMAGES[PLAYER_IDLE].append(IMAGE)

        PLAYER_IMAGES[PLAYER_MOVING] = []
        IMAGE = pygame.image.load(os.path.join('assets', 'move-1.png')).convert()
        IMAGE.set_colorkey(TRANSPARENT)
        PLAYER_IMAGES[PLAYER_MOVING].append(IMAGE)
        IMAGE = pygame.image.load(os.path.join('assets', 'move-2.png')).convert()
        IMAGE.set_colorkey(TRANSPARENT)
        PLAYER_IMAGES[PLAYER_MOVING].append(IMAGE)
        IMAGE = pygame.image.load(os.path.join('assets', 'move-3.png')).convert()
        IMAGE.set_colorkey(TRANSPARENT)
        PLAYER_IMAGES[PLAYER_MOVING].append(IMAGE)

        PLAYER_IMAGES[PLAYER_JUMPING] = []
        IMAGE = pygame.image.load(os.path.join('assets', 'jump-1.png')).convert()
        IMAGE.set_colorkey(TRANSPARENT)
        PLAYER_IMAGES[PLAYER_JUMPING].append(IMAGE)
        IMAGE = pygame.image.load(os.path.join('assets', 'jump-2.png')).convert()
        IMAGE.set_colorkey(TRANSPARENT)
        PLAYER_IMAGES[PLAYER_JUMPING].append(IMAGE)

        PLAYER_IMAGES[PLAYER_DAMAGED] = []
        IMAGE = pygame.image.load(os.path.join('assets', 'hurt-1.png')).convert()
        IMAGE.set_colorkey(TRANSPARENT)
        PLAYER_IMAGES[PLAYER_DAMAGED].append(IMAGE)
        IMAGE = pygame.image.load(os.path.join('assets', 'hurt-2.png')).convert()
        IMAGE.set_colorkey(TRANSPARENT)
        PLAYER_IMAGES[PLAYER_DAMAGED].append(IMAGE)

        return PLAYER_IMAGES


    def __init__(self, start_x=0, start_y=0):
        pygame.sprite.Sprite.__init__(self)

        self.frames = self.__setup_sprites()

        self.frame_index = 0
        self.image = self.frames[PLAYER_IDLE][self.frame_index]
        self.last_frame_update = pygame.time.get_ticks()
        self.current_animation = PLAYER_IDLE
        self.rect = self.image.get_rect()
        self.rect.x = start_x
        self.rect.y = start_y

    def update(self, *args, **kwargs) -> None:
        # assume args[0] is the type of frame we want
        if self.current_animation != args[0]:
            # if we are changing animation types, the next frame starts now
            self.last_frame_update = pygame.time.get_ticks() - 150
            self.current_animation = args[0]
        if self.last_frame_update + 150 <= pygame.time.get_ticks():
            # after 150 ms, update the frame
            if self.frame_index + 1 > len(self.frames):
                self.frame_index = 0
            else:
                self.frame_index += 1
            self.image = self.frames[args[0]][self.frame_index]

    def get_grid_coordinates(self):
        return self.rect.x // TILE_WIDTH, self.rect.y // TILE_HEIGHT

    def move_to_grid_coordinates(self, coordinates):
        self.rect.x = coordinates[0] * TILE_WIDTH
        self.rect.y = coordinates[1] * TILE_HEIGHT
