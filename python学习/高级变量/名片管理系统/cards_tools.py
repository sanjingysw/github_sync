# 对于所有操作都要使用的变量，应该定义在程序顶部
# 初始值应该为空
card_list = []

def show_menu():
    print("*" * 100)
    print("欢迎使用【名片管理系统】V1.0" "\n""\n""1.新建名片""\n""2.显示全部""\n""3.查询名片""\n""\n""0.退出系统")
    print("*" * 100)

def new_card():
    # 新增名片
    print("-" * 100)
    print("新增名片")
    # 1.提示用户输入名片详细信息
    name_user = input("请输入姓名：")
    phone_user =input("请输入电话：")
    qq_user = input("请输入QQ号码：")
    mail_user = input("请输入邮箱地址：")
    # 2.输入完成后，使用用户输入的信息，建立一个名片字典
    card_dict = {"name": name_user,
                "phone": phone_user,
                "qq": qq_user,
                "mail": mail_user}
    # 3.将名片字典添加到列表中
    card_list.append(card_dict)
    print(card_list)
    # 4.提示用户添加成功
    print("添加%s的名片成功" % name_user)

def show_all():
    # 显示全部
    print("-" * 100)
    print("显示所有名片")
    
    if len(card_list) == 0:
        print("当前没有任何名片记录，请使用【1】新建名片功能添加名片")
        # return可以返回一个函数执行结果 且下方代码不执行
        # 如果return后没有任何内容 表示会返回到调用函数的位置且不返回任何结果
        return   
    # 打印表头
    for title in ["姓名", "电话", "QQ", "邮箱"]:
        print(title, end = "\t\t")
    print("")
    # 打印分割线
    print("=" * 100)
    # 遍历名片列表一次输出所有信息
    for card_dict in card_list:
        print("%s\t\t%s\t\t%s\t\t%s" % (card_dict["name"],
                                        card_dict["phone"],
                                        card_dict["qq"],
                                        card_dict["mail"]
                                        )
            )

def search_card():
    """搜索名片
    
    """
    # 搜索名片
    print("-" * 100)
    print("搜索名片")
    # 1.提示用户输入要搜索的姓名
    find_name = input("请输入要搜索的姓名：")
    for card_dict in card_list:
        if find_name == card_dict["name"]:
            print("姓名\t\t电话\t\tQQ\t\t邮箱")
            print("=" * 100)
            print("%s\t\t%s\t\t%s\t\t%s" % (card_dict["name"],
                                            card_dict["phone"],
                                            card_dict["qq"],
                                            card_dict["mail"]))
            deal_card(card_dict)
            break
        # 2.遍历名片列表查询，如果没找到需要提示用户
    else:
        print("没找到%s的名片" % find_name)

def deal_card(find_dict):
    """处理查找到的名片
    find_dict：参数为查找到的名片
    """

    action_str = input("请选择你要执行的操作：1 修改 2 删除 0 返回上级菜单：")
    if action_str == "1":
        find_dict["name"] = input_card_info(find_dict["name"], "姓名：[回车不修改]:")
        find_dict["phone"] = input_card_info(find_dict["phone"], "电话：[回车不修改]:")
        find_dict["qq"] = input_card_info(find_dict["phone"], "QQ：[回车不修改]:")
        find_dict["mail"] = input_card_info(find_dict["phone"], "邮箱：[回车不修改]:") 
        print("修改成功")

    elif action_str == "2":
        card_list.remove(find_dict)
        print("已经删除名片")


def input_card_info(dict_value, tip_message):
    """改进输入名片信息
    dict_value：字典中原有的值
    tip_message：输入的意识文字
    return：如果用户输入内容则然后内容 否则返回原有的值
    """
    # 1.提示用户输入内容
    result_str = input(tip_message)
    # 2.如果用户输入内容，直接返回结果
    if len(result_str) > 0:
        return result_str
    # 3.如果用户没输入，返回字典中原有的值
    else:
        return dict_value