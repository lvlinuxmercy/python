#! /usr/bin/python
# -*- coding: utf-8 -*-
# 执行sql函数
import os
os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.UTF8'

def ywtj(sql):             # 定义业务统计函数，用来执行sql语句
    import cx_Oracle       # 该模块并非python自带模块，需要独立安装
    connection = cx_Oracle.connect('ali/ali@192.168.10.24/record')  # 连接oracle
    c = connection.cursor()
    x = c.execute(sql)       # 执行sql语句
    data = x.fetchone()      # 执行结果赋值给data
#   all_data=x.fetchall()
    data_rel = data[0]  # data是个只有一个值的元组，取该元组第一个值，保留2位小数
    if data_rel == None:
        data_rel = 0
    print(data)
    c.close()
    connection.close()       # 关闭连接
    return data_rel          # 返回值

# 读取文件中的sql语句并执行
print('欢迎使用陕西小号业务统计脚本V1.0')
time = input('查询时间')     # 输入查询时间
f = open(r'/pythondata/sql//aliyw.sql', encoding='gbk')    # 查询sql所在的目录
daily_print = []
for line in f:
    line = line.replace('20190221', str(time))     # 替换时间
    sql1 = line
    print('正在执行:')
    print(sql1)
    daily = ywtj(sql=sql1)                  # 调用执行sql函数，执行替换时间后的sql，结果赋值给daily
    daily_print.append(daily)        # 此处执行结果包括阿里和主动查询的结果
f.close()

def dsffile(time,appkey):     # 对第三方定义一个额外的函数，因为要区分客户
    if appkey == 'DM':
        f = open(r'/pythondata/sql//DM.sql', encoding='gbk')
    elif appkey == 'TR':
        f = open(r'/pythondata/sql//TR.sql', encoding='gbk')
    elif appkey == 'WL':
        f = open(r'/pythondata/sql//WL.sql', encoding='gbk')
    else:
        f = open(r'/pythondata/sql//ZH.sql', encoding='gbk')
    dsf_daily_print = []
    for line in f:                          # 按行读取文件中的内容
        line = line.replace('20190221', str(time))
        line = line.replace('TR', appkey)    # 替换AppKey头2位
        sql1 = line
        print ('正在执行:')
        print (sql1)
        daily = ywtj(sql=sql1)
        dsf_daily_print.append(daily)       # 将每个sql执行的结果存在一个列表里
    f.close()
    return dsf_daily_print                  # 返回执行的结果

dm_dsf = dsffile(time=time, appkey='DM')   # 东盟第三方业务查询
tr_dsf = dsffile(time=time, appkey='TR')   # 天润业务
wl_dsf = dsffile(time=time, appkey='WL')   # 微聊业务
zh_dsf = dsffile(time=time, appkey='ZH')   # 朝花夕拾业务

# import time
# time=time.strftime('%Y%m%d',time.localtime())

from openpyxl import Workbook
from openpyxl import load_workbook  # openpyxl为python自带模块
def intoexcel(append,sheet):        # 定义数据写入Excel的函数
    wb = load_workbook('/pythondata//陕西小号日报.xlsx')
    wb.guess_types = True  # 猜测格式类型
    ws = wb.get_sheet_by_name(sheet)   # 根据名称查sheet
    ws.append(append)                  # 在sheet下追加数据
    print('数据写入到：', sheet)
    # Save the file
    wb.save("/pythondata//陕西小号日报.xlsx")  # 保存退出

# 结果计算赋值
# 阿里业务
ali_used = daily_print[0]          # 阿里占用号码数
ali_unused = daily_print[1]        # 阿里剩余号码数
ali_sub_daily = daily_print[2]     # 当日绑定数
ali_call = daily_print[3]          # 总呼叫量
ali_call_success = daily_print[4]  # 呼叫成功量
ali_call_success_rate = round(ali_call_success/ali_call, 2)  # 阿里呼叫成功率
ali_call_max = daily_print[5]       # 呼叫峰值
ali_rel_add = daily_print[6]        # 净增量
ali_call_avg_time = round(daily_print[7], 2)  # 呼叫平均时长
ali_append = [time, ali_used, ali_unused, ali_sub_daily, ali_call, ali_call_success,
              ali_call_success_rate, ali_call_max, ali_rel_add, ali_call_avg_time]
