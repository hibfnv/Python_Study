# 此实例主要用途在于理解类与类的继承，通过对该实例的代码实现，以理解类与子类的继承，子类将延用父类的有用信息。
class Car():
    def __init__(self, manufacture, model, product_date):
        self.manufacture = manufacture
        self.model = model
        self.product_date = product_date
        self.odometer = 0

    def car_description(self):
        full_name = 'The ' + str(self.product_date) + 'th ' + self.manufacture + ' ' + self.model
        return full_name

    def get_odometer(self):
        print("This car has " + str(self.odometer) + " miles on it.")

    def update_odometer(self, mileage):
        if mileage >= self.odometer:
            self.odometer = mileage
        else:
            print("\033[31m输入有误，里程数比前一次小。\033[0m")

    def increase_odometer(self, miles):
        if miles > 0:
            self.odometer += miles
        else:
            print("\033[31m输入错误，新增值不能为负数。\033[0m")


my_car = Car("Benz", "GLK260", 2019)
print("\033[32m当前汽车的品牌型号及制造年份: \033[0m")
print(my_car.car_description())
print("\033[32m初始化时，车子里程数为0: \033[0m")
my_car.get_odometer()
print("\033[32m给里程表加37800公里的里程纪录: \033[0m")
my_car.update_odometer(37800)
my_car.get_odometer()
print("\033[32m汽车行驶一段时间后，里程数据又增加了200公里: \033[0m")
my_car.increase_odometer(200)
my_car.get_odometer()
print("\033[32m输入里程小于上一次里程时报错信息: \033[0m")
my_car.update_odometer(3100)
my_car.get_odometer()
print("\033[32m输入新增时程为负数时报错信息: \033[0m")
my_car.increase_odometer(-100)
my_car.get_odometer()

"""理解了类的相关操作，后续进行类的继承实例操作，以下是对类的实例进行一次演练，以很好的完成对类的继承进行理解"""
# 目前全世界都在为了节能减排做自己的贡献，我国也在大力发展新能源汽车，目前我们就以现在流行的新能源车做实例解析
# 定义一个新能源汽车的类，它既有传统汽车该有的特性，又有自己作为新能源的新特性


class electronic_car(Car):
    """新能源汽车electronic_car关联其父类Car"""
    def __init__(self, manufacture, model, product_date):
        # 在初始化electronic_car时，使用super()函数，将父类的作用继顾给子类。使子类与父类有相同的功能
        super().__init__(manufacture, model, product_date)
        # 在子类中添加一些父类没有的新功能，比如电池容量
        self.battery_size = 80

    def bt_descript(self):
        print("This car has a " + str(self.battery_size) + "-kwh battery.")


print("新能源汽车使用子类，并且子类继承了父类的相应的功能: ")
my_ecar = electronic_car("BYD", '秦EV', 2020)
print(my_ecar.car_description())
my_ecar.get_odometer()
print("\033[32m新能源汽车自身特有的功能: \033[0m")
my_ecar.bt_descript()
