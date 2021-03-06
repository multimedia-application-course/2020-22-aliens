# -*- coding utf-8 -*-
# @Time:2020/5/20 19:14
# @Author:Li Wei
# @Filename:alien_invasion.py
# @飞机大战游戏

import game_functions as gf
import pygame
from pygame.sprite import Group
from settings import Settings
from ship import Ship
from game_stats import GameStats

def run_game():
    #初始化游戏并创建一个屏幕对象
    pygame.init()
    ai_settings=Settings()
    screen=pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption("李威多媒体作业：飞机大战外星人")

    #创建一个用于存储游戏统计数据的实例
    stats=GameStats(ai_settings)
    #创建一艘飞船
    ship=Ship(ai_settings,screen)
    #创建一个用于存储子弹的编组
    bullets=Group()
    #创建一个外星人编组
    aliens=Group()
    #设置背景颜色
    bg_color=(230,230,230)

    #创建外星人群
    gf.create_fleet(ai_settings,screen,ship,aliens)



    #开始游戏主循环
    while True:
        #监视键盘和鼠标事件
        gf.check_events(ai_settings,screen,ship,bullets)

        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings,screen,ship,aliens,bullets)
            gf.update_aliens(ai_settings,stats,screen,ship,aliens,bullets)

        gf.update_screen(ai_settings,screen,ship,aliens,bullets)
run_game()