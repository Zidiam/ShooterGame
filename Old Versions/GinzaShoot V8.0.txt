# Made by Jason Melnik
# Date: 8/1/2018
# Version of game: 8.0

# Update Notes:
#added 2 automatics
#added 2 shotguns
#added 2 snipers
#
#
#
#
#
#

# Imports
import pygame
import time
import random
import operator
import fileinput
import os
import sys
import math
from pygame.math import Vector2
from globals import *
from UltraColor import *
from images import Images

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


global names_text
names_text = resource_path("resources//list_of_names.txt")
words = resource_path("resources//LemonMilkbold.otf")
# The size of the screen
WIDTH = 1250
HEIGHT = 625
FPS = 30

# A set list of high scores
for line in fileinput.FileInput(names_text, inplace=1):
    if line.rstrip():
        print(line, end='')

global list_of_names
list_of_names = {}
with open(names_text) as f:
    for line in f:
        (name, oldkills, password, rank) = line.split()
        list_of_names[str(name)] = [oldkills, password, rank]
f.close()

# Color codes
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
AQUA = (0, 255, 255)
VIOLET = (148, 0, 211)
YELLOW = (255, 255, 0)
BROWN = (165, 42, 42)
GRAY = (128, 128, 128)


def Health(value):
    health_pic_temp = pygame.image.load(os.path.abspath("resources\\health\\" + str(value) + ".png"))
    health_pic_temp = pygame.transform.scale(health_pic_temp, (50, 10))
    health_pic = pygame.Surface(health_pic_temp.get_size(), pygame.HWSURFACE)
    health_pic.blit(health_pic_temp, (0, 0))
    del health_pic_temp
    return health_pic


def F_health(value):
    health_pic_temp = pygame.image.load(os.path.abspath("resources\\health\\" + str(value) + ".png"))
    health_pic_temp = pygame.transform.scale(health_pic_temp, (300, 10))
    health_pic = pygame.Surface(health_pic_temp.get_size(), pygame.HWSURFACE)
    health_pic.blit(health_pic_temp, (0, 0))
    del health_pic_temp
    return health_pic


def XP_bar(value):
    health_pic_temp = pygame.image.load(os.path.abspath("resources\\health\\" + str(value) + ".png"))
    health_pic_temp = pygame.transform.scale(health_pic_temp, (1274, 10))
    health_pic = pygame.Surface(health_pic_temp.get_size(), pygame.HWSURFACE)
    health_pic.blit(health_pic_temp, (0, 0))
    del health_pic_temp
    return health_pic


