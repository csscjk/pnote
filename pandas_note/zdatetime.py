import numpy as np
import pandas as pd
import datetime  # datetime 属于python系统模块
from dateutil.parser import parse  # 将不含中文的日期字符串转为日期对象，


def zcreate():
    today = datetime.date.today()  # 获得今天的日期，date类型
    date1 = datetime.date(2015, 2, 7)  # 创建指定时间的date对象 2015-02-07  date类型 ,年月日
    now = datetime.datetime.now()  # 时间戳 ,获得此时此刻的时间 2021-02-10 16:40:16.656173 datetime类型，年月日时分秒
    datetime1 = datetime.datetime(2015, 2, 2)  # 2015-02-02 00:00:00
    delta = datetime1 - now  # 指定时间和当前时间相减 -2201 days, 7:09:46.384247
    delta1 = datetime.timedelta(100, 3600)  # 创建时间差对象，100天，3600秒
    datetime2 = parse('2018/1/1')  # 2018-01-01 00:00:00 <class 'datetime.datetime'>
    """
    print(today)
    print(date1)
    print(now)
    print(datetime1)
    print(delta)
    print(now-delta1)
    print(datetime2, type(datetime2))
    """




zcreate()
