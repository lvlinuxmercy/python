## 找到10000-99999 之间9876 的倍数

def get_sum01(start:int,end:int):
    #定义一个变量存储结果
    sum = 0
    #开始循环
    for i in range(start,end+1):
        sum += i
    return sum

def get_sum02(list01:list):
    sum = 0

    for i in list01:
        sum += i

    return sum

def get_num01(start:int,end:int,number:int):
    """
    统计出某个范围内某个数的倍数
    :param start: 范围起始值
    :param end: 范围结束值
    :param num: 提供的参照数
    :return: 返回范围内某个数的倍数，list 集合
    """
    # 定一个集合
    numbers = []
    #开始循环
    for i in range(start,end+1):
        if i % number == 0:
            #添加满足条件的数到集合
            numbers.append(i)
    # 返回结果
    return numbers



def get_num02(start:int,end:int,number:int):
    # 初始化一个存结果的空列表
    numbers = []
    # 初始化第一个找到的结果变量
    first_num = 0
    # 找到第一个结果
    for i in range(start,end+1):
        if i % number == 0:
            first_num = i
            # 退出循环
            break
    # 再次遍历并返回结果
    for i in range(first_num,end+1,number):
        numbers.append(i)

    return numbers





if __name__=='__main__':
    #求两个数的范围之和(10,20)
    result01 = get_sum01(1,4)
    print(result01)
    # 计算一个集合的元素之和
    result02 = get_sum02([11,22,33,44,55])
    print(result02)
    #计算某一个【12345678，87654321】范围内，所有13572468的倍数
    start = 12345678
    end = 87654321
    number = 13572468
   # result03 = get_num01(start ,end ,number)
   # print(result03)

    result04 = get_num02(start ,end ,number)
    print(result04)