import numpy as np
import pandas as pd


def zDateFramecalculate():
    """
     数值计算和统计基础
    :return:
    """
    df = pd.DataFrame({'age': [4, 5, 6, np.nan, 3], 'score': [12, 3, np.nan, 6, 4], 'school': [78, 89, 45, '4', '33j']},

                      index=list('abcde'))
    print(df)
    print("------------------\n")
    """
     # 默认算的是每一列的均值，返回值类型 <class 'pandas.core.series.Series'>,行标签是之前的列名；
     # 计算时会自动忽略NaN，如何含有字符串则不会计算该列的均值
     print(type(df.mean())) 
     # 算每一行的均值，返回值类型  <class 'pandas.core.series.Series'> ,行标签就是之前的行标签；
     # 计算时会自动忽略NaN，自动舍弃非数字即会自动舍弃字符串
     print(df.mean(axis=1)) 
     # 不会进行过滤，NaN与任何数字计算都是NaN， axis默认为0,即相对于列
     print(df.mean(axis=1,skipna=False)) 
     # 统计每一列非NaN值的数量；返回值类型Series;行标签是之前的列名;   age 4 socre 4 school 5
     print(df.count(),type(df.count()))
     # 统计每一行中非NaN值的数量
     print(df.count(axis=1))
     # 统计每一列中的最小值; 如果该列中有NaN则会 忽略NaN 的值; 如果该列中有字符串则会 忽略该列 ；
     print(df.min())
     # 统计每一行中的最小值，如果该行中有NaN或字符串，则会 忽略NaN或字符串 的值;
     print(df.min(axis=1))
     # 累计求和，该列中只能有数字和NaN
     print(df['age'].cumsum())
     print(df[['age','score']].cumsum())
     # 累计求积
     print(df[['age', 'score']].cumprod())
     # 累计最大值 该列中只能有数字和NaN, cummin 累计最小值
     print(df['age'].cummax())
     print(df[['age','score']].cummax())
    """


def zSeriesOp():
    series1 = pd.Series(list("abcdedadcd"))
    # 唯一： 进行去重，得到一个ndarray 数组
    unique1 = series1.unique()
    # 统计series中各个值出现的次数，并且会根据出现次数的大小进行排序 ; 返回一个新的Series对象
    sc = series1.value_counts()
    # 设置sort为False则不会进行排序，返回一个新的Series对象
    sc1 = series1.value_counts(sort=False)
    sc2 = pd.value_counts(series1, sort=False)
    # 判断value是否在指定的 值列表 中 ； 返回一个布尔类型的Series对象; 该方法也可以用于DataFrame对象
    si = series1.isin(['a'])
    si1 = series1.isin(['a', 'c', 'b'])
    """
    print(series1)
    # ['a' 'b' 'c' 'd' 'e'] <class 'numpy.ndarray'>
    print(unique1,type(unique1))
    print(sc)
    print(sc2)
    print(si)
    """


def zstr():
    """
    通过 Series对象的str属性来操作Series中的字符串
    通过 str然后调用字符串的各种方法来操作字符串
    :return:
    """
    series1 = pd.Series(['aa', 'ca', 'nn', 'bba', np.nan, 1])
    df1 = pd.DataFrame({'key1': ['abc', 'dfa', 'cc'], 'key2': ['jj', 'adc', 'aavd']})
    # 统计series1中各个value中出现 'a'的次数； 只会操作字符串，如果value不是字符串，则该行为NaN
    r1 = series1.str.count('a')

    """
    # str.upper()只能操作字符串
    print(df1['key1'].str.upper())
    print(df1.columns.str.upper())
    """


def zconcat():
    """
    pandas 具有全功能的，高性能内存中连接操作，与SQL等关系数据库非常类似
    pd.merge(left,right,how='inner',on=None,left_on=None,right_on=None,left_index=False,
                        right_index=False,sort=True,suffixes=('_x','_y'),copy=True,indicator=False)
     left ：  拼接的第一个DataFrame对象
     right : 拼接的第二个DataFrame对象
     on : 参考那几列 on='key1'  参考left 和 right 的key1 ； on=['key1','key2'] 参考key1 和 key2 列

    df1.join(df2) 直接按照index进行拼接
    :return:
    """
    series1 = pd.Series([1, 2, 3])
    series2 = pd.Series([4, 3, 2])
    df1 = pd.DataFrame({'key1': [1, 3, 4], 'key2': [4, 2, 2]})
    df2 = pd.DataFrame({'jk': ['d', 'f'], 'hh': ['ss', 12]}, index=['row1', 'row2'])
    # 仅仅是简单的进行拼接，行索引与原来的行索引相同，0 1 2 0 1 2
    series3 = pd.concat([series1, series2])
    # 简单进行拼接，列数增加，行数增加，相应位置若无元素则用NaN填充
    df3 = pd.concat([df1, df2])
    # axis=1 沿水平方向进行拼接，列数增加
    series4 = pd.concat([series1, series2], axis=1)
    # join='innner' 只保留交集，默认为 ’outer'保留并集 ；
    # join_axes=[['a','b','c']] 在并集join='outer'，axis=1情况下，只保留哪几行
    # keys 层次索引 key=['one','two'] 拼接后第一个DataFrame的 标题行标签为 one，第二个DataFrame为 'two'; 如果是增加列 axis=1 ，则为列名
    series5 = pd.concat([series2, series1], axis=1, join='inner')
    """
    print(series3,type(series3))
    print(df3)
    print(series4)
    """
def zduplicated():
    series =pd.Series([1,1,3,4,1,3,2])
    # 返回一个布尔Series,  series.duplicated() 判断Series对象中的value是否重复
    duplicated = series.duplicated()
    # 去重； 并将去重后的数据返回，行标签还是对应之前的行标签； inplcae = True 则会对原数据进行改变，返回值变为none
    droped = series.drop_duplicates()
    # series.replcae('a',np.nan) 将 series中 的‘a'替换为NaN;
    # series.replcae(['a','b'],np.nan)替换多个
    # series.replace({'a':'jjj','bbbd':'kjj}) 以字典的形式进行替换。a替换为jjj,bbbd替换为kjj

    """
    print(duplicated,type(duplicated))
    # 去掉重复元素，行标签还是对应之前的行标签
    print(series[duplicated==True])
    """

zduplicated()
