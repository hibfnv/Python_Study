# 通过open函数来对文本进行操作，替换文本中的关于python关键字的内容为java
import os
f = open("chap10_01.txt", mode='r', encoding='utf-8')
f_new = open("chap10_02.txt", mode='w', encoding='utf-8')
lines = f.readlines()
for line in lines:
    f_new.write(line.replace("python", "java"))
f.close()
f_new.close()
os.remove("chap10_01.txt")
os.rename("chap10_02.txt", "chap10_01.txt")

