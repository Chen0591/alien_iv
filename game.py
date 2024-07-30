import sys
import pygame
from settings import Settings
from ship import Ship
from alien import Alien
import game_functions as gf
from pygame.sprite import Group
from game_stats import GameStats


def run_game():
    """创造一艘飞船、弹药和外星人编组"""
    # 初始化游戏并创建一个屏幕对象
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    # 创造飞船实例
    ship = Ship(ai_settings, screen)
    #创造游戏统计实例
    stats=GameStats(ai_settings)
    #创造一个弹药实例
    bullets = Group()
    #创造外星人实例
    aliens=Group()
    gf.create_fleet(ai_settings,screen,ship,aliens)
    # 开始游戏的主循环
    while True:
        gf.check_events(ai_settings, screen, ship, bullets)
        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings,screen,ship,aliens,bullets)
            gf.update_aliens(ai_settings,stats,screen,ship,aliens,bullets)
        gf.update_screen(ai_settings, screen, ship, aliens,bullets)


run_game()
