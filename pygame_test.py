import pygame
import sys


def win_main():
    # 初始化pygame模块载入窗口
    pygame.init()
    screen = pygame.display.set_mode((1280, 800))
    pygame.display.set_caption("Pygame Mode Test")
    # bg_color设置为纯天蓝色
    bg_color = (30, 144, 255)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        screen.fill(bg_color)
        pygame.display.flip()


win_main()
