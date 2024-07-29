import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    """一个对飞船发射的弹药进行管理的类"""

    def __init__(self, ai_settings, screen, ship):
        super(Bullet,self).__init__()
        self.screen = screen
        # 在（0，0）处创建一个表示弹药的矩形，在设置正确的位置
        self.rect = pygame.Rect(0, 0, ai_settings.bullet_width,ai_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top
        # 存储小数表示弹药的位置
        self.y = float(self.rect.y)
        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor

    def update(self):
        """向上移动弹药"""
        # 更新位置小数值
        self.y -= self.speed_factor
        # 更新表示弹药的rect位置
        self.rect.y = self.y

    def draw_bullet(self):
        # 在屏幕上绘制弹药
        pygame.draw.rect(self.screen, self.color, self.rect)
