# 通过对车型，厂商，制造年份进行分类，将所有给出的车型建立一个类
class Car():
    def __init__(self, manufacture, model, produce_date):
        self.manufacture = manufacture
        self.model = model
        self.produce_date = produce_date
        self.odometer_reading = 0

    def get_description(self):
        car_name = 'The ' + str(self.produce_date) + 'th ' + self.manufacture.upper() + ' ' + self.model
        return car_name

    def get_odometer(self):
        print("This car has " + str(self.odometer_reading) + " miles on it.")

    def update_odometer(self, mileage):
        """将里程设定为指定数值，禁止回滚"""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("\033[31mRoll back odometer is forbidden!!\033[0m")

    def increase_odometer(self, miles):
        self.odometer_reading += miles


my_car = Car('BMW', '525Li', 2019)
print(my_car.get_description())
my_car.get_odometer()
print("When the car has run for 35780 miles:")
my_car.update_odometer(35780)
my_car.get_odometer()
print("When the car has increase 300 miles odometer:")
my_car.increase_odometer(300)
my_car.get_odometer()
