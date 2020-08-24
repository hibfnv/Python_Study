"""通过此实例，我们会实现的功能是当用户的信息是存储在我们的文件中的，我们会给出一个欢迎老用户的信息，如果是新用户则将给出欢迎新用户的信息"""
import json


def get_storeinfo():
    """如果用户名在文件信息中就读取"""
    fn = 'userinfo.json'
    try:
        f = open(fn, mode='r', encoding='utf-8')
        username = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return username


def get_newuser():
    """新用户所需的信息生成器"""
    username = input("请输入你的用户名: ")
    file = 'userinfo.json'
    f = open(file, mode='a', encoding='utf-8')
    json.dump(username, f)
    return username


def greet_user():
    username = get_storeinfo()
    if username:
        print("欢迎回来，" + username + "!")
    else:
        username = get_newuser()
        print("欢迎新用户" + username + "!")


greet_user()
