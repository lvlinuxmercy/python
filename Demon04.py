"""
从一个数值范围，随机获取到若干个互不想等的数
因为循环次数不明确，可用while循环


"""

import random
def get_numbers01(start:int,end:int,num:int):
    """

    :param start: 范围起始值
    :param end:  范围结束值
    :param num: 获取到数值个数
    :return: 返回结果，为一个列表
    """
    #定义一个字典，用于接收返回结果
    results = {'data': [],'info': ''}
    # 进行范围判断，如果范围过小，存字典info信息
    if end - start < num:
        results['info'] = '数值范围过小'
    # 如果范围正常，则执行取数过程，存入字典data数据
    else:
    # 开始循环遍历
        while True:
            # 用randint函数在指定范围内获取随机数
            temp = random.randint(start,end)
            # 对生成的随机数进行判断，如果不在列表中，则添加
            if temp not in results['data']:
                results['data'].append(temp)
            # 判断列表中的元素个数是否已达到要求，数量达到要求，退出循环
            if len(results['data']) == num:
                #结束while 循环的办法通常有两种，一是return 二是 break
                break
    #返回字典结果，针对if-else 结构的return 可以最终做一次返回，无需做两次return
    return results


def get_numbers02(start:int,end:int,num:int):
    """

    :param start: 范围起始值
    :param end:  范围结束值
    :param num: 获取到数值个数
    :return: 返回结果，为一个列表
    """
    #定义一个列表，用于接收返回结果
    numbers = []
    # 进行范围判断，如果范围过小，触发一个异常
    if end - start < num:
        #触发一个异常
        raise Exception('数值范围过小')
    # 如果范围正常，则执行取数过程，存入列表
    else:
    # 开始循环遍历
        while True:
            # 用randint函数在指定范围内获取随机数
            temp = random.randint(start,end)
            # 对生成的随机数进行判断，如果不在列表中，则添加
            if temp not in numbers:
                numbers.append(temp)
            # 判断列表中的元素个数是否已达到要求，数量达到要求，退出循环
            if len(numbers) == num:
                #结束while 循环的办法通常有两种，一是return 二是 break
                break
    #返回字典结果，针对if-else 结构的return 可以最终做一次返回，无需做两次return
    return numbers










if __name__ == '__main__':

    start = 50
    end = 70
    num = 10
    results = get_numbers01(start, end, num)
    # 进行字典value 判断，如果info信息非空，则证明数值范围过小，直接打印info信息
    if  results['info'] != '':
        print(results['info'])
    # 如果info 信息为空，则证明数值范围正常，直接打印data数据
    else:
        print(results['data'])


    """
    #使用异常处理解决范围问题
    start = 50
    end = 70
    num = 40
    try :
        list01 = get_numbers02(start, end, num)
        print(list01)
    except Exception as e:
        print(str(e))

    """

"""

如果给的数值范围过小，无法取出足够的数值，程序将进入死循环，无法退出，针对这个问题，提出三中解决方案

1 在函数点用前引入判断
2 在函数中判断
3 引入异常处理




"""