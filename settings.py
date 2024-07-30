class Settings():
    """存储《外星人入侵》的所有设置的类"""

    def __init__(self):
        """初始化游戏的设置"""
        self.screen_width = 800
        self.screen_height = 600
        self.bg_color = (230, 230, 230)

        # 飞船弹药设置

        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullet_speed_factor = 0.8
        self.bullet_allowed=3
        # 飞船设置
        self.ship_speed_factor = 0.6

        #外星人设置
        self.alien_speed_factor=0.1
        self.fleet_drop_speed=10
        #fleet_direction为1表示向右移，-1则为向左移动
        self.fleet_direction=1
