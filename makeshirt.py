# 通过传递任意数量的实参来实现对形参前的*进行理解。它的功能是收集所有用户输入的实参并传输给相应的对象，它和位置参数的顺序不能发生改变。
# 在调用形参的过程中，位置参数始终在第一位，其次是*args(任意参数),默认值参数，最后才是关键字参数。


# 传递任意数量的实参范例：
def makeShirt(s_type, *print_fonts):
    print("\nMake a " + str(s_type) + " size t-shirt and with follow text: ")
    for print_font in print_fonts:
        print("Slogan: " + print_font)


print("\033[35m=\033[0m"*30)
makeShirt("Middle", "I Love YoYo!")
print("\033[35m=\033[0m"*30)
makeShirt("Large", "Well", "You have to know that.", "She's my favor.")
print("\033[35m=\033[0m"*30)


# 使用任意数量的关键字参数范例：
def user_profile(first, last, **user_info):
    """新建一个字典用以存储用户数据"""
    profile = {'First_name': first, 'Last_name': last}
    for key, value in user_info.items():
        profile[key] = value
    return profile


# 在此处的location和field传入值，在函数中是没有定义的，但我们在函数中使用了一个key,value迭代，并指定其中的profile[key] = value
u_profile = user_profile('Jim', 'Smith', Location='Washington', Field='IT')
f = open('userinfo.txt', mode='w', encoding='utf-8')
f.write(str(u_profile))
f.write("\n")
f.close()
