
import os
#定义存放分割excel内容后存放的列表
pam=[[],[],[],[]]



#定义写入xlsx 文件的函数，写入内容为一个列表嵌套列表的集合，故用循环遍历写入

def write_xlsx(path:str,filename:str,content:list):
    #导入模块方法
    from openpyxl import Workbook
    #目录文件连接
    url = os.path.join(path, filename)
    #创建工作簿
    wb = Workbook(url)
    #创建sheet对象
    ws = wb.create_sheet("sheet")
    #循环遍历列表，写入列表元素，该列表元素也是一个列表
    for i in content:
        ws.append(i)
    #保存文件
    wb.save(url)

#定义读取xls文件内容存入列表的函数，采用列表嵌套列表的方式
def read_excel(url:str):

    """

    :param url:传入文件的url地址
    :return:返回列表形式的文件内容
    """
    import xlrd
    data = xlrd.open_workbook(url)

    table = data.sheets()[0]  ### 获取第一张sheet
    nrows = table.nrows  ##获取到行号
    #打印总行数
    print(nrows)
    #去掉标题行等分内容为4等份
    base = int((nrows-1)/4)
    # 引入修正base的算法，当总行数除以4余3时，给base加1
    if ((nrows-1) % 4) == 3:
        base += 1

    #打印等分数
    print(base)
    #根据行号依次将内容存放进空列表
    for i in range(1,base+1):
        pam[0].append(table.row_values(i))
    for i in range(base+1,2*base+1):
        pam[1].append(table.row_values(i))
    for i in range(2*base+1,3*base+1):
        pam[2].append(table.row_values(i))
    for i in range(3*base+1,nrows):
        pam[3].append(table.row_values(i))
    return pam

if __name__ == '__main__':
    # 定义待读取文件路径
    url = r'D:\record\录音抽检0508.xlsx'
    #读取文件
    read_excel(url)
    #定义待写入文件目录
    path = r'C:\Users\Administrator\Desktop\0508\录音抽检0508'
    #定义待写入文件名，是一个列表
    filename = ['吕鹏辉.xlsx','白云方.xlsx','邢述景.xlsx','郑伟.xlsx']
    #循环写入4个文件
    for i in range(4):
        write_xlsx(path,filename[i],pam[i])