# Gun Objects:
class Colt_1911(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.ammountofbullets = 100
        self.clip = 8
        self.permclip = 8
        self.reload = 0
        self.permreload = 96
        self.image = Images.Colt1911_pic
        self.rect = self.image.get_rect()
        self.rect.right = WIDTH
        self.rect.bottom = HEIGHT - HEIGHT / 10
        self.name = "Colt_1911"
        self.type = "pistol"
        self.bought = True
        self.bulletcost = 100

    # Bullet object
    class Bullet(pygame.sprite.Sprite):
        # Bullet
        def __init__(self):
            pygame.sprite.Sprite.__init__(self)
            self.image = Images.bulletpic
            self.rect = self.image.get_rect()
            self.rect.center = fighter.rect.center
            self.speed = deltatime * 200
            mouse_x, mouse_y = pygame.mouse.get_pos()
            bullet_vec_x = mouse_x - fighter.rect.center[0]
            bullet_vec_y = mouse_y - fighter.rect.center[1]
            vec_length = math.sqrt(bullet_vec_x ** 2 + bullet_vec_y ** 2)
            bullet_vec_x = (bullet_vec_x / vec_length) * self.speed  # the five is speed
            bullet_vec_y = (bullet_vec_y / vec_length) * self.speed
            self.change_x = 0
            self.change_y = 0
            self.change_x += bullet_vec_x
            self.change_y += bullet_vec_y
            self.pos_x = fighter.rect.center[0]
            self.pos_y = fighter.rect.center[1]
            self.damage = 5
            self.shootcounter = 2
            self.counter = 0
            self.nextbullet = 0
            self.ammountfornextbullet = 50
            self.firerate = 5
            self.reloadspeed = 5

        def update(self):
            self.nextbullet += 1
            if self.rect.x < -10 or self.rect.x > WIDTH + 10 or self.rect.y < -10 or self.rect.y > HEIGHT + 10:
                Bullets.remove(self)

            self.counter += 1
            if self.shootcounter < self.counter:
                self.counter = 0

                self.pos_x += self.change_x
                self.pos_y += self.change_y

                self.rect.x = self.pos_x
                self.rect.y = self.pos_y

            for i in range(len(enemy_list)):
                if pygame.sprite.collide_rect(self, enemy_list.sprites()[i]):
                    Bullets.remove(self)
                    enemy_list.sprites()[i].heal -= self.damage
                    if enemy_list.sprites()[i].heal <= 0:
                        fighter.xp += fighter.xpadd
                        fighter.kills += 1
                        enemy_list.remove(enemy_list.sprites()[i])
            if pygame.sprite.collide_rect(self, CoinObject):
                CoinObject.update()
                Bullets.remove(self)
                global coins
                coins += coinadd

    class Shop(pygame.sprite.Sprite):
        def __init__(self):
            pygame.sprite.Sprite.__init__(self)
            self.image = Images.Colt_1911_shop_selector_img
            self.rect = self.image.get_rect()
            self.rect.topleft = (800, 25)
            self.cost = 100

        def info(self):
            basicfont4 = pygame.font.Font(words, 24)  # This code displays letters onto the screen
            text4 = basicfont4.render("Cost: " + str(self.cost) + "$", True, GREEN)
            textrect4 = text4.get_rect()
            textrect4.center = (400, 45)
            screen2.blit(text4, textrect4)

            text4 = basicfont4.render("Colt1911", True, WHITE)
            textrect4 = text4.get_rect()
            textrect4.topleft = (12.5, 30)
            screen2.blit(text4, textrect4)

            # Clip:
            basicfont4 = pygame.font.Font(words, 24)  # This code displays letters onto the screen
            text4 = basicfont4.render("Clip", True, WHITE)
            textrect4 = text4.get_rect()
            textrect4.topleft = (300, 260)
            screen2.blit(text4, textrect4)

            text4 = basicfont4.render(str(colt.permclip), True, WHITE)
            textrect4 = text4.get_rect()
            textrect4.topleft = (320, 280)
            screen2.blit(text4, textrect4)

            # Ammo:
            basicfont4 = pygame.font.Font(words, 24)  # This code displays letters onto the screen
            text4 = basicfont4.render("Ammo", True, WHITE)
            textrect4 = text4.get_rect()
            textrect4.topleft = (500, 260)
            screen2.blit(text4, textrect4)

            text4 = basicfont4.render(str(colt.ammountofbullets), True, WHITE)
            textrect4 = text4.get_rect()
            textrect4.center = (545, 300)
            screen2.blit(text4, textrect4)

            text4 = basicfont4.render(str(colt.bulletcost) + "$", True, WHITE)
            textrect4 = text4.get_rect()
            textrect4.center = (545, 425)
            screen2.blit(text4, textrect4)

            # Stats:
            basicfont4 = pygame.font.Font(words, 36)  # This code displays letters onto the screen
            text4 = basicfont4.render("Stats:", True, RED)
            textrect4 = text4.get_rect()
            textrect4.topleft = (12.5, 260)
            screen2.blit(text4, textrect4)

            basicfont4 = pygame.font.Font(words, 18)  # This code displays letters onto the screen
            text4 = basicfont4.render("Damage: " + str(colt.Bullet().damage), True, RED)
            textrect4 = text4.get_rect()
            textrect4.topleft = (12.5, 310)
            screen2.blit(text4, textrect4)

            basicfont4 = pygame.font.Font(words, 18)  # This code displays letters onto the screen
            text4 = basicfont4.render("Fire Rate: " + str(colt.Bullet().firerate), True, RED)
            textrect4 = text4.get_rect()
            textrect4.topleft = (12.5, 340)
            screen2.blit(text4, textrect4)

            basicfont4 = pygame.font.Font(words, 18)  # This code displays letters onto the screen
            text4 = basicfont4.render("Reload Speed: " + str(colt.Bullet().reloadspeed), True, RED)
            textrect4 = text4.get_rect()
            textrect4.topleft = (12.5, 370)
            screen2.blit(text4, textrect4)

            basicfont4 = pygame.font.Font(words, 18)  # This code displays letters onto the screen
            text4 = basicfont4.render("Range: " + "Coming Soon!", True, RED)
            textrect4 = text4.get_rect()
            textrect4.topleft = (12.5, 400)
            screen2.blit(text4, textrect4)

            basicfont4 = pygame.font.Font(words, 18)  # This code displays letters onto the screen
            text4 = basicfont4.render("Accuracy: " + "Coming Soon!", True, RED)
            textrect4 = text4.get_rect()
            textrect4.topleft = (12.5, 430)
            screen2.blit(text4, textrect4)

            basicfont4 = pygame.font.Font(words, 18)  # This code displays letters onto the screen
            text4 = basicfont4.render("Mobility: " + "Coming Soon!", True, RED)
            textrect4 = text4.get_rect()
            textrect4.topleft = (12.5, 460)
            screen2.blit(text4, textrect4)

        class Shop_Layout(pygame.sprite.Sprite):
            def __init__(self):
                pygame.sprite.Sprite.__init__(self)
                self.image = Images.shop_format_img
                self.rect = self.image.get_rect()
                self.rect.topleft = (0, 25)

        class gun_img(pygame.sprite.Sprite):
            def __init__(self):
                pygame.sprite.Sprite.__init__(self)
                self.image = Images.colt_1911_img
                self.rect = self.image.get_rect()
                self.rect.topleft = (75, 75)

        class buy(pygame.sprite.Sprite):
            def __init__(self):
                pygame.sprite.Sprite.__init__(self)
                self.image = Images.buypic
                self.rect = self.image.get_rect()
                self.rect.topright = (789, 35)
                self.cost = 100

        class equip(pygame.sprite.Sprite):
            def __init__(self):
                pygame.sprite.Sprite.__init__(self)
                self.image = Images.equip_pic
                self.rect = self.image.get_rect()
                self.rect.topright = (789, 35)

        class equiped(pygame.sprite.Sprite):
            def __init__(self):
                pygame.sprite.Sprite.__init__(self)
                self.image = Images.equiped_pic
                self.rect = self.image.get_rect()
                self.rect.topright = (789, 35)

        class Bullet_Shop(pygame.sprite.Sprite):
            def __init__(self):
                pygame.sprite.Sprite.__init__(self)
                self.image = Images.buy_ammo_img
                self.rect = self.image.get_rect()
                self.rect.center = (545, 475)
                self.cost = 100


# Pistol Object:
class Browning_Hi_Power(pygame.sprite.Sprite):  # faster and stronger than colt
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.ammountofbullets = 130
        self.clip = 13
        self.permclip = 13
        self.reload = 0
        self.permreload = 96
        self.image = Images.Browning_Hi_Power_img
        self.rect = self.image.get_rect()
        self.rect.right = WIDTH
        self.rect.bottom = HEIGHT - HEIGHT / 10
        self.name = "Browning_Hi-Power"
        self.type = "pistol"
        self.bought = False
        self.bulletcost = 150

    # Bullet object
    class Bullet(pygame.sprite.Sprite):
        # Bullet
        def __init__(self):
            pygame.sprite.Sprite.__init__(self)
            self.image = Images.bulletpic
            self.rect = self.image.get_rect()
            self.rect.center = fighter.rect.center
            self.speed = deltatime * 300
            mouse_x, mouse_y = pygame.mouse.get_pos()
            bullet_vec_x = mouse_x - fighter.rect.center[0]
            bullet_vec_y = mouse_y - fighter.rect.center[1]
            vec_length = math.sqrt(bullet_vec_x ** 2 + bullet_vec_y ** 2)
            bullet_vec_x = (bullet_vec_x / vec_length) * self.speed  # the five is speed
            bullet_vec_y = (bullet_vec_y / vec_length) * self.speed
            self.change_x = 0
            self.change_y = 0
            self.change_x += bullet_vec_x
            self.change_y += bullet_vec_y
            self.pos_x = fighter.rect.center[0]
            self.pos_y = fighter.rect.center[1]
            self.damage = 10
            self.shootcounter = 2
            self.counter = 0
            self.nextbullet = 0
            self.ammountfornextbullet = 50
            self.firerate = 10
            self.reloadspeed = 5

        def update(self):
            self.nextbullet += 1
            if self.rect.x < -10 or self.rect.x > WIDTH + 10 or self.rect.y < -10 or self.rect.y > HEIGHT + 10:
                Bullets.remove(self)

            self.counter += 1
            if self.shootcounter < self.counter:
                self.counter = 0

                self.pos_x += self.change_x
                self.pos_y += self.change_y

                self.rect.x = self.pos_x
                self.rect.y = self.pos_y

            for i in range(len(enemy_list)):
                if pygame.sprite.collide_rect(self, enemy_list.sprites()[i]):
                    Bullets.remove(self)
                    enemy_list.sprites()[i].heal -= self.damage
                    if enemy_list.sprites()[i].heal <= 0:
                        fighter.xp += fighter.xpadd
                        fighter.kills += 1
                        enemy_list.remove(enemy_list.sprites()[i])
            if pygame.sprite.collide_rect(self, CoinObject):
                CoinObject.update()
                Bullets.remove(self)
                global coins
                coins += coinadd

    class Shop(pygame.sprite.Sprite):
        def __init__(self):
            pygame.sprite.Sprite.__init__(self)
            self.image = Images.Browning_Hi_Power_shop_selector_img
            self.rect = self.image.get_rect()
            self.rect.topleft = (800, 75)
            self.cost = 1000

        def info(self):
            basicfont4 = pygame.font.Font(words, 24)  # This code displays letters onto the screen
            text4 = basicfont4.render("Cost: " + str(self.cost) + "$", True, GREEN)
            textrect4 = text4.get_rect()
            textrect4.center = (400, 45)
            screen2.blit(text4, textrect4)

            text4 = basicfont4.render("Browning_Hi-Power", True, WHITE)
            textrect4 = text4.get_rect()
            textrect4.topleft = (12.5, 30)
            screen2.blit(text4, textrect4)

            # Clip:
            basicfont4 = pygame.font.Font(words, 24)  # This code displays letters onto the screen
            text4 = basicfont4.render("Clip", True, WHITE)
            textrect4 = text4.get_rect()
            textrect4.topleft = (300, 260)
            screen2.blit(text4, textrect4)

            text4 = basicfont4.render(str(bhp.permclip), True, WHITE)
            textrect4 = text4.get_rect()
            textrect4.topleft = (320, 280)
            screen2.blit(text4, textrect4)

            # Ammo:
            basicfont4 = pygame.font.Font(words, 24)  # This code displays letters onto the screen
            text4 = basicfont4.render("Ammo", True, WHITE)
            textrect4 = text4.get_rect()
            textrect4.topleft = (500, 260)
            screen2.blit(text4, textrect4)

            text4 = basicfont4.render(str(bhp.ammountofbullets), True, WHITE)
            textrect4 = text4.get_rect()
            textrect4.center = (545, 300)
            screen2.blit(text4, textrect4)

            text4 = basicfont4.render(str(bhp.bulletcost) + "$", True, WHITE)
            textrect4 = text4.get_rect()
            textrect4.center = (545, 425)
            screen2.blit(text4, textrect4)

            # Stats:
            basicfont4 = pygame.font.Font(words, 36)  # This code displays letters onto the screen
            text4 = basicfont4.render("Stats:", True, RED)
            textrect4 = text4.get_rect()
            textrect4.topleft = (12.5, 260)
            screen2.blit(text4, textrect4)

            basicfont4 = pygame.font.Font(words, 18)  # This code displays letters onto the screen
            text4 = basicfont4.render("Damage: " + str(bhp.Bullet().damage), True, RED)
            textrect4 = text4.get_rect()
            textrect4.topleft = (12.5, 310)
            screen2.blit(text4, textrect4)

            basicfont4 = pygame.font.Font(words, 18)  # This code displays letters onto the screen
            text4 = basicfont4.render("Fire Rate: " + str(bhp.Bullet().firerate), True, RED)
            textrect4 = text4.get_rect()
            textrect4.topleft = (12.5, 340)
            screen2.blit(text4, textrect4)

            basicfont4 = pygame.font.Font(words, 18)  # This code displays letters onto the screen
            text4 = basicfont4.render("Reload Speed: " + str(bhp.Bullet().reloadspeed), True, RED)
            textrect4 = text4.get_rect()
            textrect4.topleft = (12.5, 370)
            screen2.blit(text4, textrect4)

            basicfont4 = pygame.font.Font(words, 18)  # This code displays letters onto the screen
            text4 = basicfont4.render("Range: " + "Coming Soon!", True, RED)
            textrect4 = text4.get_rect()
            textrect4.topleft = (12.5, 400)
            screen2.blit(text4, textrect4)

            basicfont4 = pygame.font.Font(words, 18)  # This code displays letters onto the screen
            text4 = basicfont4.render("Accuracy: " + "Coming Soon!", True, RED)
            textrect4 = text4.get_rect()
            textrect4.topleft = (12.5, 430)
            screen2.blit(text4, textrect4)

            basicfont4 = pygame.font.Font(words, 18)  # This code displays letters onto the screen
            text4 = basicfont4.render("Mobility: " + "Coming Soon!", True, RED)
            textrect4 = text4.get_rect()
            textrect4.topleft = (12.5, 460)
            screen2.blit(text4, textrect4)

        class Shop_Layout(pygame.sprite.Sprite):
            def __init__(self):
                pygame.sprite.Sprite.__init__(self)
                self.image = Images.shop_format_img
                self.rect = self.image.get_rect()
                self.rect.topleft = (0, 25)

        class gun_img(pygame.sprite.Sprite):
            def __init__(self):
                pygame.sprite.Sprite.__init__(self)
                self.image = Images.Browning_Hi_Power_shop_img
                self.rect = self.image.get_rect()
                self.rect.topleft = (75, 75)

        class buy(pygame.sprite.Sprite):
            def __init__(self):
                pygame.sprite.Sprite.__init__(self)
                self.image = Images.buypic
                self.rect = self.image.get_rect()
                self.rect.topright = (789, 35)
                self.cost = 1000

        class equip(pygame.sprite.Sprite):
            def __init__(self):
                pygame.sprite.Sprite.__init__(self)
                self.image = Images.equip_pic
                self.rect = self.image.get_rect()
                self.rect.topright = (789, 35)

        class equiped(pygame.sprite.Sprite):
            def __init__(self):
                pygame.sprite.Sprite.__init__(self)
                self.image = Images.equiped_pic
                self.rect = self.image.get_rect()
                self.rect.topright = (789, 35)

        class Bullet_Shop(pygame.sprite.Sprite):
            def __init__(self):
                pygame.sprite.Sprite.__init__(self)
                self.image = Images.buy_ammo_img
                self.rect = self.image.get_rect()
                self.rect.center = (545, 475)
                self.cost = 150


# Pistol Object
class Mauser_C96(pygame.sprite.Sprite):  # faster and stronger than colt
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.ammountofbullets = 200
        self.clip = 20
        self.permclip = 20
        self.reload = 0
        self.permreload = 96
        self.image = Images.Mauser_C96_img
        self.rect = self.image.get_rect()
        self.rect.right = WIDTH
        self.rect.bottom = HEIGHT - HEIGHT / 10
        self.name = "Mauser C96"
        self.type = "pistol"
        self.bought = False
        self.bulletcost = 200

    # Bullet object
    class Bullet(pygame.sprite.Sprite):
        # Bullet
        def __init__(self):
            pygame.sprite.Sprite.__init__(self)
            self.image = Images.bulletpic
            self.rect = self.image.get_rect()
            self.rect.center = fighter.rect.center
            self.speed = deltatime * 300
            mouse_x, mouse_y = pygame.mouse.get_pos()
            bullet_vec_x = mouse_x - fighter.rect.center[0]
            bullet_vec_y = mouse_y - fighter.rect.center[1]
            vec_length = math.sqrt(bullet_vec_x ** 2 + bullet_vec_y ** 2)
            bullet_vec_x = (bullet_vec_x / vec_length) * self.speed  # the five is speed
            bullet_vec_y = (bullet_vec_y / vec_length) * self.speed
            self.change_x = 0
            self.change_y = 0
            self.change_x += bullet_vec_x
            self.change_y += bullet_vec_y
            self.pos_x = fighter.rect.center[0]
            self.pos_y = fighter.rect.center[1]
            self.damage = 1
            self.shootcounter = 2
            self.counter = 0
            self.nextbullet = 0
            self.ammountfornextbullet = 10
            self.firerate = 20
            self.reloadspeed = 5

        def update(self):
            self.nextbullet += 1
            if self.rect.x < -10 or self.rect.x > WIDTH + 10 or self.rect.y < -10 or self.rect.y > HEIGHT + 10:
                Bullets.remove(self)

            self.counter += 1
            if self.shootcounter < self.counter:
                self.counter = 0

                self.pos_x += self.change_x
                self.pos_y += self.change_y

                self.rect.x = self.pos_x
                self.rect.y = self.pos_y

            for i in range(len(enemy_list)):
                if pygame.sprite.collide_rect(self, enemy_list.sprites()[i]):
                    Bullets.remove(self)
                    enemy_list.sprites()[i].heal -= self.damage
                    if enemy_list.sprites()[i].heal <= 0:
                        fighter.xp += fighter.xpadd
                        fighter.kills += 1
                        enemy_list.remove(enemy_list.sprites()[i])
            if pygame.sprite.collide_rect(self, CoinObject):
                CoinObject.update()
                Bullets.remove(self)
                global coins
                coins += coinadd

    class Shop(pygame.sprite.Sprite):
        def __init__(self):
            pygame.sprite.Sprite.__init__(self)
            self.image = Images.Mauser_C96_Power_shop_selector_img
            self.rect = self.image.get_rect()
            self.rect.topleft = (800, 125)
            self.cost = 1000

        def info(self):
            basicfont4 = pygame.font.Font(words, 24)  # This code displays letters onto the screen
            text4 = basicfont4.render("Cost: " + str(self.cost) + "$", True, GREEN)
            textrect4 = text4.get_rect()
            textrect4.center = (400, 45)
            screen2.blit(text4, textrect4)

            text4 = basicfont4.render("Mauser C96", True, WHITE)
            textrect4 = text4.get_rect()
            textrect4.topleft = (12.5, 30)
            screen2.blit(text4, textrect4)

            # Clip:
            basicfont4 = pygame.font.Font(words, 24)  # This code displays letters onto the screen
            text4 = basicfont4.render("Clip", True, WHITE)
            textrect4 = text4.get_rect()
            textrect4.topleft = (300, 260)
            screen2.blit(text4, textrect4)

            text4 = basicfont4.render(str(mauser.permclip), True, WHITE)
            textrect4 = text4.get_rect()
            textrect4.topleft = (320, 280)
            screen2.blit(text4, textrect4)

            # Ammo:
            basicfont4 = pygame.font.Font(words, 24)  # This code displays letters onto the screen
            text4 = basicfont4.render("Ammo", True, WHITE)
            textrect4 = text4.get_rect()
            textrect4.topleft = (500, 260)
            screen2.blit(text4, textrect4)

            text4 = basicfont4.render(str(mauser.ammountofbullets), True, WHITE)
            textrect4 = text4.get_rect()
            textrect4.center = (545, 300)
            screen2.blit(text4, textrect4)

            text4 = basicfont4.render(str(mauser.bulletcost) + "$", True, WHITE)
            textrect4 = text4.get_rect()
            textrect4.center = (545, 425)
            screen2.blit(text4, textrect4)

            # Stats:
            basicfont4 = pygame.font.Font(words, 36)  # This code displays letters onto the screen
            text4 = basicfont4.render("Stats:", True, RED)
            textrect4 = text4.get_rect()
            textrect4.topleft = (12.5, 260)
            screen2.blit(text4, textrect4)

            basicfont4 = pygame.font.Font(words, 18)  # This code displays letters onto the screen
            text4 = basicfont4.render("Damage: " + str(mauser.Bullet().damage), True, RED)
            textrect4 = text4.get_rect()
            textrect4.topleft = (12.5, 310)
            screen2.blit(text4, textrect4)

            basicfont4 = pygame.font.Font(words, 18)  # This code displays letters onto the screen
            text4 = basicfont4.render("Fire Rate: " + str(mauser.Bullet().firerate), True, RED)
            textrect4 = text4.get_rect()
            textrect4.topleft = (12.5, 340)
            screen2.blit(text4, textrect4)

            basicfont4 = pygame.font.Font(words, 18)  # This code displays letters onto the screen
            text4 = basicfont4.render("Reload Speed: " + str(mauser.Bullet().reloadspeed), True, RED)
            textrect4 = text4.get_rect()
            textrect4.topleft = (12.5, 370)
            screen2.blit(text4, textrect4)

            basicfont4 = pygame.font.Font(words, 18)  # This code displays letters onto the screen
            text4 = basicfont4.render("Range: " + "Coming Soon!", True, RED)
            textrect4 = text4.get_rect()
            textrect4.topleft = (12.5, 400)
            screen2.blit(text4, textrect4)

            basicfont4 = pygame.font.Font(words, 18)  # This code displays letters onto the screen
            text4 = basicfont4.render("Accuracy: " + "Coming Soon!", True, RED)
            textrect4 = text4.get_rect()
            textrect4.topleft = (12.5, 430)
            screen2.blit(text4, textrect4)

            basicfont4 = pygame.font.Font(words, 18)  # This code displays letters onto the screen
            text4 = basicfont4.render("Mobility: " + "Coming Soon!", True, RED)
            textrect4 = text4.get_rect()
            textrect4.topleft = (12.5, 460)
            screen2.blit(text4, textrect4)

        class Shop_Layout(pygame.sprite.Sprite):
            def __init__(self):
                pygame.sprite.Sprite.__init__(self)
                self.image = Images.shop_format_img
                self.rect = self.image.get_rect()
                self.rect.topleft = (0, 25)

        class gun_img(pygame.sprite.Sprite):
            def __init__(self):
                pygame.sprite.Sprite.__init__(self)
                self.image = Images.Mauser_C96_shop_img
                self.rect = self.image.get_rect()
                self.rect.topleft = (75, 75)

        class buy(pygame.sprite.Sprite):
            def __init__(self):
                pygame.sprite.Sprite.__init__(self)
                self.image = Images.buypic
                self.rect = self.image.get_rect()
                self.rect.topright = (789, 35)
                self.cost = 1000

        class equip(pygame.sprite.Sprite):
            def __init__(self):
                pygame.sprite.Sprite.__init__(self)
                self.image = Images.equip_pic
                self.rect = self.image.get_rect()
                self.rect.topright = (789, 35)

        class equiped(pygame.sprite.Sprite):
            def __init__(self):
                pygame.sprite.Sprite.__init__(self)
                self.image = Images.equiped_pic
                self.rect = self.image.get_rect()
                self.rect.topright = (789, 35)

        class Bullet_Shop(pygame.sprite.Sprite):
            def __init__(self):
                pygame.sprite.Sprite.__init__(self)
                self.image = Images.buy_ammo_img
                self.rect = self.image.get_rect()
                self.rect.center = (545, 475)
                self.cost = 120

#AutoMatics
class MG_30(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.ammountofbullets = 90
        self.clip = 30
        self.permclip = 30
        self.reload = 0
        self.permreload = 100
        self.image = Images.autogunpic
        self.rect = self.image.get_rect()
        self.rect.right = WIDTH
        self.rect.bottom = HEIGHT - HEIGHT / 10
        self.name = "MG_30"
        self.type = "automatic"
        self.bought = False
        self.bulletcost = 100

    # Bullet object
    class Bullet(pygame.sprite.Sprite):
        # Bullet
        def __init__(self):
            pygame.sprite.Sprite.__init__(self)
            self.image = Images.bulletpic
            self.rect = self.image.get_rect()
            self.rect.center = fighter.rect.center
            self.speed = deltatime * 200
            mouse_x, mouse_y = pygame.mouse.get_pos()
            bullet_vec_x = mouse_x - fighter.rect.center[0]
            bullet_vec_y = mouse_y - fighter.rect.center[1]
            vec_length = math.sqrt(bullet_vec_x ** 2 + bullet_vec_y ** 2)
            bullet_vec_x = (bullet_vec_x / vec_length) * self.speed  # the five is speed
            bullet_vec_y = (bullet_vec_y / vec_length) * self.speed
            self.change_x = 0
            self.change_y = 0
            self.change_x += bullet_vec_x
            self.change_y += bullet_vec_y
            self.pos_x = fighter.rect.center[0]
            self.pos_y = fighter.rect.center[1]
            self.damage = 2
            self.shootcounter = 2
            self.counter = 0
            self.nextbullet = 0
            self.ammountfornextbullet = 2
            self.firerate = 5
            self.reloadspeed = 5

        def update(self):
            self.nextbullet += 1
            if self.rect.x < -10 or self.rect.x > WIDTH + 10 or self.rect.y < -10 or self.rect.y > HEIGHT + 10:
                Bullets.remove(self)

            self.counter += 1
            if self.shootcounter < self.counter:
                self.counter = 0

                self.pos_x += self.change_x
                self.pos_y += self.change_y

                self.rect.x = self.pos_x
                self.rect.y = self.pos_y

            for i in range(len(enemy_list)):
                if pygame.sprite.collide_rect(self, enemy_list.sprites()[i]):
                    Bullets.remove(self)
                    enemy_list.sprites()[i].heal -= self.damage
                    if enemy_list.sprites()[i].heal <= 0:
                        fighter.xp += fighter.xpadd
                        fighter.kills += 1
                        enemy_list.remove(enemy_list.sprites()[i])
            if pygame.sprite.collide_rect(self, CoinObject):
                CoinObject.update()
                Bullets.remove(self)
                global coins
                coins += coinadd

    # This object is just to click on in the shop
    class Shop(pygame.sprite.Sprite):
        def __init__(self):
            pygame.sprite.Sprite.__init__(self)
            self.image = Images.MG_30_shop_selector_img
            self.rect = self.image.get_rect()
            self.rect.topleft = (800, 25)
            self.cost = 100

        def info(self):
            basicfont4 = pygame.font.Font(words, 24)  # This code displays letters onto the screen
            text4 = basicfont4.render("Cost: " + str(self.cost) + "$", True, GREEN)
            textrect4 = text4.get_rect()
            textrect4.center = (400, 45)
            screen2.blit(text4, textrect4)

            text4 = basicfont4.render("MG30", True, WHITE)
            textrect4 = text4.get_rect()
            textrect4.topleft = (12.5, 30)
            screen2.blit(text4, textrect4)

            # Clip:
            basicfont4 = pygame.font.Font(words, 24)  # This code displays letters onto the screen
            text4 = basicfont4.render("Clip", True, WHITE)
            textrect4 = text4.get_rect()
            textrect4.topleft = (300, 260)
            screen2.blit(text4, textrect4)

            text4 = basicfont4.render(str(MG30.permclip), True, WHITE)
            textrect4 = text4.get_rect()
            textrect4.topleft = (320, 280)
            screen2.blit(text4, textrect4)

            # Ammo:
            basicfont4 = pygame.font.Font(words, 24)  # This code displays letters onto the screen
            text4 = basicfont4.render("Ammo", True, WHITE)
            textrect4 = text4.get_rect()
            textrect4.topleft = (500, 260)
            screen2.blit(text4, textrect4)

            text4 = basicfont4.render(str(MG30.ammountofbullets), True, WHITE)
            textrect4 = text4.get_rect()
            textrect4.center = (545, 300)
            screen2.blit(text4, textrect4)

            text4 = basicfont4.render(str(MG30.bulletcost) + "$", True, WHITE)
            textrect4 = text4.get_rect()
            textrect4.center = (545, 425)
            screen2.blit(text4, textrect4)

            # Stats:
            basicfont4 = pygame.font.Font(words, 36)  # This code displays letters onto the screen
            text4 = basicfont4.render("Stats:", True, RED)
            textrect4 = text4.get_rect()
            textrect4.topleft = (12.5, 260)
            screen2.blit(text4, textrect4)

            basicfont4 = pygame.font.Font(words, 18)  # This code displays letters onto the screen
            text4 = basicfont4.render("Damage: " + str(MG30.Bullet().damage), True, RED)
            textrect4 = text4.get_rect()
            textrect4.topleft = (12.5, 310)
            screen2.blit(text4, textrect4)

            basicfont4 = pygame.font.Font(words, 18)  # This code displays letters onto the screen
            text4 = basicfont4.render("Fire Rate: " + str(MG30.Bullet().firerate), True, RED)
            textrect4 = text4.get_rect()
            textrect4.topleft = (12.5, 340)
            screen2.blit(text4, textrect4)

            basicfont4 = pygame.font.Font(words, 18)  # This code displays letters onto the screen
            text4 = basicfont4.render("Reload Speed: " + str(MG30.Bullet().reloadspeed), True, RED)
            textrect4 = text4.get_rect()
            textrect4.topleft = (12.5, 370)
            screen2.blit(text4, textrect4)

            basicfont4 = pygame.font.Font(words, 18)  # This code displays letters onto the screen
            text4 = basicfont4.render("Range: " + "Coming Soon!", True, RED)
            textrect4 = text4.get_rect()
            textrect4.topleft = (12.5, 400)
            screen2.blit(text4, textrect4)

            basicfont4 = pygame.font.Font(words, 18)  # This code displays letters onto the screen
            text4 = basicfont4.render("Accuracy: " + "Coming Soon!", True, RED)
            textrect4 = text4.get_rect()
            textrect4.topleft = (12.5, 430)
            screen2.blit(text4, textrect4)

            basicfont4 = pygame.font.Font(words, 18)  # This code displays letters onto the screen
            text4 = basicfont4.render("Mobility: " + "Coming Soon!", True, RED)
            textrect4 = text4.get_rect()
            textrect4.topleft = (12.5, 460)
            screen2.blit(text4, textrect4)

        class Shop_Layout(pygame.sprite.Sprite):
            def __init__(self):
                pygame.sprite.Sprite.__init__(self)
                self.image = Images.shop_format_img
                self.rect = self.image.get_rect()
                self.rect.topleft = (0, 25)
                self.cost = 100

        class gun_img(pygame.sprite.Sprite):
            def __init__(self):
                pygame.sprite.Sprite.__init__(self)
                self.image = Images.mg_30_img
                self.rect = self.image.get_rect()
                self.rect.topleft = (75, 75)
                self.cost = 100

        class buy(pygame.sprite.Sprite):
            def __init__(self):
                pygame.sprite.Sprite.__init__(self)
                self.image = Images.buypic
                self.rect = self.image.get_rect()
                self.rect.topright = (789, 35)
                self.cost = 100

        class equip(pygame.sprite.Sprite):
            def __init__(self):
                pygame.sprite.Sprite.__init__(self)
                self.image = Images.equip_pic
                self.rect = self.image.get_rect()
                self.rect.topright = (789, 35)
                self.cost = 100

        class equiped(pygame.sprite.Sprite):
            def __init__(self):
                pygame.sprite.Sprite.__init__(self)
                self.image = Images.equiped_pic
                self.rect = self.image.get_rect()
                self.rect.topright = (789, 35)
                self.cost = 100

        class Bullet_Shop(pygame.sprite.Sprite):
            def __init__(self):
                pygame.sprite.Sprite.__init__(self)
                self.image = Images.buy_ammo_img
                self.rect = self.image.get_rect()
                self.rect.center = (545, 475)
                self.cost = 100

class Volkssturmgewehr(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.ammountofbullets = 90
        self.clip = 30
        self.permclip = 30
        self.reload = 0
        self.permreload = 100
        self.image = Images.Volkssturmgewehr_img
        self.rect = self.image.get_rect()
        self.rect.right = WIDTH
        self.rect.bottom = HEIGHT - HEIGHT / 10
        self.name = "Volkssturmgewehr"
        self.type = "automatic"
        self.bought = False
        self.bulletcost = 200

    # Bullet object
    class Bullet(pygame.sprite.Sprite):
        # Bullet
        def __init__(self):
            pygame.sprite.Sprite.__init__(self)
            self.image = Images.bulletpic
            self.rect = self.image.get_rect()
            self.rect.center = fighter.rect.center
            self.speed = deltatime * 300
            mouse_x, mouse_y = pygame.mouse.get_pos()
            bullet_vec_x = mouse_x - fighter.rect.center[0]
            bullet_vec_y = mouse_y - fighter.rect.center[1]
            vec_length = math.sqrt(bullet_vec_x ** 2 + bullet_vec_y ** 2)
            bullet_vec_x = (bullet_vec_x / vec_length) * self.speed  # the five is speed
            bullet_vec_y = (bullet_vec_y / vec_length) * self.speed
            self.change_x = 0
            self.change_y = 0
            self.change_x += bullet_vec_x
            self.change_y += bullet_vec_y
            self.pos_x = fighter.rect.center[0]
            self.pos_y = fighter.rect.center[1]
            self.damage = 5
            self.shootcounter = 2
            self.counter = 0
            self.nextbullet = 0
            self.ammountfornextbullet = 7
            self.firerate = 2
            self.reloadspeed = 5

        def update(self):
            self.nextbullet += 1
            if self.rect.x < -10 or self.rect.x > WIDTH + 10 or self.rect.y < -10 or self.rect.y > HEIGHT + 10:
                Bullets.remove(self)

            self.counter += 1
            if self.shootcounter < self.counter:
                self.counter = 0

                self.pos_x += self.change_x
                self.pos_y += self.change_y

                self.rect.x = self.pos_x
                self.rect.y = self.pos_y

            for i in range(len(enemy_list)):
                if pygame.sprite.collide_rect(self, enemy_list.sprites()[i]):
                    Bullets.remove(self)
                    enemy_list.sprites()[i].heal -= self.damage
                    if enemy_list.sprites()[i].heal <= 0:
                        fighter.xp += fighter.xpadd
                        fighter.kills += 1
                        enemy_list.remove(enemy_list.sprites()[i])
            if pygame.sprite.collide_rect(self, CoinObject):
                CoinObject.update()
                Bullets.remove(self)
                global coins
                coins += coinadd

    # This object is just to click on in the shop
    class Shop(pygame.sprite.Sprite):
        def __init__(self):
            pygame.sprite.Sprite.__init__(self)
            self.image = Images.Volkssturmgewehr_shop_selector_img
            self.rect = self.image.get_rect()
            self.rect.topleft = (800, 75)
            self.cost = 2000

        def info(self):
            basicfont4 = pygame.font.Font(words, 24)  # This code displays letters onto the screen
            text4 = basicfont4.render("Cost: " + str(self.cost) + "$", True, GREEN)
            textrect4 = text4.get_rect()
            textrect4.center = (400, 45)
            screen2.blit(text4, textrect4)

            text4 = basicfont4.render("volkssturmgewehr", True, WHITE)
            textrect4 = text4.get_rect()
            textrect4.topleft = (12.5, 30)
            screen2.blit(text4, textrect4)

            # Clip:
            basicfont4 = pygame.font.Font(words, 24)  # This code displays letters onto the screen
            text4 = basicfont4.render("Clip", True, WHITE)
            textrect4 = text4.get_rect()
            textrect4.topleft = (300, 260)
            screen2.blit(text4, textrect4)

            text4 = basicfont4.render(str(volkssturmgewehr.permclip), True, WHITE)
            textrect4 = text4.get_rect()
            textrect4.topleft = (320, 280)
            screen2.blit(text4, textrect4)

            # Ammo:
            basicfont4 = pygame.font.Font(words, 24)  # This code displays letters onto the screen
            text4 = basicfont4.render("Ammo", True, WHITE)
            textrect4 = text4.get_rect()
            textrect4.topleft = (500, 260)
            screen2.blit(text4, textrect4)

            text4 = basicfont4.render(str(volkssturmgewehr.ammountofbullets), True, WHITE)
            textrect4 = text4.get_rect()
            textrect4.center = (545, 300)
            screen2.blit(text4, textrect4)

            text4 = basicfont4.render(str(volkssturmgewehr.bulletcost) + "$", True, WHITE)
            textrect4 = text4.get_rect()
            textrect4.center = (545, 425)
            screen2.blit(text4, textrect4)

            # Stats:
            basicfont4 = pygame.font.Font(words, 36)  # This code displays letters onto the screen
            text4 = basicfont4.render("Stats:", True, RED)
            textrect4 = text4.get_rect()
            textrect4.topleft = (12.5, 260)
            screen2.blit(text4, textrect4)

            basicfont4 = pygame.font.Font(words, 18)  # This code displays letters onto the screen
            text4 = basicfont4.render("Damage: " + str(volkssturmgewehr.Bullet().damage), True, RED)
            textrect4 = text4.get_rect()
            textrect4.topleft = (12.5, 310)
            screen2.blit(text4, textrect4)

            basicfont4 = pygame.font.Font(words, 18)  # This code displays letters onto the screen
            text4 = basicfont4.render("Fire Rate: " + str(volkssturmgewehr.Bullet().firerate), True, RED)
            textrect4 = text4.get_rect()
            textrect4.topleft = (12.5, 340)
            screen2.blit(text4, textrect4)

            basicfont4 = pygame.font.Font(words, 18)  # This code displays letters onto the screen
            text4 = basicfont4.render("Reload Speed: " + str(volkssturmgewehr.Bullet().reloadspeed), True, RED)
            textrect4 = text4.get_rect()
            textrect4.topleft = (12.5, 370)
            screen2.blit(text4, textrect4)

            basicfont4 = pygame.font.Font(words, 18)  # This code displays letters onto the screen
            text4 = basicfont4.render("Range: " + "Coming Soon!", True, RED)
            textrect4 = text4.get_rect()
            textrect4.topleft = (12.5, 400)
            screen2.blit(text4, textrect4)

            basicfont4 = pygame.font.Font(words, 18)  # This code displays letters onto the screen
            text4 = basicfont4.render("Accuracy: " + "Coming Soon!", True, RED)
            textrect4 = text4.get_rect()
            textrect4.topleft = (12.5, 430)
            screen2.blit(text4, textrect4)

            basicfont4 = pygame.font.Font(words, 18)  # This code displays letters onto the screen
            text4 = basicfont4.render("Mobility: " + "Coming Soon!", True, RED)
            textrect4 = text4.get_rect()
            textrect4.topleft = (12.5, 460)
            screen2.blit(text4, textrect4)

        class Shop_Layout(pygame.sprite.Sprite):
            def __init__(self):
                pygame.sprite.Sprite.__init__(self)
                self.image = Images.shop_format_img
                self.rect = self.image.get_rect()
                self.rect.topleft = (0, 25)
                self.cost = 100

        class gun_img(pygame.sprite.Sprite):
            def __init__(self):
                pygame.sprite.Sprite.__init__(self)
                self.image = Images.Volkssturmgewehr_shop_img
                self.rect = self.image.get_rect()
                self.rect.topleft = (75, 75)
                self.cost = 100

        class buy(pygame.sprite.Sprite):
            def __init__(self):
                pygame.sprite.Sprite.__init__(self)
                self.image = Images.buypic
                self.rect = self.image.get_rect()
                self.rect.topright = (789, 35)
                self.cost = 2000

        class equip(pygame.sprite.Sprite):
            def __init__(self):
                pygame.sprite.Sprite.__init__(self)
                self.image = Images.equip_pic
                self.rect = self.image.get_rect()
                self.rect.topright = (789, 35)
                self.cost = 100

        class equiped(pygame.sprite.Sprite):
            def __init__(self):
                pygame.sprite.Sprite.__init__(self)
                self.image = Images.equiped_pic
                self.rect = self.image.get_rect()
                self.rect.topright = (789, 35)
                self.cost = 100

        class Bullet_Shop(pygame.sprite.Sprite):
            def __init__(self):
                pygame.sprite.Sprite.__init__(self)
                self.image = Images.buy_ammo_img
                self.rect = self.image.get_rect()
                self.rect.center = (545, 475)
                self.cost = 100

class Spz(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.ammountofbullets = 90
        self.clip = 30
        self.permclip = 30
        self.reload = 0
        self.permreload = 100
        self.image = Images.Spz_img
        self.rect = self.image.get_rect()
        self.rect.right = WIDTH
        self.rect.bottom = HEIGHT - HEIGHT / 10
        self.name = "Spz"
        self.type = "automatic"
        self.bought = False
        self.bulletcost = 400

    # Bullet object
    class Bullet(pygame.sprite.Sprite):
        # Bullet
        def __init__(self):
            pygame.sprite.Sprite.__init__(self)
            self.image = Images.bulletpic
            self.rect = self.image.get_rect()
            self.rect.center = fighter.rect.center
            self.speed = deltatime * 500
            mouse_x, mouse_y = pygame.mouse.get_pos()
            bullet_vec_x = mouse_x - fighter.rect.center[0]
            bullet_vec_y = mouse_y - fighter.rect.center[1]
            vec_length = math.sqrt(bullet_vec_x ** 2 + bullet_vec_y ** 2)
            bullet_vec_x = (bullet_vec_x / vec_length) * self.speed  # the five is speed
            bullet_vec_y = (bullet_vec_y / vec_length) * self.speed
            self.change_x = 0
            self.change_y = 0
            self.change_x += bullet_vec_x
            self.change_y += bullet_vec_y
            self.pos_x = fighter.rect.center[0]
            self.pos_y = fighter.rect.center[1]
            self.damage = 10
            self.shootcounter = 2
            self.counter = 0
            self.nextbullet = 0
            self.ammountfornextbullet = 10
            self.firerate = 2
            self.reloadspeed = 5

        def update(self):
            self.nextbullet += 1
            if self.rect.x < -10 or self.rect.x > WIDTH + 10 or self.rect.y < -10 or self.rect.y > HEIGHT + 10:
                Bullets.remove(self)

            self.counter += 1
            if self.shootcounter < self.counter:
                self.counter = 0

                self.pos_x += self.change_x
                self.pos_y += self.change_y

                self.rect.x = self.pos_x
                self.rect.y = self.pos_y

            for i in range(len(enemy_list)):
                if pygame.sprite.collide_rect(self, enemy_list.sprites()[i]):
                    Bullets.remove(self)
                    enemy_list.sprites()[i].heal -= self.damage
                    if enemy_list.sprites()[i].heal <= 0:
                        fighter.xp += fighter.xpadd
                        fighter.kills += 1
                        enemy_list.remove(enemy_list.sprites()[i])
            if pygame.sprite.collide_rect(self, CoinObject):
                CoinObject.update()
                Bullets.remove(self)
                global coins
                coins += coinadd

    # This object is just to click on in the shop
    class Shop(pygame.sprite.Sprite):
        def __init__(self):
            pygame.sprite.Sprite.__init__(self)
            self.image = Images.Spz_shop_selector_img
            self.rect = self.image.get_rect()
            self.rect.topleft = (800, 125)
            self.cost = 4000

        def info(self):
            basicfont4 = pygame.font.Font(words, 24)  # This code displays letters onto the screen
            text4 = basicfont4.render("Cost: " + str(self.cost) + "$", True, GREEN)
            textrect4 = text4.get_rect()
            textrect4.center = (400, 45)
            screen2.blit(text4, textrect4)

            text4 = basicfont4.render("Spz", True, WHITE)
            textrect4 = text4.get_rect()
            textrect4.topleft = (12.5, 30)
            screen2.blit(text4, textrect4)

            # Clip:
            basicfont4 = pygame.font.Font(words, 24)  # This code displays letters onto the screen
            text4 = basicfont4.render("Clip", True, WHITE)
            textrect4 = text4.get_rect()
            textrect4.topleft = (300, 260)
            screen2.blit(text4, textrect4)

            text4 = basicfont4.render(str(spz.permclip), True, WHITE)
            textrect4 = text4.get_rect()
            textrect4.topleft = (320, 280)
            screen2.blit(text4, textrect4)

            # Ammo:
            basicfont4 = pygame.font.Font(words, 24)  # This code displays letters onto the screen
            text4 = basicfont4.render("Ammo", True, WHITE)
            textrect4 = text4.get_rect()
            textrect4.topleft = (500, 260)
            screen2.blit(text4, textrect4)

            text4 = basicfont4.render(str(spz.ammountofbullets), True, WHITE)
            textrect4 = text4.get_rect()
            textrect4.center = (545, 300)
            screen2.blit(text4, textrect4)

            text4 = basicfont4.render(str(spz.bulletcost) + "$", True, WHITE)
            textrect4 = text4.get_rect()
            textrect4.center = (545, 425)
            screen2.blit(text4, textrect4)

            # Stats:
            basicfont4 = pygame.font.Font(words, 36)  # This code displays letters onto the screen
            text4 = basicfont4.render("Stats:", True, RED)
            textrect4 = text4.get_rect()
            textrect4.topleft = (12.5, 260)
            screen2.blit(text4, textrect4)

            basicfont4 = pygame.font.Font(words, 18)  # This code displays letters onto the screen
            text4 = basicfont4.render("Damage: " + str(spz.Bullet().damage), True, RED)
            textrect4 = text4.get_rect()
            textrect4.topleft = (12.5, 310)
            screen2.blit(text4, textrect4)

            basicfont4 = pygame.font.Font(words, 18)  # This code displays letters onto the screen
            text4 = basicfont4.render("Fire Rate: " + str(spz.Bullet().firerate), True, RED)
            textrect4 = text4.get_rect()
            textrect4.topleft = (12.5, 340)
            screen2.blit(text4, textrect4)

            basicfont4 = pygame.font.Font(words, 18)  # This code displays letters onto the screen
            text4 = basicfont4.render("Reload Speed: " + str(spz.Bullet().reloadspeed), True, RED)
            textrect4 = text4.get_rect()
            textrect4.topleft = (12.5, 370)
            screen2.blit(text4, textrect4)

            basicfont4 = pygame.font.Font(words, 18)  # This code displays letters onto the screen
            text4 = basicfont4.render("Range: " + "Coming Soon!", True, RED)
            textrect4 = text4.get_rect()
            textrect4.topleft = (12.5, 400)
            screen2.blit(text4, textrect4)

            basicfont4 = pygame.font.Font(words, 18)  # This code displays letters onto the screen
            text4 = basicfont4.render("Accuracy: " + "Coming Soon!", True, RED)
            textrect4 = text4.get_rect()
            textrect4.topleft = (12.5, 430)
            screen2.blit(text4, textrect4)

            basicfont4 = pygame.font.Font(words, 18)  # This code displays letters onto the screen
            text4 = basicfont4.render("Mobility: " + "Coming Soon!", True, RED)
            textrect4 = text4.get_rect()
            textrect4.topleft = (12.5, 460)
            screen2.blit(text4, textrect4)

        class Shop_Layout(pygame.sprite.Sprite):
            def __init__(self):
                pygame.sprite.Sprite.__init__(self)
                self.image = Images.shop_format_img
                self.rect = self.image.get_rect()
                self.rect.topleft = (0, 25)
                self.cost = 100

        class gun_img(pygame.sprite.Sprite):
            def __init__(self):
                pygame.sprite.Sprite.__init__(self)
                self.image = Images.Spz_shop_img
                self.rect = self.image.get_rect()
                self.rect.topleft = (75, 75)
                self.cost = 100

        class buy(pygame.sprite.Sprite):
            def __init__(self):
                pygame.sprite.Sprite.__init__(self)
                self.image = Images.buypic
                self.rect = self.image.get_rect()
                self.rect.topright = (789, 35)
                self.cost = 4000

        class equip(pygame.sprite.Sprite):
            def __init__(self):
                pygame.sprite.Sprite.__init__(self)
                self.image = Images.equip_pic
                self.rect = self.image.get_rect()
                self.rect.topright = (789, 35)
                self.cost = 100

        class equiped(pygame.sprite.Sprite):
            def __init__(self):
                pygame.sprite.Sprite.__init__(self)
                self.image = Images.equiped_pic
                self.rect = self.image.get_rect()
                self.rect.topright = (789, 35)
                self.cost = 100

        class Bullet_Shop(pygame.sprite.Sprite):
            def __init__(self):
                pygame.sprite.Sprite.__init__(self)
                self.image = Images.buy_ammo_img
                self.rect = self.image.get_rect()
                self.rect.center = (545, 475)
                self.cost = 100

#Snipers:
class K98k(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.ammountofbullets = 10
        self.clip = 1
        self.permclip = 1
        self.reload = 0
        self.permreload = 100
        self.image = Images.snipergunpic
        self.rect = self.image.get_rect()
        self.rect.right = WIDTH
        self.rect.bottom = HEIGHT - HEIGHT / 10
        self.name = "K98k"
        self.type = "sniper"
        self.bought = False
        self.bulletcost = 100

    # Bullet object
    class Bullet(pygame.sprite.Sprite):
        # Bullet that shoots up
        def __init__(self):
            pygame.sprite.Sprite.__init__(self)
            self.image = Images.bulletpic
            self.rect = self.image.get_rect()
            self.rect.center = fighter.rect.center
            self.speed = deltatime * 600
            mouse_x, mouse_y = pygame.mouse.get_pos()
            bullet_vec_x = mouse_x - fighter.rect.center[0]
            bullet_vec_y = mouse_y - fighter.rect.center[1]
            vec_length = math.sqrt(bullet_vec_x ** 2 + bullet_vec_y ** 2)
            bullet_vec_x = (bullet_vec_x / vec_length) * self.speed  # the five is speed
            bullet_vec_y = (bullet_vec_y / vec_length) * self.speed
            self.change_x = 0
            self.change_y = 0
            self.change_x += bullet_vec_x
            self.change_y += bullet_vec_y
            self.pos_x = fighter.rect.center[0]
            self.pos_y = fighter.rect.center[1]
            self.damage = 100
            self.shootcounter = 1
            self.counter = 0
            self.nextbullet = 0
            self.ammountfornextbullet = 1000
            self.firerate = 5
            self.reloadspeed = 5

        def update(self):
            self.nextbullet += 1
            if self.rect.x < -10 or self.rect.x > WIDTH + 10 or self.rect.y < -10 or self.rect.y > HEIGHT + 10:
                Bullets.remove(self)

            self.counter += 1
            if self.shootcounter < self.counter:
                self.counter = 0

                self.pos_x += self.change_x
                self.pos_y += self.change_y

                self.rect.x = self.pos_x
                self.rect.y = self.pos_y

            for i in range(len(enemy_list)):
                if pygame.sprite.collide_rect(self, enemy_list.sprites()[i]):
                    Bullets.remove(self)
                    enemy_list.sprites()[i].heal -= self.damage
                    if enemy_list.sprites()[i].heal <= 0:
                        fighter.xp += fighter.xpadd
                        fighter.kills += 1
                        enemy_list.remove(enemy_list.sprites()[i])
            if pygame.sprite.collide_rect(self, CoinObject):
                CoinObject.update()
                Bullets.remove(self)
                global coins
                coins += coinadd

    class Shop(pygame.sprite.Sprite):
        def __init__(self):
            pygame.sprite.Sprite.__init__(self)
            self.image = Images.K98k_shop_selector_img
            self.rect = self.image.get_rect()
            self.rect.topleft = (800, 25)
            self.cost = 100

        def info(self):
            basicfont4 = pygame.font.Font(words, 24)  # This code displays letters onto the screen
            text4 = basicfont4.render("Cost: " + str(self.cost) + "$", True, GREEN)
            textrect4 = text4.get_rect()
            textrect4.center = (400, 45)
            screen2.blit(text4, textrect4)

            text4 = basicfont4.render("K98k", True, WHITE)
            textrect4 = text4.get_rect()
            textrect4.topleft = (12.5, 30)
            screen2.blit(text4, textrect4)

            # Clip:
            basicfont4 = pygame.font.Font(words, 24)  # This code displays letters onto the screen
            text4 = basicfont4.render("Clip", True, WHITE)
            textrect4 = text4.get_rect()
            textrect4.topleft = (300, 260)
            screen2.blit(text4, textrect4)

            text4 = basicfont4.render(str(K98K.permclip), True, WHITE)
            textrect4 = text4.get_rect()
            textrect4.topleft = (320, 280)
            screen2.blit(text4, textrect4)

            # Ammo:
            basicfont4 = pygame.font.Font(words, 24)  # This code displays letters onto the screen
            text4 = basicfont4.render("Ammo", True, WHITE)
            textrect4 = text4.get_rect()
            textrect4.topleft = (500, 260)
            screen2.blit(text4, textrect4)

            text4 = basicfont4.render(str(K98K.ammountofbullets), True, WHITE)
            textrect4 = text4.get_rect()
            textrect4.center = (545, 300)
            screen2.blit(text4, textrect4)

            text4 = basicfont4.render(str(K98K.bulletcost) + "$", True, WHITE)
            textrect4 = text4.get_rect()
            textrect4.center = (545, 425)
            screen2.blit(text4, textrect4)

            # Stats:
            basicfont4 = pygame.font.Font(words, 36)  # This code displays letters onto the screen
            text4 = basicfont4.render("Stats:", True, RED)
            textrect4 = text4.get_rect()
            textrect4.topleft = (12.5, 260)
            screen2.blit(text4, textrect4)

            basicfont4 = pygame.font.Font(words, 18)  # This code displays letters onto the screen
            text4 = basicfont4.render("Damage: " + str(K98K.Bullet().damage), True, RED)
            textrect4 = text4.get_rect()
            textrect4.topleft = (12.5, 310)
            screen2.blit(text4, textrect4)

            basicfont4 = pygame.font.Font(words, 18)  # This code displays letters onto the screen
            text4 = basicfont4.render("Fire Rate: " + str(K98K.Bullet().firerate), True, RED)
            textrect4 = text4.get_rect()
            textrect4.topleft = (12.5, 340)
            screen2.blit(text4, textrect4)

            basicfont4 = pygame.font.Font(words, 18)  # This code displays letters onto the screen
            text4 = basicfont4.render("Reload Speed: " + str(K98K.Bullet().reloadspeed), True, RED)
            textrect4 = text4.get_rect()
            textrect4.topleft = (12.5, 370)
            screen2.blit(text4, textrect4)

            basicfont4 = pygame.font.Font(words, 18)  # This code displays letters onto the screen
            text4 = basicfont4.render("Range: " + "Coming Soon!", True, RED)
            textrect4 = text4.get_rect()
            textrect4.topleft = (12.5, 400)
            screen2.blit(text4, textrect4)

            basicfont4 = pygame.font.Font(words, 18)  # This code displays letters onto the screen
            text4 = basicfont4.render("Accuracy: " + "Coming Soon!", True, RED)
            textrect4 = text4.get_rect()
            textrect4.topleft = (12.5, 430)
            screen2.blit(text4, textrect4)

            basicfont4 = pygame.font.Font(words, 18)  # This code displays letters onto the screen
            text4 = basicfont4.render("Mobility: " + "Coming Soon!", True, RED)
            textrect4 = text4.get_rect()
            textrect4.topleft = (12.5, 460)
            screen2.blit(text4, textrect4)

        class Shop_Layout(pygame.sprite.Sprite):
            def __init__(self):
                pygame.sprite.Sprite.__init__(self)
                self.image = Images.shop_format_img
                self.rect = self.image.get_rect()
                self.rect.topleft = (0, 25)
                self.cost = 100

        class gun_img(pygame.sprite.Sprite):
            def __init__(self):
                pygame.sprite.Sprite.__init__(self)
                self.image = Images.k98k_img
                self.rect = self.image.get_rect()
                self.rect.topleft = (75, 75)
                self.cost = 100

        class buy(pygame.sprite.Sprite):
            def __init__(self):
                pygame.sprite.Sprite.__init__(self)
                self.image = Images.buypic
                self.rect = self.image.get_rect()
                self.rect.topright = (789, 35)
                self.cost = 100

        class equip(pygame.sprite.Sprite):
            def __init__(self):
                pygame.sprite.Sprite.__init__(self)
                self.image = Images.equip_pic
                self.rect = self.image.get_rect()
                self.rect.topright = (789, 35)
                self.cost = 100

        class equiped(pygame.sprite.Sprite):
            def __init__(self):
                pygame.sprite.Sprite.__init__(self)
                self.image = Images.equiped_pic
                self.rect = self.image.get_rect()
                self.rect.topright = (789, 35)
                self.cost = 100

        class Bullet_Shop(pygame.sprite.Sprite):
            def __init__(self):
                pygame.sprite.Sprite.__init__(self)
                self.image = Images.buy_ammo_img
                self.rect = self.image.get_rect()
                self.rect.center = (545, 475)
                self.cost = 100

class Puska(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.ammountofbullets = 10
        self.clip = 5
        self.permclip = 5
        self.reload = 0
        self.permreload = 100
        self.image = Images.Puska_img
        self.rect = self.image.get_rect()
        self.rect.right = WIDTH
        self.rect.bottom = HEIGHT - HEIGHT / 10
        self.name = "Puska"
        self.type = "sniper"
        self.bought = False
        self.bulletcost = 200

    # Bullet object
    class Bullet(pygame.sprite.Sprite):
        # Bullet that shoots up
        def __init__(self):
            pygame.sprite.Sprite.__init__(self)
            self.image = Images.bulletpic
            self.rect = self.image.get_rect()
            self.rect.center = fighter.rect.center
            self.speed = deltatime * 600
            mouse_x, mouse_y = pygame.mouse.get_pos()
            bullet_vec_x = mouse_x - fighter.rect.center[0]
            bullet_vec_y = mouse_y - fighter.rect.center[1]
            vec_length = math.sqrt(bullet_vec_x ** 2 + bullet_vec_y ** 2)
            bullet_vec_x = (bullet_vec_x / vec_length) * self.speed  # the five is speed
            bullet_vec_y = (bullet_vec_y / vec_length) * self.speed
            self.change_x = 0
            self.change_y = 0
            self.change_x += bullet_vec_x
            self.change_y += bullet_vec_y
            self.pos_x = fighter.rect.center[0]
            self.pos_y = fighter.rect.center[1]
            self.damage = 50
            self.shootcounter = 1
            self.counter = 0
            self.nextbullet = 0
            self.ammountfornextbullet = 500
            self.firerate = 5
            self.reloadspeed = 5

        def update(self):
            self.nextbullet += 1
            if self.rect.x < -10 or self.rect.x > WIDTH + 10 or self.rect.y < -10 or self.rect.y > HEIGHT + 10:
                Bullets.remove(self)

            self.counter += 1
            if self.shootcounter < self.counter:
                self.counter = 0

                self.pos_x += self.change_x
                self.pos_y += self.change_y

                self.rect.x = self.pos_x
                self.rect.y = self.pos_y

            for i in range(len(enemy_list)):
                if pygame.sprite.collide_rect(self, enemy_list.sprites()[i]):
                    Bullets.remove(self)
                    enemy_list.sprites()[i].heal -= self.damage
                    if enemy_list.sprites()[i].heal <= 0:
                        fighter.xp += fighter.xpadd
                        fighter.kills += 1
                        enemy_list.remove(enemy_list.sprites()[i])
            if pygame.sprite.collide_rect(self, CoinObject):
                CoinObject.update()
                Bullets.remove(self)
                global coins
                coins += coinadd

    class Shop(pygame.sprite.Sprite):
        def __init__(self):
            pygame.sprite.Sprite.__init__(self)
            self.image = Images.Puska_shop_selector_img
            self.rect = self.image.get_rect()
            self.rect.topleft = (800, 75)
            self.cost = 1000

        def info(self):
            basicfont4 = pygame.font.Font(words, 24)  # This code displays letters onto the screen
            text4 = basicfont4.render("Cost: " + str(self.cost) + "$", True, GREEN)
            textrect4 = text4.get_rect()
            textrect4.center = (400, 45)
            screen2.blit(text4, textrect4)

            text4 = basicfont4.render("Puska", True, WHITE)
            textrect4 = text4.get_rect()
            textrect4.topleft = (12.5, 30)
            screen2.blit(text4, textrect4)

            # Clip:
            basicfont4 = pygame.font.Font(words, 24)  # This code displays letters onto the screen
            text4 = basicfont4.render("Clip", True, WHITE)
            textrect4 = text4.get_rect()
            textrect4.topleft = (300, 260)
            screen2.blit(text4, textrect4)

            text4 = basicfont4.render(str(puska.permclip), True, WHITE)
            textrect4 = text4.get_rect()
            textrect4.topleft = (320, 280)
            screen2.blit(text4, textrect4)

            # Ammo:
            basicfont4 = pygame.font.Font(words, 24)  # This code displays letters onto the screen
            text4 = basicfont4.render("Ammo", True, WHITE)
            textrect4 = text4.get_rect()
            textrect4.topleft = (500, 260)
            screen2.blit(text4, textrect4)

            text4 = basicfont4.render(str(puska.ammountofbullets), True, WHITE)
            textrect4 = text4.get_rect()
            textrect4.center = (545, 300)
            screen2.blit(text4, textrect4)

            text4 = basicfont4.render(str(puska.bulletcost) + "$", True, WHITE)
            textrect4 = text4.get_rect()
            textrect4.center = (545, 425)
            screen2.blit(text4, textrect4)

            # Stats:
            basicfont4 = pygame.font.Font(words, 36)  # This code displays letters onto the screen
            text4 = basicfont4.render("Stats:", True, RED)
            textrect4 = text4.get_rect()
            textrect4.topleft = (12.5, 260)
            screen2.blit(text4, textrect4)

            basicfont4 = pygame.font.Font(words, 18)  # This code displays letters onto the screen
            text4 = basicfont4.render("Damage: " + str(puska.Bullet().damage), True, RED)
            textrect4 = text4.get_rect()
            textrect4.topleft = (12.5, 310)
            screen2.blit(text4, textrect4)

            basicfont4 = pygame.font.Font(words, 18)  # This code displays letters onto the screen
            text4 = basicfont4.render("Fire Rate: " + str(puska.Bullet().firerate), True, RED)
            textrect4 = text4.get_rect()
            textrect4.topleft = (12.5, 340)
            screen2.blit(text4, textrect4)

            basicfont4 = pygame.font.Font(words, 18)  # This code displays letters onto the screen
            text4 = basicfont4.render("Reload Speed: " + str(puska.Bullet().reloadspeed), True, RED)
            textrect4 = text4.get_rect()
            textrect4.topleft = (12.5, 370)
            screen2.blit(text4, textrect4)

            basicfont4 = pygame.font.Font(words, 18)  # This code displays letters onto the screen
            text4 = basicfont4.render("Range: " + "Coming Soon!", True, RED)
            textrect4 = text4.get_rect()
            textrect4.topleft = (12.5, 400)
            screen2.blit(text4, textrect4)

            basicfont4 = pygame.font.Font(words, 18)  # This code displays letters onto the screen
            text4 = basicfont4.render("Accuracy: " + "Coming Soon!", True, RED)
            textrect4 = text4.get_rect()
            textrect4.topleft = (12.5, 430)
            screen2.blit(text4, textrect4)

            basicfont4 = pygame.font.Font(words, 18)  # This code displays letters onto the screen
            text4 = basicfont4.render("Mobility: " + "Coming Soon!", True, RED)
            textrect4 = text4.get_rect()
            textrect4.topleft = (12.5, 460)
            screen2.blit(text4, textrect4)

        class Shop_Layout(pygame.sprite.Sprite):
            def __init__(self):
                pygame.sprite.Sprite.__init__(self)
                self.image = Images.shop_format_img
                self.rect = self.image.get_rect()
                self.rect.topleft = (0, 25)
                self.cost = 100

        class gun_img(pygame.sprite.Sprite):
            def __init__(self):
                pygame.sprite.Sprite.__init__(self)
                self.image = Images.Puska_shop_pic
                self.rect = self.image.get_rect()
                self.rect.topleft = (75, 75)
                self.cost = 100

        class buy(pygame.sprite.Sprite):
            def __init__(self):
                pygame.sprite.Sprite.__init__(self)
                self.image = Images.buypic
                self.rect = self.image.get_rect()
                self.rect.topright = (789, 35)
                self.cost = 1000

        class equip(pygame.sprite.Sprite):
            def __init__(self):
                pygame.sprite.Sprite.__init__(self)
                self.image = Images.equip_pic
                self.rect = self.image.get_rect()
                self.rect.topright = (789, 35)
                self.cost = 100

        class equiped(pygame.sprite.Sprite):
            def __init__(self):
                pygame.sprite.Sprite.__init__(self)
                self.image = Images.equiped_pic
                self.rect = self.image.get_rect()
                self.rect.topright = (789, 35)
                self.cost = 100

        class Bullet_Shop(pygame.sprite.Sprite):
            def __init__(self):
                pygame.sprite.Sprite.__init__(self)
                self.image = Images.buy_ammo_img
                self.rect = self.image.get_rect()
                self.rect.center = (545, 475)
                self.cost = 200

class ZH_29(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.ammountofbullets = 200
        self.clip = 20
        self.permclip = 20
        self.reload = 0
        self.permreload = 100
        self.image = Images.ZH_29_img
        self.rect = self.image.get_rect()
        self.rect.right = WIDTH
        self.rect.bottom = HEIGHT - HEIGHT / 10
        self.name = "ZH-29"
        self.type = "sniper"
        self.bought = False
        self.bulletcost = 400

    # Bullet object
    class Bullet(pygame.sprite.Sprite):
        # Bullet that shoots up
        def __init__(self):
            pygame.sprite.Sprite.__init__(self)
            self.image = Images.bulletpic
            self.rect = self.image.get_rect()
            self.rect.center = fighter.rect.center
            self.speed = deltatime * 1000
            mouse_x, mouse_y = pygame.mouse.get_pos()
            bullet_vec_x = mouse_x - fighter.rect.center[0]
            bullet_vec_y = mouse_y - fighter.rect.center[1]
            vec_length = math.sqrt(bullet_vec_x ** 2 + bullet_vec_y ** 2)
            bullet_vec_x = (bullet_vec_x / vec_length) * self.speed  # the five is speed
            bullet_vec_y = (bullet_vec_y / vec_length) * self.speed
            self.change_x = 0
            self.change_y = 0
            self.change_x += bullet_vec_x
            self.change_y += bullet_vec_y
            self.pos_x = fighter.rect.center[0]
            self.pos_y = fighter.rect.center[1]
            self.damage = 25
            self.shootcounter = 1
            self.counter = 0
            self.nextbullet = 0
            self.ammountfornextbullet = 250
            self.firerate = 5
            self.reloadspeed = 5

        def update(self):
            self.nextbullet += 1
            if self.rect.x < -10 or self.rect.x > WIDTH + 10 or self.rect.y < -10 or self.rect.y > HEIGHT + 10:
                Bullets.remove(self)

            self.counter += 1
            if self.shootcounter < self.counter:
                self.counter = 0

                self.pos_x += self.change_x
                self.pos_y += self.change_y

                self.rect.x = self.pos_x
                self.rect.y = self.pos_y

            for i in range(len(enemy_list)):
                if pygame.sprite.collide_rect(self, enemy_list.sprites()[i]):
                    Bullets.remove(self)
                    enemy_list.sprites()[i].heal -= self.damage
                    if enemy_list.sprites()[i].heal <= 0:
                        fighter.xp += fighter.xpadd
                        fighter.kills += 1
                        enemy_list.remove(enemy_list.sprites()[i])
            if pygame.sprite.collide_rect(self, CoinObject):
                CoinObject.update()
                Bullets.remove(self)
                global coins
                coins += coinadd

    class Shop(pygame.sprite.Sprite):
        def __init__(self):
            pygame.sprite.Sprite.__init__(self)
            self.image = Images.ZH_29_shop_selector_img
            self.rect = self.image.get_rect()
            self.rect.topleft = (800, 125)
            self.cost = 4000

        def info(self):
            basicfont4 = pygame.font.Font(words, 24)  # This code displays letters onto the screen
            text4 = basicfont4.render("Cost: " + str(self.cost) + "$", True, GREEN)
            textrect4 = text4.get_rect()
            textrect4.center = (400, 45)
            screen2.blit(text4, textrect4)

            text4 = basicfont4.render("ZH-29", True, WHITE)
            textrect4 = text4.get_rect()
            textrect4.topleft = (12.5, 30)
            screen2.blit(text4, textrect4)

            # Clip:
            basicfont4 = pygame.font.Font(words, 24)  # This code displays letters onto the screen
            text4 = basicfont4.render("Clip", True, WHITE)
            textrect4 = text4.get_rect()
            textrect4.topleft = (300, 260)
            screen2.blit(text4, textrect4)

            text4 = basicfont4.render(str(zh29.permclip), True, WHITE)
            textrect4 = text4.get_rect()
            textrect4.topleft = (320, 280)
            screen2.blit(text4, textrect4)

            # Ammo:
            basicfont4 = pygame.font.Font(words, 24)  # This code displays letters onto the screen
            text4 = basicfont4.render("Ammo", True, WHITE)
            textrect4 = text4.get_rect()
            textrect4.topleft = (500, 260)
            screen2.blit(text4, textrect4)

            text4 = basicfont4.render(str(zh29.ammountofbullets), True, WHITE)
            textrect4 = text4.get_rect()
            textrect4.center = (545, 300)
            screen2.blit(text4, textrect4)

            text4 = basicfont4.render(str(zh29.bulletcost) + "$", True, WHITE)
            textrect4 = text4.get_rect()
            textrect4.center = (545, 425)
            screen2.blit(text4, textrect4)

            # Stats:
            basicfont4 = pygame.font.Font(words, 36)  # This code displays letters onto the screen
            text4 = basicfont4.render("Stats:", True, RED)
            textrect4 = text4.get_rect()
            textrect4.topleft = (12.5, 260)
            screen2.blit(text4, textrect4)

            basicfont4 = pygame.font.Font(words, 18)  # This code displays letters onto the screen
            text4 = basicfont4.render("Damage: " + str(zh29.Bullet().damage), True, RED)
            textrect4 = text4.get_rect()
            textrect4.topleft = (12.5, 310)
            screen2.blit(text4, textrect4)

            basicfont4 = pygame.font.Font(words, 18)  # This code displays letters onto the screen
            text4 = basicfont4.render("Fire Rate: " + str(zh29.Bullet().firerate), True, RED)
            textrect4 = text4.get_rect()
            textrect4.topleft = (12.5, 340)
            screen2.blit(text4, textrect4)

            basicfont4 = pygame.font.Font(words, 18)  # This code displays letters onto the screen
            text4 = basicfont4.render("Reload Speed: " + str(zh29.Bullet().reloadspeed), True, RED)
            textrect4 = text4.get_rect()
            textrect4.topleft = (12.5, 370)
            screen2.blit(text4, textrect4)

            basicfont4 = pygame.font.Font(words, 18)  # This code displays letters onto the screen
            text4 = basicfont4.render("Range: " + "Coming Soon!", True, RED)
            textrect4 = text4.get_rect()
            textrect4.topleft = (12.5, 400)
            screen2.blit(text4, textrect4)

            basicfont4 = pygame.font.Font(words, 18)  # This code displays letters onto the screen
            text4 = basicfont4.render("Accuracy: " + "Coming Soon!", True, RED)
            textrect4 = text4.get_rect()
            textrect4.topleft = (12.5, 430)
            screen2.blit(text4, textrect4)

            basicfont4 = pygame.font.Font(words, 18)  # This code displays letters onto the screen
            text4 = basicfont4.render("Mobility: " + "Coming Soon!", True, RED)
            textrect4 = text4.get_rect()
            textrect4.topleft = (12.5, 460)
            screen2.blit(text4, textrect4)

        class Shop_Layout(pygame.sprite.Sprite):
            def __init__(self):
                pygame.sprite.Sprite.__init__(self)
                self.image = Images.shop_format_img
                self.rect = self.image.get_rect()
                self.rect.topleft = (0, 25)
                self.cost = 100

        class gun_img(pygame.sprite.Sprite):
            def __init__(self):
                pygame.sprite.Sprite.__init__(self)
                self.image = Images.ZH_29_shop_pic
                self.rect = self.image.get_rect()
                self.rect.topleft = (75, 75)
                self.cost = 100

        class buy(pygame.sprite.Sprite):
            def __init__(self):
                pygame.sprite.Sprite.__init__(self)
                self.image = Images.buypic
                self.rect = self.image.get_rect()
                self.rect.topright = (789, 35)
                self.cost = 4000

        class equip(pygame.sprite.Sprite):
            def __init__(self):
                pygame.sprite.Sprite.__init__(self)
                self.image = Images.equip_pic
                self.rect = self.image.get_rect()
                self.rect.topright = (789, 35)
                self.cost = 100

        class equiped(pygame.sprite.Sprite):
            def __init__(self):
                pygame.sprite.Sprite.__init__(self)
                self.image = Images.equiped_pic
                self.rect = self.image.get_rect()
                self.rect.topright = (789, 35)
                self.cost = 100

        class Bullet_Shop(pygame.sprite.Sprite):
            def __init__(self):
                pygame.sprite.Sprite.__init__(self)
                self.image = Images.buy_ammo_img
                self.rect = self.image.get_rect()
                self.rect.center = (545, 475)
                self.cost = 400

# Shotguns:
class M97(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.ammountofbullets = 100
        self.clip = 8
        self.permclip = 8
        self.reload = 0
        self.permreload = 96
        self.image = Images.M97_pic
        self.rect = self.image.get_rect()
        self.rect.right = WIDTH
        self.rect.bottom = HEIGHT - HEIGHT / 10
        self.name = "M97"
        self.type = "shotgun"
        self.bought = False
        self.bulletcost = 100

    # Bullet1 object
    class Bullet1(pygame.sprite.Sprite):
        # Bullet
        def __init__(self):
            pygame.sprite.Sprite.__init__(self)
            self.image = Images.bulletpic
            self.rect = self.image.get_rect()
            self.rect.center = fighter.rect.center
            self.speed = deltatime * 200
            mouse_x, mouse_y = pygame.mouse.get_pos()
            bullet_vec_x = mouse_x - fighter.rect.center[0]
            bullet_vec_y = mouse_y - fighter.rect.center[1]
            vec_length = math.sqrt(bullet_vec_x ** 2 + bullet_vec_y ** 2)
            bullet_vec_x = (bullet_vec_x / vec_length) * self.speed  # the five is speed
            bullet_vec_y = (bullet_vec_y / vec_length) * self.speed
            self.change_x = 0
            self.change_y = 0
            self.change_x += bullet_vec_x
            self.change_y += bullet_vec_y
            self.pos_x = fighter.rect.center[0]
            self.pos_y = fighter.rect.center[1]
            self.damage = 10
            self.shootcounter = 2
            self.counter = 0
            self.nextbullet = 0
            self.ammountfornextbullet = 50
            self.firerate = 5
            self.reloadspeed = 5

        def update(self):
            self.nextbullet += 1
            if self.rect.x < -10 or self.rect.x > WIDTH + 10 or self.rect.y < -10 or self.rect.y > HEIGHT + 10:
                Bullets.remove(self)

            self.counter += 1
            if self.shootcounter < self.counter:
                self.counter = 0

                self.pos_x += self.change_x
                self.pos_y += self.change_y

                self.rect.x = self.pos_x
                self.rect.y = self.pos_y

            for i in range(len(enemy_list)):
                if pygame.sprite.collide_rect(self, enemy_list.sprites()[i]):
                    Bullets.remove(self)
                    enemy_list.sprites()[i].heal -= self.damage
                    if enemy_list.sprites()[i].heal <= 0:
                        fighter.xp += fighter.xpadd
                        fighter.kills += 1
                        enemy_list.remove(enemy_list.sprites()[i])
            if pygame.sprite.collide_rect(self, CoinObject):
                CoinObject.update()
                Bullets.remove(self)
                global coins
                coins += coinadd

    # Bullet1 object
    class Bullet2(pygame.sprite.Sprite):
        # Bullet
        def __init__(self):
            pygame.sprite.Sprite.__init__(self)
            self.image = Images.bulletpic
            self.rect = self.image.get_rect()
            self.rect.center = fighter.rect.center
            self.speed = deltatime * 200
            distance = math.sqrt(math.pow(pygame.mouse.get_pos()[0] - fighter.rect.centerx, 2) + math.pow(
                pygame.mouse.get_pos()[1] - fighter.rect.centery, 2))
            dist = int(distance * math.tan(math.radians(30)) / 2)
            mouse_x, mouse_y = (pygame.mouse.get_pos()[0] - dist, pygame.mouse.get_pos()[1] - dist)
            bullet_vec_x = mouse_x - fighter.rect.center[0]
            bullet_vec_y = mouse_y - fighter.rect.center[1]
            vec_length = math.sqrt(bullet_vec_x ** 2 + bullet_vec_y ** 2)
            bullet_vec_x = (bullet_vec_x / vec_length) * self.speed  # the five is speed
            bullet_vec_y = (bullet_vec_y / vec_length) * self.speed
            self.change_x = 0
            self.change_y = 0
            self.change_x += bullet_vec_x
            self.change_y += bullet_vec_y
            self.pos_x = fighter.rect.center[0]
            self.pos_y = fighter.rect.center[1]
            self.damage = 10
            self.shootcounter = 2
            self.counter = 0
            self.nextbullet = 0
            self.ammountfornextbullet = 50

        def update(self):
            self.nextbullet += 1
            if self.rect.x < -10 or self.rect.x > WIDTH + 10 or self.rect.y < -10 or self.rect.y > HEIGHT + 10:
                Bullets.remove(self)

            self.counter += 1
            if self.shootcounter < self.counter:
                self.counter = 0

                self.pos_x += self.change_x
                self.pos_y += self.change_y

                self.rect.x = self.pos_x
                self.rect.y = self.pos_y

            for i in range(len(enemy_list)):
                if pygame.sprite.collide_rect(self, enemy_list.sprites()[i]):
                    Bullets.remove(self)
                    enemy_list.sprites()[i].heal -= self.damage
                    if enemy_list.sprites()[i].heal <= 0:
                        fighter.xp += fighter.xpadd
                        fighter.kills += 1
                        enemy_list.remove(enemy_list.sprites()[i])
            if pygame.sprite.collide_rect(self, CoinObject):
                CoinObject.update()
                Bullets.remove(self)
                global coins
                coins += coinadd

    # Bullet1 object
    class Bullet3(pygame.sprite.Sprite):
        # Bullet
        def __init__(self):
            pygame.sprite.Sprite.__init__(self)
            self.image = Images.bulletpic
            self.rect = self.image.get_rect()
            self.rect.center = fighter.rect.center
            self.speed = deltatime * 200
            distance = math.sqrt(math.pow(pygame.mouse.get_pos()[0] - fighter.rect.centerx, 2) + math.pow(
                pygame.mouse.get_pos()[1] - fighter.rect.centery, 2))
            dist = int(distance * math.tan(math.radians(30)) / 2)
            mouse_x, mouse_y = (pygame.mouse.get_pos()[0] + dist, pygame.mouse.get_pos()[1] + dist)
            bullet_vec_x = mouse_x - fighter.rect.center[0]
            bullet_vec_y = mouse_y - fighter.rect.center[1]
            vec_length = math.sqrt(bullet_vec_x ** 2 + bullet_vec_y ** 2)
            bullet_vec_x = (bullet_vec_x / vec_length) * self.speed  # the five is speed
            bullet_vec_y = (bullet_vec_y / vec_length) * self.speed
            self.change_x = 0
            self.change_y = 0
            self.change_x += bullet_vec_x
            self.change_y += bullet_vec_y
            self.pos_x = fighter.rect.center[0]
            self.pos_y = fighter.rect.center[1]
            self.damage = 10
            self.shootcounter = 2
            self.counter = 0
            self.nextbullet = 0
            self.ammountfornextbullet = 50

        def update(self):
            self.nextbullet += 1
            if self.rect.x < -10 or self.rect.x > WIDTH + 10 or self.rect.y < -10 or self.rect.y > HEIGHT + 10:
                Bullets.remove(self)

            self.counter += 1
            if self.shootcounter < self.counter:
                self.counter = 0

                self.pos_x += self.change_x
                self.pos_y += self.change_y

                self.rect.x = self.pos_x
                self.rect.y = self.pos_y

            for i in range(len(enemy_list)):
                if pygame.sprite.collide_rect(self, enemy_list.sprites()[i]):
                    Bullets.remove(self)
                    enemy_list.sprites()[i].heal -= self.damage
                    if enemy_list.sprites()[i].heal <= 0:
                        fighter.xp += fighter.xpadd
                        fighter.kills += 1
                        enemy_list.remove(enemy_list.sprites()[i])
            if pygame.sprite.collide_rect(self, CoinObject):
                CoinObject.update()
                Bullets.remove(self)
                global coins
                coins += coinadd

    class Shop(pygame.sprite.Sprite):
        def __init__(self):
            pygame.sprite.Sprite.__init__(self)
            Colt_1911.__init__(self)
            self.image = Images.M97_shop_selector_img
            self.rect = self.image.get_rect()
            self.rect.topleft = (800, 25)
            self.cost = 100

        def info(self):
            basicfont4 = pygame.font.Font(words, 24)  # This code displays letters onto the screen
            text4 = basicfont4.render("Cost: " + str(self.cost) + "$", True, GREEN)
            textrect4 = text4.get_rect()
            textrect4.center = (400, 45)
            screen2.blit(text4, textrect4)

            text4 = basicfont4.render("M97", True, WHITE)
            textrect4 = text4.get_rect()
            textrect4.topleft = (12.5, 30)
            screen2.blit(text4, textrect4)

            # Clip:
            basicfont4 = pygame.font.Font(words, 24)  # This code displays letters onto the screen
            text4 = basicfont4.render("Clip", True, WHITE)
            textrect4 = text4.get_rect()
            textrect4.topleft = (300, 260)
            screen2.blit(text4, textrect4)

            text4 = basicfont4.render(str(m97.permclip), True, WHITE)
            textrect4 = text4.get_rect()
            textrect4.topleft = (320, 280)
            screen2.blit(text4, textrect4)

            # Ammo:
            basicfont4 = pygame.font.Font(words, 24)  # This code displays letters onto the screen
            text4 = basicfont4.render("Ammo", True, WHITE)
            textrect4 = text4.get_rect()
            textrect4.topleft = (500, 260)
            screen2.blit(text4, textrect4)

            text4 = basicfont4.render(str(m97.ammountofbullets), True, WHITE)
            textrect4 = text4.get_rect()
            textrect4.center = (545, 300)
            screen2.blit(text4, textrect4)

            text4 = basicfont4.render(str(m97.bulletcost) + "$", True, WHITE)
            textrect4 = text4.get_rect()
            textrect4.center = (545, 425)
            screen2.blit(text4, textrect4)

            # Stats:
            basicfont4 = pygame.font.Font(words, 36)  # This code displays letters onto the screen
            text4 = basicfont4.render("Stats:", True, RED)
            textrect4 = text4.get_rect()
            textrect4.topleft = (12.5, 260)
            screen2.blit(text4, textrect4)

            basicfont4 = pygame.font.Font(words, 18)  # This code displays letters onto the screen
            text4 = basicfont4.render("Damage: " + str(m97.Bullet1().damage), True, RED)
            textrect4 = text4.get_rect()
            textrect4.topleft = (12.5, 310)
            screen2.blit(text4, textrect4)

            basicfont4 = pygame.font.Font(words, 18)  # This code displays letters onto the screen
            text4 = basicfont4.render("Fire Rate: " + str(m97.Bullet1().firerate), True, RED)
            textrect4 = text4.get_rect()
            textrect4.topleft = (12.5, 340)
            screen2.blit(text4, textrect4)

            basicfont4 = pygame.font.Font(words, 18)  # This code displays letters onto the screen
            text4 = basicfont4.render("Reload Speed: " + str(m97.Bullet1().reloadspeed), True, RED)
            textrect4 = text4.get_rect()
            textrect4.topleft = (12.5, 370)
            screen2.blit(text4, textrect4)

            basicfont4 = pygame.font.Font(words, 18)  # This code displays letters onto the screen
            text4 = basicfont4.render("Range: " + "Coming Soon!", True, RED)
            textrect4 = text4.get_rect()
            textrect4.topleft = (12.5, 400)
            screen2.blit(text4, textrect4)

            basicfont4 = pygame.font.Font(words, 18)  # This code displays letters onto the screen
            text4 = basicfont4.render("Accuracy: " + "Coming Soon!", True, RED)
            textrect4 = text4.get_rect()
            textrect4.topleft = (12.5, 430)
            screen2.blit(text4, textrect4)

            basicfont4 = pygame.font.Font(words, 18)  # This code displays letters onto the screen
            text4 = basicfont4.render("Mobility: " + "Coming Soon!", True, RED)
            textrect4 = text4.get_rect()
            textrect4.topleft = (12.5, 460)
            screen2.blit(text4, textrect4)

        class Shop_Layout(pygame.sprite.Sprite):
            def __init__(self):
                pygame.sprite.Sprite.__init__(self)
                self.image = Images.shop_format_img
                self.rect = self.image.get_rect()
                self.rect.topleft = (0, 25)
                self.cost = 100

        class gun_img(pygame.sprite.Sprite):
            def __init__(self):
                pygame.sprite.Sprite.__init__(self)
                self.image = Images.m97_img
                self.rect = self.image.get_rect()
                self.rect.topleft = (75, 75)
                self.cost = 100

        class buy(pygame.sprite.Sprite):
            def __init__(self):
                pygame.sprite.Sprite.__init__(self)
                self.image = Images.buypic
                self.rect = self.image.get_rect()
                self.rect.topright = (789, 35)
                self.cost = 100

        class equip(pygame.sprite.Sprite):
            def __init__(self):
                pygame.sprite.Sprite.__init__(self)
                self.image = Images.equip_pic
                self.rect = self.image.get_rect()
                self.rect.topright = (789, 35)
                self.cost = 100

        class equiped(pygame.sprite.Sprite):
            def __init__(self):
                pygame.sprite.Sprite.__init__(self)
                self.image = Images.equiped_pic
                self.rect = self.image.get_rect()
                self.rect.topright = (789, 35)
                self.cost = 100

        class Bullet_Shop(pygame.sprite.Sprite):
            def __init__(self):
                pygame.sprite.Sprite.__init__(self)
                self.image = Images.buy_ammo_img
                self.rect = self.image.get_rect()
                self.rect.center = (545, 475)
                self.cost = 100

class A5(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.ammountofbullets = 200
        self.clip = 20
        self.permclip = 20
        self.reload = 0
        self.permreload = 96
        self.image = Images.A5_img
        self.rect = self.image.get_rect()
        self.rect.right = WIDTH
        self.rect.bottom = HEIGHT - HEIGHT / 10
        self.name = "A5"
        self.type = "shotgun"
        self.bought = False
        self.bulletcost = 100

    # Bullet1 object
    class Bullet1(pygame.sprite.Sprite):
        # Bullet
        def __init__(self):
            pygame.sprite.Sprite.__init__(self)
            self.image = Images.bulletpic
            self.rect = self.image.get_rect()
            self.rect.center = fighter.rect.center
            self.speed = deltatime * 500
            mouse_x, mouse_y = pygame.mouse.get_pos()
            bullet_vec_x = mouse_x - fighter.rect.center[0]
            bullet_vec_y = mouse_y - fighter.rect.center[1]
            vec_length = math.sqrt(bullet_vec_x ** 2 + bullet_vec_y ** 2)
            bullet_vec_x = (bullet_vec_x / vec_length) * self.speed  # the five is speed
            bullet_vec_y = (bullet_vec_y / vec_length) * self.speed
            self.change_x = 0
            self.change_y = 0
            self.change_x += bullet_vec_x
            self.change_y += bullet_vec_y
            self.pos_x = fighter.rect.center[0]
            self.pos_y = fighter.rect.center[1]
            self.damage = 10
            self.shootcounter = 2
            self.counter = 0
            self.nextbullet = 0
            self.ammountfornextbullet = 10
            self.firerate = 5
            self.reloadspeed = 5

        def update(self):
            self.nextbullet += 1
            if self.rect.x < -10 or self.rect.x > WIDTH + 10 or self.rect.y < -10 or self.rect.y > HEIGHT + 10:
                Bullets.remove(self)

            self.counter += 1
            if self.shootcounter < self.counter:
                self.counter = 0

                self.pos_x += self.change_x
                self.pos_y += self.change_y

                self.rect.x = self.pos_x
                self.rect.y = self.pos_y

            for i in range(len(enemy_list)):
                if pygame.sprite.collide_rect(self, enemy_list.sprites()[i]):
                    Bullets.remove(self)
                    enemy_list.sprites()[i].heal -= self.damage
                    if enemy_list.sprites()[i].heal <= 0:
                        fighter.xp += fighter.xpadd
                        fighter.kills += 1
                        enemy_list.remove(enemy_list.sprites()[i])
            if pygame.sprite.collide_rect(self, CoinObject):
                CoinObject.update()
                Bullets.remove(self)
                global coins
                coins += coinadd

    # Bullet1 object
    class Bullet2(pygame.sprite.Sprite):
        # Bullet
        def __init__(self):
            pygame.sprite.Sprite.__init__(self)
            self.image = Images.bulletpic
            self.rect = self.image.get_rect()
            self.rect.center = fighter.rect.center
            self.speed = deltatime * 500
            distance = math.sqrt(math.pow(pygame.mouse.get_pos()[0] - fighter.rect.centerx, 2) + math.pow(
                pygame.mouse.get_pos()[1] - fighter.rect.centery, 2))
            dist = int(distance * math.tan(math.radians(30)) / 2)
            mouse_x, mouse_y = (pygame.mouse.get_pos()[0] - dist, pygame.mouse.get_pos()[1] - dist)
            bullet_vec_x = mouse_x - fighter.rect.center[0]
            bullet_vec_y = mouse_y - fighter.rect.center[1]
            vec_length = math.sqrt(bullet_vec_x ** 2 + bullet_vec_y ** 2)
            bullet_vec_x = (bullet_vec_x / vec_length) * self.speed  # the five is speed
            bullet_vec_y = (bullet_vec_y / vec_length) * self.speed
            self.change_x = 0
            self.change_y = 0
            self.change_x += bullet_vec_x
            self.change_y += bullet_vec_y
            self.pos_x = fighter.rect.center[0]
            self.pos_y = fighter.rect.center[1]
            self.damage = 10
            self.shootcounter = 2
            self.counter = 0
            self.nextbullet = 0
            self.ammountfornextbullet = 10

        def update(self):
            self.nextbullet += 1
            if self.rect.x < -10 or self.rect.x > WIDTH + 10 or self.rect.y < -10 or self.rect.y > HEIGHT + 10:
                Bullets.remove(self)

            self.counter += 1
            if self.shootcounter < self.counter:
                self.counter = 0

                self.pos_x += self.change_x
                self.pos_y += self.change_y

                self.rect.x = self.pos_x
                self.rect.y = self.pos_y

            for i in range(len(enemy_list)):
                if pygame.sprite.collide_rect(self, enemy_list.sprites()[i]):
                    Bullets.remove(self)
                    enemy_list.sprites()[i].heal -= self.damage
                    if enemy_list.sprites()[i].heal <= 0:
                        fighter.xp += fighter.xpadd
                        fighter.kills += 1
                        enemy_list.remove(enemy_list.sprites()[i])
            if pygame.sprite.collide_rect(self, CoinObject):
                CoinObject.update()
                Bullets.remove(self)
                global coins
                coins += coinadd

    # Bullet1 object
    class Bullet3(pygame.sprite.Sprite):
        # Bullet
        def __init__(self):
            pygame.sprite.Sprite.__init__(self)
            self.image = Images.bulletpic
            self.rect = self.image.get_rect()
            self.rect.center = fighter.rect.center
            self.speed = deltatime * 500
            distance = math.sqrt(math.pow(pygame.mouse.get_pos()[0] - fighter.rect.centerx, 2) + math.pow(
                pygame.mouse.get_pos()[1] - fighter.rect.centery, 2))
            dist = int(distance * math.tan(math.radians(30)) / 2)
            mouse_x, mouse_y = (pygame.mouse.get_pos()[0] + dist, pygame.mouse.get_pos()[1] + dist)
            bullet_vec_x = mouse_x - fighter.rect.center[0]
            bullet_vec_y = mouse_y - fighter.rect.center[1]
            vec_length = math.sqrt(bullet_vec_x ** 2 + bullet_vec_y ** 2)
            bullet_vec_x = (bullet_vec_x / vec_length) * self.speed  # the five is speed
            bullet_vec_y = (bullet_vec_y / vec_length) * self.speed
            self.change_x = 0
            self.change_y = 0
            self.change_x += bullet_vec_x
            self.change_y += bullet_vec_y
            self.pos_x = fighter.rect.center[0]
            self.pos_y = fighter.rect.center[1]
            self.damage = 10
            self.shootcounter = 2
            self.counter = 0
            self.nextbullet = 0
            self.ammountfornextbullet = 10

        def update(self):
            self.nextbullet += 1
            if self.rect.x < -10 or self.rect.x > WIDTH + 10 or self.rect.y < -10 or self.rect.y > HEIGHT + 10:
                Bullets.remove(self)

            self.counter += 1
            if self.shootcounter < self.counter:
                self.counter = 0

                self.pos_x += self.change_x
                self.pos_y += self.change_y

                self.rect.x = self.pos_x
                self.rect.y = self.pos_y

            for i in range(len(enemy_list)):
                if pygame.sprite.collide_rect(self, enemy_list.sprites()[i]):
                    Bullets.remove(self)
                    enemy_list.sprites()[i].heal -= self.damage
                    if enemy_list.sprites()[i].heal <= 0:
                        fighter.xp += fighter.xpadd
                        fighter.kills += 1
                        enemy_list.remove(enemy_list.sprites()[i])
            if pygame.sprite.collide_rect(self, CoinObject):
                CoinObject.update()
                Bullets.remove(self)
                global coins
                coins += coinadd

    class Shop(pygame.sprite.Sprite):
        def __init__(self):
            pygame.sprite.Sprite.__init__(self)
            Colt_1911.__init__(self)
            self.image = Images.A5_shop_selector_img
            self.rect = self.image.get_rect()
            self.rect.topleft = (800, 75)
            self.cost = 2000

        def info(self):
            basicfont4 = pygame.font.Font(words, 24)  # This code displays letters onto the screen
            text4 = basicfont4.render("Cost: " + str(self.cost) + "$", True, GREEN)
            textrect4 = text4.get_rect()
            textrect4.center = (400, 45)
            screen2.blit(text4, textrect4)

            text4 = basicfont4.render("M97", True, WHITE)
            textrect4 = text4.get_rect()
            textrect4.topleft = (12.5, 30)
            screen2.blit(text4, textrect4)

            # Clip:
            basicfont4 = pygame.font.Font(words, 24)  # This code displays letters onto the screen
            text4 = basicfont4.render("Clip", True, WHITE)
            textrect4 = text4.get_rect()
            textrect4.topleft = (300, 260)
            screen2.blit(text4, textrect4)

            text4 = basicfont4.render(str(a5.permclip), True, WHITE)
            textrect4 = text4.get_rect()
            textrect4.topleft = (320, 280)
            screen2.blit(text4, textrect4)

            # Ammo:
            basicfont4 = pygame.font.Font(words, 24)  # This code displays letters onto the screen
            text4 = basicfont4.render("Ammo", True, WHITE)
            textrect4 = text4.get_rect()
            textrect4.topleft = (500, 260)
            screen2.blit(text4, textrect4)

            text4 = basicfont4.render(str(a5.ammountofbullets), True, WHITE)
            textrect4 = text4.get_rect()
            textrect4.center = (545, 300)
            screen2.blit(text4, textrect4)

            text4 = basicfont4.render(str(a5.bulletcost) + "$", True, WHITE)
            textrect4 = text4.get_rect()
            textrect4.center = (545, 425)
            screen2.blit(text4, textrect4)

            # Stats:
            basicfont4 = pygame.font.Font(words, 36)  # This code displays letters onto the screen
            text4 = basicfont4.render("Stats:", True, RED)
            textrect4 = text4.get_rect()
            textrect4.topleft = (12.5, 260)
            screen2.blit(text4, textrect4)

            basicfont4 = pygame.font.Font(words, 18)  # This code displays letters onto the screen
            text4 = basicfont4.render("Damage: " + str(a5.Bullet1().damage), True, RED)
            textrect4 = text4.get_rect()
            textrect4.topleft = (12.5, 310)
            screen2.blit(text4, textrect4)

            basicfont4 = pygame.font.Font(words, 18)  # This code displays letters onto the screen
            text4 = basicfont4.render("Fire Rate: " + str(a5.Bullet1().firerate), True, RED)
            textrect4 = text4.get_rect()
            textrect4.topleft = (12.5, 340)
            screen2.blit(text4, textrect4)

            basicfont4 = pygame.font.Font(words, 18)  # This code displays letters onto the screen
            text4 = basicfont4.render("Reload Speed: " + str(a5.Bullet1().reloadspeed), True, RED)
            textrect4 = text4.get_rect()
            textrect4.topleft = (12.5, 370)
            screen2.blit(text4, textrect4)

            basicfont4 = pygame.font.Font(words, 18)  # This code displays letters onto the screen
            text4 = basicfont4.render("Range: " + "Coming Soon!", True, RED)
            textrect4 = text4.get_rect()
            textrect4.topleft = (12.5, 400)
            screen2.blit(text4, textrect4)

            basicfont4 = pygame.font.Font(words, 18)  # This code displays letters onto the screen
            text4 = basicfont4.render("Accuracy: " + "Coming Soon!", True, RED)
            textrect4 = text4.get_rect()
            textrect4.topleft = (12.5, 430)
            screen2.blit(text4, textrect4)

            basicfont4 = pygame.font.Font(words, 18)  # This code displays letters onto the screen
            text4 = basicfont4.render("Mobility: " + "Coming Soon!", True, RED)
            textrect4 = text4.get_rect()
            textrect4.topleft = (12.5, 460)
            screen2.blit(text4, textrect4)

        class Shop_Layout(pygame.sprite.Sprite):
            def __init__(self):
                pygame.sprite.Sprite.__init__(self)
                self.image = Images.shop_format_img
                self.rect = self.image.get_rect()
                self.rect.topleft = (0, 25)
                self.cost = 100

        class gun_img(pygame.sprite.Sprite):
            def __init__(self):
                pygame.sprite.Sprite.__init__(self)
                self.image = Images.A5_shop_img
                self.rect = self.image.get_rect()
                self.rect.topleft = (75, 75)
                self.cost = 100

        class buy(pygame.sprite.Sprite):
            def __init__(self):
                pygame.sprite.Sprite.__init__(self)
                self.image = Images.buypic
                self.rect = self.image.get_rect()
                self.rect.topright = (789, 35)
                self.cost = 2000

        class equip(pygame.sprite.Sprite):
            def __init__(self):
                pygame.sprite.Sprite.__init__(self)
                self.image = Images.equip_pic
                self.rect = self.image.get_rect()
                self.rect.topright = (789, 35)
                self.cost = 100

        class equiped(pygame.sprite.Sprite):
            def __init__(self):
                pygame.sprite.Sprite.__init__(self)
                self.image = Images.equiped_pic
                self.rect = self.image.get_rect()
                self.rect.topright = (789, 35)
                self.cost = 100

        class Bullet_Shop(pygame.sprite.Sprite):
            def __init__(self):
                pygame.sprite.Sprite.__init__(self)
                self.image = Images.buy_ammo_img
                self.rect = self.image.get_rect()
                self.rect.center = (545, 475)
                self.cost = 200

class Ithaca_37(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.ammountofbullets = 280
        self.clip = 28
        self.permclip = 28
        self.reload = 0
        self.permreload = 96
        self.image = Images.Ithaca_37_img
        self.rect = self.image.get_rect()
        self.rect.right = WIDTH
        self.rect.bottom = HEIGHT - HEIGHT / 10
        self.name = "Ithaca 37"
        self.type = "shotgun"
        self.bought = False
        self.bulletcost = 400

    # Bullet1 object
    class Bullet1(pygame.sprite.Sprite):
        # Bullet
        def __init__(self):
            pygame.sprite.Sprite.__init__(self)
            self.image = Images.bulletpic
            self.rect = self.image.get_rect()
            self.rect.center = fighter.rect.center
            self.speed = deltatime * 800
            mouse_x, mouse_y = pygame.mouse.get_pos()
            bullet_vec_x = mouse_x - fighter.rect.center[0]
            bullet_vec_y = mouse_y - fighter.rect.center[1]
            vec_length = math.sqrt(bullet_vec_x ** 2 + bullet_vec_y ** 2)
            bullet_vec_x = (bullet_vec_x / vec_length) * self.speed  # the five is speed
            bullet_vec_y = (bullet_vec_y / vec_length) * self.speed
            self.change_x = 0
            self.change_y = 0
            self.change_x += bullet_vec_x
            self.change_y += bullet_vec_y
            self.pos_x = fighter.rect.center[0]
            self.pos_y = fighter.rect.center[1]
            self.damage = 50
            self.shootcounter = 2
            self.counter = 0
            self.nextbullet = 0
            self.ammountfornextbullet = 500
            self.firerate = 5
            self.reloadspeed = 5

        def update(self):
            self.nextbullet += 1
            if self.rect.x < -10 or self.rect.x > WIDTH + 10 or self.rect.y < -10 or self.rect.y > HEIGHT + 10:
                Bullets.remove(self)

            self.counter += 1
            if self.shootcounter < self.counter:
                self.counter = 0

                self.pos_x += self.change_x
                self.pos_y += self.change_y

                self.rect.x = self.pos_x
                self.rect.y = self.pos_y

            for i in range(len(enemy_list)):
                if pygame.sprite.collide_rect(self, enemy_list.sprites()[i]):
                    Bullets.remove(self)
                    enemy_list.sprites()[i].heal -= self.damage
                    if enemy_list.sprites()[i].heal <= 0:
                        fighter.xp += fighter.xpadd
                        fighter.kills += 1
                        enemy_list.remove(enemy_list.sprites()[i])
            if pygame.sprite.collide_rect(self, CoinObject):
                CoinObject.update()
                Bullets.remove(self)
                global coins
                coins += coinadd

    # Bullet1 object
    class Bullet2(pygame.sprite.Sprite):
        # Bullet
        def __init__(self):
            pygame.sprite.Sprite.__init__(self)
            self.image = Images.bulletpic
            self.rect = self.image.get_rect()
            self.rect.center = fighter.rect.center
            self.speed = deltatime * 800
            distance = math.sqrt(math.pow(pygame.mouse.get_pos()[0] - fighter.rect.centerx, 2) + math.pow(
                pygame.mouse.get_pos()[1] - fighter.rect.centery, 2))
            dist = int(distance * math.tan(math.radians(30)) / 2)
            mouse_x, mouse_y = (pygame.mouse.get_pos()[0] - dist, pygame.mouse.get_pos()[1] - dist)
            bullet_vec_x = mouse_x - fighter.rect.center[0]
            bullet_vec_y = mouse_y - fighter.rect.center[1]
            vec_length = math.sqrt(bullet_vec_x ** 2 + bullet_vec_y ** 2)
            bullet_vec_x = (bullet_vec_x / vec_length) * self.speed  # the five is speed
            bullet_vec_y = (bullet_vec_y / vec_length) * self.speed
            self.change_x = 0
            self.change_y = 0
            self.change_x += bullet_vec_x
            self.change_y += bullet_vec_y
            self.pos_x = fighter.rect.center[0]
            self.pos_y = fighter.rect.center[1]
            self.damage = 50
            self.shootcounter = 2
            self.counter = 0
            self.nextbullet = 0
            self.ammountfornextbullet = 500

        def update(self):
            self.nextbullet += 1
            if self.rect.x < -10 or self.rect.x > WIDTH + 10 or self.rect.y < -10 or self.rect.y > HEIGHT + 10:
                Bullets.remove(self)

            self.counter += 1
            if self.shootcounter < self.counter:
                self.counter = 0

                self.pos_x += self.change_x
                self.pos_y += self.change_y

                self.rect.x = self.pos_x
                self.rect.y = self.pos_y

            for i in range(len(enemy_list)):
                if pygame.sprite.collide_rect(self, enemy_list.sprites()[i]):
                    Bullets.remove(self)
                    enemy_list.sprites()[i].heal -= self.damage
                    if enemy_list.sprites()[i].heal <= 0:
                        fighter.xp += fighter.xpadd
                        fighter.kills += 1
                        enemy_list.remove(enemy_list.sprites()[i])
            if pygame.sprite.collide_rect(self, CoinObject):
                CoinObject.update()
                Bullets.remove(self)
                global coins
                coins += coinadd

    # Bullet1 object
    class Bullet3(pygame.sprite.Sprite):
        # Bullet
        def __init__(self):
            pygame.sprite.Sprite.__init__(self)
            self.image = Images.bulletpic
            self.rect = self.image.get_rect()
            self.rect.center = fighter.rect.center
            self.speed = deltatime * 800
            distance = math.sqrt(math.pow(pygame.mouse.get_pos()[0] - fighter.rect.centerx, 2) + math.pow(
                pygame.mouse.get_pos()[1] - fighter.rect.centery, 2))
            dist = int(distance * math.tan(math.radians(30)) / 2)
            mouse_x, mouse_y = (pygame.mouse.get_pos()[0] + dist, pygame.mouse.get_pos()[1] + dist)
            bullet_vec_x = mouse_x - fighter.rect.center[0]
            bullet_vec_y = mouse_y - fighter.rect.center[1]
            vec_length = math.sqrt(bullet_vec_x ** 2 + bullet_vec_y ** 2)
            bullet_vec_x = (bullet_vec_x / vec_length) * self.speed  # the five is speed
            bullet_vec_y = (bullet_vec_y / vec_length) * self.speed
            self.change_x = 0
            self.change_y = 0
            self.change_x += bullet_vec_x
            self.change_y += bullet_vec_y
            self.pos_x = fighter.rect.center[0]
            self.pos_y = fighter.rect.center[1]
            self.damage = 50
            self.shootcounter = 2
            self.counter = 0
            self.nextbullet = 0
            self.ammountfornextbullet = 500

        def update(self):
            self.nextbullet += 1
            if self.rect.x < -10 or self.rect.x > WIDTH + 10 or self.rect.y < -10 or self.rect.y > HEIGHT + 10:
                Bullets.remove(self)

            self.counter += 1
            if self.shootcounter < self.counter:
                self.counter = 0

                self.pos_x += self.change_x
                self.pos_y += self.change_y

                self.rect.x = self.pos_x
                self.rect.y = self.pos_y

            for i in range(len(enemy_list)):
                if pygame.sprite.collide_rect(self, enemy_list.sprites()[i]):
                    Bullets.remove(self)
                    enemy_list.sprites()[i].heal -= self.damage
                    if enemy_list.sprites()[i].heal <= 0:
                        fighter.xp += fighter.xpadd
                        fighter.kills += 1
                        enemy_list.remove(enemy_list.sprites()[i])
            if pygame.sprite.collide_rect(self, CoinObject):
                CoinObject.update()
                Bullets.remove(self)
                global coins
                coins += coinadd

    class Shop(pygame.sprite.Sprite):
        def __init__(self):
            pygame.sprite.Sprite.__init__(self)
            Colt_1911.__init__(self)
            self.image = Images.Ithaca_37_shop_selector_img
            self.rect = self.image.get_rect()
            self.rect.topleft = (800, 125)
            self.cost = 4000

        def info(self):
            basicfont4 = pygame.font.Font(words, 24)  # This code displays letters onto the screen
            text4 = basicfont4.render("Cost: " + str(self.cost) + "$", True, GREEN)
            textrect4 = text4.get_rect()
            textrect4.center = (400, 45)
            screen2.blit(text4, textrect4)

            text4 = basicfont4.render("Ithaca 37", True, WHITE)
            textrect4 = text4.get_rect()
            textrect4.topleft = (12.5, 30)
            screen2.blit(text4, textrect4)

            # Clip:
            basicfont4 = pygame.font.Font(words, 24)  # This code displays letters onto the screen
            text4 = basicfont4.render("Clip", True, WHITE)
            textrect4 = text4.get_rect()
            textrect4.topleft = (300, 260)
            screen2.blit(text4, textrect4)

            text4 = basicfont4.render(str(Ithaca.permclip), True, WHITE)
            textrect4 = text4.get_rect()
            textrect4.topleft = (320, 280)
            screen2.blit(text4, textrect4)

            # Ammo:
            basicfont4 = pygame.font.Font(words, 24)  # This code displays letters onto the screen
            text4 = basicfont4.render("Ammo", True, WHITE)
            textrect4 = text4.get_rect()
            textrect4.topleft = (500, 260)
            screen2.blit(text4, textrect4)

            text4 = basicfont4.render(str(Ithaca.ammountofbullets), True, WHITE)
            textrect4 = text4.get_rect()
            textrect4.center = (545, 300)
            screen2.blit(text4, textrect4)

            text4 = basicfont4.render(str(Ithaca.bulletcost) + "$", True, WHITE)
            textrect4 = text4.get_rect()
            textrect4.center = (545, 425)
            screen2.blit(text4, textrect4)

            # Stats:
            basicfont4 = pygame.font.Font(words, 36)  # This code displays letters onto the screen
            text4 = basicfont4.render("Stats:", True, RED)
            textrect4 = text4.get_rect()
            textrect4.topleft = (12.5, 260)
            screen2.blit(text4, textrect4)

            basicfont4 = pygame.font.Font(words, 18)  # This code displays letters onto the screen
            text4 = basicfont4.render("Damage: " + str(Ithaca.Bullet1().damage), True, RED)
            textrect4 = text4.get_rect()
            textrect4.topleft = (12.5, 310)
            screen2.blit(text4, textrect4)

            basicfont4 = pygame.font.Font(words, 18)  # This code displays letters onto the screen
            text4 = basicfont4.render("Fire Rate: " + str(Ithaca.Bullet1().firerate), True, RED)
            textrect4 = text4.get_rect()
            textrect4.topleft = (12.5, 340)
            screen2.blit(text4, textrect4)

            basicfont4 = pygame.font.Font(words, 18)  # This code displays letters onto the screen
            text4 = basicfont4.render("Reload Speed: " + str(Ithaca.Bullet1().reloadspeed), True, RED)
            textrect4 = text4.get_rect()
            textrect4.topleft = (12.5, 370)
            screen2.blit(text4, textrect4)

            basicfont4 = pygame.font.Font(words, 18)  # This code displays letters onto the screen
            text4 = basicfont4.render("Range: " + "Coming Soon!", True, RED)
            textrect4 = text4.get_rect()
            textrect4.topleft = (12.5, 400)
            screen2.blit(text4, textrect4)

            basicfont4 = pygame.font.Font(words, 18)  # This code displays letters onto the screen
            text4 = basicfont4.render("Accuracy: " + "Coming Soon!", True, RED)
            textrect4 = text4.get_rect()
            textrect4.topleft = (12.5, 430)
            screen2.blit(text4, textrect4)

            basicfont4 = pygame.font.Font(words, 18)  # This code displays letters onto the screen
            text4 = basicfont4.render("Mobility: " + "Coming Soon!", True, RED)
            textrect4 = text4.get_rect()
            textrect4.topleft = (12.5, 460)
            screen2.blit(text4, textrect4)

        class Shop_Layout(pygame.sprite.Sprite):
            def __init__(self):
                pygame.sprite.Sprite.__init__(self)
                self.image = Images.shop_format_img
                self.rect = self.image.get_rect()
                self.rect.topleft = (0, 25)
                self.cost = 100

        class gun_img(pygame.sprite.Sprite):
            def __init__(self):
                pygame.sprite.Sprite.__init__(self)
                self.image = Images.A5_shop_img
                self.rect = self.image.get_rect()
                self.rect.topleft = (75, 75)
                self.cost = 100

        class buy(pygame.sprite.Sprite):
            def __init__(self):
                pygame.sprite.Sprite.__init__(self)
                self.image = Images.buypic
                self.rect = self.image.get_rect()
                self.rect.topright = (789, 35)
                self.cost = 4000

        class equip(pygame.sprite.Sprite):
            def __init__(self):
                pygame.sprite.Sprite.__init__(self)
                self.image = Images.equip_pic
                self.rect = self.image.get_rect()
                self.rect.topright = (789, 35)
                self.cost = 100

        class equiped(pygame.sprite.Sprite):
            def __init__(self):
                pygame.sprite.Sprite.__init__(self)
                self.image = Images.equiped_pic
                self.rect = self.image.get_rect()
                self.rect.topright = (789, 35)
                self.cost = 100

        class Bullet_Shop(pygame.sprite.Sprite):
            def __init__(self):
                pygame.sprite.Sprite.__init__(self)
                self.image = Images.buy_ammo_img
                self.rect = self.image.get_rect()
                self.rect.center = (545, 475)
                self.cost = 200

# Fighter Object
class Fighter(pygame.sprite.Sprite):
    # Fighter that moves around
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = Images.fighter_img
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 3, HEIGHT / 3)
        self.orig_image = self.image  # Store a reference to the original.
        self.rect = self.image.get_rect(center=self.rect.center)
        self.pos = Vector2(self.rect.center)

        self.size = 26
        self.heal = 100
        self.startinghealth = 100

        self.xp = 0
        self.rank = oldrank
        self.rankxp = 100
        self.xpadd = 10
        with open(names_text) as f:
            for line in f:
                (name, oldkills, password, rank) = line.split()
                list_of_names[str(name)] = [oldkills, password, rank]
        f.close()
        oldkills = int(list_of_names[login_line.word][0])

        self.kills = int(oldkills)

    def update(self):
        mouse_x, mouse_y = pygame.mouse.get_pos()
        rel_x, rel_y = mouse_x - self.rect.centerx, mouse_y - self.rect.centery
        angle = (180 / math.pi) * -math.atan2(rel_y, rel_x)
        # Rotate the image by the negative angle (y-axis in pygame is flipped).
        self.image = pygame.transform.rotate(self.orig_image, (angle - 90))
        # Create a new rect with the center of the old rect.
        self.rect = self.image.get_rect(center=self.rect.center)

    def health(self):
        if self.heal <= 0:
            global gameExit
            gameExit = True
            Globals.scene = "Gameover"
            oldkills = fighter.kills
        if self.heal >= 0:
            screen.blit(F_health(math.floor((self.heal / self.startinghealth) * 100)), (98, 0))

    def stats(self):
        screen.blit(Images.face1_img, [0, 0])

        basicfont4 = pygame.font.Font(words, 10)  # This code displays letters onto the screen
        text4 = basicfont4.render("Rank: " + str(self.rank), True, Color.Orange)
        textrect4 = text4.get_rect()
        textrect4.topleft = (98, 10)
        screen.blit(text4, textrect4)

        text4 = basicfont4.render("Coins: " + str(coins), True, Color.Gold)
        textrect4 = text4.get_rect()
        textrect4.topleft = (95, 25)
        screen.blit(text4, textrect4)

        text4 = basicfont4.render("Kills: " + str(self.kills), True, Color.OrangeRed)
        textrect4 = text4.get_rect()
        textrect4.topleft = (90, 40)
        screen.blit(text4, textrect4)

        basicfont4 = pygame.font.Font(words, 30)  # This code displays letters onto the screen
        text4 = basicfont4.render(str(login_line.word), True, Color.WhiteSmoke)
        textrect4 = text4.get_rect()
        textrect4.topleft = (0, 95)
        screen.blit(text4, textrect4)

    def Xp(self):
        global oldrank
        if self.xp >= self.rankxp:
            self.xp = self.xp - self.rankxp
            self.rankxp = math.floor(self.rankxp * 1.05)
            self.rank += 1
            oldrank = self.rank
        screen.blit(XP_bar(math.floor((self.xp / self.rankxp) * 100)), (-12, HEIGHT - 5))

        basicfont4 = pygame.font.Font(words, 10)  # This code displays letters onto the screen
        text4 = basicfont4.render(str(self.xp) + "/" + str(self.rankxp), True, GREEN)
        textrect4 = text4.get_rect()
        textrect4.bottomright = (1250, 623)
        screen.blit(text4, textrect4)

    def up(self):
        if self.rect.midtop[1] > 0:
            self.rect.y -= deltatime * 300

    def down(self):
        if self.rect.midbottom[1] < HEIGHT:
            self.rect.y += deltatime * 300

    def left(self):
        if self.rect.midleft[0] > 0:
            self.rect.x -= deltatime * 300

    def right(self):
        if self.rect.midright[0] < WIDTH:
            self.rect.x += deltatime * 300


def show_fps():
    fps_font = pygame.font.Font(words, 10)
    fps_overlay = fps_font.render("FPS: " + str(FPS), True, BLACK)
    screen.blit(fps_overlay, (85, 55))


def count_fps():
    global FPS
    global deltatime
    FPS = clock.get_fps()
    if FPS > 0:
        deltatime = 1 / FPS


def get_angle(origin, destination):
    """Returns angle in radians from origin to destination.
       This is the angle that you would get if the points were
       on a cartesian grid. Arguments of (0,0), (1, -1)
       return pi/4 (45 deg) rather than  7/4.
       """
    x_dist = destination[0] - origin[0]
    y_dist = destination[1] - origin[1]
    return math.atan2(-y_dist, x_dist) % (2 * math.pi)


def project(pos, angle, distance):
    """
   Returns tuple of pos projected distance at angle
   adjusted for pygame's y-axis.

   EXAMPLES

   Move a sprite using it's angle and speed
   new_pos = project(sprite.pos, sprite.angle, sprite.speed)

   Find the relative x and y components of an angle and speed
   x_and_y = project((0, 0), angle, speed)
   """
    return (pos[0] + (math.cos(angle) * distance),
            pos[1] - (math.sin(angle) * distance))


# Enemy Object
class Easy_Enemy(pygame.sprite.Sprite):
    # Enemy Zombie that moves around
    def __init__(self, enemy_x, enemy_y):  # These are its features
        pygame.sprite.Sprite.__init__(self)
        self.image = Images.zombie_img
        self.rect = self.image.get_rect()
        self.rect.center = (enemy_x, enemy_y)
        self.speed = 0.05

        self.orig_image = self.image  # Store a reference to the original.
        self.rect = self.image.get_rect(center=self.rect.center)
        self.pos = Vector2(self.rect.center)

        self.startinghealth = 100
        self.heal = 100
        self.damage = 1

        self.pos = self.rect.center

    def update(self):
        mouse_x, mouse_y = fighter.rect.center
        rel_x, rel_y = mouse_x - self.rect.centerx, mouse_y - self.rect.centery
        angle = (180 / math.pi) * -math.atan2(rel_y, rel_x)
        # Rotate the image by the negative angle (y-axis in pygame is flipped).
        self.image = pygame.transform.rotate(self.orig_image, (angle - 90))
        # Create a new rect with the center of the old rect.
        self.rect = self.image.get_rect(center=self.rect.center)

        angle = get_angle(self.rect.center, fighter.rect.center)
        self.pos = project(self.pos, angle, self.speed * 30)
        self.rect.center = self.pos
        if pygame.sprite.collide_rect(self, fighter):
            fighter.heal -= self.damage

    def health(self):
        screen.blit(Health(math.floor((self.heal / self.startinghealth) * 100)),
                    (self.rect.centerx - 25, self.rect.centery - 35))


# Coin Object
class Coin_Object(pygame.sprite.Sprite):
    def __init__(self):
        coin_random_x = random.randint(20, WIDTH - 20)
        coin_random_y = random.randint(20, HEIGHT - 20)
        pygame.sprite.Sprite.__init__(self)

        self.image = Images.gcoin
        self.rect = self.image.get_rect()
        self.rect.center = (coin_random_x, coin_random_y)

    def update(self):
        coin_random_x = random.randint(20, WIDTH - 20)
        coin_random_y = random.randint(20, HEIGHT - 20)
        self.rect.center = (coin_random_x, coin_random_y)


# Shop Object
class Shop_Pistols(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = Images.shop_pistols_img
        self.rect = self.image.get_rect()
        self.rect.center = (100, 12.5)
        self.name = "pistols"


class Shop_Automatics(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = Images.shop_automatics_img
        self.rect = self.image.get_rect()
        self.rect.center = (300, 12.5)
        self.name = "automatics"


class Shop_Snipers(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = Images.shop_snipers_img
        self.rect = self.image.get_rect()
        self.rect.center = (500, 12.5)
        self.name = "snipers"


class Shop_Shotguns(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = Images.shop_shotguns_img
        self.rect = self.image.get_rect()
        self.rect.center = (700, 12.5)
        self.name = "shotguns"


class Shop_Ranks(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = Images.shop_ranks_img
        self.rect = self.image.get_rect()
        self.rect.center = (900, 12.5)
        self.name = "ranks"


# This object is for controls
class Controls(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        Controlstemp = pygame.image.load(os.path.abspath("resources//images//Controls.png"))
        Controlstemp = pygame.transform.scale(Controlstemp, (100, 100))
        Controls = pygame.Surface(Controlstemp.get_size(), pygame.HWSURFACE)
        Controls.blit(Controlstemp, (0, 0))
        del Controlstemp

        self.image = Controls
        self.rect = self.image.get_rect()
        self.rect.center = (800, 325)


# This object is for controls
class SControls(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        SControlstemp = pygame.image.load(os.path.abspath("resources//images//SControls.png"))
        SControlstemp = pygame.transform.scale(SControlstemp, (100, 100))
        SControls = pygame.Surface(SControlstemp.get_size(), pygame.HWSURFACE)
        SControls.blit(SControlstemp, (0, 0))
        del SControlstemp

        self.image = SControls
        self.rect = self.image.get_rect()
        self.rect.center = (500, 325)


# Buttons
class Button_login(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = Images.login_button_img
        self.rect = self.image.get_rect()
        self.rect.center = (625, 300)


class Button_exit(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = Images.exit_button_img
        self.rect = self.image.get_rect()
        self.rect.center = (625, 400)


class Button_play(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = Images.play_button_img
        self.rect = self.image.get_rect()
        self.rect.center = (625, 200)
        self.cost = 100
        self.play = False


class Button_signup(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = Images.sign_up_img
        self.rect = self.image.get_rect()
        self.rect.center = (625, 500)


class Button_control(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = Images.controls_button_img
        self.rect = self.image.get_rect()
        self.rect.center = (625, 300)


class Button_back(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = Images.back_button_img
        self.rect = self.image.get_rect()
        self.rect.bottomleft = (0, HEIGHT)


class Login_line(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = Images.blank_line_img
        self.rect = self.image.get_rect()
        self.rect.center = (625, 200)

        self.collide = False
        self.word = ""

    def update(self):
        basicfont4 = pygame.font.Font(words, 30)  # This code displays letters onto the screen
        text4 = basicfont4.render(self.word, True, BLACK)
        textrect4 = text4.get_rect()
        textrect4.midleft = (435, 200)
        screen.blit(text4, textrect4)


class Password_line(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = Images.blank_line_img
        self.rect = self.image.get_rect()
        self.rect.center = (625, 400)

        self.collide = False
        self.word = ""

    def update(self):
        basicfont4 = pygame.font.Font(words, 30)  # This code displays letters onto the screen
        text4 = basicfont4.render(self.word, True, BLACK)
        textrect4 = text4.get_rect()
        textrect4.midleft = (435, 400)
        screen.blit(text4, textrect4)


def Password_check(user, pword):
    list_of_names = {}
    with open(names_text) as f:
        for line in f:
            (name, oldkills, password, rank) = line.split()
            list_of_names[str(name)] = [oldkills, password, rank]
    f.close()

    if list_of_names[user][1] == pword:
        global oldrank
        oldrank = int(list_of_names[user][2])
        Globals.start = True
        return True
    else:
        return False


def Sign_up(user, pword):
    list_of_names = {}
    with open(names_text) as f:
        for line in f:
            (name, oldkills, password, rank) = line.split()
            list_of_names[str(name)] = [oldkills, password, rank]
    f.close()

    if not (user in list_of_names):
        f = open(names_text, "r")
        lines = f.readlines()
        f.close()
        s = open(names_text, "w")
        for line in lines:
            if line != (user + " " + "0 " + pword + " 1"):
                s.write(line)
        s.close()

        t = open(names_text, 'a')
        t.write("\n" + str(user) + " " + "0 " + str(pword) + " 1")
        t.close()

        for line in fileinput.FileInput(names_text, inplace=1):
            if line.rstrip():
                print(line, end='')

        return True

    else:
        return False


# My level algorith that creates levels for me
def levels(x):
    global enemy_death_count
    enemy_death_count = 0
    global enemy_y
    global enemy_x
    global continue_level
    global enemy_list
    continue_level = 0
    for i in range(x):  # random places to put the zombies
        side = random.randint(1, 4)
        if side == 1:  # Top
            enemy_y = -10
            enemy_x = random.randint(10, WIDTH - 10)
        if side == 2:  # Bottom
            enemy_y = 635
            enemy_x = random.randint(10, WIDTH - 10)
        if side == 3:  # Left
            enemy_y = random.randint(0, HEIGHT - 10)
            enemy_x = -10
        if side == 4:  # Right
            enemy_y = random.randint(0, HEIGHT - 10)
            enemy_x = 1260
        enemy = Easy_Enemy(enemy_x, enemy_y)
        enemy_list.add(enemy)
    global start_level
    start_level = 1


def gameLoop():  # The start of the whole game
    # Global Initiation
    global shop_background_img
    global movement_counter
    global swait
    global shoot_counter
    global enemy_counter
    global enemy_x
    global enemy_y
    global start_level
    global level
    global total_level
    global name
    global left_key
    global right_key
    global enemy_list
    global bullet
    global shop
    global move_timer
    global bullet_timer
    global bullet_speed
    global coins
    global movement
    global speed
    global move
    global wait
    global extra_bullet_object
    global Extra_Bullet
    global movement_speed
    global Bullets
    global AllCoins
    global coin_timer
    global coin_timer_counter
    global coin_delay
    global coin_ammount
    global coin_delay_counter
    global coin_spawn
    global how_many_coinspeed
    global how_many_coindelay
    global coinadd
    global coinadd_counter
    global oldrank
    global start
    global CoinObject
    global coins
    global gcoin
    global enemy_counter
    global fighter
    global automatic_bullets
    global sniper_bullets
    global Equiped_Gun
    global automatic
    global sniper
    global colt
    global reload
    global screen2
    global Gun_List
    global Shop_Sprites
    global clock
    global screen
    global shopscreen
    global bhp
    global m97
    global K98K
    global MG30
    global volkssturmgewehr
    global gameExit
    global deltatime
    global login_line
    global password_line
    global oldkills
    global mauser
    global spz
    global zh29
    global puska
    global a5
    global Ithaca

    # Pygame Setup
    pygame.init()
    pygame.mixer.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.HWSURFACE | pygame.DOUBLEBUF)  # Sets the screen size
    pygame.display.set_caption("Ginza Arcade")  # sets the caption
    clock = pygame.time.Clock()

    # All starting values
    clock = pygame.time.Clock()
    reload = False
    movement_counter = 0
    swait = 0
    shoot_counter = 0
    start = False
    coin_timer_counter = 0
    coin_delayer = 1000
    coin_delay_counter = 0
    name = ""
    coin_timer = 1000
    coins = 1000000
    coinadd = 5
    coinadd_counter = 0
    how_many_coinspeed = 0
    how_many_coindelay = 0
    wait = 0
    speed = 0
    move = 0
    total_level = 10
    movement = 1
    bullet_timer = 0
    bullet_speed = 50
    move_timer = 0
    shop = False
    gameExit = False
    left_key = 0
    right_key = 0
    enemy_counter = 0
    enemy_x = 20
    enemy_y = 20
    start_level = 0
    level = 10
    shopscreen = "pistols"
    deltatime = 0.02

    # Button Initialization
    Menu_List = pygame.sprite.Group()
    Login_List = pygame.sprite.Group()
    Control_List = pygame.sprite.Group()
    play = Button_play()
    exitb = Button_exit()
    login = Button_login()
    signup = Button_signup()
    controls = Button_control()
    login_line = Login_line()
    password_line = Password_line()
    back = Button_back()

    Menu_List.add(play)
    Menu_List.add(exitb)
    Menu_List.add(controls)
    Login_List.add(back)
    Login_List.add(login)
    Login_List.add(signup)
    Login_List.add(login_line)
    Login_List.add(password_line)

    ccontrols = Controls()
    scontrols = SControls()
    Control_List.add(back)
    Control_List.add(ccontrols)
    Control_List.add(scontrols)

    pygame.init()
    pygame.mixer.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.HWSURFACE | pygame.DOUBLEBUF)
    pygame.display.set_caption("Ginza Arcade")
    clock = pygame.time.Clock()

    word_length = 0
    wait1 = 0
    wait2 = 0
    wait3 = 0
    wait4 = 0

    while Globals.start == False:
        if Globals.scene == "Menu":
            if play.play == False:
                screen.blit(Images.menu_img, (0, 0))

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:  # If you click on the X on the screen it asks if you want to close the game
                        gameExit = True
                        Globals.scene = "Gameover"
                        Globals.quit = True
                        pygame.quit()
                        exit()

                    if event.type == pygame.MOUSEBUTTONUP:
                        pos = pygame.mouse.get_pos()
                        if play.rect.collidepoint(pos):
                            play.play = False
                            Globals.scene = "Login"
                        if exitb.rect.collidepoint(pos):
                            gameExit = True
                            Globals.scene = "Gameover"
                            Globals.quit = True
                            pygame.quit()
                            exit()
                        if controls.rect.collidepoint(pos):
                            Globals.scene = "Controls"
                Menu_List.draw(screen)
                pygame.display.update()

        if Globals.scene == "Controls":
            for event in pygame.event.get():
                if event.type == pygame.QUIT:  # If you click on the X on the screen it asks if you want to close the game
                    gameExit = True
                    Globals.scene = "Gameover"
                    Globals.quit = True
                    pygame.quit()
                    exit()
                if event.type == pygame.MOUSEBUTTONUP:
                    pos = pygame.mouse.get_pos()
                    if back.rect.collidepoint(pos):
                        Globals.scene = "Menu"

            screen.blit(Images.menu_img, [0, 0])

            Control_List.draw(screen)
            pygame.display.update()

        if Globals.scene == "Login":
            for event in pygame.event.get():
                if event.type == pygame.QUIT:  # If you click on the X on the screen it asks if you want to close the game
                    gameExit = True
                    Globals.scene = "Gameover"
                    Globals.quit = True
                    pygame.quit()
                    exit()
                if event.type == pygame.MOUSEBUTTONUP:
                    pos = pygame.mouse.get_pos()
                    if back.rect.collidepoint(pos):
                        Globals.scene = "Menu"
                    if login.rect.collidepoint(pos):
                        list_of_names = {}
                        with open(names_text) as f:
                            for line in f:
                                (name, kills, password, rank) = line.split()
                                list_of_names[str(name)] = [kills, password, rank]
                        f.close()

                        if login_line.word in list_of_names:
                            if Password_check(login_line.word, password_line.word):
                                Globals.scene = "Game"
                            else:
                                wait1 = 100
                        else:
                            wait4 = 100
                    if signup.rect.collidepoint(pos):
                        if Sign_up(login_line.word, password_line.word):
                            wait2 = 100
                        else:
                            wait3 = 100
                    if login_line.rect.collidepoint(pos):
                        login_line.collide = True
                        password_line.collide = False
                        word_length = len(login_line.word)

                    if password_line.rect.collidepoint(pos):
                        password_line.collide = True
                        login_line.collide = False
                        word_length = len(password_line.word)

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_KP_ENTER:  # If you click enter it jumps to the game if theres no one in the list that has that name
                        list_of_names = {}
                        with open(names_text) as f:
                            for line in f:
                                (name, kills, password, rank) = line.split()
                                list_of_names[str(name)] = [kills, password, rank]
                        f.close()

                        if login_line.word in list_of_names:
                            if Password_check(login_line.word, password_line.word):
                                Globals.scene = "Game"
                            else:
                                wait1 = 100
                        else:
                            wait4 = 100
                    if word_length < 25:
                        if event.key == pygame.K_a:
                            if login_line.collide == True:
                                login_line.word += "A"
                            if password_line.collide == True:
                                password_line.word += "A"
                            word_length += 1
                        if event.key == pygame.K_b:
                            if login_line.collide == True:
                                login_line.word += "B"
                            if password_line.collide == True:
                                password_line.word += "B"
                            word_length += 1
                        if event.key == pygame.K_c:
                            if login_line.collide == True:
                                login_line.word += "C"
                            if password_line.collide == True:
                                password_line.word += "C"
                            word_length += 1
                        if event.key == pygame.K_d:
                            if login_line.collide == True:
                                login_line.word += "D"
                            if password_line.collide == True:
                                password_line.word += "D"
                            word_length += 1
                        if event.key == pygame.K_e:
                            if login_line.collide == True:
                                login_line.word += "E"
                            if password_line.collide == True:
                                password_line.word += "E"
                            word_length += 1
                        if event.key == pygame.K_f:
                            if login_line.collide == True:
                                login_line.word += "F"
                            if password_line.collide == True:
                                password_line.word += "F"
                            word_length += 1
                        if event.key == pygame.K_g:
                            if login_line.collide == True:
                                login_line.word += "G"
                            if password_line.collide == True:
                                password_line.word += "G"
                            word_length += 1
                        if event.key == pygame.K_h:
                            if login_line.collide == True:
                                login_line.word += "H"
                            if password_line.collide == True:
                                password_line.word += "H"
                            word_length += 1
                        if event.key == pygame.K_i:
                            if login_line.collide == True:
                                login_line.word += "I"
                            if password_line.collide == True:
                                password_line.word += "I"
                            word_length += 1
                        if event.key == pygame.K_j:
                            word_length += 1
                            if login_line.collide == True:
                                login_line.word += "J"
                            if password_line.collide == True:
                                password_line.word += "J"
                        if event.key == pygame.K_k:
                            word_length += 1
                            if login_line.collide == True:
                                login_line.word += "K"
                            if password_line.collide == True:
                                password_line.word += "K"
                        if event.key == pygame.K_l:
                            word_length += 1
                            if login_line.collide == True:
                                login_line.word += "L"
                            if password_line.collide == True:
                                password_line.word += "L"
                        if event.key == pygame.K_m:
                            word_length += 1
                            if login_line.collide == True:
                                login_line.word += "M"
                            if password_line.collide == True:
                                password_line.word += "M"
                        if event.key == pygame.K_n:
                            word_length += 1
                            if login_line.collide == True:
                                login_line.word += "N"
                            if password_line.collide == True:
                                password_line.word += "N"
                        if event.key == pygame.K_o:
                            word_length += 1
                            if login_line.collide == True:
                                login_line.word += "O"
                            if password_line.collide == True:
                                password_line.word += "O"
                        if event.key == pygame.K_p:
                            word_length += 1
                            if login_line.collide == True:
                                login_line.word += "P"
                            if password_line.collide == True:
                                password_line.word += "P"
                        if event.key == pygame.K_q:
                            word_length += 1
                            if login_line.collide == True:
                                login_line.word += "Q"
                            if password_line.collide == True:
                                password_line.word += "Q"
                        if event.key == pygame.K_r:
                            word_length += 1
                            if login_line.collide == True:
                                login_line.word += "R"
                            if password_line.collide == True:
                                password_line.word += "R"
                        if event.key == pygame.K_s:
                            word_length += 1
                            if login_line.collide == True:
                                login_line.word += "S"
                            if password_line.collide == True:
                                password_line.word += "S"
                        if event.key == pygame.K_t:
                            word_length += 1
                            if login_line.collide == True:
                                login_line.word += "T"
                            if password_line.collide == True:
                                password_line.word += "T"
                        if event.key == pygame.K_u:
                            word_length += 1
                            if login_line.collide == True:
                                login_line.word += "U"
                            if password_line.collide == True:
                                password_line.word += "U"
                        if event.key == pygame.K_v:
                            word_length += 1
                            if login_line.collide == True:
                                login_line.word += "V"
                            if password_line.collide == True:
                                password_line.word += "V"
                        if event.key == pygame.K_w:
                            word_length += 1
                            if login_line.collide == True:
                                login_line.word += "W"
                            if password_line.collide == True:
                                password_line.word += "W"
                        if event.key == pygame.K_x:
                            word_length += 1
                            if login_line.collide == True:
                                login_line.word += "X"
                            if password_line.collide == True:
                                password_line.word += "X"
                        if event.key == pygame.K_y:
                            word_length += 1
                            if login_line.collide == True:
                                login_line.word += "Y"
                            if password_line.collide == True:
                                password_line.word += "Y"
                        if event.key == pygame.K_z:
                            word_length += 1
                            if login_line.collide == True:
                                login_line.word += "Z"
                            if password_line.collide == True:
                                password_line.word += "Z"
                        if event.key == pygame.K_SPACE:
                            word_length += 1
                            if login_line.collide == True:
                                login_line.word += " "
                            if password_line.collide == True:
                                password_line.word += " "
                    if word_length > 0:
                        if event.key == pygame.K_BACKSPACE:  # if you click backspace it gets rid of a letter in name
                            word_length -= 1
                            if login_line.collide == True:
                                temp = login_line.word
                                temp = list(temp)
                                del temp[-1]
                                temp = ''.join(temp)
                                login_line.word = temp

                            if password_line.collide == True:
                                temp = password_line.word
                                temp = list(temp)
                                del temp[-1]
                                temp = ''.join(temp)
                                password_line.word = temp

            screen.blit(Images.menu_img, [0, 0])

            Login_List.draw(screen)
            login_line.update()
            password_line.update()

            if wait1 > 0:
                wait1 -= 1
                basicfont4 = pygame.font.Font(words, 30)  # This code displays letters onto the screen
                text4 = basicfont4.render("Wrong Password Try Again", True, BLACK)
                textrect4 = text4.get_rect()
                textrect4.midbottom = (WIDTH / 2, HEIGHT)
                screen.blit(text4, textrect4)

            if wait2 > 0:
                wait2 -= 1
                basicfont4 = pygame.font.Font(words, 30)  # This code displays letters onto the screen
                text4 = basicfont4.render("You can now log in!!", True, BLACK)
                textrect4 = text4.get_rect()
                textrect4.midbottom = (WIDTH / 2, HEIGHT)
                screen.blit(text4, textrect4)

            if wait3 > 0:
                wait3 -= 1
                basicfont4 = pygame.font.Font(words, 30)  # This code displays letters onto the screen
                text4 = basicfont4.render("Sorry someone already has that username", True, BLACK)
                textrect4 = text4.get_rect()
                textrect4.midbottom = (WIDTH / 2, HEIGHT)
                screen.blit(text4, textrect4)

            if wait4 > 0:
                wait4 -= 1
                basicfont4 = pygame.font.Font(words, 30)  # This code displays letters onto the screen
                text4 = basicfont4.render("That Username hasnt been registered, click sign up!", True, BLACK)
                textrect4 = text4.get_rect()
                textrect4.midbottom = (WIDTH / 2, HEIGHT)
                screen.blit(text4, textrect4)

            pygame.display.update()

    pygame.init()

    # Object Setup
    Equiped_Gun = pygame.sprite.Group()
    Main = pygame.sprite.Group()
    Bullets = pygame.sprite.Group()
    enemy_list = pygame.sprite.Group()
    AllCoins = pygame.sprite.Group()
    Gun_List = pygame.sprite.Group()
    CoinObject = Coin_Object()
    AllCoins.add(CoinObject)
    Pistol_List = pygame.sprite.Group()
    AutoMatic_List = pygame.sprite.Group()
    Sniper_List = pygame.sprite.Group()
    Shotgun_List = pygame.sprite.Group()
    Shop_Click = pygame.sprite.Group()
    Shop_Show = pygame.sprite.Group()
    Gun_Menu = pygame.sprite.Group()

    # all Guns:
    MG30 = MG_30()
    K98K = K98k()
    colt = Colt_1911()
    bhp = Browning_Hi_Power()
    m97 = M97()
    mauser = Mauser_C96()
    volkssturmgewehr = Volkssturmgewehr()
    spz = Spz()
    zh29 = ZH_29()
    puska = Puska()
    a5 = A5()
    Ithaca = Ithaca_37()

    # Putting all guns into a list
    Gun_List.add(MG30)
    Gun_List.add(K98K)
    Gun_List.add(colt)
    Gun_List.add(bhp)
    Gun_List.add(m97)
    Gun_List.add(mauser)
    Gun_List.add(volkssturmgewehr)
    Gun_List.add(spz)
    Gun_List.add(zh29)
    Gun_List.add(puska)
    Gun_List.add(a5)
    Gun_List.add(Ithaca)

    # Putting pistols in one sprite group
    Pistol_List.add(colt)
    Pistol_List.add(bhp)
    Pistol_List.add(mauser)

    # Automatic list
    AutoMatic_List.add(MG30)
    AutoMatic_List.add(volkssturmgewehr)
    AutoMatic_List.add(spz)

    # Sniper List
    Sniper_List.add(K98K)
    Sniper_List.add(zh29)
    Sniper_List.add(puska)

    # Shotgun List
    Shotgun_List.add(m97)
    Shotgun_List.add(a5)
    Shotgun_List.add(Ithaca)

    # Starting Gun
    Equiped_Gun.add(colt)

    fighter = Fighter()
    Main.add(fighter)
    start = True

    # Shop Click
    shop_pistols = Shop_Pistols()
    shop_automatics = Shop_Automatics()
    shop_snipers = Shop_Snipers()
    shop_shotguns = Shop_Shotguns()
    shop_ranks = Shop_Ranks()

    # add shop click
    Shop_Click.add(shop_pistols)
    Shop_Click.add(shop_automatics)
    Shop_Click.add(shop_shotguns)
    Shop_Click.add(shop_snipers)
    Shop_Click.add(shop_ranks)

    # Shop Sprites
    Shop_Sprites = pygame.sprite.Group()

    for i in range(len(Pistol_List.sprites())):
        Gun_Menu.add(Pistol_List.sprites()[i].Shop())

    Shop_Show.add(Pistol_List.sprites()[0])

    Shop_Sprites.add(Shop_Show.sprites()[0].Shop().Shop_Layout())
    Shop_Sprites.add(Shop_Show.sprites()[0].Shop().gun_img())
    Shop_Sprites.add(Equiped_Gun.sprites()[0].Shop().equiped())

    while not gameExit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # If you click on the X on the screen it asks if you want to close the game
                gameExit = True
                Globals.scene = "Gameover"

        clock.tick()
        count_fps()

        screen.blit(Images.game_background_img, [0, 0])

        show_fps()

        if Globals.scene == "Shop":  # This is the start of the shop code
            keystate = pygame.key.get_pressed()
            if keystate[pygame.K_p]:
                if swait > 5:
                    swait = 0
                    Globals.scene = "Game"
            swait += 1
            pygame.init()
            pygame.mixer.init()
            screen2 = pygame.display.set_mode((WIDTH, HEIGHT))
            pygame.display.set_caption("Ginza Arcade")

            screen2.blit(shop_background_img, [0, 0])
            basicfont4 = pygame.font.Font(words, 15)  # This code displays letters onto the screen

            for event in pygame.event.get():
                if event.type == pygame.QUIT:  # If you click on the X on the screen it asks if you want to close the game
                    gameExit = True
                    Globals.scene = "Gameover"
                if event.type == pygame.MOUSEBUTTONUP:
                    pos = pygame.mouse.get_pos()

                    for i in range(len(Shop_Click.sprites())):
                        if Shop_Click.sprites()[i].rect.collidepoint(pos):
                            shopscreen = Shop_Click.sprites()[i].name
                            Shop_Sprites = pygame.sprite.Group()

                            if shopscreen == "pistols":
                                Shop_Show.remove(Shop_Show.sprites()[0])
                                Shop_Show.add(Pistol_List.sprites()[0])
                            if shopscreen == "automatics":
                                Shop_Show.remove(Shop_Show.sprites()[0])
                                Shop_Show.add(AutoMatic_List.sprites()[0])
                            if shopscreen == "snipers":
                                Shop_Show.remove(Shop_Show.sprites()[0])
                                Shop_Show.add(Sniper_List.sprites()[0])
                            if shopscreen == "shotguns":
                                Shop_Show.remove(Shop_Show.sprites()[0])
                                Shop_Show.add(Shotgun_List.sprites()[0])
                            if shopscreen == "ranks":
                                Shop_Sprites = pygame.sprite.Group()
                                Gun_Menu = pygame.sprite.Group()

                    if shopscreen == "pistols":
                        for i in range(len(Pistol_List.sprites())):
                            if Pistol_List.sprites()[i].Shop().rect.collidepoint(pos):
                                Shop_Show.remove(Shop_Show.sprites()[0])
                                Shop_Show.add(Pistol_List.sprites()[i])

                    if shopscreen == "automatics":
                        for i in range(len(AutoMatic_List.sprites())):
                            if AutoMatic_List.sprites()[i].Shop().rect.collidepoint(pos):
                                Shop_Show.remove(Shop_Show.sprites()[0])
                                Shop_Show.add(AutoMatic_List.sprites()[i])

                    if shopscreen == "snipers":
                        for i in range(len(Sniper_List.sprites())):
                            if Sniper_List.sprites()[i].Shop().rect.collidepoint(pos):
                                Shop_Show.remove(Shop_Show.sprites()[0])
                                Shop_Show.add(Sniper_List.sprites()[i])

                    if shopscreen == "shotguns":
                        for i in range(len(Shotgun_List.sprites())):
                            if Shotgun_List.sprites()[i].Shop().rect.collidepoint(pos):
                                Shop_Show.remove(Shop_Show.sprites()[0])
                                Shop_Show.add(Shotgun_List.sprites()[i])

                    if shopscreen != "ranks":
                        if Shop_Show.sprites()[0].Shop().buy().rect.collidepoint(pos) and Shop_Show.sprites()[
                            0].bought == False:
                            if coins > Shop_Show.sprites()[0].Shop().buy().cost:
                                Equiped_Gun.remove(Equiped_Gun.sprites()[0])
                                Equiped_Gun.add(Shop_Show.sprites()[0])
                                Shop_Show.sprites()[0].bought = True
                                coins -= Shop_Show.sprites()[0].Shop().buy().cost
                            else:
                                wait = 1000

                        if Shop_Show.sprites()[0].Shop().equip().rect.collidepoint(pos):
                            Equiped_Gun.remove(Equiped_Gun.sprites()[0])
                            Equiped_Gun.add(Shop_Show.sprites()[0])
                            Shop_Show.remove(Shop_Show.sprites()[0].Shop().equip().rect.collidepoint(pos))
                            Shop_Sprites.add(Equiped_Gun.sprites()[0].Shop().equiped())

                        if Shop_Show.sprites()[0].Shop().Bullet_Shop().rect.collidepoint(pos):
                            if coins > Shop_Show.sprites()[0].bulletcost and Shop_Show.sprites()[0].bought == True:
                                coins -= Shop_Show.sprites()[0].bulletcost
                                Shop_Show.sprites()[0].bulletcost = math.floor(Shop_Show.sprites()[0].bulletcost * 1.05)
                                Shop_Show.sprites()[0].ammountofbullets += Shop_Show.sprites()[0].permclip
                            else:
                                wait = 1000

            if shopscreen == "pistols":
                Shop_Sprites = pygame.sprite.Group()
                Gun_Menu = pygame.sprite.Group()

                for i in range(len(Pistol_List.sprites())):
                    Gun_Menu.add(Pistol_List.sprites()[i].Shop())

                Shop_Sprites.add(Shop_Show.sprites()[0].Shop().Shop_Layout())

                Shop_Sprites.add(Shop_Show.sprites()[0].Shop().gun_img())

                Shop_Sprites.add(Shop_Show.sprites()[0].Shop().Bullet_Shop())

                if Shop_Show.sprites()[0].bought == False:
                    Shop_Sprites.add(Shop_Show.sprites()[0].Shop().buy())
                elif Shop_Show.sprites()[0] == Equiped_Gun.sprites()[0]:
                    Shop_Sprites.add(Equiped_Gun.sprites()[0].Shop().equiped())
                else:
                    Shop_Sprites.add(Shop_Show.sprites()[0].Shop().equip())

            if shopscreen == "automatics":
                Shop_Sprites = pygame.sprite.Group()
                Gun_Menu = pygame.sprite.Group()

                for i in range(len(AutoMatic_List.sprites())):
                    Gun_Menu.add(AutoMatic_List.sprites()[i].Shop())

                Shop_Sprites.add(Shop_Show.sprites()[0].Shop().Shop_Layout())

                Shop_Sprites.add(Shop_Show.sprites()[0].Shop().gun_img())

                Shop_Sprites.add(Shop_Show.sprites()[0].Shop().Bullet_Shop())

                if Shop_Show.sprites()[0].bought == False:
                    Shop_Sprites.add(Shop_Show.sprites()[0].Shop().buy())
                elif Shop_Show.sprites()[0] == Equiped_Gun.sprites()[0]:
                    Shop_Sprites.add(Equiped_Gun.sprites()[0].Shop().equiped())
                else:
                    Shop_Sprites.add(Shop_Show.sprites()[0].Shop().equip())

            if shopscreen == "snipers":
                Shop_Sprites = pygame.sprite.Group()
                Gun_Menu = pygame.sprite.Group()

                for i in range(len(Sniper_List.sprites())):
                    Gun_Menu.add(Sniper_List.sprites()[i].Shop())

                Shop_Sprites.add(Shop_Show.sprites()[0].Shop().Shop_Layout())

                Shop_Sprites.add(Shop_Show.sprites()[0].Shop().gun_img())

                Shop_Sprites.add(Shop_Show.sprites()[0].Shop().Bullet_Shop())

                if Shop_Show.sprites()[0].bought == False:
                    Shop_Sprites.add(Shop_Show.sprites()[0].Shop().buy())
                elif Shop_Show.sprites()[0] == Equiped_Gun.sprites()[0]:
                    Shop_Sprites.add(Equiped_Gun.sprites()[0].Shop().equiped())
                else:
                    Shop_Sprites.add(Shop_Show.sprites()[0].Shop().equip())
            if shopscreen == "shotguns":
                Shop_Sprites = pygame.sprite.Group()
                Gun_Menu = pygame.sprite.Group()

                for i in range(len(Shotgun_List.sprites())):
                    Gun_Menu.add(Shotgun_List.sprites()[i].Shop())

                Shop_Sprites.add(Shop_Show.sprites()[0].Shop().Shop_Layout())

                Shop_Sprites.add(Shop_Show.sprites()[0].Shop().gun_img())

                Shop_Sprites.add(Shop_Show.sprites()[0].Shop().Bullet_Shop())

                if Shop_Show.sprites()[0].bought == False:
                    Shop_Sprites.add(Shop_Show.sprites()[0].Shop().buy())
                elif Shop_Show.sprites()[0] == Equiped_Gun.sprites()[0]:
                    Shop_Sprites.add(Equiped_Gun.sprites()[0].Shop().equiped())
                else:
                    Shop_Sprites.add(Shop_Show.sprites()[0].Shop().equip())
            if wait >= 1:
                basicfont4 = pygame.font.Font(words, 42)  # This code displays letters onto the screen
                text4 = basicfont4.render("Not Enough Coins!", True, RED)
                textrect4 = text4.get_rect()
                textrect4.centerx = 250
                textrect4.centery = 250
                screen2.blit(text4, textrect4)
                wait -= 1

            basicfont4 = pygame.font.Font(words, 30)  # This code displays letters onto the screen
            text4 = basicfont4.render("Press P to leave shop!", True, AQUA)
            textrect4 = text4.get_rect()
            textrect4.centerx = WIDTH / 2
            textrect4.centery = HEIGHT - 30
            screen2.blit(text4, textrect4)

            basicfont4 = pygame.font.Font(words, 12)  # This code displays letters onto the screen
            text6 = basicfont4.render("Coins: " + str(coins), True, YELLOW)
            textrect6 = text6.get_rect()
            textrect6.right = WIDTH
            screen.blit(text6, textrect6)

            Shop_Sprites.draw(screen2)
            Gun_Menu.draw(screen2)
            Shop_Click.draw(screen2)

            if shopscreen != "ranks":
                Shop_Show.sprites()[0].Shop().info()
            else:
                # if not ranks what to do>
                basicfont4 = pygame.font.Font(words, 100)  # This code displays letters onto the screen
                text4 = basicfont4.render("Rank: " + str(oldrank), True, AQUA)
                textrect4 = text4.get_rect()
                textrect4.midleft = (0, 312.5)
                screen.blit(text4, textrect4)

            pygame.display.flip()
            pygame.display.update()

        if Globals.scene == "Game":  # The part of the code that makes it happen
            keystate = pygame.key.get_pressed()

            if Equiped_Gun.sprites()[0].clip > 0:
                if pygame.mouse.get_pressed()[0]:
                    try:
                        if Bullets.sprites()[-1].nextbullet > Bullets.sprites()[-1].ammountfornextbullet:
                            Equiped_Gun.sprites()[0].clip -= 1
                            if Equiped_Gun.sprites()[0].type == "shotgun":
                                bullet = Equiped_Gun.sprites()[0].Bullet1()
                                bullet.rect.center = fighter.rect.center
                                Bullets.add(bullet)
                                bullet = Equiped_Gun.sprites()[0].Bullet2()
                                bullet.rect.center = fighter.rect.center
                                Bullets.add(bullet)
                                bullet = Equiped_Gun.sprites()[0].Bullet3()
                                bullet.rect.center = fighter.rect.center
                                Bullets.add(bullet)
                            else:
                                bullet = Equiped_Gun.sprites()[0].Bullet()
                                bullet.rect.center = fighter.rect.center
                                Bullets.add(bullet)
                    except IndexError:
                        Equiped_Gun.sprites()[0].clip -= 1

                        if Equiped_Gun.sprites()[0].type == "shotgun":
                            bullet = Equiped_Gun.sprites()[0].Bullet1()
                            bullet.rect.center = fighter.rect.center
                            Bullets.add(bullet)
                            bullet = Equiped_Gun.sprites()[0].Bullet2()
                            bullet.rect.center = fighter.rect.center
                            Bullets.add(bullet)
                            bullet = Equiped_Gun.sprites()[0].Bullet3()
                            bullet.rect.center = fighter.rect.center
                            Bullets.add(bullet)
                        else:
                            bullet = Equiped_Gun.sprites()[0].Bullet()
                            bullet.rect.center = fighter.rect.center
                            Bullets.add(bullet)

            elif (Equiped_Gun.sprites()[0].ammountofbullets > 0):  # reload
                Equiped_Gun.sprites()[0].reload += 1
                basicfont4 = pygame.font.Font(words, 15)  # This code displays letters onto the screen
                text5 = basicfont4.render("Reloading...", True, RED)
                textrect5 = text5.get_rect()
                textrect5.centerx = WIDTH / 2
                textrect5.centery = HEIGHT / 2 + HEIGHT / 3
                screen.blit(text5, textrect5)

                if (Equiped_Gun.sprites()[0].permreload < Equiped_Gun.sprites()[0].reload):
                    Equiped_Gun.sprites()[0].ammountofbullets -= Equiped_Gun.sprites()[0].permclip
                    Equiped_Gun.sprites()[0].clip = Equiped_Gun.sprites()[0].permclip
                    Equiped_Gun.sprites()[0].reload = 0

            if reload == True:
                Equiped_Gun.sprites()[0].reload += 1
                basicfont4 = pygame.font.Font(words, 15)  # This code displays letters onto the screen
                text5 = basicfont4.render("Reloading...", True, RED)
                textrect5 = text5.get_rect()
                textrect5.centerx = WIDTH / 2
                textrect5.centery = HEIGHT / 2 + HEIGHT / 3
                screen.blit(text5, textrect5)

                if (Equiped_Gun.sprites()[0].permreload < Equiped_Gun.sprites()[0].reload):
                    Equiped_Gun.sprites()[0].ammountofbullets -= Equiped_Gun.sprites()[0].permclip - \
                                                                 Equiped_Gun.sprites()[
                                                                     0].clip
                    Equiped_Gun.sprites()[0].clip = Equiped_Gun.sprites()[0].permclip
                    Equiped_Gun.sprites()[0].reload = 0
                    reload = False

            for i in range(len(Bullets)):
                try:
                    Bullets.sprites()[i].update()
                except IndexError:
                    continue

            movement_counter += 1
            if movement_counter >= movement:
                if keystate[pygame.K_w] and keystate[pygame.K_d]:
                    fighter.up()
                    fighter.right()
                elif keystate[pygame.K_a] and keystate[pygame.K_w]:
                    fighter.up()
                    fighter.left()
                elif keystate[pygame.K_a] and keystate[pygame.K_s]:
                    fighter.down()
                    fighter.left()
                elif keystate[pygame.K_s] and keystate[pygame.K_d]:
                    fighter.down()
                    fighter.right()


                elif keystate[pygame.K_a]:
                    fighter.left()
                elif keystate[pygame.K_d]:
                    fighter.right()
                elif keystate[pygame.K_w]:
                    fighter.up()
                elif keystate[pygame.K_s]:
                    fighter.down()

                if keystate[pygame.K_r]:
                    reload = True
                movement_counter = 0

            swait += 1
            wait = 0
            if start_level == 0:  # Checks if its a new level and if yes then make new enemys
                levels(level)
            if len(enemy_list.sprites()) == 0:
                start_level = 0
                level += 1
                total_level = total_level + 1
                coins = coins + coinadd

            for i in range(len(enemy_list.sprites())):
                enemy_list.sprites()[i].update()

            for i in range(len(enemy_list.sprites())):
                enemy_list.sprites()[i].health()

            fighter.health()

            bullet_timer += 100
            if bullet_timer >= bullet_speed:
                try:
                    for i in range(len(Bullets.sprites())):
                        Bullets.sprites()[i].update()
                except IndexError:
                    continue
                bullet_timer = 0

            basicfont4 = pygame.font.Font(words, 25)  # This code displays letters onto the screen
            text4 = basicfont4.render(
                str(Equiped_Gun.sprites()[0].ammountofbullets) + "/" + str(Equiped_Gun.sprites()[0].clip), True, RED)
            textrect4 = text4.get_rect()
            textrect4.right = WIDTH
            textrect4.top = HEIGHT - HEIGHT / 10
            screen.blit(text4, textrect4)

            # Draw/Render
            coin_timer_counter += 1
            if coin_timer_counter >= coin_timer:
                AllCoins.draw(screen)
                coin_delay_counter += 1
                if coin_delayer == coin_delay_counter:
                    CoinObject.update()
                    AllCoins.sprites()[0].update()
                    coin_delay_counter = 0
                    coin_timer_counter = 0

            fighter.Xp()
            fighter.stats()

            Equiped_Gun.draw(screen)
            Bullets.draw(screen)
            Main.draw(screen)
            enemy_list.draw(screen)
            # after drawwing flip display
            fighter.update()
            pygame.display.update()

            if keystate[pygame.K_p]:
                if swait > 5:
                    pygame.image.save(screen, 'game_capture_img.png')

                    shop_background_img_temp = pygame.image.load(os.path.abspath("game_capture_img.png"))
                    shop_background_img_temp = pygame.transform.scale(shop_background_img_temp, (1250, 625))
                    shop_background_img = pygame.Surface(shop_background_img_temp.get_size(),
                                                         pygame.HWSURFACE | pygame.SRCALPHA)
                    shop_background_img.blit(shop_background_img_temp, (0, 0))
                    del shop_background_img_temp

                    shop_background_img.fill((64, 64, 64, 100), special_flags=pygame.BLEND_MIN)
                    swait = 0
                    Globals.scene = "Shop"


def Gameoverloop():
    if Globals.listnam == False:
        f = open(names_text, "r")
        lines = f.readlines()
        f.close()
        s = open(names_text, "w")
        for line in lines:
            if line != (
                    str(login_line.word) + " " + str(oldkills) + " " + str(password_line.word) + " " + str(oldrank)):
                print(1)
                s.write(line)
        s.close()

        t = open(names_text, 'a')
        t.write("\n" + str(login_line.word) + " " + str(fighter.kills) + " " + str(password_line.word) + " " + str(
            fighter.rank))
        t.close()
        Globals.listnam = True

        for line in fileinput.FileInput(names_text, inplace=1):
            if line.rstrip():
                print(line, end='')

        Globals.listnam = True

    pygame.init()
    pygame.mixer.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.HWSURFACE | pygame.DOUBLEBUF)
    pygame.display.set_caption("High Scores:")

    screen.blit(Images.game_background_img, [0, 0])

    # Setting up ranks
    list_of_names = {}
    with open(names_text) as f:
        for line in f:
            (name, kills, password, rank) = line.split()
            list_of_names[str(name)] = int(rank)
    f.close()

    allnames = list_of_names  # sorting code
    allnames = sorted(allnames.items(), key=operator.itemgetter(1))
    allnames.reverse()

    basicfont4 = pygame.font.Font(words, 24)  # This code displays letters onto the screen

    x = 40
    for i in range(10):
        text4 = basicfont4.render((str(i + 1) + ": " + str(allnames[i][0]) + " " + str(allnames[i][1])), True,
                                  Color.Yellow)
        textrect4 = text4.get_rect()
        textrect4.topleft = (0, x)
        screen.blit(text4, textrect4)
        x += 40
    # Setting up ranks ^^
    # Setting up kills
    list_of_names = {}
    with open(names_text) as f:
        for line in f:
            (name, kills, password, rank) = line.split()
            list_of_names[str(name)] = int(kills)
    f.close()

    allnames = list_of_names  # sorting code
    allnames = sorted(allnames.items(), key=operator.itemgetter(1))
    allnames.reverse()

    basicfont4 = pygame.font.Font(words, 24)  # This code displays letters onto the screen

    x = 40
    for i in range(10):
        text4 = basicfont4.render((str(i + 1) + ": " + str(allnames[i][0]) + " " + str(allnames[i][1])), True,
                                  Color.Yellow)
        textrect4 = text4.get_rect()
        textrect4.topright = (1250, x)
        screen.blit(text4, textrect4)
        x += 40
    # Setting up kills ^^^
    text4 = basicfont4.render("Press q to quit or c to continue", True, AQUA)
    textrect4 = text4.get_rect()
    textrect4.centerx = WIDTH / 2
    textrect4.centery = HEIGHT / 2 + HEIGHT / 10
    screen.blit(text4, textrect4)

    text4 = basicfont4.render("Top Ranks:", True, Color.Black)
    textrect4 = text4.get_rect()
    textrect4.topleft = (0, 0)
    screen.blit(text4, textrect4)

    text4 = basicfont4.render("Top Kills:", True, Color.Black)
    textrect4 = text4.get_rect()
    textrect4.topright = (1250, 0)
    screen.blit(text4, textrect4)

    text4 = basicfont4.render("GAME OVER", True, Color.Black)
    textrect4 = text4.get_rect()
    textrect4.midtop = (625, 0)
    screen.blit(text4, textrect4)

    basicfont5 = pygame.font.Font(words, 24)  # This code displays letters onto the screen
    text4 = basicfont5.render("Credits: ", True, RED)
    textrect4 = text4.get_rect()
    textrect4.centerx = WIDTH / 2 - WIDTH / 4
    textrect4.centery = HEIGHT / 2 + HEIGHT / 4
    screen.blit(text4, textrect4)

    text4 = basicfont4.render("Game Developer -- Jason Melnik", True, RED)
    textrect4 = text4.get_rect()
    textrect4.centerx = WIDTH / 2
    textrect4.centery = HEIGHT / 2 + HEIGHT / 3
    screen.blit(text4, textrect4)

    text4 = basicfont4.render("Graphics Design - me for now she is on break", True, RED)
    textrect4 = text4.get_rect()
    textrect4.centerx = WIDTH / 2
    textrect4.centery = HEIGHT / 2 + HEIGHT / 2.5
    screen.blit(text4, textrect4)

    pygame.display.flip()
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # If you click on the X on the screen it asks if you want to close the game
            Globals.quit = True
            pygame.quit()
            break
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:  # Quits the whole game
                Globals.quit = True
                pygame.quit()
                break
            if event.key == pygame.K_c:
                Globals.scene = "Menu"
                pygame.quit()
                break


while Globals.quit == False:

    if Globals.scene == "Gameover":
        Gameoverloop()
    else:
        gameLoop()