import pygame
import constants
from character import CharacterClass
from weapon import Weapon
from damageText import DamageText
from utils import scale_img

# TODO AFTER LOGIC PART IS FINISHED, REWRITE CODE FOLLOWING GOOD PRACTICES

# UNIVERSAL NEEDS
pygame.init()

# GAME SCREEN
screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
pygame.display.set_caption("Sample Name")

# GAME UNIVERSAL CLOCK
clock = pygame.time.Clock()

# FIXED VARS
moving_left = False
moving_right = False
moving_up = False
moving_down = False
font = pygame.font.Font("assets/fonts/AtariClassic.ttf", 20)
# --------------- START RENDER SECTION-------------------------------------------------------

bow_image = scale_img(
    pygame.image.load(f"assets/images/weapons/bow.png").convert_alpha(),
    constants.WEAPON_SCALE,
)

arrow_image = scale_img(
    pygame.image.load(f"assets/images/weapons/arrow.png").convert_alpha(),
    constants.WEAPON_SCALE,
)
# --------------- END RENDER SECTION-------------------------------------------------------
# --------------- START LOAD SECTION-------------------------------------------------------

mob_animations = []
mob_types = ["elf", "imp", "skeleton", "goblin", "muddy", "tiny_zombie", "big_demon"]

animation_types = ["idle", "run"]
for mob in mob_types:
    animation_list = []
    for animation in animation_types:
        temp_list = []
        for i in range(4):
            img = pygame.image.load(
                f"assets\images\characters\{mob}\{animation}\{i}.png"
            ).convert_alpha()
            img = scale_img(img, constants.SCALE)
            temp_list.append(img)
        animation_list.append(temp_list)
    mob_animations.append(animation_list)


# --------------- END LOAD SECTION-------------------------------------------------------
# --------------- START CREATION SECTION-------------------------------------------------
player = CharacterClass(100, 100, 100, mob_animations, 0)
enemy = CharacterClass(200, 300, 100, mob_animations, 1)
bow = Weapon(bow_image, arrow_image)

# ENEMY LIST
enemy_list = []
enemy_list.append(enemy)


# ARROW GROUP
damage_text_group = pygame.sprite.Group()
arrow_group = pygame.sprite.Group()
# --------------- START MAIN GAME LOOP -------------------------------------------------------
run = True
while run:
    # FRAME RATE CONTROL
    clock.tick(constants.FPS)
    screen.fill(constants.BG)
    # --------------- START MOVE SECTION-------------------------------------------------------
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
    player.move(dx, dy)
    # --------------- END MOVE SECTION---------------------------------------------------------
    # --------------- START UPDATE SECTION-----------------------------------------------------
    player.update()
    arrow = bow.update(player)

    if arrow:
        arrow_group.add(arrow)

    for arrow in arrow_group:
        damage, damage_pos = arrow.update(enemy_list)
        if damage:
            damage_text = DamageText(
                damage_pos.centerx, damage_pos.y, damage, constants.RED, font
            )
            damage_text_group.add(damage_text)

    damage_text_group.update()

    for enemy in enemy_list:
        enemy.update()
    # --------------- END UPDATE SECTION-------------------------------------------------------
    # --------------- START DRAW SECTION-------------------------------------------------------
    for enemy in enemy_list:
        enemy.draw(screen)

    player.draw(screen)
    bow.draw(screen)
    damage_text_group.draw(screen)

    for arrow in arrow_group:
        arrow.draw(screen)
    # --------------- END DRAW SECTION---------------------------------------------------------
    # --------------- EVENTS SECTION-----------------------------------------------------------
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        # KEYBOARD INPUTS
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                moving_left = True
            if event.key == pygame.K_d:
                moving_right = True
            if event.key == pygame.K_w:
                moving_up = True
            if event.key == pygame.K_s:
                moving_down = True
        # RESET MOVEMENT
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                moving_left = False
            if event.key == pygame.K_d:
                moving_right = False
            if event.key == pygame.K_w:
                moving_up = False
            if event.key == pygame.K_s:
                moving_down = False

    # UPDATE THE DISPLAY
    pygame.display.update()

pygame.quit()
