
list01 = [11,22,33,44,55]


## 第一种， 不能改变列表元素
"""
for item in list01:
    print (item)
    
"""
## 第二种方法
## 可以改变列表元素， 但是元素的操作要依赖列表索引号

"""
for index in range(0,len(list01)):
    print('索引是: ',index,'元素为：',list01[index])
"""

#第三种，对元素的操作不依赖索引，比较灵活

dn = '15502126720'
list02 = tuple(dn)
print(list02)

list02 = str(tuple(list02)).replace(',','')


# print(list02)
# for index,item in enumerate(list01):
#     print(index,item)