# 主动查询业务
lj_call_2min = daily_print[8]      # 主动查询2分钟以内呼叫成功总数
lj_call_b2min = daily_print[9]     # 主动查询大于2分钟（每分钟按一次计）呼叫成功分钟数
lj_call = lj_call_2min+lj_call_b2min  # 主动查询总呼叫成功数
lj_call_avg_time = round(daily_print[10], 2)    # 呼叫平均时长
lj_call_max = daily_print[11]         # 呼叫峰值
lj_income = round(lj_call*0.015, 2)   # 主动查询日收入，日报邮件内容里不要出现
dm_dsf_call = dm_dsf[0]               # 东盟多方总呼叫量
dm_dsf_call_success = dm_dsf[1]       # 呼叫成功量
dm_dsf_call_success_rate = round(dm_dsf_call_success/dm_dsf_call, 2)  # 呼叫成功率
dm_dsf_record = dm_dsf[3]+dm_dsf[4]   # 带录音呼叫成功量
dm_dsf_norecord = dm_dsf[1]+dm_dsf[2]-dm_dsf[3]-dm_dsf[4]  # 不带录音呼叫成功量
dm_dsf_call_max = dm_dsf[5]           # 呼叫峰值
dm_dsf_call_time_avg = round(dm_dsf[6], 2)      # 呼叫平均时长
dm_dsf_income = round((dm_dsf_record*0.015)+(dm_dsf_norecord*0.0125), 2)    # 东盟第三方收入
dm_income = lj_income + dm_dsf_income   # 东盟日收入
lj_append = [time, lj_call, lj_call_max, lj_call_avg_time, lj_call, 0, lj_income, dm_dsf_call, dm_dsf_call_success,dm_dsf_call_success_rate, dm_dsf_call_max, dm_dsf_call_time_avg, dm_dsf_record, dm_dsf_norecord,dm_dsf_income, dm_income]  # 东盟sheet里追加的内容
# 天润业务统计 同东盟第三方
tr_dsf_call = tr_dsf[0]
tr_dsf_call_success = tr_dsf[1]
tr_dsf_call_success_rate = round(tr_dsf_call_success/tr_dsf_call, 2)
tr_dsf_record = tr_dsf[3] + tr_dsf[4]
tr_dsf_norecord = tr_dsf[1] + tr_dsf[2] - tr_dsf_record
tr_dsf_call_max = tr_dsf[5]
tr_dsf_call_time_avg = round(dm_dsf[6], 2)
tr_incom = round((tr_dsf_record*0.015) + (tr_dsf_norecord*0.0125), 2)
tr_append = [time, tr_dsf_call, tr_dsf_call_success, tr_dsf_call_success_rate, tr_dsf_call_max,
             tr_dsf_call_time_avg, tr_dsf_record, tr_dsf_norecord, tr_incom]
# 微聊业务
wl_dsf_call = wl_dsf[0]
wl_dsf_call_success = wl_dsf[1]
wl_dsf_call_success_rate = round(wl_dsf_call_success/wl_dsf_call, 2)
wl_dsf_record = wl_dsf[3] + wl_dsf[4]
wl_dsf_norecord = wl_dsf[1] + wl_dsf[2] - wl_dsf_record
wl_dsf_call_max = wl_dsf[5]
wl_dsf_call_time_avg = round(wl_dsf[6], 2)
wl_incom = round((wl_dsf_record*0.015) + (wl_dsf_norecord*0.0125), 2)
wl_append = [time, wl_dsf_call, wl_dsf_call_success, wl_dsf_call_success_rate, wl_dsf_call_max,
             wl_dsf_call_time_avg, wl_dsf_record, wl_dsf_norecord, wl_incom]
# 朝花夕拾
zh_dsf_call = zh_dsf[0]
zh_dsf_call_success = zh_dsf[1]
zh_dsf_call_success_rate = round(zh_dsf_call_success/zh_dsf_call, 2)
zh_dsf_record = zh_dsf[3] + zh_dsf[4]
zh_dsf_norecord = zh_dsf[1] + zh_dsf[2] - zh_dsf_record
zh_dsf_call_max = zh_dsf[5]
zh_dsf_call_time_avg = round(zh_dsf[6], 2)
zh_incom = round((zh_dsf_record*0.015) + (zh_dsf_norecord*0.0125), 2)
zh_append = [time, zh_dsf_call, zh_dsf_call_success, zh_dsf_call_success_rate, zh_dsf_call_max,
             zh_dsf_call_time_avg, zh_dsf_record, zh_dsf_norecord, zh_incom]


'''dsf_call = daily_print[12]
dsf_call_success = daily_print[13]
dsf_call_success_b2min = daily_print[14]
dsf_call_success_record_2min = daily_print[15]
dsf_call_success_record_b2min = daily_print[16]
dsf_call_max = daily_print[17]
dsf_call_avg_time = daily_print[18]
dsf_call_success_rate = format(dsf_call_success/dsf_call,'2f')
dsf_call_record = dsf_call_success_record_2min + dsf_call_success_record_b2min
dsf_call_no_record = dsf_call_success + dsf_call_success_b2min - dsf_call_record
dsf_income = round((dsf_call_record * 0.015) + (dsf_call_no_record * 0.0125),2)
dsf_append = [time,dsf_call,dsf_call_success,dsf_call_success_rate,
dsf_call_max,dsf_call_avg_time,dsf_call_record, dsf_call_no_record, dsf_income]
'''
# 格式化输出
# info1='''********************************************阿里业务统计**********************************************
# 号码占用  号码剩余  当日绑定数  总呼叫量  呼叫成功量  呼叫成功率  呼叫峰值（呼/分钟)  净增量  呼叫平均时长
# {号码占用}  {号码剩余}  {当日绑定数}  {总呼叫量}  {呼叫成功量}  {呼叫成功率}  {呼叫峰值}  {净增量}  {呼叫平均时长}
# *********************************************************************************************************
# '''.format(号码占用=ali_used,号码剩余=ali_unused,当日绑定数=ali_sub_daily,总呼叫量=ali_call,呼叫成功量=ali_call_success,
#          呼叫成功率=ali_call_success_rate,呼叫峰值=ali_call_max,净增量=ali_rel_add,呼叫平均时长=ali_call_avg_time)
# print(info1)
# sql1='select count(*) as 号码占用 from t_smb_msisdn where dn in (select smbms from t_user_mobile_dz)'

# 调用写入Excel函数
intoexcel(append=ali_append, sheet='C小号业务')
intoexcel(append=lj_append, sheet='东盟信息港')
intoexcel(append=tr_append, sheet='天润融通')
intoexcel(append=wl_append, sheet='杭州微聊')
intoexcel(append=zh_append, sheet='朝花夕拾')
# (append=dm_dsf_append,sheet='多方接入业务')

# 读文件改时间 执行语句 结果计算 格式输出or写入Excel
