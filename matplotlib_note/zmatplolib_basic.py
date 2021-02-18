import numpy as np
import pandas as pd
import matplotlib as mpb
import matplotlib.pyplot as plt



def zbasic():
    """
     图名，图例，轴标签，轴边界，轴刻度，轴刻度标签

    :return:
    """
    # 图表窗口  plt.show()
    """
    arr = np.random.randint(1, 100, size=100)
    plt.plot(arr)
    plt.show()
    """
    df1 = pd.DataFrame(np.random.rand(10, 2), columns=['a', 'b'])
    # figsize 创建图表窗口，设置窗口大小 ，也可以不设置
    df1.plot(figsize=(6, 4))
    # 设置表名
    plt.title('title')
    # 设置轴标签
    plt.xlabel('X-X')
    plt.ylabel('Y_Y')
    # 设置轴刻度
    plt.xticks(range(10))
    # 注释 ： 横坐标， 纵坐标，字符串，字体大小
    plt.text(5, 0.3, 'hhh', fontsize=12)
    # 显示网格； linestyle 设置网格样式； color 颜色； linewidth 线宽； axis 坐标轴可以为 x，y，默认both
    # plt.grid(True,linestyle='--',color='red',linewidth='1',marker='.' )
    """
     marker取值 ： ’.'    ','   '*'    'o'     'V'     '^'     '<'     '>'     '1'     '2'     '3'     '4'     '5'     's'     '-'     '|'
    """

    # 设置图例， 直接使用DataFrame对象进行画图会自动添加图例
    # plt.legend('best') 0 自适应； 'upper right' 1 ; 'upper left' 2 ; 'lower left' 2; 'lower right' 3
    # 'right' 5 ; 'center left' 6 ; 'center right' 7 ; 'low center' 8 ; 'upper center' 9 ; 'center' 10;
    plt.legend('upper center')
    # 隐藏坐标轴
    # plt.axis('off')
    # 图表输出,支持，png,pdf,svg... ; dpi 分辨率；
    # bbox_inches 图表需要保存的部分，如果设置为 'tight' 则尝试剪除图表周围空白的部分
    # facecolor,edgecolor 图像背景颜色，默认为'w' 白色
    plt.savefig('D:/save.png', dpi=400, facecolor='white', edgecolor='blue')
    plt.show()


def zsubplot():
    """
     在matplotlib中，整个图像为一个Figure对象
     在Figure对象中可以包含一个或者多个Axes对象
     每一个Axes(ax)对象都是一个拥有自己坐标系的绘图区域
    plt.figure(num=None,figsize=None,dpi=None,facecolor=None,edgecolor=None,
            frameon=True,FigureClass=<class 'matplotlib.figure.Figure'>,**kwargs)
    :return:
    """
    """
    # 子图的创建方式1 ，先建立子图在填充图表
    fig = plt.figure(facecolor='pink')
    ax1 = fig.add_subplot(2,2,1) # 2行2列的第一个子图
    # 在一张图上画  三个个 曲线
    ax1.plot(np.random.randint(30,40,size=10))
    # 会自动添加到上面的子图上
    plt.plot(np.random.randint(10,size=20),linestyle='--',marker='*')
    plt.plot(np.random.randint(20,30,size=10),linestyle=':',marker='1')
    
    ax2= fig.add_subplot(2,2,2)
    # 直方图
    ax2.hist(np.random.randint(10,20,size=100))

    ax4 = fig.add_subplot(2,2,4)
    df2 = pd.DataFrame(np.random.randint(20,40,size=(10,4)),columns=list('abcd'))
    ax4.plot(df2,alpha=0.5,linestyle='--',marker='*')
    plt.show()
    """
    """
    # 子图创建方式2 创建一个新的figure，并返回一个subplot对象的numpy数组
    # sharex ， sharey 是否共享 x轴 y轴的刻度 ；取值 'all', 'row', 'col', 'none'

    fig, axes = plt.subplots(2, 3, figsize=(10, 4), sharex='all', sharey='all')
    ts = pd.Series(np.random.randn(100).cumsum())
    # 生成图表对象的数组
    ax1 = axes[0, 1]
    axes[0, 2].hist(np.random.randint(10, 20, size=100))
    axes[0, 0].hist(np.random.randint(10, 20, size=100))
    axes[1, 2].hist(np.random.randint(10, 20, size=100))
    ax1.plot(ts)
    # 控制subplot之间的距离
    plt.subplots_adjust(wspace=0.5, hspace=250)
    plt.show()
    """
    """
    # 创建子图的方式 3
    df2 = pd.DataFrame(np.random.randint(20,40,size=(10,4)),columns=list('abcd'))
    df2.plot(style='--',grid=True,sharex=True,subplots=True,layout=(2,4))
    plt.show()
    """


