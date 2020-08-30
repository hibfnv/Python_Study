"""
    第五节，大型项目为了简化代码结构一般会重构部分代码，使其更容易扩展，这里通过rocket_function模块，避免主程序太长，使其逻辑更易理解
"""
import sys
import pygame


# 第十节，将检测追踪键盘鼠标动作的内容再细分为两个按下和松开键盘部分
def check_keydown_events(event, rocket):
    """按下键盘获得的状态"""
    if event.key == pygame.K_RIGHT:
        rocket.move_right = True
    elif event.key == pygame.K_LEFT:
        rocket.move_left = True
    elif event.key == pygame.K_UP:
        rocket.move_up = True
    elif event.key == pygame.K_DOWN:
        rocket.move_down = True


# 此处是松开键盘按键的状态
def check_keyup_events(event, rocket):
    """松开键盘按键后的状态呈现"""
    if event.key == pygame.K_RIGHT:
        rocket.move_right = False
    elif event.key == pygame.K_LEFT:
        rocket.move_left = False
    elif event.key == pygame.K_UP:
        rocket.move_up = False
    elif event.key == pygame.K_DOWN:
        rocket.move_down = False


# 判断用户键盘和鼠标事件
# 第七节，由于早期追踪键鼠没有带入参数，现在需要判断火箭的移动，所以要将rocket代入check_events(rocket)
def check_events(rocket):
    """检测和追踪键盘鼠标操作"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        # 这里通过对键盘右键的按下和松开，判断移动状态
        elif event.type == pygame.KEYDOWN:
            """
            此处内容通过新方法check_keydown_events(event, rocket)来完成
            if event.key == pygame.K_RIGHT:
                rocket.move_right = True
            elif event.key == pygame.K_LEFT:
                rocket.move_left = True
            elif event.key == pygame.K_UP:
                rocket.move_up = True
            elif event.key == pygame.K_DOWN:
                rocket.move_down = True
            """
            check_keydown_events(event, rocket)
        elif event.type == pygame.KEYUP:
            """
            此处由新生成的方法取代，只需要直接调用check_keyup_events(event, rocket)来实现
            if event.key == pygame.K_RIGHT:
                rocket.move_right = False
            elif event.key == pygame.K_LEFT:
                rocket.move_left = False
            elif event.key == pygame.K_UP:
                rocket.move_up = False
            elif event.key == pygame.K_DOWN:
                rocket.move_down = False
            """
            check_keyup_events(event, rocket)


# 这里将主程序下面绘制屏幕的内容重新定义为update_screen方法
def update_screen(r_settings, screen, rocket):
    """更新屏幕上的图像，并切换到新屏幕"""
    # 每次循环都重绘屏幕
    screen.fill(r_settings.bg_color)
    rocket.rocket_draw()
    # 让最近绘制的屏幕可见
    pygame.display.flip()
