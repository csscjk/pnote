import numpy as np
import pandas as pd
import datetime

"""
Pandas时刻数据：Timestamp
时刻数据代表时间点，是pandas的数据类型，是将值与时间点相关联的基本类型的时间序列数据
pandas.Timestamp()
"""


def zcreate():
    date1 = '2017/1/1'
    date2 = datetime.datetime(2013, 2, 1, 10)
    # Timestamp直接将直接将  单个 ”时间数据“生成Timestamp对象
    timestamp1 = pd.Timestamp(date1)
    timestamp2 = pd.Timestamp(date2)
    # to_datetime,如果是单个数据则生成Timestamp对象，多个”时间数据“生成DatetimeIndex
    timestamps1 = pd.to_datetime(date1)
    timestamps2 = pd.to_datetime(date2)
    list_times = ['2012/1/1', '2012-2-23', '3/2/2013']
    timestamps3 = pd.to_datetime(list_times)
    """
    print(timestamp1, type(timestamp1)) # 2017-01-01 00:00:00 <class 'pandas._libs.tslibs.timestamps.Timestamp'>
    print(timestamp2, type(timestamp2)) # 2013-02-01 10:00:00 <class 'pandas._libs.tslibs.timestamps.Timestamp'>
    print(timestamps1, type(timestamps1))  # 2017-01-01 00:00:00 <class 'pandas._libs.tslibs.timestamps.Timestamp'>
    print(timestamps2, type(timestamps2))  # 2013-02-01 10:00:00 <class 'pandas._libs.tslibs.timestamps.Timestamp'>
    # DatetimeIndex(['2012-01-01', '2012-02-23', '2013-03-02'], dtype='datetime64[ns]', freq=None) <class 'pandas.core.indexes.datetimes.DatetimeIndex'> 
    print(timestamps3,type(timestamps3))
    print(pd.Timestamp('4/3/2013')) # 2013-04-03 00:00:00
    """


def ztimestampindex():
    """
    时间戳索引：DatetimeIndex
    时间序列：以DatetimeIndex为index的Series
    核心：pd.date_range(start=None,end=None,freq='D',tz=None,normalize=False,name=None,closed=None,**kwargs) 日期范围生成，生成日期范围
        start开始时间
        end 结束时间
        freq频率  pd.date_range默认为天,pd.bdate_range默认为工作日，  fre='D' 日; 'B' 工作日;  'H' 小时；
                                                                             'T'或 ’MIN‘ 分
                                                                             'S' 秒； 'L' 毫秒;  'U' 微秒;
                                                                  'W-MON'  周 ; 从星期几开始算起, 星期几所写 MON/TUB/WED/THU/FRI/SAT/SUN
                                                                  'WOM-2MON' 每月的第几个星期几开始算; 每月的第2个星期一
                                                                  'M' 每月的最后一个日历日即每月最后一天
                                                                  'Q' 月 ，
        tz时区
        periods 偏移量
        normalize 如果为True会将时间归一到 0分0秒

    两种生产方式： 第一种：start+end，第二种：start/end + periods
    默认频率day
    :return:
    """
    datetimeIndex = pd.DatetimeIndex(['2012-01-01', '2012-02-23', '2013-03-02'])
    timeSeries = pd.Series(np.arange(3), index=datetimeIndex)
    # pd.date_range
    range1 = pd.date_range('1/2/2014', '2/25/2014')  # 生成一个DatetimeIndex 日期从2014-01-02  到  2014-02-25
    range2 = pd.date_range(start='1/2/2014', periods=10)  # 产生一个DatetimeIndex 从2014-01-02开始，每次增加一天 ，产生10个时间串 至01-11结束
    range3 = pd.date_range(end='1/2/2014', periods=3)  # 到2014-01-02结束 ，3个时间串
    # 返回由工作日组成的DatetimeIndex  ['2017-02-03', '2017-02-06', '2017-02-07', '2017-02-08','2017-02-09', '2017-02-10']
    range4 = pd.bdate_range('2017/2/3', '2017/2/10')
    range5 = pd.bdate_range(start='2013/2/3', periods=10)  # 产生一个DatetimeIndex，由10个工作日组成
    """
    # DatetimeIndex(['2012-01-01', '2012-02-23', '2013-03-02'], dtype='datetime64[ns]', freq=None) 
    # <class 'pandas.core.indexes.datetimes.DatetimeIndex'>
    print(datetimeIndex,type(datetimeIndex))
    # 2012-01-01    0
    # 2012-02-23    1
    # 2013-03-02    2
    # dtype: int32 <class 'pandas.core.series.Series'>
    print(timeSeries,type(timeSeries))
    print(range1)
    print(range2)
    print(range3)
    print(range4)
    print(list(range4)) # DatatimeIndex变成由时间戳Timestamp组成的列表
    print(range5)
    """


ztimestampindex()
