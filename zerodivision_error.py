# 这是一个利用try-except来进行一个程序错误的人性化提示的代码，它主要功能是将报错信息人性化显示。
# 此实例是一个被除数为0的除法，这个时候，程序运行就会报错，因此我们利用给定的内容来提示异常
print("请输入两个数值，我会计算它们相除后的结果是多少. ")
print("退出程序请按q。")
while 1:
    first_number = input("\n请输入除数: ")
    if first_number == 'q':
        break
    second_number = input("请输入被除数: ")
    if second_number == 'q':
        break
    try:
        result = int(first_number) / int(second_number)
    except ZeroDivisionError:
        print("\033[31m被除数不能为0!\033[0m")
    except ValueError:
        print("\033[31m请输入正确的数字！\033[0m")
    else:
        print(result)
