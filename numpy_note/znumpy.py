import numpy as np
import os


def step():
    for i in range(1, 14, 4):
        print(i)
    arr = np.arange(1, 15, 2)  # np.arange(start,end+1,step)；np.arange(start,end+1) 步长默认为 1； np.arange(end+1) 从零开始步长为1；
    print(arr)


def zslice():
    arr = np.arange(10)
    arr1 = arr[1:8:2]  # arr[start:end+1:step] 步长默认为 1； arr[end+1] start为 0 ，步长为 1； arr[start:] end为该维结束位置的索引，步长为1 ；
    print(arr1)
    arr2 = arr[1:]
    print(arr2)
    arr3 = arr[arr > 3]  # 布尔接片，返回arr中该维所有大于3的元素
    print(arr3)
    print(arr[-1]) # 输出最后一个元素


def zstore():
    arr = np.arange(14).reshape(2, -1)
    # os.chdir('D:\\')  # os.chdir(指定路径） 改变工作路径，文件会被保存到当前指定的路径下
    # 保存为 npy 文件
    np.save('test', arr)  # np.save('自定义文件名',arr) 保存文件，并在指定的文件名后加上.npy后缀
    ar = np.load('test.npy')  # 加载指定的npy文件，必须带文件名后缀
    print(ar)
    # 保存为文本文件
    np.savetxt('test.txt', arr,
               delimiter=',')  # 保存为文本文件，不会自动添加后缀，delimiter 指定分割符，也可以不指定，默认为空格
    # ，也可以使用fat指定保存的格式，fat='%i'保存为整数，fat='%.2f'保留两位小数
    ar2 = np.loadtxt('test.txt', delimiter=',')  # 读取文本文件，如果文件的分隔符为空格则可以不使用delimiter指定。
    print(ar2)


def zrandom():
    arr = np.random.normal(size=(4, 4))  # np.random.normal(size=指定形状) 产生一个指定形状的标准正态分布的数组
    arr_1 = np.random.randn(4, 4)  # 返回一个4*4的正态分布数组，大于零小于1
    print(arr)
    arr2 = np.random.rand(
        5)  # 产生一个长度为5的一维数组，np.random.rand(num) 产生指定数量的浮点数，平均分布，数字在0到1之间，如果不指定num的值则返回一个数字，否则返回一个长度为num的数组
    print(arr2)
    arr3 = np.random.rand(2, 3, 4)  # 产生一个2*3*4的三维数组
    print(arr3)
    arr4 = np.random.random(10)  # 产生一个长度为10的一维数组，元素大于0小于1，如果不指定参数则返回一个大于0小于1的随机数。
    print(arr4)


zslice()
