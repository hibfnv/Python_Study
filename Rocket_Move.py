"""
    本实例是利用12章相关的内容设计一个可上下左右移动的火箭，但要求火箭移动时不能超出屏幕范围
    通过该实例主要目的是训练程序员对代码的相关思路理解。
"""
# 导入所需要的pygame游戏模块，用以在桌面绘制一个可见的游戏窗口。同时按下窗口的关闭则退出，需要sys模块提供sys.exit()方法
import sys
import pygame
# 第三节，新建rocket_settings模块，里面包含RocketSettings类
from Rocket_Nav.rocket_settings import RocketSettings
# 第四节，新建rocket模块，里面有Rocket类
from Rocket_Nav.rocket import Rocket
# 第五节，将主程序中循环追踪键盘鼠标操作的步骤作为一个模块实现
import Rocket_Nav.rocket_function as rocket_fun


# 调用主窗口的方法，这里命名为main
def main_game():
    # 初始化，在屏幕上绘制窗口
    pygame.init()
    # 第三节，因为导入了rocket_settings模块的RocketSettings类，此处定义r_settings实参来代替RocketSettings类
    r_settings = RocketSettings()
    """初始化屏幕窗口的大小为1280x800"""
    # screen = pygame.display.set_mode((1280, 800))
    # 第三节，将RocketSettings类用r_settings代替，并调用RocketSettings类中的screen_width,screen_height和bg_color实参
    screen = pygame.display.set_mode((r_settings.screen_width, r_settings.screen_height))
    """窗口显示的标题名称是Rocket Move"""
    pygame.display.set_caption("Rocket Move")
    # 第二小节，给绘制的窗口添加背景颜色
    # bg_color = (87, 255, 250)
    # 第四节，这里定义rocket参数代替rocket模块的Rocket类
    rocket = Rocket(r_settings, screen)

    # 开始游戏的主循环
    while True:
        # 追踪用户键盘和鼠标的操作
        """ 
        for event in pygame.event.get():
            # if event.type == pygame.QUIT:
                # sys.exit()
        """
        # 第五节，调用检测键盘鼠标事件的方法
        # 第七节，因为前期键鼠检测没有加入rocket参数，现在带入rocket参数。
        rocket_fun.check_events(rocket)
        # 第八节，通过修改rocket_update方法来让火箭不停的移动
        rocket.rocket_update()
        # 第二小节，循环窗口时重新绘制屏幕
        # screen.fill(bg_color)
        # 因为在RocketSettings类已经定义了bg_color,这里只需要调用即可
        # screen.fill(r_settings.bg_color)
        # 第四节，导入了rocket模块并指定了rocket代替Rocket类，则如下调用火箭图片：
        # rocket.rocket_draw()
        """以下是让绘制的屏幕窗口可见，目前只是一个纯黑色的窗口"""
        # pygame.display.flip()
        # 第六节，这里重新定义了屏幕绘制的方法
        rocket_fun.update_screen(r_settings, screen, rocket)


# 调用窗口，使其在电脑桌面显示
main_game()
