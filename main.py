import pygame
import constants
from character import CharacterClass
from weapon import Weapon
from utils import scale_img

pygame.init()


screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
pygame.display.set_caption("Sample Name")

# create clock to mantain frame rate
clock = pygame.time.Clock()

# define player mov var
moving_left = False
moving_right = False
moving_up = False
moving_down = False


# load weapons images
bow_image = scale_img(
    pygame.image.load(f"assets/images/weapons/bow.png").convert_alpha(),
    constants.WEAPON_SCALE,
)

arrow_image = scale_img(
    pygame.image.load(f"assets/images/weapons/arrow.png").convert_alpha(),
    constants.WEAPON_SCALE,
)


# load character images
mob_animations = []
mob_types = ["elf", "imp", "skeleton", "goblin", "muddy", "tiny_zombie", "big_demon"]

animation_types = ["idle", "run"]
for mob in mob_types:
    # load images
    animation_list = []
    for animation in animation_types:
        # reset temporary list of images
        temp_list = []
        for i in range(4):
            img = pygame.image.load(
                f"assets\images\characters\{mob}\{animation}\{i}.png"
            ).convert_alpha()
            img = scale_img(img, constants.SCALE)
            temp_list.append(img)
        animation_list.append(temp_list)
    mob_animations.append(animation_list)

# Create Player
player = CharacterClass(100, 100, mob_animations, 0)

# create player weapon
bow = Weapon(bow_image, arrow_image)


# create sprite groups
arrow_group = pygame.sprite.Group()

# main game loop

run = True

while run:
    # control frame rate
    clock.tick(constants.FPS)

    screen.fill(constants.BG)

    # calculate player movement before drawing it
    dx = 0
    dy = 0

    if moving_right:
        dx = constants.SPEED

    if moving_left:
        dx = -constants.SPEED

    if moving_up:
        dy = -constants.SPEED

    if moving_down:
        dy = constants.SPEED

    # move player

    player.move(dx, dy)
    # update player
    player.update()
    arrow = bow.update(player)
    if arrow:
        arrow_group.add(arrow)
    for arrow in arrow_group:
        arrow.update()

    # draw player
    player.draw(screen)
    bow.draw(screen)
    for arrow in arrow_group:
        arrow.draw(screen)

    # event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        # take keyboard input
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                moving_left = True
            if event.key == pygame.K_d:
                moving_right = True
            if event.key == pygame.K_w:
                moving_up = True
            if event.key == pygame.K_s:
                moving_down = True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                moving_left = False
            if event.key == pygame.K_d:
                moving_right = False
            if event.key == pygame.K_w:
                moving_up = False
            if event.key == pygame.K_s:
                moving_down = False

    pygame.display.update()

pygame.quit()
