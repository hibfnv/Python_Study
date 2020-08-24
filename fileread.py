# 利用open函数以打开文件，并写入相应的数据，利用不同的模式实现文件的写，读，追加操作
f = open('chap10_01.txt', mode='w', encoding='utf-8')
f.write("I love python, that's so interesting!!")
f.write("\n")
f.write("Well, you know python has so easy to learn for beginner.")
f.close()

f = open('chap10_01.txt', mode='r', encoding='utf-8')
lines = f.readlines()
for line in lines:
    print(line.rstrip())
f.close()
f = open('chap10_01.txt', mode='a', encoding='utf-8')
f.write("\n")
f.write("So great testing for python.")
f.write("\n")
f.write("I am not sure I have already master the python language, but I will try my best.")
f.close()
