"""通过使用json模块下的dump,load,dumps,loads来进行数据的存储与数据载入，实现数据的可读写操作"""
# 导入json模块
import json
list1 = [2, 4, 5, 8, 12, 24, 33, 38, 57, 62]
fn = 'list_num.json'
f = open(fn, mode='w', encoding='utf-8')
json.dump(list1, f)
"""通过json.load读取前面保存的数据"""
f = open(fn, mode='r', encoding='utf-8')
new_list = json.load(f)
print("从json存储的文件中读取数据：")
print(new_list)
"""同理，在json.dums和loads操作相同，只是针对的及是列表和字典以及集合。"""
