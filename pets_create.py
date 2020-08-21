# 此脚本主要用途在于项固实参，形参的使用，同时理解实参与形参的关系类型。
"""
在需要用户自己输入相关字段的形式下，函数有时并不需要形参或实参来进行数据交互，但在一些过程中也会用到。如果是程序自己调用函数中，可能会因为需要得到某一关键
位置或是字段，而进行过程定义的情况下，会使用形参或实参来传递有效的数值给对应的函数.
如此例中，实际中可以给函数定义实参，而且在函数运行时给其初始化使用了形参使用了空值
形参定义：在函数开始定义的一个或多个变量，它在定义的过程中。比如:def pets(p_type, p_pets),其中的p_type, p_pets均为形参
实参定义：在函数定义中，在函数内部，给形参赋的值，比如本实例中的p_type=XXX, p_pets=XXX
"""


def t_pets(t_type, t_pet):
    print("我有一条很大很大的" + t_type)
    print("它的名字叫" + t_pet)


def pets(p_type, p_pets):
    p_type = input("请输入你的宠物类型：")
    p_pets = input("请输入你的宠物名字：")
    print("你的宠物是：" + p_pets + "，它是一只" + p_type)


print('='*30)
# 在形参中，位置参数相当重要，如果位置序列错误，程序问题将非常严重。
t_pets("大狼狗", "七月")
print('='*30)
# 在调用t_pets将位置中的数据顺序调换位置后得到的结果
t_pets("七月", "大狼狗")
print('='*30)
pets("", "")
