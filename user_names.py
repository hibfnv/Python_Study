"""通过用户输入来获取用户的姓和名，然后输出为用户全名"""
from Chap11.name_function import get_formatted_name
print("退出程序请按q。")
while 1:
    first = input("请输入你的姓（请用英文输入）：")
    if first =='q':
        break
    last = input("请输入你的名(请用英文输入）：")
    if last =='q':
        break

    formatted_name = get_formatted_name(first, last)
    print("你输入的用户姓名是：" + formatted_name + "!")


