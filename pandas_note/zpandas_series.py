import numpy as np
import pandas as pd


def zcreateSeries():
    """
    pandas 可以通过多维python列表来创建，但是只能通过一维numpy数组创建
    """
    se = pd.Series(['2', '3', 4], index=['t1', 't2', 't3'])
    se1 = pd.Series(range(3, 6))  # pd.Series([3,4,5])   索引默认为 0,1,2
    se2 = pd.Series([[1, 2, 3], [3, 'k'], []], index=['m1', 'm2', 'm3'])
    se3 = pd.Series(np.arange(4, 9))
    se4 = pd.Series(np.arange(5, 8), index=['a1', 'a2', 'a3'])
    se5 = pd.Series({'d1': [2], 'd2': [3, 'f'], 'd3': 5})  # index标签的值为字典key的值
    se6 = pd.Series({'dd1': 4, 'dd2': 9})
    se7 = pd.Series(30, index=range(3))  # 通过标量创建Series，总共3个值，均为30
    """
    print(se)
    print(se1)
    print(se2)
    print(se3)
    """
    print(se7)


def zslice():
    # 位置下标，标签索引，切片索引，布尔型索引
    se = pd.Series([[2], [3], 9])
    print(se[0], se[0:2])  # 位置下标不能使用负值
    se1 = pd.Series([list('row1'), list('tes2'), list('row3')], index=list('abc'))
    print(se1['a'], se1['a':'c'])
    print(type(se1['a']))  # 标签索引返回一行的值,一个list对象即列表
    print(type(se1[['b', 'a']]))  # 返回一个由指定行的值组成的Series对象, b行，a行
    print(se1[list('bb')])  # 返回一个Serise对象，b行，b行
    print(se1[se1.index == 'a'])


def zdataOp():
    """
    Series中数据查看，重新索引，对齐，添加，删除，修改
    :return:
    """
    # 数据查看
    se = pd.Series(np.arange(8))
    """
    print(se.head(2))  # 取前面指定行数的数据，默认取前5行
    print(se.tail(7))  # 取后面指定行数的数据，默认取后5行
    """
    # 重新索引 reindex
    se1 = pd.Series(np.arange(9, 13), index=list('abcd'))
    se2 = se1.reindex(['b', 'c', 'd', 'f'], fill_value=8)  # 从se1中选取指定列组成一个新的series，如果没有该该标签列则默认用NaN填充，否则用fill_value填充
    """
     print(se1, se2)
    """
    # 对齐
    se3 = pd.Series(np.arange(3), index=list('abc'))
    se4 = pd.Series(np.arange(7, 10), index=list('acf'))
    """
    print(se3+se4) # se3 和 se4 相应列进行加操作并返回由结果组成的一个Series，NaN加一个数还是NaN，se3没有f行，se4没有b行，所以结果Series b行和f行均为NaN
    """
    # 删除 drop
    se5 = pd.Series(np.arange(5), index=list('abcde'))
    se6 = se5.drop('a')  # 删除指定标签行，并返回剩下的标签行'bcde'行组成的一个Series ，inplace默认维False不会修改原数据，
    se7 = se5.drop(['b', 'c'])  # 删除多行，implace如果为True则会修改原数据
    """
    print(se6)
    print(se7)
    se8 = se5.drop('a',inplace=True)
    print(se5)
    """
    # 添加
    se8 = pd.Series(np.arange(4), index=list('abcd'))
    se8['f'] = [1, 2, 3]  # 有责修改无责添加
    se9 = pd.Series(np.arange(8, 9))
    se9[2] = 9999
    se10 = se8.append(se9)  # 不会修改原数据，在se8后面添加se9并将结果组成一个Series返回
    """
    print(se10)
    print(se8)
    """



zdataOp()
