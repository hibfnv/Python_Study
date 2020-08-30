"""
    第四节，为空白的屏幕添加一些欢快的元互素，比如这里添加一个火箭图片，将它放置在屏幕底部中央
    同样，因为是游戏，少不了导入pygame模块
"""
import pygame


class Rocket():
    def __init__(self, r_settings, screen):
        """火箭在屏幕上的初始位置"""
        self.screen = screen
        """加载火箭图片，并获取图片外接的矩形"""
        self.r_settings = r_settings
        self.image = pygame.image.load("imgs/rock_smp.png")
        # 获取图片矩形的大小
        self.rect = self.image.get_rect()
        # 获取屏幕矩形的大小
        self.screen_rect = screen.get_rect()
        # 将火箭放置的位置在屏幕中央位置
        self.rect.centerx = self.screen_rect.centerx
        self.rect.centery = self.screen_rect.centery
        # 在火箭属性center中存储小数值
        self.centerx = float(self.rect.centerx)
        self.centery = float(self.rect.centery)
        # 初始移动状态为不可用
        self.move_right = False
        self.move_left = False
        self.move_down = False
        self.move_up = False

    def rocket_update(self):
        """根据火箭的移动状态调整火箭移动位置"""
        if self.move_right and self.rect.right < self.screen_rect.right:
            # 更新火箭的center值，而不是rect
            self.centerx += self.r_settings.speed_rate
        if self.move_left and self.rect.left > 0:
            self.centerx -= self.r_settings.speed_rate
        if self.move_up and self.rect.top > 0:
            self.centery -= self.r_settings.speed_rate
        if self.move_down and self.rect.bottom < self.screen_rect.bottom:
            self.centery += self.r_settings.speed_rate
        # 根据self.center更新rect对象
        self.rect.centerx = self.centerx
        self.rect.centery = self.centery

    def rocket_draw(self):
        """在底部中央的位置绘制图形"""
        self.screen.blit(self.image, self.rect)
