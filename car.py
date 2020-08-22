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
        print("This car has " + str(self.odometer_reading) + " miles on it."
my_car = Car('BMW', '525Li', 2019)
print(my_car.get_description())
my_car.get_odometer()
