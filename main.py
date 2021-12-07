import os, sys
import pygame
import random
from constants import *
from draw_text import drawText
from sprites import *

if getattr(sys, 'frozen', False):
    os.chdir(sys._MEIPASS)

pygame.font.init()  # for writing text to the screen
pygame.mixer.init()  # for sound

pygame.display.set_caption("Run Away")

WIN = pygame.display.set_mode((WIDTH, HEIGHT))

# TODO: set the icon of the running window
# pygame.display.set_icon(CAKE_IMAGE)

LARGE_MAP = pygame.surface.Surface((LARGE_MAP_WIDTH, LARGE_MAP_HEIGHT))
camera = pygame.Rect((LARGE_MAP_WIDTH // 2 - WIDTH // 2 - 200, LARGE_MAP_HEIGHT // 2 - HEIGHT // 2 + 500), (WIDTH, HEIGHT))






TERRAIN_IMAGES = dict()

TEXT_FONT = pygame.font.SysFont('lucidaconsole', 40)
DESC_FONT = pygame.font.SysFont('lucidaconsole', 20)
CELL_FONT = pygame.font.SysFont('lucidaconsole', 25)
BABY_FONT = pygame.font.SysFont('lucidaconsole', 21)

all_sprites = pygame.sprite.Group()
terrain_sprites = pygame.sprite.Group()
menu_sprites = pygame.sprite.Group()


def coordinates_to_xy(coordinates):
    return coordinates[0] * TILE_WIDTH, coordinates[1] * TILE_HEIGHT


def draw_window(flags):
    pygame.draw.rect(LARGE_MAP, GRAY, pygame.Rect(0, 0, LARGE_MAP_WIDTH, LARGE_MAP_HEIGHT))

    all_sprites.draw(LARGE_MAP)

    WIN.blit(LARGE_MAP, (0, 0), camera)

    pygame.display.update()


def add_sprite_to_group(sprite, group):
    group.add(sprite)
    # do not add the sprite twice if the group given is all_sprites
    if not group == all_sprites:
        all_sprites.add(sprite)


def get_random_terrain_image():
    return TERRAIN_IMAGES[random.randint(0, 2)]

def game():
    # pygame.mixer.music.load(os.path.join('assets', 'xDeviruchi - Exploring The Unknown (Loop).wav'))
    # pygame.mixer.music.set_volume(0.1)
    # pygame.mixer.music.play(-1)
    # locks mouse into window
    # pygame.event.set_grab(True)
    restart = False
    clock = pygame.time.Clock()
    title_mode = True
    run = True
    frames = 0
    time_ms = 0
    game_begin_time = pygame.time.get_ticks()  # the time that the game actually began
    start_time = pygame.time.get_ticks()  # the time that the maze we're on began
    # idk what a reasonable starting value is.
    cursor_xy_coordinates = (WIDTH // 2, HEIGHT // 2)
    pygame.mouse.set_pos(cursor_xy_coordinates)

    flags = dict()

    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            # handle events
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                break
            # escape should be allowed, right?
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    run = False
                    pygame.quit()
                    continue
        if not run:
            continue
        draw_window()
        if not action_menu_sprites_added:
            action_menu_sprites_added = True

        frames += 1
        current_time_ms = pygame.time.get_ticks() % 1000
        if time_ms > current_time_ms:
            frames_string = repr(frames)
            frames = 0
        time_ms = current_time_ms
    if restart:
        game()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    game()
