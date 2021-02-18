import numpy as np
import pandas as pd


def zread_file():
    """
        read_table,read_csv,read_excel
    read_table 可以读取csv文件和txt文件
    read_csv 读取csv文件; csv文件数据以逗号进行分隔


    :return:
    """

    # delimiter 分割符，用于拆分的字符串，也可以用 seq = ',' 代替
    # header 用作列名的序号,用哪一行作为列名，默认为0（第一行）
    # index_col 指定某列为行索引，否则自动索引0，1，2...
    data1 = pd.read_table('data.txt', delimiter=',', header=0, index_col=1)

    # engine : 使用的分析引擎，可以选择C或者python，C引擎快但是python引擎功能更加完备
    # encoding ：指定字符集类型即编码，通常指定为utf8,解决乱码
    data2 = pd.read_csv('data.csv',engine='python',encoding='gbk')

    # io 文件路径
    # sheet_name 一个xlsx中有多张表时，可以使用该参数指定读取那张表，
    #           sheetname=0读取第一张表 返回值类型 <class 'pandas.core.frame.DataFrame'>，
    #           sheetname=[0,1]读取第一张和第二张表，返回一个字典
    #           sheetname=None 读取所有的表
    #           sheetname='学生名单' 读取名为'学生名单'的表
    # header 指定列名行，默认0即以第一行作为列名
    # index_col 指定索引列即指定某列为行标签
    data3 = pd.read_excel('data.xlsx',sheet_name=0)
    """
     print(data1)
     print(data2)
    """
    print(data3,type(data3))



zread_file()
