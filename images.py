import pygame
import os

class Images:
    fighter_imgtemp = pygame.image.load(os.path.abspath("resources//images//fighter_img.png"))
    fighter_imgtemp = pygame.transform.scale(fighter_imgtemp, (50, 50))
    fighter_img = pygame.Surface(fighter_imgtemp.get_size(), pygame.HWSURFACE | pygame.SRCALPHA)
    fighter_img.blit(fighter_imgtemp, (0, 0))
    del fighter_imgtemp

    zombie_imgtemp = pygame.image.load(os.path.abspath("resources//images//zombie_img.png"))
    zombie_imgtemp = pygame.transform.scale(zombie_imgtemp, (50, 50))
    zombie_img = pygame.Surface(zombie_imgtemp.get_size(), pygame.HWSURFACE | pygame.SRCALPHA)
    zombie_img.blit(zombie_imgtemp, (0, 0))
    del zombie_imgtemp

    bulletpictemp = pygame.image.load(os.path.abspath("resources//images//bulletpic.png"))
    bulletpictemp = pygame.transform.scale(bulletpictemp, (5, 5))
    bulletpic = pygame.Surface(bulletpictemp.get_size(), pygame.HWSURFACE)
    bulletpic.blit(bulletpictemp, (0, 0))
    del bulletpictemp

    buypictemp = pygame.image.load(os.path.abspath("resources//images//buypic.png"))
    buypictemp = pygame.transform.scale(buypictemp, (75, 75))
    buypic = pygame.Surface(buypictemp.get_size(), pygame.HWSURFACE)
    buypic.blit(buypictemp, (0, 0))
    del buypictemp

    buy_ammo_imgtemp = pygame.image.load(os.path.abspath("resources//images//buy_ammo_img.png"))
    buy_ammo_imgtemp = pygame.transform.scale(buy_ammo_imgtemp, (75, 75))
    buy_ammo_img = pygame.Surface(buy_ammo_imgtemp.get_size(), pygame.HWSURFACE)
    buy_ammo_img.blit(buy_ammo_imgtemp, (0, 0))
    del buy_ammo_imgtemp

    gcointemp = pygame.image.load(os.path.abspath("resources//images//gcoin.png"))
    gcointemp = pygame.transform.scale(gcointemp, (20, 20))
    gcoin = pygame.Surface(gcointemp.get_size(), pygame.HWSURFACE | pygame.SRCALPHA)
    gcoin.blit(gcointemp, (0, 0))
    del gcointemp

    autogunpictemp = pygame.image.load(os.path.abspath("resources//images//AutoMaticGun.png"))
    autogunpictemp = pygame.transform.scale(autogunpictemp, (200, 50))
    autogunpic = pygame.Surface(autogunpictemp.get_size(), pygame.HWSURFACE)
    autogunpic.blit(autogunpictemp, (0, 0))
    del autogunpictemp

    snipergunpictemp = pygame.image.load(os.path.abspath("resources//images//SniperGunPic.png"))
    snipergunpictemp = pygame.transform.scale(snipergunpictemp, (200, 50))
    snipergunpic = pygame.Surface(snipergunpictemp.get_size(), pygame.HWSURFACE)
    snipergunpic.blit(snipergunpictemp, (0, 0))
    del snipergunpictemp

    Colt1911_pictemp = pygame.image.load(os.path.abspath("resources//guns//Colt_1911_img.png"))
    Colt1911_pictemp = pygame.transform.scale(Colt1911_pictemp, (200, 50))
    Colt1911_pic = pygame.Surface(Colt1911_pictemp.get_size(), pygame.HWSURFACE | pygame.SRCALPHA)
    Colt1911_pic.blit(Colt1911_pictemp, (0, 0))
    del Colt1911_pictemp

    Browning_Hi_Power_imgtemp = pygame.image.load(os.path.abspath("resources//guns//Browning_Hi-Power_img.png"))
    Browning_Hi_Power_imgtemp = pygame.transform.scale(Browning_Hi_Power_imgtemp, (200, 50))
    Browning_Hi_Power_img = pygame.Surface(Browning_Hi_Power_imgtemp.get_size(), pygame.HWSURFACE | pygame.SRCALPHA)
    Browning_Hi_Power_img.blit(Browning_Hi_Power_imgtemp, (0, 0))
    del Browning_Hi_Power_imgtemp

    Mauser_C96_imgtemp = pygame.image.load(os.path.abspath("resources//guns//Mauser_C96.png"))
    Mauser_C96_imgtemp = pygame.transform.scale(Mauser_C96_imgtemp, (200, 50))
    Mauser_C96_img = pygame.Surface(Mauser_C96_imgtemp.get_size(), pygame.HWSURFACE | pygame.SRCALPHA)
    Mauser_C96_img.blit(Mauser_C96_imgtemp, (0, 0))
    del Mauser_C96_imgtemp

    Volkssturmgewehr_imgtemp = pygame.image.load(os.path.abspath("resources//guns//Volkssturmgewehr_img.png"))
    Volkssturmgewehr_imgtemp = pygame.transform.scale(Volkssturmgewehr_imgtemp, (200, 50))
    Volkssturmgewehr_img = pygame.Surface(Volkssturmgewehr_imgtemp.get_size(), pygame.HWSURFACE | pygame.SRCALPHA)
    Volkssturmgewehr_img.blit(Volkssturmgewehr_imgtemp, (0, 0))
    del Volkssturmgewehr_imgtemp

    Spz_imgtemp = pygame.image.load(os.path.abspath("resources//guns//Spz_img.png"))
    Spz_imgtemp = pygame.transform.scale(Spz_imgtemp, (200, 50))
    Spz_img = pygame.Surface(Spz_imgtemp.get_size(), pygame.HWSURFACE | pygame.SRCALPHA)
    Spz_img.blit(Spz_imgtemp, (0, 0))
    del Spz_imgtemp

    ZH_29_imgtemp = pygame.image.load(os.path.abspath("resources//guns//ZH_29_img.png"))
    ZH_29_imgtemp = pygame.transform.scale(ZH_29_imgtemp, (200, 50))
    ZH_29_img = pygame.Surface(ZH_29_imgtemp.get_size(), pygame.HWSURFACE | pygame.SRCALPHA)
    ZH_29_img.blit(ZH_29_imgtemp, (0, 0))
    del ZH_29_imgtemp

    Puska_imgtemp = pygame.image.load(os.path.abspath("resources//guns//Puska_img.png"))
    Puska_imgtemp = pygame.transform.scale(Puska_imgtemp, (200, 50))
    Puska_img = pygame.Surface(Puska_imgtemp.get_size(), pygame.HWSURFACE | pygame.SRCALPHA)
    Puska_img.blit(Puska_imgtemp, (0, 0))
    del Puska_imgtemp

    A5_imgtemp = pygame.image.load(os.path.abspath("resources//guns//A5_img.png"))
    A5_imgtemp = pygame.transform.scale(A5_imgtemp, (200, 50))
    A5_img = pygame.Surface(A5_imgtemp.get_size(), pygame.HWSURFACE | pygame.SRCALPHA)
    A5_img.blit(A5_imgtemp, (0, 0))
    del A5_imgtemp

    Ithaca_37_imgtemp = pygame.image.load(os.path.abspath("resources//guns//Ithaca_37_img.png"))
    Ithaca_37_imgtemp = pygame.transform.scale(Ithaca_37_imgtemp, (200, 50))
    Ithaca_37_img = pygame.Surface(Ithaca_37_imgtemp.get_size(), pygame.HWSURFACE | pygame.SRCALPHA)
    Ithaca_37_img.blit(Ithaca_37_imgtemp, (0, 0))
    del Ithaca_37_imgtemp

    shop_pistols_imgtemp = pygame.image.load(os.path.abspath("resources//images//shop_pistols_img.png"))
    shop_pistols_imgtemp = pygame.transform.scale(shop_pistols_imgtemp, (200, 25))
    shop_pistols_img = pygame.Surface(shop_pistols_imgtemp.get_size(), pygame.HWSURFACE)
    shop_pistols_img.blit(shop_pistols_imgtemp, (0, 0))
    del shop_pistols_imgtemp

    shop_ranks_imgtemp = pygame.image.load(os.path.abspath("resources//images//shop_ranks_img.png"))
    shop_ranks_imgtemp = pygame.transform.scale(shop_ranks_imgtemp, (200, 25))
    shop_ranks_img = pygame.Surface(shop_ranks_imgtemp.get_size(), pygame.HWSURFACE)
    shop_ranks_img.blit(shop_ranks_imgtemp, (0, 0))
    del shop_ranks_imgtemp

    shop_automatics_imgtemp = pygame.image.load(os.path.abspath("resources//images//shop_automatics_img.png"))
    shop_automatics_imgtemp = pygame.transform.scale(shop_automatics_imgtemp, (200, 25))
    shop_automatics_img = pygame.Surface(shop_automatics_imgtemp.get_size(), pygame.HWSURFACE)
    shop_automatics_img.blit(shop_automatics_imgtemp, (0, 0))
    del shop_automatics_imgtemp

    shop_snipers_imgtemp = pygame.image.load(os.path.abspath("resources//images//shop_snipers_img.png"))
    shop_snipers_imgtemp = pygame.transform.scale(shop_snipers_imgtemp, (200, 25))
    shop_snipers_img = pygame.Surface(shop_snipers_imgtemp.get_size(), pygame.HWSURFACE)
    shop_snipers_img.blit(shop_snipers_imgtemp, (0, 0))
    del shop_snipers_imgtemp

    shop_shotguns_imgtemp = pygame.image.load(os.path.abspath("resources//images//shop_shotguns_img.png"))
    shop_shotguns_imgtemp = pygame.transform.scale(shop_shotguns_imgtemp, (200, 25))
    shop_shotguns_img = pygame.Surface(shop_shotguns_imgtemp.get_size(), pygame.HWSURFACE)
    shop_shotguns_img.blit(shop_shotguns_imgtemp, (0, 0))
    del shop_shotguns_imgtemp

    M97_pictemp = pygame.image.load(os.path.abspath("resources//guns//M97_img.png"))
    M97_pictemp = pygame.transform.scale(M97_pictemp, (200, 50))
    M97_pic = pygame.Surface(M97_pictemp.get_size(), pygame.HWSURFACE)
    M97_pic.blit(M97_pictemp, (0, 0))
    del M97_pictemp

    Colt_1911_shop_pic_temp = pygame.image.load(os.path.abspath("resources//images//Colt_1911_shop_pic.png"))
    Colt_1911_shop_pic_temp = pygame.transform.scale(Colt_1911_shop_pic_temp, (400, 150))
    Colt_1911_shop_pic = pygame.Surface(Colt_1911_shop_pic_temp.get_size(), pygame.HWSURFACE)
    Colt_1911_shop_pic.blit(Colt_1911_shop_pic_temp, (0, 0))
    del Colt_1911_shop_pic_temp

    Mauser_C96_shop_pic_temp = pygame.image.load(os.path.abspath("resources//guns//Mauser_C96.png"))
    Mauser_C96_shop_pic_temp = pygame.transform.scale(Mauser_C96_shop_pic_temp, (400, 150))
    Mauser_C96_shop_img = pygame.Surface(Mauser_C96_shop_pic_temp.get_size(), pygame.HWSURFACE | pygame.SRCALPHA)
    Mauser_C96_shop_img.blit(Mauser_C96_shop_pic_temp, (0, 0))
    del Mauser_C96_shop_pic_temp

    A5_shop_img_temp = pygame.image.load(os.path.abspath("resources//guns//A5_img.png"))
    A5_shop_img_temp = pygame.transform.scale(A5_shop_img_temp, (400, 150))
    A5_shop_img = pygame.Surface(A5_shop_img_temp.get_size(), pygame.HWSURFACE | pygame.SRCALPHA)
    A5_shop_img.blit(A5_shop_img_temp, (0, 0))
    del A5_shop_img_temp

    Ithaca_37_shop_img_temp = pygame.image.load(os.path.abspath("resources//guns//Ithaca_37_img.png"))
    Ithaca_37_shop_img_temp = pygame.transform.scale(Ithaca_37_shop_img_temp, (400, 150))
    Ithaca_37_shop_img = pygame.Surface(Ithaca_37_shop_img_temp.get_size(), pygame.HWSURFACE | pygame.SRCALPHA)
    Ithaca_37_shop_img.blit(Ithaca_37_shop_img_temp, (0, 0))
    del Ithaca_37_shop_img_temp

    Volkssturmgewehr_shop_img_temp = pygame.image.load(os.path.abspath("resources//guns//Volkssturmgewehr_img.png"))
    Volkssturmgewehr_shop_img_temp = pygame.transform.scale(Volkssturmgewehr_shop_img_temp, (400, 150))
    Volkssturmgewehr_shop_img = pygame.Surface(Volkssturmgewehr_shop_img_temp.get_size(), pygame.HWSURFACE | pygame.SRCALPHA)
    Volkssturmgewehr_shop_img.blit(Volkssturmgewehr_shop_img_temp, (0, 0))
    del Volkssturmgewehr_shop_img_temp

    Spz_shop_img_temp = pygame.image.load(os.path.abspath("resources//guns//Spz_img.png"))
    Spz_shop_img_temp = pygame.transform.scale(Spz_shop_img_temp, (400, 150))
    Spz_shop_img = pygame.Surface(Spz_shop_img_temp.get_size(), pygame.HWSURFACE | pygame.SRCALPHA)
    Spz_shop_img.blit(Spz_shop_img_temp, (0, 0))
    del Spz_shop_img_temp

    Browning_Hi_Power_imgtemp = pygame.image.load(os.path.abspath("resources//guns//Browning_Hi-Power_img.png"))
    Browning_Hi_Power_imgtemp = pygame.transform.scale(Browning_Hi_Power_imgtemp, (400, 150))
    Browning_Hi_Power_shop_img = pygame.Surface(Browning_Hi_Power_imgtemp.get_size(), pygame.HWSURFACE | pygame.SRCALPHA)
    Browning_Hi_Power_shop_img.blit(Browning_Hi_Power_imgtemp, (0, 0))
    del Browning_Hi_Power_imgtemp

    ZH_29_shop_pic_temp = pygame.image.load(os.path.abspath("resources//guns//ZH_29_img.png"))
    ZH_29_shop_pic_temp = pygame.transform.scale(ZH_29_shop_pic_temp, (600, 150))
    ZH_29_shop_pic = pygame.Surface(ZH_29_shop_pic_temp.get_size(), pygame.HWSURFACE | pygame.SRCALPHA)
    ZH_29_shop_pic.blit(ZH_29_shop_pic_temp, (0, 0))
    del ZH_29_shop_pic_temp

    Puska_shop_pic_temp = pygame.image.load(os.path.abspath("resources//guns//Puska_img.png"))
    Puska_shop_pic_temp = pygame.transform.scale(Puska_shop_pic_temp, (600, 150))
    Puska_shop_pic = pygame.Surface(Puska_shop_pic_temp.get_size(), pygame.HWSURFACE | pygame.SRCALPHA)
    Puska_shop_pic.blit(Puska_shop_pic_temp, (0, 0))
    del Puska_shop_pic_temp

    K98k_shop_pic_temp = pygame.image.load(os.path.abspath("resources//images//K98k_shop_pic.png"))
    K98k_shop_pic_temp = pygame.transform.scale(K98k_shop_pic_temp, (400, 150))
    K98k_shop_pic = pygame.Surface(K98k_shop_pic_temp.get_size(), pygame.HWSURFACE)
    K98k_shop_pic.blit(K98k_shop_pic_temp, (0, 0))
    del K98k_shop_pic_temp

    M97_shop_pic_temp = pygame.image.load(os.path.abspath("resources//images//M97_shop_pic.png"))
    M97_shop_pic_temp = pygame.transform.scale(M97_shop_pic_temp, (400, 150))
    M97_shop_pic = pygame.Surface(M97_shop_pic_temp.get_size(), pygame.HWSURFACE)
    M97_shop_pic.blit(M97_shop_pic_temp, (0, 0))
    del M97_shop_pic_temp

    MG_30_shop_pic_temp = pygame.image.load(os.path.abspath("resources//images//MG_30_shop_pic.png"))
    MG_30_shop_pic_temp = pygame.transform.scale(MG_30_shop_pic_temp, (400, 150))
    MG_30_shop_pic = pygame.Surface(MG_30_shop_pic_temp.get_size(), pygame.HWSURFACE)
    MG_30_shop_pic.blit(MG_30_shop_pic_temp, (0, 0))
    del MG_30_shop_pic_temp

    equip_pic_temp = pygame.image.load(os.path.abspath("resources//images//equip_pic.png"))
    equip_pic_temp = pygame.transform.scale(equip_pic_temp, (100, 40))
    equip_pic = pygame.Surface(equip_pic_temp.get_size(), pygame.HWSURFACE)
    equip_pic.blit(equip_pic_temp, (0, 0))
    del equip_pic_temp

    shop_format_img_temp = pygame.image.load(os.path.abspath("resources//images//shop_format_img.png"))
    shop_format_img_temp = pygame.transform.scale(shop_format_img_temp, (800, 500))
    shop_format_img = pygame.Surface(shop_format_img_temp.get_size(), pygame.HWSURFACE)
    shop_format_img.blit(shop_format_img_temp, (0, 0))
    del shop_format_img_temp

    colt_1911_img_temp = pygame.image.load(os.path.abspath("resources//guns//Colt_1911_img.png"))
    colt_1911_img_temp = pygame.transform.scale(colt_1911_img_temp, (400, 200))
    colt_1911_img = pygame.Surface(colt_1911_img_temp.get_size(), pygame.HWSURFACE | pygame.SRCALPHA)
    colt_1911_img.blit(colt_1911_img_temp, (0, 0))
    del colt_1911_img_temp

    k98k_img_temp = pygame.image.load(os.path.abspath("resources//guns//K98k_img.png"))
    k98k_img_temp = pygame.transform.scale(k98k_img_temp, (700, 200))
    k98k_img = pygame.Surface(k98k_img_temp.get_size(), pygame.HWSURFACE | pygame.SRCALPHA)
    k98k_img.blit(k98k_img_temp, (0, 0))
    del k98k_img_temp

    m97_img_temp = pygame.image.load(os.path.abspath("resources//guns//M97_img.png"))
    m97_img_temp = pygame.transform.scale(m97_img_temp, (700, 200))
    m97_img = pygame.Surface(m97_img_temp.get_size(), pygame.HWSURFACE | pygame.SRCALPHA)
    m97_img.blit(m97_img_temp, (0, 0))
    del m97_img_temp

    mg_30_img_temp = pygame.image.load(os.path.abspath("resources//guns//MG_30_img.png"))
    mg_30_img_temp = pygame.transform.scale(mg_30_img_temp, (400, 200))
    mg_30_img = pygame.Surface(mg_30_img_temp.get_size(), pygame.HWSURFACE | pygame.SRCALPHA)
    mg_30_img.blit(mg_30_img_temp, (0, 0))
    del mg_30_img_temp

    Colt_1911_shop_selector_img_temp = pygame.image.load(os.path.abspath("resources//images//Colt_1911_shop_selector_img.png"))
    Colt_1911_shop_selector_img_temp = pygame.transform.scale(Colt_1911_shop_selector_img_temp, (200, 50))
    Colt_1911_shop_selector_img = pygame.Surface(Colt_1911_shop_selector_img_temp.get_size(), pygame.HWSURFACE | pygame.SRCALPHA)
    Colt_1911_shop_selector_img.blit(Colt_1911_shop_selector_img_temp, (0, 0))
    del Colt_1911_shop_selector_img_temp

    Mauser_C96_Power_shop_selector_img_temp = pygame.image.load(os.path.abspath("resources//images//Mauser_C96_Power_shop_selector_img.png"))
    Mauser_C96_Power_shop_selector_img_temp = pygame.transform.scale(Mauser_C96_Power_shop_selector_img_temp, (200, 50))
    Mauser_C96_Power_shop_selector_img = pygame.Surface(Mauser_C96_Power_shop_selector_img_temp.get_size(), pygame.HWSURFACE | pygame.SRCALPHA)
    Mauser_C96_Power_shop_selector_img.blit(Mauser_C96_Power_shop_selector_img_temp, (0, 0))
    del Mauser_C96_Power_shop_selector_img_temp

    Volkssturmgewehr_shop_selector_img_temp = pygame.image.load(os.path.abspath("resources//images//Volkssturmgewehr_shop_selector_img.png"))
    Volkssturmgewehr_shop_selector_img_temp = pygame.transform.scale(Volkssturmgewehr_shop_selector_img_temp, (200, 50))
    Volkssturmgewehr_shop_selector_img = pygame.Surface(Volkssturmgewehr_shop_selector_img_temp.get_size(), pygame.HWSURFACE | pygame.SRCALPHA)
    Volkssturmgewehr_shop_selector_img.blit(Volkssturmgewehr_shop_selector_img_temp, (0, 0))
    del Volkssturmgewehr_shop_selector_img_temp

    Spz_shop_selector_img_temp = pygame.image.load(os.path.abspath("resources//images//Spz_shop_selector_img.png"))
    Spz_shop_selector_img_temp = pygame.transform.scale(Spz_shop_selector_img_temp, (200, 50))
    Spz_shop_selector_img = pygame.Surface(Spz_shop_selector_img_temp.get_size(), pygame.HWSURFACE | pygame.SRCALPHA)
    Spz_shop_selector_img.blit(Spz_shop_selector_img_temp, (0, 0))
    del Spz_shop_selector_img_temp

    ZH_29_shop_selector_img_temp = pygame.image.load(os.path.abspath("resources//images//ZH_29_shop_selector_img.png"))
    ZH_29_shop_selector_img_temp = pygame.transform.scale(ZH_29_shop_selector_img_temp, (200, 50))
    ZH_29_shop_selector_img = pygame.Surface(ZH_29_shop_selector_img_temp.get_size(), pygame.HWSURFACE | pygame.SRCALPHA)
    ZH_29_shop_selector_img.blit(ZH_29_shop_selector_img_temp, (0, 0))
    del ZH_29_shop_selector_img_temp

    Puska_shop_selector_img_temp = pygame.image.load(os.path.abspath("resources//images//Puska_shop_selector_img.png"))
    Puska_shop_selector_img_temp = pygame.transform.scale(Puska_shop_selector_img_temp, (200, 50))
    Puska_shop_selector_img = pygame.Surface(Puska_shop_selector_img_temp.get_size(), pygame.HWSURFACE | pygame.SRCALPHA)
    Puska_shop_selector_img.blit(Puska_shop_selector_img_temp, (0, 0))
    del Puska_shop_selector_img_temp

    M97_shop_selector_img_temp = pygame.image.load(os.path.abspath("resources//images//M97_shop_selector_img.png"))
    M97_shop_selector_img_temp = pygame.transform.scale(M97_shop_selector_img_temp, (200, 50))
    M97_shop_selector_img = pygame.Surface(M97_shop_selector_img_temp.get_size(), pygame.HWSURFACE | pygame.SRCALPHA)
    M97_shop_selector_img.blit(M97_shop_selector_img_temp, (0, 0))
    del M97_shop_selector_img_temp

    A5_shop_selector_img_temp = pygame.image.load(os.path.abspath("resources//images//A5_shop_selector_img.png"))
    A5_shop_selector_img_temp = pygame.transform.scale(A5_shop_selector_img_temp, (200, 50))
    A5_shop_selector_img = pygame.Surface(A5_shop_selector_img_temp.get_size(), pygame.HWSURFACE | pygame.SRCALPHA)
    A5_shop_selector_img.blit(A5_shop_selector_img_temp, (0, 0))
    del A5_shop_selector_img_temp

    Ithaca_37_shop_selector_img_temp = pygame.image.load(os.path.abspath("resources//images//Ithaca_37_shop_selector_img.png"))
    Ithaca_37_shop_selector_img_temp = pygame.transform.scale(Ithaca_37_shop_selector_img_temp, (200, 50))
    Ithaca_37_shop_selector_img = pygame.Surface(Ithaca_37_shop_selector_img_temp.get_size(), pygame.HWSURFACE | pygame.SRCALPHA)
    Ithaca_37_shop_selector_img.blit(Ithaca_37_shop_selector_img_temp, (0, 0))
    del Ithaca_37_shop_selector_img_temp

    MG_30_shop_selector_img_temp = pygame.image.load(os.path.abspath("resources//images//MG_30_shop_selector_img.png"))
    MG_30_shop_selector_img_temp = pygame.transform.scale(MG_30_shop_selector_img_temp, (200, 50))
    MG_30_shop_selector_img = pygame.Surface(MG_30_shop_selector_img_temp.get_size(), pygame.HWSURFACE | pygame.SRCALPHA)
    MG_30_shop_selector_img.blit(MG_30_shop_selector_img_temp, (0, 0))
    del MG_30_shop_selector_img_temp

    Browning_Hi_Power_shop_selector_img_temp = pygame.image.load(os.path.abspath("resources//images//Browning_Hi_Power_shop_selector_img.png"))
    Browning_Hi_Power_shop_selector_img_temp = pygame.transform.scale(Browning_Hi_Power_shop_selector_img_temp,
                                                                      (200, 50))
    Browning_Hi_Power_shop_selector_img = pygame.Surface(Browning_Hi_Power_shop_selector_img_temp.get_size(), pygame.HWSURFACE | pygame.SRCALPHA)
    Browning_Hi_Power_shop_selector_img.blit(Browning_Hi_Power_shop_selector_img_temp, (0, 0))
    del Browning_Hi_Power_shop_selector_img_temp

    K98k_shop_selector_img_temp = pygame.image.load(os.path.abspath("resources//images//K98k_shop_selector_img.png"))
    K98k_shop_selector_img_temp = pygame.transform.scale(K98k_shop_selector_img_temp, (200, 50))
    K98k_shop_selector_img = pygame.Surface(K98k_shop_selector_img_temp.get_size(), pygame.HWSURFACE | pygame.SRCALPHA)
    K98k_shop_selector_img.blit(K98k_shop_selector_img_temp, (0, 0))
    del K98k_shop_selector_img_temp

    equiped_pic_temp = pygame.image.load(os.path.abspath("resources//images//equiped_pic.png"))
    equiped_pic_temp = pygame.transform.scale(equiped_pic_temp, (100, 40))
    equiped_pic = pygame.Surface(equiped_pic_temp.get_size(), pygame.HWSURFACE | pygame.SRCALPHA)
    equiped_pic.blit(equiped_pic_temp, (0, 0))
    del equiped_pic_temp

    game_background_img_temp = pygame.image.load(os.path.abspath("resources//images//game_background_img.png"))
    game_background_img_temp = pygame.transform.scale(game_background_img_temp, (1250, 625))
    game_background_img = pygame.Surface(game_background_img_temp.get_size(), pygame.HWSURFACE | pygame.SRCALPHA)
    game_background_img.blit(game_background_img_temp, (0, 0))
    del game_background_img_temp

    menu_img_temp = pygame.image.load(os.path.abspath("resources//images//menu_img.png"))
    menu_img_temp = pygame.transform.scale(menu_img_temp, (1250, 625))
    menu_img = pygame.Surface(menu_img_temp.get_size(), pygame.HWSURFACE | pygame.SRCALPHA)
    menu_img.blit(menu_img_temp, (0, 0))
    del menu_img_temp

    face1_img_temp = pygame.image.load(os.path.abspath("resources//faces//face1.png"))
    face1_img_temp = pygame.transform.scale(face1_img_temp, (100, 100))
    face1_img = pygame.Surface(face1_img_temp.get_size(), pygame.HWSURFACE | pygame.SRCALPHA)
    face1_img.blit(face1_img_temp, (0, 0))
    del face1_img_temp

    play_button_img_temp = pygame.image.load(os.path.abspath("resources//images//play_button_img.png"))
    play_button_img_temp = pygame.transform.scale(play_button_img_temp, (200, 50))
    play_button_img = pygame.Surface(play_button_img_temp.get_size(), pygame.HWSURFACE | pygame.SRCALPHA)
    play_button_img.blit(play_button_img_temp, (0, 0))
    del play_button_img_temp

    exit_button_img_temp = pygame.image.load(os.path.abspath("resources//images//exit_button_img.png"))
    exit_button_img_temp = pygame.transform.scale(exit_button_img_temp, (200, 50))
    exit_button_img = pygame.Surface(exit_button_img_temp.get_size(), pygame.HWSURFACE | pygame.SRCALPHA)
    exit_button_img.blit(exit_button_img_temp, (0, 0))
    del exit_button_img_temp

    login_button_img_temp = pygame.image.load(os.path.abspath("resources//images//login_button_img.png"))
    login_button_img_temp = pygame.transform.scale(login_button_img_temp, (200, 50))
    login_button_img = pygame.Surface(login_button_img_temp.get_size(), pygame.HWSURFACE | pygame.SRCALPHA)
    login_button_img.blit(login_button_img_temp, (0, 0))
    del login_button_img_temp

    back_button_img_temp = pygame.image.load(os.path.abspath("resources//images//back_button_img.png"))
    back_button_img_temp = pygame.transform.scale(back_button_img_temp, (200, 50))
    back_button_img = pygame.Surface(back_button_img_temp.get_size(), pygame.HWSURFACE | pygame.SRCALPHA)
    back_button_img.blit(back_button_img_temp, (0, 0))
    del back_button_img_temp

    sign_up_img_temp = pygame.image.load(os.path.abspath("resources//images//sign_up_img.png"))
    sign_up_img_temp = pygame.transform.scale(sign_up_img_temp, (200, 50))
    sign_up_img = pygame.Surface(sign_up_img_temp.get_size(), pygame.HWSURFACE | pygame.SRCALPHA)
    sign_up_img.blit(sign_up_img_temp, (0, 0))
    del sign_up_img_temp

    controls_button_img_temp = pygame.image.load(os.path.abspath("resources//images//controls_button_img.png"))
    controls_button_img_temp = pygame.transform.scale(controls_button_img_temp, (200, 50))
    controls_button_img = pygame.Surface(controls_button_img_temp.get_size(), pygame.HWSURFACE | pygame.SRCALPHA)
    controls_button_img.blit(controls_button_img_temp, (0, 0))
    del controls_button_img_temp

    blank_line_img_temp = pygame.image.load(os.path.abspath("resources//images//blank_line_img.png"))
    blank_line_img_temp = pygame.transform.scale(blank_line_img_temp, (400, 50))
    blank_line_img = pygame.Surface(blank_line_img_temp.get_size(), pygame.HWSURFACE | pygame.SRCALPHA)
    blank_line_img.blit(blank_line_img_temp, (0, 0))
    del blank_line_img_temp

    wall_img_temp = pygame.image.load(os.path.abspath("resources//images//wall_img.png"))
    wall_img_temp = pygame.transform.scale(wall_img_temp, (400, 50))
    wall_img = pygame.Surface(wall_img_temp.get_size(), pygame.HWSURFACE | pygame.SRCALPHA)
    wall_img.blit(wall_img_temp, (0, 0))
    del wall_img_temp