# 利用try-except方法来定义一个文件不存在的错误信息，通过这个信息人性化告知用户没有这个文件


def count_words(fn):
    """计算文件大致包含多少个单词"""
    try:
        f = open(fn, mode='r', encoding='utf-8')
        contents = f.read()
    except FileNotFoundError:
        message = "Sorry, I can't find " + fn + " in this folder. "
        print(message)
    else:
        words = contents.split()
        num_words = len(words)
        print("The file " + fn + " has about " + str(num_words) + " words.")


files = ['chap10_01.txt', 'chap10_02.txt']
for fn in files:
    count_words(fn)
