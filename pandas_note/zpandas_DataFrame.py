import numpy as np
import pandas as pd

"""
DataFrame相当于一个‘二维数组’，是一个表格型数据结构，包含一组有序的列，其列的值类型可以是数值，字符串，布尔值等
DataFrame中的数据以一个或多个二维块存放，不是列表，字典或一维数组结构 
DataFrame具有行标签index和列表签column
"""


def zcreateDataFrame():
    #  通过列表创建
    d1 = pd.DataFrame([[2, 3], [3]])  # 长度可以不同，以最长的长度为准，元素不够NaN代替
    d = pd.DataFrame([4, [8, 9]])  # 一维数组，不会报错，只有一列； [[8,9],4] 会报错，长度不同
    # 通过二维数组创建
    d2 = pd.DataFrame(np.arange(14).reshape(2, 7), columns=list('abcdefg'), index=['row1', 'row2'])
    # 通过字典创建
    d3 = pd.DataFrame({'names': 89, 'sex': ['d', 'f']})  # names 列的值在每一行都会是89，sex列的值在第一行为d，第二行为f
    d4 = pd.DataFrame({'names': [9, 8], 'sex': ['f', 'd']})  # 第一行 9 f 第二行 8 d    ; 此处两个列表的长度必须相同
    d5 = pd.DataFrame(d4, columns=['sex', 'names',
                                   'cre'])  # 重新指定列的顺序,并将结果组成的DataFrame返回，原数据不变，如果没有该列'cre' 则用NaN填充;
    d6 = pd.DataFrame(d4, columns=['sex'])  # 列数可以小于原数据的列数
    # 通过字典Series创建，各个Series长度可以不同，不够补NaN；如果给Series设置了标签则使用设置的行标签，并且会自动对齐。如果没有设置则使用0,1,2..
    dicS = {
        'sex': pd.Series(list("789"), index=list('cba')),
        'name': pd.Series(list('3456'), index=list('bcad'))  # 会先对列名进行排序，abcd
    }
    d7 = pd.DataFrame(dicS)
    # 通过列表字典创建，key会当作列名，不够补NaN
    listD = [{'one': 34, 'two': 89}, {'one': 90, 'two': 88, 'three': 99999}]
    d8 = pd.DataFrame(listD)
    d9 = pd.DataFrame(listD, columns=['two', 'one',
                                      'jk'])  # 提取listD中的 'one','two'，'jk' 列，没有则补NaN；columns指定了提取的列及列顺序  tow one jk
    # 通过字典字典创建，最外层的key作为列名，内层的key作为行名，不够补NaN
    dicD = {'name': {'sex': 34, 'age': 90}, 'school': {'sex': 44, 'age': 9090, 'killer': 89888}}
    d10 = pd.DataFrame(dicD)
    d11 = pd.DataFrame(dicD, index=['sex', 'a', 'b'])  # 返回指定行组成的Series，无则补NaN
    """
    print(d1)
    print(d2)
    print(d3)
    print(d4) 
    print(d4.index, "  ||   ", type(d4.index))
    print(d4.columns, "  ||   ", type(d4.columns))
    print(d4.values, "  ||   ", type(d4.values))  # d4.values 为numpy.ndarray
    print(d4)
    print(d5)
    print(d6)   
    print(d)
    print(d7)
    print(d8)
    print(d9)
    print(d10)
    print(d11)
    """


def zindex():
    """
    DataFrame既有行索引也有列索引，
    选择列、选择行、切片、布尔判断
    :return:
    """
    df1 = pd.DataFrame(np.arange(12).reshape(3, 4), index=list('abc'), columns=list('1234'))
    """
    print(df1['2']) # 返回一个Series 这种方式只能选取列，不能选取行； df1['a']将会报错
    print(df1[['1','2']]) # 返回一个DataFrame ，返回多列
    print(df1.loc['a'])  # 返回一个列表，行标签为原数据的列名
    print(df1.loc[['b', 'a']])  # 返回一个DataFrame ，由指定列组成行标签为选择的行名,排列顺序，b a
    print(df1[:1]) # 通过切片选取前1行，返回一个DataFrame
    print(df1.loc['a':'c']) # 索引行切片，末端包含
    print(df1.iloc[0])  # 按整数索引提取指定行，索引不能超过 行的最大长度-1，
    print(df1.iloc[-1])
    print(df1.iloc[1:3])
    print(df1.iloc[[0, 2, 1]])
    bd = df1>5  # 返回一个布尔DataFrame
    print(bd)
    print(df1.iloc[:2])
    print(df1[df1>5]) # 为True的位置的数据留下，False的位置的变为NaN
    bd1 = df1['1'] > 5
    print(bd1)  # 布尔Series ，一二行对应的位置为Flase，第三行对应的位置为True
    print(df1[bd1])  # 只会保留为True的位置对应的行的数据，只保留第三行。保留一整行，其他全部舍弃
    df2 = pd.DataFrame(np.random.randint(12, size=(3, 4)), index=list('abc'), columns=list('1234'))
    print(df2)
    bd2 = df2[['1', '2']] > 5  # 返回一个DataFrame
    print(bd2)
    print(df2[bd2])  # 返回一个DataFrame，bd2中没有的位置以及bd2中为False的位置全部变为NaN，bd2中为True的位置的数据保留；不舍弃，仅仅变为NaN
    print(df1['1'].loc[['a','b']])
    """


def zDataFrameOp():
    """
    DataFrame 数据查看，转置，添加，修改，删除，对齐，排序
    :return:
    """

    df1 = pd.DataFrame(np.arange(30).reshape(6, 5), columns=list("abcde"),
                       index=['row1', 'row2', 'row3', 'row4', 'row5', 'row6'])
    # 数据查看，转置，添加，修改，删除
    """
    print(df1.head())  # 默认查看前5行 ,也可以指定查看的行数
    print(df1.head(2))
    print(df1.tail())  # 默认查看后5行 ,也可以指定查看的行数
    print(df1.T) # 转置
    df1['a'] = 99999  # 修改指定列，全部为99999；如果指定值为列表则长度必须和之前相同 df1['a'] = list('abcedf')
    df1['hj'] = 99999  # 添加一列，该列值全部为99999
    df1.loc['jk']='jjjj' # 新增行或修改行，有则修改无责添加
    df1[['a','b','q']] = 'kkkk' # 操作多行，有责修改无责添加
    df1.iloc[::2] = 'jjjjjjj--j' # 操作多行
    del df1['a'] # 删除指定列
    df1.drop('row1') # 删除一行
    df1.drop(['row1','row2']) # 删除多行
    df1.drop(['row1','row2'],inplace=True) # 删除多行并改变原数据
    df1.drop('a',axis=1) # 删除指定列，   df1+df2 对齐操作，无责补NaN，有则相加，行列相交点确定一个位置
    """
    # 排序
    df2 = pd.DataFrame(np.arange(15).reshape(3, 5), columns=list('abcde'), index=list('123'))

    """
    print(df2)
    print(df2.sort_values(['a'], ascending=True))  # 以 'a' 列为基准按照升序排序
    print(df2.sort_values(['a'], ascending=False))  # 以 'a' 列为基准按照降序排序
    print(df2.sort_values(['a', 'c'], ascending=False))  # 以 'a','c' 列为基准按照降序排序，先比较 'a'列，再比较 'c'列
    print(df2.sort_index())  # 按照行标签进行排序，默认剩下 ascending = False 降序
    """



zDataFrameOp()
