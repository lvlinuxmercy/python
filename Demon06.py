##字典的三种遍历


if __name__ == '__main__':
    #定义一个字典，key不能重复，key,value 是无序的
    dict01 = {'sno':95001,'name':'Alice','birthday':'1990-10-10'}

    print(dict01.keys()) #把所有的key存储在一个列表中
    print(dict01.values()) #把所有的value存储在一个列表中
    print(dict01.items())  #把key，value作为一个整体以元组的形式存入列表中
    #第一种遍历方法,使用values()方法只打印vaule
    for v in dict01.values():
        print("value:",v)
    # 第二种遍历，使用keys()方法，打印key,value

    for k in dict01.keys():
        print("key:",k,end='\t')
        print("value",dict01[k])

    #第三种遍历，使用items()方法，一次打印出key，vaule
    for k,v in dict01.items():
        print(k,":",v)