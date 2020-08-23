# 利用列表的形式，结合pop()方法对给定的列表中相应的字符做打印输出，并列出打印中以及打印完成的数据


def unprint_mode(unprint_list, complete_modules):
    while unprint_list:
        current_design = unprint_list.pop()
        print("Printing name:" + current_design)
        complete_modules.append(current_design)


def printed_mode(compete_modules):
    print("\nThe following names have been printed:")
    for complete_module in complete_modules:
        print(complete_module)


unprint_list = ["Adobe", "Apple", "Asus", "Benq", "Benz", "BMW", "Barret", "Bitcommet"]
complete_modules = []
unprint_mode(unprint_list, complete_modules)
printed_mode(complete_modules)