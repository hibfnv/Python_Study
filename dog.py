# 通过对类的定义和应用来理解类，并通过类的方法实现对类的掌握
class Dog():
    """一次模拟小狗的简单实现方法"""
    def __init__(self, name, age):
        """初始化属性name和age"""
        self.name = name
        self.age = age

    def sit(self):
        """模拟命令小狗蹲下"""
        print(self.name.title() + " is now sitting.")

    def roll_over(self):
        """模拟命令小狗打滚"""
        print(self.name.title() + " rolled over!")


my_dog = Dog('Williams', 12)
print("\033[35m==\033[0m" * 20)
print("My dog's name is " + my_dog.name.title() + ".")
print("My dog is " + str(my_dog.age) + " years old.")
print("\033[35m==\033[0m" * 20)
my_dog.sit()
print("\033[35m==\033[0m" * 20)
my_dog.roll_over()
print("\033[35m==\033[0m" * 20)
