"""导入os模块给文件重命名"""
import os

f = open("test.txt", 'w', encoding='utf-8')
f.write("This is a test file")
f.write('\n')
f.close()
os.rename('test.txt', 'test1.txt')
