
##函数的命名为 动词+名词格式

#提供一个PI的常量值，对于接收常量值的变量名要大写， 一般变量名和函数名都小写
PI = 3.1415926


def check_radius():
    """
    对输入的半径进行校验，直到输入正确为止
    :return: 返回正确的半径数值
    """
    # 引入while循环进行反复输入
    while True:
        # 请用户输入一个半径
        input_num = input("请输入圆的半径：")
        # 引入try 异常处理判断输入是否正确
        try:
            #如果输入有误，则进行字符转换时会抛出异常，用try 语句捕捉该异常
            input_str = float(input_num)
            # 如果没有异常，直接返回输入结果
            return input_str
        except:
            #输入有误，捕捉到异常，给出提示
            print("输入有误")

def get_circumference(radius:float):
    """
    获取圆的周长
    :param radius:提供的圆的半径
    :return:  返回周长的值
    """
    #直接返回
    return 2 * PI * radius





def get_Circular_area(radius:float):
   """
   获取圆的面积
   :param radius: 提供的圆的半径
   :return:  返回圆的面积
   """
   # 直接返回结果
   return PI * radius * radius








# 主函数

if __name__ == '__main__':
    # 提供输入的半径
    input_num = check_radius()
    # 直接输出周长
    print("圆的周长为: %.2f" % get_circumference(input_num))
    # 直接输出面积
    print("圆的面积为: %.2f" % get_Circular_area(input_num))