"""
    第五节，大型项目为了简化代码结构一般会重构部分代码，使其更容易扩展，这里通过rocket_function模块，避免主程序太长，使其逻辑更易理解
"""
import sys
import pygame


# 判断用户键盘和鼠标事件
# 第七节，由于早期追踪键鼠没有带入参数，现在需要判断火箭的移动，所以要将rocket代入check_events(rocket)
def check_events(rocket):
    """检测和追踪键盘鼠标操作"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        # 这里通过对键盘右键的按下和松开，判断移动状态
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                rocket.move_right = True
            elif event.key == pygame.K_LEFT:
                rocket.move_left = True
            elif event.key == pygame.K_UP:
                rocket.move_up = True
            elif event.key == pygame.K_DOWN:
                rocket.move_down = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                rocket.move_right = False
            elif event.key == pygame.K_LEFT:
                rocket.move_left = False
            elif event.key == pygame.K_UP:
                rocket.move_up = False
            elif event.key == pygame.K_DOWN:
                rocket.move_down = False


# 这里将主程序下面绘制屏幕的内容重新定义为update_screen方法
def update_screen(r_settings, screen, rocket):
    """更新屏幕上的图像，并切换到新屏幕"""
    # 每次循环都重绘屏幕
    screen.fill(r_settings.bg_color)
    rocket.rocket_draw()
    # 让最近绘制的屏幕可见
    pygame.display.flip()
