# -> 序列.
"""
list1 = [1, 3, 4, 5]
list2 = [3, 4, 5]
list3 = list1 + list2  # 序列连接
print("序列连接", list3)
list4 = list1 * 2  # 序列重复
print("序列重复", list4)

# -> 输入 input
int_value = int(input("输入一个整数："))
print("int_value: ", int_value)

# -> 元组比较大小
tuple1 = (1, 2)
tuple2 = (2, 4)
tuple3 = (0, 5)
print("(1,2)<(2,4):", tuple1 < tuple2) # True
print("(1,2)<(0,5):", tuple1 < tuple3) # False
print("(2,4)>(0,5):", tuple2 > tuple3) # True
tuple1 = (1, 2)
tuple2 = (2, )
print("(1,2)<(2,):", tuple1 < tuple2) # True

# -> 字典推导式
list4 = ['name','sex','gender']
tuple4 = {i:0 for i in list4}
print("列表推导式:",tuple4) # 列表推导式: {'name': 0, 'sex': 0, 'gender': 0}

# ->文件操作,文件内建函数和方法
# open()打开文件,得到文件对象，
# 文件对象的方法：
#   read() 读取文件所有内容，readline()读取一行返回一个字符串，readlines()读取多行返回一个列表，
#   seek(pos，offset) 在文件内移动，
#       offset 为0表示从文件头开始偏移，1表示从当前位置开始偏移 默认，2从文件结尾开始偏移
#   write() 向文件中写入内容， close() 关闭文件，tell() 得到文件指针的位置
fl = open("test.txt",'w')
fl.write("a test")
fl.close()
# ---
fl = open("test.txt")
print("文件指针的位置:", fl.tell())  # 文件指针的位置: 0
begin = fl.read(1)
print("第一个字符:", begin)  # 第一个字符: a
print("文件指针的位置:", fl.tell())  # 文件指针的位置: 1
fl.seek(0)  # 回到文件开头
print(fl.tell())  # 0

# ->异常检测和处理
try:
    print(1/0)
except (ValueError,AttributeError,ZeroDivisionError) as e:
    print("----",e)
except Exception as e:
    print("捕获所有异常:",e)
finally:
    print("测试结束")

# --- 自定义异常信息
try:
    raise NameError("猪猪猪") # 通过raise关键字产生一个NameError 异常
except NameError as e:
    print("自定义异常信息:",e)
finally:
    print("自定义异常结束")

# -> 函数作用域
global_1 = 'test_global_1'
global_2 = 'test_global_2'
def test_global():
    global_1 = '函数内部变量—1'
    global global_2  # 必须先声明，不能直接global global_2 = '在函数内部定义全局变量'
    global_2 = '在函数内部定义全局变量'
    print("函数内部global_1:", global_1)
    print("函数内部global_2:", global_2)


print("函数外部global_1:", global_1)  # 函数外部global_1: test_global_1
print("函数外部global_2", global_2)  # 函数外部global_2 test_global_2
test_global()
# 函数内部global_1: 函数内部变量—1
# 函数内部global_2: 在函数内部定义全局变量
print("函数外部global_1:", global_1)  # 函数外部global_1: test_global_1
print("函数外部global_2", global_2)  # 函数外部global_2 在函数内部定义全局变量

# ->函数迭代器
def iterator(start, stop, step):
    x = start
    while x < stop:
        yield x # 每次执行到这个位置，便停止，并记录当前位置，下次会从这个地方继续
        x += step

for i in iterator(1,4,0.5):
    print(i)
    # 1
    # 1.5
    # 2.0
    # 2.5
    # 3.0
    # 3.5

# ->python内建函数
# filter(lambda表达式) 返回满足条件的元素
# map函数对各个元素分别处理然后返回
# zip函数 ，将两个元组合并成包含是元组的元组，实现字典键值位置的转换
# reduce函数
list_test = [1, 3, 4, 6, 9]
result = list(filter(lambda x:x>4,list_test))
print(result) # [6, 9]
result = list(map(lambda x : x+4,list_test)) # 注意此处直接使用 x+4.而不是 x = x+4
print(result) # [5, 7, 8, 10, 13]
dict1 = {'name':'test','age':12}
new_dict = dict(zip(dict1.values(),dict1.keys()))
print(new_dict) # {'test': 'name', 12: 'age'}
tuple1 = (1,4,5)
tuple2 = (4,1,9)
tuple3 = tuple(zip(tuple1,tuple2)) # tuple() 类型转换
print(tuple3) # ((1, 4), (4, 1), (5, 9))

# ->闭包
def outter(a):
    def inner(b):
        return b + a

    return inner

test_closure = outter(3)
print(test_closure(4))  # 7

# 装饰器
def tips(func): # 函数
    def inner(a,b):# 形参
        print("start:")
        func(a,b)
        print("end")
    return inner

@tips
def add(a,b):
    print("add--inner",a+b)
    return "add__return" # 实际并不会返回值

print(add(3,5))
# start:
# add--inner 8
# end
# None



# ->装饰器 ，传参
def new_tips(arg): # 参数
    def tips(func): # 函数
        def inner(a, b):# 形参
            print("start:", arg)
            func(a, b)
            print("end")

        return inner

    return tips  # 此处返回的是第二层函数


@new_tips("装饰器传参")
def add(a, b):
    print("add--inner", a + b)
    return "jk"


print(add(3, 5))
# start: 装饰器传参
# add--inner 8
# end
# None



# ->类
class Test():
    # 在成员变量前加上两个下划线 __ 则改变了必须通过方法来访问，无法直接通过对象.成员变量的形式访问
    __private_variable = 12

    # 该方法可以通过对象.方法的形式访问
    def __init__(self):
        print("Test_Begin")

    # 方法前加两个下划线 __ 则无法通过 对象.方法 的形式访问该方法
    def __add(self):
        self.__private_variable += 11

    def add(self):
        self.__add()

    def out(self):
        print(self.__private_variable)


test = Test()
test.out()
test.add()
test.out()

class Par:
    def __init__(self):
        print("par")


class Son(Par):
    def __init__(self):
        print("son")
        super().__init__()  # 如果不写此行代码，则父类的构造器不会被调用


son = Son()
print(isinstance(son, Par))  # 判断一个实例是否是一个类的类型或其子类的类型

# -> 自定义with语句
class Testwith: # 使用class关键字定义一个类！！！
    def __enter__(self): # 进入
        print("begin")

    def __exit__(self, exc_type, exc_val, exc_tb): # 结束 ,traceback
        if exc_tb is None:
            print("normal__正常")
        else:
            print("有错")


with Testwith():
    print("tets---runn")

# -> 正则表达式
import re

# 匹配年月日，并取出年月日
# 在字符串前加 r 取消转义，这样在字符串表示 \d 时便不用写成\\d
p = re.compile(r'(\d+)-(\d+)-(\d+)')
# print(p.match("2019-03-12")) # match 完全匹配，如果不完全匹配返回None且不能调用group方法否则报错，若完全匹配则返回匹配对象
# print(p.search("aa2019-03-12bbb") # search不完全匹配只要有就行，若有则返回匹配对象
# print(p.match('2019-02-12').group(1)) #匹配对象的group方法，2019 ,此处是group(zf_index),index从1开始
print(p.match("2019-02-45"))
year, month, day = p.match("2019-02-11").groups()  # 注意此处时groups()，匹配对象的groups方法
print("year: %s" % year, "month: %s" % month, "day: %s" % day) # year: 2019 month: 02 day: 11

# re库中的sub函数实现字符替换，sub(pattern，new_letters,variable)
variable = "12-1-1"
va = re.sub(r"\D","",variable)
print("variable: %s"%variable) # variable: 12-1-1
print("va: %s"%va ) # va: 1211

# 日期和时间库
import time

print(time.time())  # 输出1971.10.01 到现在所经历过的秒数
print(time.localtime()) # 返回当前的年月日等时间信息
print(time.strftime('%Y-%m-%d %H-%M-%S')) # 将当前时间以指定的形式输出 2020-10-15 13-03-30

import numpy as np
test = np.arange(10)
print(test)
test_1 = test
print(test_1)
test_1 = test_1*3
print(test_1)
print(test)
"""
# pandas: Series,DataFrame
