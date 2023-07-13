import matplotlib
matplotlib.use('QtAgg')  # 或者 'QtAgg'
import matplotlib.pyplot as plt
import numpy as np

def fun_BarName(a=5):
    BarName = ['D10', 'D13', 'D16', 'D19', 'D22', 'D25', 'D29', 'D32', 'D36', 'D39', 'D43', 'D50', 'D57']
    return BarName[a]

def fun_BarNo(a=5):
    BarNo=[3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 14, 16, 18]
    return BarNo[a]

def fun_BarDb(a=5):
    BarDb=[0.953, 1.27, 1.59, 1.91, 2.22, 2.54, 2.87, 3.22, 3.58, 3.94, 4.3, 5.02, 5.73]
    return BarDb[a]

def fun_BarAb (a=5):
    BarAb=[0.7133, 1.267, 1.986, 2.865, 3.871, 5.067, 6.469, 8.143, 10.07, 12.19, 14.52, 19.79, 25.79]
    return BarAb[a]

def fun_BarL (a=5):
    BarL=['3#', '4#', '5#', '6#', '7#', '8#', '9#', '10.1', '11.3', '12.4', '13.5', '15.8', '18#']
    return BarL[a]

# 設定矩形尺寸
def func_beam(dd=-1, b=35, h=60,EpslonS=0.005, BarAsi=5, NumAs=2, NumOfBarAsP=0,
              Es=2040000, fy=4200, ic=-1, layer=1, NumAs2=2, BarAsPi=5):
    def draw_circles(x1, x2, n, D, y1):
        x_centers = np.linspace(x1, x2, n)
        x_ranges = [(x, x + D) for x in x_centers]

        for (x_min, x_max) in x_ranges:
            draw_circle = plt.Circle((x_min, y1), D/2, facecolor='k', fill=True)
            ax.add_patch(draw_circle)

    def comment_x(x1, y1, x2, y2, offset,str1='',str2='cm'):
        plt.plot([x1, x2], [y1-offset, y2-offset], [x1, x1], [y1-offset-1, y1-offset+1], [x2, x2], [y2-offset-1, y2-offset+1], color='k')
        ax.text((x1+x2)/2, y1-offset, f'{str1}' + f'{  round(x2-x1, 2)}' + f'{str2}', ha='center', va='center', multialignment='center', backgroundcolor='w')

    def comment_y(x1, y1, x2, y2, offset,str1='',str2='cm'):
        plt.plot([x1-offset, x2-offset], [y1, y2], [x1-offset-1, x1-offset+1], [y1, y1], [x2-offset-1, x2-offset+1], [y2, y2], color='k')
        ax.text(x1-offset, (y1+y2)/2, f'{str1}' + f'{round(y2-y1, 2)}\n'+ f'{str2}', ha='center', va='center', multialignment='center', backgroundcolor='w')
    def comment_y2(x1, y1, x2, y2, offset,str1='',str2='cm'):
        plt.plot([x1+offset, x2+offset], [y1, y2], [x1+offset-1, x1+offset+1], [y1, y1], [x2+offset-1, x2+offset+1], [y2, y2], color='k')
        ax.text(x1+offset, y2+13, f'{str1}' + f'{round(y2-y1, 2)}\n'+ f'{str2}', ha='center', va='center', multialignment='center', backgroundcolor='w')
    def comment_s(x1, y1, x2, y2, offset,str1=0):
        plt.plot([x1, x2], [y1-offset, y2-offset], [x1, x1], [y1-offset-1, y1-offset+1], [x2, x2], [y2-offset-1, y2-offset+1], color='k')
        ax.text((x1+x2)/2, y1-offset, f'{round(str1,4)}', ha='center', va='center', multialignment='center', backgroundcolor='w')
    # b = 35
    # h = 60
    origin_x = 0
    origin_y = 0
    # db = 2.54
    # NumAs=2
    # BarNo2=2
    # layer = 1
    # dbs = 2.54
    # n3=2
    # fy=4200
    # Es=2040000
    # EpslonS = 0.005
    BarName3 = fun_BarName(BarAsPi)
    BarName = fun_BarName(BarAsi)
    db = fun_BarDb(BarAsi)
    dbs = fun_BarDb(BarAsPi)
    if dd <= 0 and ic <= 0:
        ic=6.5
        dd=h-ic
    elif dd <= 0:
        dd=h-ic
    else:
        ic = h-dd-db/2




    # 創建圖形物件和軸物件
    fig = plt.figure()
    ax = fig.add_subplot()

    # 繪製矩形
    rectangle = plt.Rectangle((origin_x, origin_y), b, h, edgecolor='black', facecolor='none', fill=True)
    ax.add_patch(rectangle)

    # 繪製箍筋矩形
    # ic = 6.5

    rectangle2 = plt.Rectangle((origin_x+ic, origin_y+ic), b-ic*2, h-ic*2, edgecolor='black', facecolor='none', fill=True, linewidth=1.27)
    ax.add_patch(rectangle2)

    # 繪製拉力鋼筋
    # db = 2.54
    # BarNo=2
    # BarNo2=2
    # layer = 1
    if layer == 2:
        n = 2
        x1 = origin_x + (h-dd)
        x2 = origin_x + b - (h-dd)
        d = origin_y + (h-dd)
        draw_circles(x1, x2, NumAs, db, origin_y + (h-dd))
        draw_circles(x1, x2, NumAs2, db, origin_y + (h-dd) + 2.5 + db)
        ax.text(origin_x + b/2, origin_y + 20, f'{NumAs+NumAs2} {BarName}', ha='center')
    elif   layer == 1:
        n = NumAs
        x1 = origin_x + (h-dd)
        x2 = origin_x + b - (h-dd)
        d = origin_y + (h-dd)
        draw_circles(x1, x2, n, db, origin_y + (h-dd))
        ax.text(origin_x + b/2, origin_y + 20, f'{n} {BarName}', ha='center')

    # 繪製壓力鋼筋
    # dbs = 2.54
    # n3=2
    if NumOfBarAsP != 0:
      draw_circles(x1, x2, NumOfBarAsP, dbs, origin_y + h - ic - dbs/2)
      ax.text(origin_x + b/2, h-d-10, f'{NumOfBarAsP} {BarName3}', ha='center')

    # 繪製註解線和尺寸標註
    comment_x(origin_x, origin_y, origin_x+b, origin_y, 10)
    comment_y(origin_x, origin_y, origin_x, origin_y+h, 35 )
    comment_y(origin_x, d, origin_x, origin_y+h, 15)


    # 應變圖
    # fy=4200
    # Es=2040000

    EpslonY = fy / Es
    EpslonC = 0.003
    Epslon_n=4000
    Epslon_offset=(origin_x+b)+50
    x_b = [Epslon_offset-Epslon_n*EpslonY,Epslon_offset,Epslon_offset,Epslon_offset+Epslon_n*EpslonC,Epslon_offset-Epslon_n*EpslonY]
    y_b = [d,d,h,h,d]
    #plt.plot(x_b, y_b, 'k-',linestyle="--")
    plt.plot(x_b, y_b, 'k--')
    x_s = [Epslon_offset-Epslon_n*EpslonS,Epslon_offset,Epslon_offset,Epslon_offset+Epslon_n*EpslonC,Epslon_offset-Epslon_n*EpslonS]
    y_s = [d,d,h,h,d]
    # plt.plot(x_s, y_s, 'k-',linestyle="-")
    plt.plot(x_s, y_s, 'k-')
    print(EpslonY)
    comment_y2(Epslon_offset, d+(1-EpslonC/(EpslonY+EpslonC))*(h-d), Epslon_offset, origin_y+h, 70,str1='xb ')
    comment_y2(Epslon_offset, d+(1-EpslonC/(EpslonS+EpslonC))*(h-d), Epslon_offset, origin_y+h, 30,str1='x ')
    comment_s(x_b[0], y_b[0], x_b[1], y_b[1], 10-2,str1=EpslonS)
    comment_s(x_s[2], y_s[2], x_s[3], y_s[3], -10+2,str1=EpslonC)
    # 設定坐標軸範圍
    ax.axis('equal')
    ax_offset = 22

    ax.set_ylim(-ax_offset, h+ax_offset+5)
    ax.set_xlim(-ax_offset-40, b+ax_offset+120)
    plt.title('Beam')


    # # 顯示圖形
    A=plt.show()
    return A
