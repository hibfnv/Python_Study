# 创建一个输出简洁用户全名的代码


def get_formatted_name(first, last, middle=''):
    """创建一个获取用户全名的方法"""
    if middle:
        full_name = first + ' ' + middle + ' ' + last
    else:
        full_name = first + ' ' + last
    return full_name.title()