def zgraphDraw():
    """
        图表类别： 线性图，柱状图，密度图，以横纵坐标两个维度为主
        plt.plot(kind='line',ax=None,figsize=None,use_index=True
                            title=None,grid=None, legend=False,
                            style=None,logx=False,loglog=False,
                            xticks=None,yticks=None,xlim=None,ylim=None,
                            rot=None,fontsize=None,table=False,
                            yerr=None,xerr=None,label=None,
                            secondary_y=False,**karg)
        kind 图表种类，line,bar,barh (折线图，柱状图。。
        label 图列标签 DataFrame以列名坐标标签
        style 风格字符串，-  .
        color 颜色
        alpha 透明度
        figsize 图像大小
        title 图名
        rot 图表旋转的角度
        use_index 是否使用index作为横坐标轴
        colormap 当有多个序列时可以选择画图时使用的色系 ， DataFrame中使用
    :return:
    """
    # series直接生成图表
    series = pd.Series(np.random.randint(1, 100, size=100))
    series = series.cumsum()
    """
    series.plot(kind='line',label='hehe',legend=True,style='--',
                color='r',alpha=0.4,grid=True,ylim=[0,3000],title='tes',
                figsize=(8,4),rot=45)
    """
    df = pd.DataFrame(np.random.randint(100, size=(50, 5)), columns=list('abcde'))
    # subplots是否画成子图
    df.plot(kind='line', legend=True, style='.-',
            colormap='viridis', grid=True, subplots=True)
    plt.show()


def zgraphDraw2():
    """
        柱状图 ，堆叠图
    柱状图： plt.plot(kind='bar') 或 plt.bar()
    :return:
    """
    fig, axes = plt.subplots(5, 1)
    series = pd.Series(np.random.randint(100, size=5), index=list('abcde'))
    df = pd.DataFrame(np.random.rand(10, 3), columns=list('abc'))
    """ 
    ## 将柱状图绘制到第0个子图上；  单系列柱状图
    series.plot(kind='bar',ax=axes[0])
    """
    ## 多系列柱状图
    df.plot(kind='bar', ax=axes[1])
    ## 多系列 堆叠图,设置stacked为True
    df.plot(kind='bar', stacked=True, ax=axes[2])
    # 多系列 柱状图
    df.plot.bar(ax=axes[3])
    # hist直方图
    df.plot.hist(ax=axes[4])

    ## 柱状图第二种绘制方法
    x = np.random.rand(10)
    y = np.sin(x)
    # facecolor 柱状图里面填充什么颜色，edgecolor 柱状图边框填充什么颜色
    plt.bar(x, y, width=1, facecolor='yellowgreen',
            edgecolor='white')

    plt.show()


def zgraphDraw3():
    """
    面积图，填图，饼图
        plt.plot.area()
        plt.fill(),plt.fill_between()
        plt.pie()
    :return:
    """

    ## 面积图
    fig, axes = plt.subplots(2, 1)
    df = pd.DataFrame(np.random.rand(10, 3), columns=list('abc'))
    #  通过 series.plot.area() 或 df.plot.area() 画面积图；
    #  可以设置stacked，默认为True，在为True时每列的坐标必须都是正值或都是负值；否则需要设置为False
    #  当数据有NaN时自动填充 0
    df.plot.area(colormap='Greens_r', alpha=0.5, ax=axes[0], stacked=False)

    ## 填图
    x = np.linspace(0, 4 * np.pi, 200)
    y = np.sin(x)
    y2 = np.sin(-x + 1)
    axes[1].fill(x, y, label='y1')
    axes[1].fill(x, y2, label='y2')
    axes[1].fill_between(x, y, y2, color='b', alpha=0.5, label='area')

    plt.show()


def zgraphDraw4():
    """
    直方图   密度图
    :return:
    """

    series = pd.Series(np.random.randn(1000))
    # 直方图
    """
        bins 箱子宽度
        histtype 风格  bar  step   stepfilled
        orientation 方向 水平或垂直， 'horizontal' 'vertical'
        align    'left' 'mid' 'right'  optional(对齐方式）
    """
    """
    series.hist(bins=20,histtype='bar',align='mid',
                orientation='vertical',alpha=0.5)
    """
    """
     # 密度图  , 
    series.plot(kind='kde',style='--')
    """
    plt.show()

def zgraphDraw5():
    """
     散点图 ，矩阵散点图
     plt.scatter() pd.scatter_matrix()
     matplotlib.pyplot.scatter(x, y, s=None, c=None, marker=None, cmap=None,
                                    norm=None, vmin=None, vmax=None, alpha=None,
                                    linewidths=None, verts=<deprecated parameter>,
                                    edgecolors=None, *, plotnonfinite=False, data=None, **kwargs)

     s : 散点大小.可以设置成一个标量
     c : 散点颜色,可以设置成一个值
     vmin,vmax : 亮度设置，标量
     cmap : colormap

    :return:
    """
    x = np.random.randn(1000)
    y = np.random.randn(1000)
    """
    plt.scatter(x,y,marker='*',
                s=np.random.rand(1000)*100,cmap='Reds',c=np.random.randn(1000)*100)
    """
    df = pd.DataFrame(np.random.randn(100,4),columns=list('abcd'))
    # 散点矩阵 ； diagonal ： hist直方图 或 kde 密度图
    # range_padding  每个坐标图中’点‘与’轴‘之间的距离
    pd.plotting.scatter_matrix(df,marker='*',diagonal='kde',
                               range_padding=0)
    plt.show()
zgraphDraw5()