#singe_beam()

def funcT_beam(dd=-1, be = 50,bw = 50.0,h =80.0,hf = 15.0,ic = -1, NumAs = 2,
               NumAs2 = 2,layer = 1, NumOfBarAsP = 2,fy=4200,Es=2040000,
               EpslonS = 0.001, BarAsi=5 , BarAsPi=5):
    # 定義T型梁的尺寸
    # be = 50
    # bw = 50.0
    # h =80.0
    # hf = 15.0       T
    origin_x=0
    origin_y=0
    # ic = 6.5
    # db = 2.54
    # BarNo = 2
    # BarNo2 = 2
    # layer = 1
    # dbs = 2.54
    # n3 = 2
    # fy=4200
    # Es=2040000
    # EpslonS = 0.001
    BarName3 = fun_BarName(BarAsPi)
    BarName = fun_BarName(BarAsi)
    db = fun_BarDb(BarAsi)
    dbs = fun_BarDb(BarAsPi)
    if dd == -1 and ic ==-1:
        ic=6.5
        dd=h-ic
    elif dd == -1:
        dd=h-ic
    else:
        ic = h-dd-db/2


    def draw_circles(x1, x2, n, D, y1):
        x_centers = np.linspace(x1, x2, n)
        x_ranges = [(x, x + D) for x in x_centers]

        for (x_min, x_max) in x_ranges:
            draw_circle = plt.Circle((x_min, y1), D/2, facecolor='k', fill=True)
            ax.add_patch(draw_circle)

    def comment_x(x1, y1, x2, y2, offset,str1='',str2='cm'):
        plt.plot([x1, x2], [y1-offset, y2-offset], [x1, x1], [y1-offset-1, y1-offset+1], [x2, x2], [y2-offset-1, y2-offset+1], color='k')
        ax.text((x1+x2)/2, y1-offset, f'{str1}' + f'{  round(x2-x1, 2)}' + f'{str2}', ha='center', va='center', multialignment='center', backgroundcolor='w')

    def comment_y(x1, y1, x2, y2, offset,str1='',str2='cm'):
        plt.plot([x1-offset, x2-offset], [y1, y2], [x1-offset-1, x1-offset+1], [y1, y1], [x2-offset-1, x2-offset+1], [y2, y2], color='k')
        ax.text(x1-offset, (y1+y2)/2, f'{str1}' + f'{round(y2-y1, 2)}\n'+ f'{str2}', ha='center', va='center', multialignment='center', backgroundcolor='w')
    def comment_y2(x1, y1, x2, y2, offset,str1='',str2='cm'):
        plt.plot([x1+offset, x2+offset], [y1, y2], [x1+offset-1, x1+offset+1], [y1, y1], [x2+offset-1, x2+offset+1], [y2, y2], color='k')
        ax.text(x1+offset, y2+20, f'{str1}' + f'{round(y2-y1, 2)}\n'+ f'{str2}', ha='center', va='center', multialignment='center', backgroundcolor='w')
    def comment_s(x1, y1, x2, y2, offset,str1=0):
        plt.plot([x1, x2], [y1-offset, y2-offset], [x1, x1], [y1-offset-1, y1-offset+1], [x2, x2], [y2-offset-1, y2-offset+1], color='k')
        ax.text((x1+x2)/2, y1-offset, f'{round(str1,4)}', ha='center', va='center', multialignment='center', backgroundcolor='w')


    # 繪製T型梁
    x = [0, be, be, be-(be-bw)/2, be-(be-bw)/2, (be-bw)/2 , (be-bw)/2, 0,0]
    x =[i+origin_x for i in x]
    y = [h, h, h-hf, h-hf, 0, 0, h-hf, h-hf, h]
    y =[i+origin_y for i in y]
    fig, ax = plt.subplots()
    plt.plot(x, y, 'k-')
    # ic = 6.5
    rectangle2 = plt.Rectangle((x[5]+ic, y[5]+ic), bw-ic*2, h-ic*2, edgecolor='black', facecolor='none', fill=True, linewidth=1.27)
    ax.add_patch(rectangle2)

    # 繪製拉力鋼筋
    # db = 2.54
    # BarNo = 2
    # BarNo2 = 2

    # layer = 1
    if layer == 2:
        x1 = x[5] + ic + db/2
        x2 = x[5] + bw - ic - db/2
        d = y[5] + ic + db/2
        draw_circles(x1, x2, NumAs, db, origin_y + ic + db/2)
        draw_circles(x1, x2, NumAs2, db, origin_y + ic + db/2 + 2.5 + db)
        ax.text(x[5] + bw/2, y[5] + h/4, f'{NumAs+NumAs2}  {BarName}', ha='center')
    elif layer == 1:
        x1 = x[5] + ic + db/2
        x2 = x[5] + bw - ic - db/2
        d = y[5] + ic + db/2
        draw_circles(x1, x2, NumAs, db, origin_y + ic + db/2)
        ax.text(x[5] + bw/2, y[5] + h/4, f'{NumAs} {BarName}', ha='center')
    # 繪製壓力鋼筋
    # dbs = 2.54
    # n3 = 2
    if NumOfBarAsP != 0:
        draw_circles(x1, x2, NumOfBarAsP, dbs, origin_y + h - ic - dbs/2)
        ax.text(x[5] + bw/2, y[5] + h*3/4, f'{NumOfBarAsP} {BarName3}', ha='center')


    # 設置圖形屬性
    ax.axis('equal')
    plt.title('T-Beam')



    # 繪製註解線和尺寸標註

    comment_x(x[5], y[5], x[5]+bw, y[5], 15)
    comment_x(x[0], y[0], x[1], y[1],-15)
    comment_y(x[5], y[5], x[5], y[5]+h, (be-bw)/2+60)
    comment_y(x[5], d, x[5],y[5]+h,(be-bw)/2+20)

    # 應變圖
    # fy=4200
    # Es=2040000
    EpslonY = fy / Es
    # EpslonS = 0.001
    EpslonC = 0.003
    Epslon_n=4000
    Epslon_offset=(origin_x+be)+30
    x_b = [Epslon_offset-Epslon_n*EpslonY,Epslon_offset,Epslon_offset,Epslon_offset+Epslon_n*EpslonC,Epslon_offset-Epslon_n*EpslonY]
    y_b = [d,d,h,h,d]
    plt.plot(x_b, y_b, 'k-',linestyle="--")
    x_s = [Epslon_offset-Epslon_n*EpslonS,Epslon_offset,Epslon_offset,Epslon_offset+Epslon_n*EpslonC,Epslon_offset-Epslon_n*EpslonS]
    y_s = [d,d,h,h,d]
    plt.plot(x_s, y_s, 'k-',linestyle="-")
    print(EpslonY)
    comment_y2(Epslon_offset, d+(1-EpslonC/(EpslonY+EpslonC))*(h-d), Epslon_offset, origin_y+h,100,str1='xb ')
    comment_y2(Epslon_offset, d+(1-EpslonC/(EpslonS+EpslonC))*(h-d), Epslon_offset, origin_y+h,40,str1='x ')
    comment_s(x_b[0], y_b[0], x_b[1], y_b[1], 20,str1=EpslonS)
    comment_s(x_s[2], y_s[2], x_s[3], y_s[3], -20,str1=EpslonC)


    # 顯示圖形
    A=plt.show()
    return  A
#funcT_beam()