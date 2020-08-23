# 利用传统汽车和新能源汽车的不同之处，通过继承传统汽车的一些实用功能，然后新增一些新能源汽车特有属性
class TraditionalCar():
    def __init__(self, manufacture, model, prod_date):
        self.manufacture = manufacture
        self.model = model
        self.prod_date = prod_date
        self.odometer = 0

    def car_description(self):
        description_car = 'The ' + str(self.prod_date) + 'th ' + self.manufacture + ' ' + self.model
        return description_car

    def update_odometer(self, mileage):
        if mileage >= self.odometer:
            self.odometer = mileage
        else:
            print("\033[31m输入错误，输入数据小于上一次数据.\033[0m")

    def get_odometer(self):
        print(self.car_description() + " has " + str(self.odometer) + " miles on it.")

    def add_odometer(self, miles):
        if miles > 0:
            self.odometer += miles
        else:
            print("\033[31m输入错误，数值不能是负数。")


my_car = TraditionalCar('Audi', 'A6L', 2016)
print(my_car.car_description())
my_car.get_odometer()

# 定义一个电池的相关类，使其能被新能源汽车所使用
"""对新能源汽车进行类的继承进添加新功能"""


class Battery():
    def __init__(self, battery_size=85):
        self.battery_size = battery_size

    def get_battery(self):
        print("This car has a " + str(self.battery_size) + " -kwh battery.")

    def get_range(self):
        """根据电池的容量，得出续航里程数据"""
        if self.battery_size == 70:
            real_odometer = 240
        elif self.battery_size == 85:
            real_odometer = 270
        message = "This car can go approximately " + str(real_odometer)
        message += " miles on a full charge."
        print(message)


class ElectronicCar(TraditionalCar):
    # 使用新能源汽车类electronic_car,使其继承traditional_car的相关功能。
    def __init__(self, manufacture, model, prod_date):
        super().__init__(manufacture, model, prod_date)
        self.battery = Battery()


my_ecar = ElectronicCar('Rowe', 'Marvel', 2020)


print(my_car.car_description())
my_ecar.battery.get_battery()
my_ecar.battery.get_range()
