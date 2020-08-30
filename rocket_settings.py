"""
    第三节，因为是游戏，在添加新功能的时候，同样会有很多的新设置需要添加，如果在主游戏上修改，很容易产生问题，并且代码量会非常大。
    这里引入设置，一旦需要添加新功能，只需要在这里添加即可。
"""


class RocketSettings():
    """存储火箭移动的所有设置的类"""
    def __init__(self):
        """初始化游戏设置"""
        self.screen_width = 1280
        self.screen_height = 800
        self.bg_color = (87, 255, 250)
        # 第九节，调整火箭的速度
        self.speed_rate = 0.5
