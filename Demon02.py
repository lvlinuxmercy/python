"""
定一个类统计一个文本中各个字符的数量
1 大写字母
2 小写字母
3 数字
4 汉字
5 其他字符(符号，特殊符号）


"""
import os


#
class CharNumber:


    #初始化数据
    def __init__(self,path:str):
        #通过类对象传入文本路径
        self.path = path
        #定一个属性接收文本内容
        self.file_str = ""
        #定义一个字典，接收各种字符数据,其中字典的value初始化为整形，后面可以进行累加运算
        self.num_dict = {'upper':0,'lower':0,'num':0,'chinese':0,'other':0}
        #自动获取文本内容
        self.get_txt_content()
        #自动统计字符数量
        self.get_char_number()

    #获取文本内容
    def get_txt_content(self):
        #引入try异常机制读取文件
        # try:
            #使用open函数读取文件
            with open(self.path, mode='r',encoding='utf-8') as fd:
                # 将读取内容存储到类属性
                self.file_str = fd.read()
        # except Exception as e:
        #     raise e

    #统计数量

    def get_char_number(self):
        # 循环遍历每一个字符
        for char in self.file_str:
            if (char >='A') and (char <= 'Z'):  # 大写字母
                self.num_dict['upper'] += 1
            elif (ord(char) >=97) and (ord(char) <=122):  #小写字母
                self.num_dict['lower'] += 1
            elif (ord(char) >=48) and (ord(char) <=57):  #数字
                self.num_dict['num'] += 1
            elif (char >= '\u4e00') and (char <='\u9fa5'): #汉字为unicode 编码
                self.num_dict['chinese'] += 1
            else:
                self.num_dict['other'] += 1


if __name__ == '__main__':

    # 用系统自带方法进行目录文件拼接，形成绝对路径，可以跨平台使用
    path = os.path.join('files','str.txt')
    # 类的实例化
    try:
        obj = CharNumber(path)  #该异常出现在类的实例化时， 因为此时会初始化get_txt_content() 方法
        print("大写字母: %d\n小写字母: %d\n数字: %d\n汉字: %d\n其他字符:%d" % (obj.num_dict['upper'],
            obj.num_dict['lower'], obj.num_dict['num'],
            obj.num_dict['chinese'], obj.num_dict['other']))
    except Exception as e:
        print("打开文件失败，错误原因是: " +str(e))

