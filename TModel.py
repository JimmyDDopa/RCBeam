import math

vbCr = '\n'
global AreaSelectedAs ,NumOfBarAs,RhoSelectedAs,RhoSelectedAsp,NumOfBarAsP,AreaSelectedAsp,SpaceAsp,SpaceAs
dic={'D10': (0.953, 0.71),
 'D13': (1.27, 1.27),
 'D16': (1.59, 1.99),
 'D19': (1.91, 2.87),
 'D22': (2.22, 3.87),
 'D25': (2.54, 5.07),
 'D29': (2.87, 6.47),
 'D32': (3.22, 8.14),
 'D36': (3.58, 10.07),
 'D43': (4.3, 14.52),
 'D57': (5.73, 25.79)}

def solve_quadratic_equation(a, b, c):
    discriminant = b**2 - 4*a*c
    X = []

    if discriminant > 0:
        # 有二個實根
        x1 = (-b + math.sqrt(discriminant)) / (2*a)
        x2 = (-b - math.sqrt(discriminant)) / (2*a)
        X = [x1, x2]
    elif discriminant == 0:
        # 有一個實根
        x = -b / (2*a)
        X = [x]

    # 篩選整的最小值
    positive_x = [i for i in X if i > 0]

    if len(positive_x) > 0:
        # 返回最小值
        min_positive_x = min(positive_x)
        return min_positive_x
    else:
        #沒有實根
        return False

def Eq2(a, b, c, T):
    fn_return_value = 0

    x1 = 0.0

    x2 = 0.0

    x = 0.0
    if ( b * b - 4 * a * c )  < 0:
        # Msg = '解一元二次方程式 ' + Format(a, 2,' X2 + ') + Format(b, '  X + ') + Format(c, 2,' 時,得虛根, 不合理')
        # MsgBox(Msg, vbInformation, 'Ｔ形梁斷面設計')

        return fn_return_value
    x1 = ( - b + (b * b - 4 * a * c)**(1/2) )  / 2 / a
    x2 = ( - b - (b * b - 4 * a * c)**(1/2) )  / 2 / a

    if x1 < 0 and x2 < 0:
        return fn_return_value
    x = x1
    if x > x2:
        x = x2
    if x > T:
        fn_return_value = x
    return fn_return_value

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

def fun_BarL(a=5):
    BarL=['3#', '4#', '5#', '6#', '7#', '8#', '9#', '10.1', '11.3', '12.4', '13.5', '15.8', '18#']
    return BarL[a]

def ArrangeBar(Ars, ArsP, BarAsi, BarAsPi, Bw, D, Be = -1):
    if Be == -1:
        Be = Bw
    global AreaSelectedAs, NumOfBarAs, RhoSelectedAs, RhoSelectedAsp, NumOfBarAsP, AreaSelectedAsp, SpaceAsp, SpaceAs
    sp = 0.0
    # 一般尺寸的梁使用11號或較小號鋼筋,  11號鋼筋的標稱直徑為 3.58 cm
    NumOfBarAs = int(Ars / fun_BarAb(BarAsi)) + 1
    AreaSelectedAs = fun_BarAb(BarAsi) * NumOfBarAs
    RhoSelectedAs = AreaSelectedAs / Bw / D
    NumOfBarAsP = int(ArsP / fun_BarAb(BarAsPi)) + 1
    AreaSelectedAsp = fun_BarAb(BarAsPi) * NumOfBarAsP
    RhoSelectedAsp = AreaSelectedAsp / Be / D
    #
    SpaceAs = 2.5
    if SpaceAs < fun_BarDb(BarAsi):
        SpaceAs = fun_BarDb(BarAsi)
    sp = int(SpaceAs * 10) / 5
    if sp == int(sp):
        SpaceAs = sp / 2
    else:
        SpaceAs = ( int(sp) + 1 )  / 2
    SpaceAsp = 2.5
    if SpaceAsp < fun_BarDb(BarAsPi):
        SpaceAsp = fun_BarDb(BarAsPi)
    sp = int(SpaceAsp * 10) / 5
    if sp == int(sp):
        SpaceAsp = sp / 2
    else:
        SpaceAsp = ( int(sp) + 1 )  / 2

def Format(X, S =3,U=''):
    Ans = ''
    if S == 0:
        Ans = f'{X:.0f}'+U
    elif S == 1:
        Ans = f'{X:.1f}'+U
    elif S == 2:
        Ans = f'{X:.2f}'+U
    elif S == 3:
        Ans = f'{X:.3f}'+U
    elif S == 4:
        Ans = f'{X:.4f}'+U
    elif S == 5:
        Ans = f'{X:.5f}'+U
    else :
        Ans = f'{X:.6f}'+U
    return Ans

def Sqr(a):
  return a**(1/2)

def Quad(a, b, c):
    discriminant = b**2 - 4*a*c
    X = []

    if discriminant > 0:
        # 有二個實根
        x1 = (-b + math.sqrt(discriminant)) / (2*a)
        x2 = (-b - math.sqrt(discriminant)) / (2*a)
        X = [x1, x2]
    elif discriminant == 0:
        # 有一個實根
        x = -b / (2*a)
        X = [x]

    # 篩選整的最小值
    positive_x = [i for i in X if i > 0]

    if len(positive_x) > 0:
        # 返回最小值
        min_positive_x = min(positive_x)
        return min_positive_x
    else:
        #沒有實根
        return False

def A001_Func(b, NumAs, BarName, StirrupName="D13", Wc=0,
              h=0, Es=2040000, fy=4200, fcp=280, ic=4, D=0,
              layer=1, NumAs2=0, BarName2="D25"):
    #input
    #b=矩形梁寬度        cm
    #D=矩形梁有效深度    cm
    #h=矩形梁實際深度    cm
    #Wc=混泥土單位重     kg/m^3
    #fcp=混凝土抗壓強度  kg/cm^2
    #fy=鋼筋降伏強度     kg/cm^2
    #Es=鋼筋彈性模數     kg/cm^2
    #BarNo=幾號鋼筋英制   #8
    #BarName=幾號鋼筋台制 D25
    #NumAs=幾根拉力鋼筋
    #AreaS=拉力筋面積    cm^2
    #ic=保護層厚度
    #StirrupName=幾號箍筋
    #layer = 幾層鋼筋
    # 單筋梁分析
    dicInfo={}



    results = []
    db = dic[BarName][0]
    Adb = dic[BarName][1]
    ds = dic[StirrupName][0]
    Ads = dic[StirrupName][1]
    db2 = dic[BarName2][0]
    Adb2 = dic[BarName2][1]
    
    # 2023.06.27 ic defulat 6.5
    if D <= 0 and ic <=0:
        ic=6.5
    if D <= 0 :
        D = h-ic-ds-db/2
    # 2023.06.27 ic defulat 用D 計算
    if ic <= 0:
        ic = h-D-db/2
    if h <= 0:
        h = D + 6.5
    if layer == 2:
        D1=h-ic-ds-db/2
        D2=h-ic-ds-db-2.5-db2/2
        D=(D1*NumAs+D2*NumAs2)/(NumAs+NumAs2)
        Dt = D1
        As = NumAs*Adb + NumAs2*Adb2
        str4 = f"第一層拉力鋼筋為 #{BarName} X {NumAs} 第二層拉力鋼筋為#{BarName2} X {NumAs2} 拉力鋼筋量 As= {As:.2f} cm\u00B2"
    else :
        Dt=D
        As = NumAs*Adb
        str4= f"拉力鋼筋為 #{BarName} X {NumAs} 拉力鋼筋量 As= {As:.2f} cm\u00B2"


    WperCubMeter = Wc
    if Wc == 0:
        Ec=4270* (Wc*1000)**(1.5)*math.sqrt(fcp)
    else:
        Ec=15000*math.sqrt(fcp)
    if fy == 4200:
        EpslonY = 0.002
    else:
        EpslonY = fy / Es
    EpslonC = 0.003
    if fcp <= 280:
        beta = 0.85
    elif fcp < 560 :
        beta = 0.85 - (0.2/280)*(fcp-280)
    else:
        beta = 0.65

    WperMeter = WperCubMeter * b * h / 10000

    #程式碼
    R = As / b / D       #實際鋼筋比ρ (rho)

    xb = D * EpslonC / (EpslonC + EpslonY)
    Rb = 0.85 * beta * fcp / fy * EpslonC / (EpslonC + EpslonY)
    Asb = Rb * b * D
    Rmax = 0.85 * beta * fcp / fy * EpslonC / (EpslonC + 0.004)
    Rmin = max(14 / fy, 0.8*math.sqrt(fcp)/fy)
    Asmin = Rmin * b * D
    Asmax = Rmax * b * D

    if As > Asb:
        A = 0.85 * fcp * b * beta
        B = 6120 * As
        C = -6120 * As * D
        x = solve_quadratic_equation(A, B, C)
        a = beta * x
        str1 = "As > Asb 拉力筋不降伏"
    else:
        x = As*fy/(0.85*fcp*b*beta)
        a = beta*x
        str1 = "As < Asb 拉力筋降伏"
    EpslonS = 0.003 * (D - x) / x

    Epslon_t = 0.003 * (Dt - x) / x
    if Epslon_t <= EpslonY:
        phi = 0.65
        str2 = "εs < εy 壓力斷面"
    elif Epslon_t < 0.005:
        phi = 0.65 + (0.9-0.65) / 0.003 * (Epslon_t-0.002)
        str2 = "εy < εs < 0.005   過度斷面"
    else :
        phi = 0.9
        str2 = "εs > 0.005 拉力斷面"

    Cc = 0.85 * fcp * b * beta
    T = As * fy
    Mn = T * (D-a/2)
    phiMn = phi * Mn
    Mnb= Asb * fy * (D-xb*beta/2)
    phiMnb=0.65*Mnb
    if As < Asmin:
          str3='鋼筋用量不合乎規範值  (鋼筋量小於最小鋼筋量)'
    elif As > Asmax:
          str3='鋼筋用量不合乎規範值  (鋼筋量大於最大鋼筋量)'
    else:
          str3='鋼筋用量合乎規範值'
    #輸出文字
    results.append(f"矩形梁寬度 (cm) b = {b:.2f}")
    results.append(f"矩形梁有效深度 (cm) d = {D:.2f}")
    results.append(f"矩形梁有效深度 (cm) dt = {Dt:.2f}")
    results.append(f"矩形梁實際深度 (cm) h= {h:.2f}")
    results.append(f"矩形梁每公尺重量 (Kg/m) wc= {WperMeter} (以每立方公尺2400 Kg計)")
    results.append(str4)
    results.append(f"混凝土抗壓強度 (Kg/cm\u00B2) f′c= {fcp}")
    results.append(f"混凝土抗壓強度乘數 β1 = {beta:.2f}")
    results.append(f"鋼筋降伏強度 (Kg/cm\u00B2) fy= {fy:}")
    results.append(f"鋼筋彈性模數 (Kg/cm\u00B2) Es= {Es:}")
    results.append("-----------------------計算-----------------------")
    results.append(f"實際鋼筋比 ρ= {R:.4f}")
    results.append(f"平衡鋼筋比 ρb= {Rb:.4f}")
    results.append(f"最小鋼筋比 ρ,min= {Rmin:.4f}")
    results.append(f"最大鋼筋比 ρ,max= {Rmax:.4f}")
    results.append(f"實際鋼筋量 As= {As:.3f} cm\u00B2")
    results.append(f"平衡鋼筋量 Asb= {Asb:.3f} cm\u00B2")
    results.append(f"最小鋼筋量 As,min= {Asmin:.3f} cm\u00B2")
    results.append(f"最大鋼筋量 As,max= {Asmax:.3f} cm\u00B2")
    results.append(f"x = {x:.3f}")
    results.append(f"a = {a:.3f}")
    results.append(f"xb = {xb:.3f}")
    results.append(f"x,0.004 = {D*3/7:.3f}")
    results.append(f"x,0.005 = {D*3/8:.3f}")
    results.append(str1)
    results.append(f"εs = {EpslonS:.3f}"+'  '+ str2)
    results.append(f"φ = {phi:.3f}")
    results.append(f"矩形梁平衡彎矩強度 Mnb = {Mnb / 100000:.3f} tf-m")
    results.append(f"矩形梁平衡設計彎矩強度 φMnb = {phiMnb / 100000:.3f} tf-m")
    results.append(f"矩形梁彎矩強度 Mn = {Mn / 100000:.3f} tf-m")
    results.append(f"矩形梁設計彎矩強度 φMn = {phiMn / 100000:.3f} tf-m")
    results.append('check--'+str3)
    dicInfo['EpslonS'] = EpslonS
    #dicInfo['x'] = x
    # dicInfo['xb'] = xb
    
    
    dicInfo['b']=b # 矩形樑樑寬 (cm) b		
    dicInfo['h']=h # 矩形樑實際樑深 (cm) h	
    dicInfo['WperMeter']=WperMeter # 矩形梁每公尺重量 (Kg/m)		
    dicInfo['D']=D # 矩形樑有效樑深 (cm) d	
    dicInfo['fcp']=fcp # 混凝土抗壓強度(kg/cm2)fc'		
    dicInfo['Wc']=Wc # 混凝土單位重 kg/m3	
    dicInfo['fy']=fy # 鋼筋降伏應力 (Kg/cm2) fy		
    dicInfo['Es']=Es # 鋼筋彈性模數 Kg/cm2	
    dicInfo['beta'] = beta
    dicInfo['xb']=xb # 中性軸距壓力面外援的深度		
    dicInfo['xb_beta']=xb*beta # 等值壓力塊的深度
    dicInfo['Rb']=Rb	# 平衡破壞時的鋼筋比	
    dicInfo['Rb_bD']=Rb*b*D # 平衡破壞時的鋼筋量	
    dicInfo['rmin']=Rmin # 拉力破壞的最小鋼筋比		
    dicInfo['Asmin']=Asmin # 最小鋼筋量	
    dicInfo['rmax']=Rmax # 拉力破壞的最大鋼筋比			
    dicInfo['Asmax']=Asmax # 最大鋼筋量		
    dicInfo['AreaS']= As# 拉力鋼筋量 As cm2	
    dicInfo['R']=R # 實際鋼筋比
    dicInfo['barinfo'] = f"{BarName} X {NumAs}"
    
    # print('dicInfo')
    # print(dicInfo)
    # print('results')
    # print(results)
    # print('end')
    return results, dicInfo

def A002_Func(Doption, b, D, dp, h, fcp, fy, Es, Wc, NumOfBarAs,
              NumOfBarAsP, BarAsPi=5, BarAsi=5):
    # Dim b As Double     ' Doption = 1
    # Dim D As Double     ' Doption = 2
    # Dim dp As Double    ' Doption = 4
    # Dim h As Double     ' Doption = 8
    # Dim Mn As Double    ' Doption = 16
    # Dim Mu As Double    ' Doption = 32
    # Dim fcp As Double   ' Doption = 64
    # Dim fy As Double    ' Doption = 128
    # Dim Es As Double    ' Doption = 256
    # Dim Wc As Double    ' Doption = 512

    AreaS = fun_BarAb(BarAsi) * NumOfBarAs
    AreaSp = fun_BarAb(BarAsPi) * NumOfBarAsP
    # za = Double()

    # zb = Double()

    # zc = Double()
    EpslonC=0.003
    # Icase = Integer()
    Msg = '因缺少下列要項......' + vbCr + vbCr
    MsgLen = len(Msg)
    if ( Doption & 1 )  == 0:
        Msg = Msg + '雙筋梁梁寬b' + vbCr
    if ( Doption & 2 )  == 0:
        Msg = Msg + '拉力筋有效深度 d' + vbCr
    if ( Doption & 4 )  == 0:
        Msg = Msg + '壓力筋有效深度 d\'' + vbCr
    if ( Doption & 16 )  == 0:
        Msg = Msg + '混凝土抗壓強度 fc\' ' + vbCr
    if ( Doption & 32 )  == 0:
        Msg = Msg + '鋼筋降伏強度 fy' + vbCr
    if ( Doption & 64 )  == 0:
        Msg = Msg + '鋼筋彈性模數 Es' + vbCr
    if ( Doption & 128 )  == 0:
        Msg = Msg + '混凝土單位重' + vbCr
    if ( Doption & 256 )  == 0:
        Msg = Msg + '拉力鋼筋 As' + vbCr
    if ( Doption & 512 )  == 0:
        Msg = Msg + '壓力鋼筋 As\'' + vbCr
    if len(Msg) > MsgLen:
        Msg = Msg + vbCr
        Msg = Msg + '而無法進行 雙筋梁斷面分析' + vbCr
        # MsgBox(Msg, vbCritical + vbOKOnly, '雙筋矩形梁斷面分析')
        return Msg
    if ( Doption and 8 )  != 8:
        h = D + dp
    elif h <  ( D + dp ) :
        Msg = '梁的實際深度(h)小於拉力筋有效深度(d)與壓力筋有效深度(d\')的和,不合理' + vbCr
        zc = D + dp
        Msg = Msg + '設定實際深度 h = ' + Format(zc, 2,' cm  接受嗎?')
        # if MsgBox(Msg, vbOKCancel, '') == vbCancel:
        #     return Msg
        h = zc

    WperMeter = Wc * b * h / 10000
    #AreaS = 58
    #AreaSp = 11.1
    EpslonY = fy / Es
    rho = AreaS / b / D
    rhop = AreaSp / b / D
    Xb = D * EpslonC /  ( EpslonC + EpslonY )
    if fcp <= 280:
        beta = 0.85
    else:
        beta = 0.85 - int(( fcp - 280 )  / 50) * 0.05
        if beta < 0.65:
            beta = 0.65
    # WkRng.Cells[21, 1] = ''
    # WkRng.Cells[9, 4] = Xb
    # WkRng.Cells[9, 8] = beta * Xb
    rmin = 0.8 * Sqr(fcp) / fy
    if rmin < 14 / fy:
        rmin = 14 / fy

    lstAns=[]
    AreaSy = 0.85 * beta * EpslonC /  ( EpslonC - EpslonY )  * fcp * b * dp / fy + AreaSp *  ( 1 - 0.85 * fcp / fy )

    lstAns.append('梁寬 b = ' + Format(b, 2,' cm'))
    lstAns.append('拉力筋有效深度 d = ' + Format(D, 2,' cm'))
    lstAns.append('壓力筋有效深度 d\' = ' + Format(dp, 2,' cm'))
    lstAns.append('實際深度 h = ' + Format(h, 2,' cm'))
    lstAns.append('拉力鋼筋  #' + Format(fun_BarNo(BarAsi), 0, '#(') + fun_BarName(BarAsi) + ')X' + Format(NumOfBarAs, 0) + '   面積 =' + Format(AreaS, 2,' cm2') + '  鋼筋比 = ' + Format(rho, 4))
    lstAns.append('壓力鋼筋  #' + Format(fun_BarNo(BarAsPi), 0, '#(') + fun_BarName(BarAsPi) + ')X' + Format(NumOfBarAsP, 0) + '   面積 =' + Format(AreaSp, 2,' cm2') + '  鋼筋比 = ' + Format(rhop, 4))
    lstAns.append('混凝土抗壓強度 fc\' = ' + Format(fcp, 2,' kg/cm2'))
    lstAns.append('鋼筋降伏強度 fy = ' + Format(fy, 2,' kg/cm2'))
    lstAns.append('鋼筋彈性模數 Es = ' + Format(Es, 2,' Kg/cm2'))
    lstAns.append('混凝土單位重 = ' + Format(Wc, 2,' Kg/m3'))
    lstAns.append('混凝土梁每公尺重 = ' + Format(WperMeter, 2,' Kg'))
    lstAns.append('---------------------------------------')
    lstAns.append('鋼筋應變量 = ' + Format(EpslonY, 4) + '   混凝土應變量 = ' + Format(EpslonC, 6))
    lstAns.append('抗壓鋼筋降伏之最低抗拉鋼筋量Ay = ' + Format(AreaSy, 2,' cm2'))
    # if len(Trim(txtName.Text)) == 0:
        # WkRng.Cells[1, 1] = '雙筋梁斷面分析'
    # else:
    #     WkRng.Cells[1, 1] = '[ ' + Trim(txtName.Text) + ' ]' + '雙筋梁斷面分析'
    # WkRng.Cells[2, 4] = b
    # WkRng.Cells[3, 4] = D
    # WkRng.Cells[4, 4] = dp
    # WkRng.Cells[5, 4] = h
    # WkRng.Cells[2, 8] = fcp
    # WkRng.Cells[3, 8] = fy
    # WkRng.Cells[4, 8] = Es
    # WkRng.Cells[5, 8] = WperMeter
    # WkRng.Cells[6, 3] = '#' + Format(BarNo(BarAsi), '#(') + BarName(BarAsi) + ')X' + Format(NumOfBarAs)
    # WkRng.Cells[6, 4] = AreaS
    # WkRng.Cells[6, 6] = rho
    # WkRng.Cells[7, 3] = '#' + Format(BarNo(BarAsPi), '#(') + BarName(BarAsPi) + ')X' + Format(NumOfBarAsP)
    # WkRng.Cells[7, 4] = AreaSp
    # WkRng.Cells[7, 6] = rhop
    # WkRng.Cells[6, 8] = EpslonY
    # WkRng.Cells[7, 8] = beta

    if AreaSy <= AreaS:
        fsp = fy
        AreaSb = 0.85 * beta * b * D * EpslonC /  ( EpslonC + EpslonY )  * fcp / fy + AreaSp *  ( 1 - 0.85 * fcp / fy )
        Rb = 0.85 * beta * fcp / fy * EpslonC /  ( EpslonC + EpslonY )  + rhop *  ( 1 - 0.85 * fcp / fy )
        rmax = 0.75 * 0.85 * beta * fcp / fy * EpslonC /  ( EpslonC + EpslonY )  + rhop *  ( 1 - 0.85 * fcp / fy )
        select_variable_0 = True

        if  abs(AreaS - AreaSb) < 0.01:
            x = Xb
            a = beta * x
            cc = 0.85 * fcp * b * a
            CS = AreaSp *  ( fy - 0.85 * fcp )
            T = AreaS * fy
            Mn = cc *  ( D - 0.5 * a )  + CS *  ( D - dp )
            Mn = ( AreaS - AreaSp )  * fy *  ( D - 0.5 * a )  + AreaSp * fy *  ( D - dp )
            Mn = Mn / 100000
            Mu = 0.9 * Mn
            FS = fy
            lstAns.append('====> 平衡破壞, 壓力鋼筋已經降伏 <=====')
            # WkRng.Cells[14, 2] = '\'====> 平衡破壞, 壓力鋼筋已經降伏 <====='
        elif (AreaS < AreaSb):

            CS = AreaSp *  ( fy - 0.85 * fcp )
            T = AreaS * fy
            a = ( T - CS )  /  ( 0.85 * fcp * b )
            cc = 0.85 * fcp * b * a
            x = a / beta
            Mn = cc *  ( D - 0.5 * a )  + CS *  ( D - dp )
            Mn = Mn / 100000
            Mu = 0.9 * Mn
            FS = fy
            lstAns.append('====> 拉力破壞, 壓力鋼筋已經降伏 <=====')
            # WkRng.Cells[14, 2] = '\'====> 拉力破壞, 壓力鋼筋已經降伏 <====='
        elif ( AreaS > AreaSb):

            za = 0.85 * fcp * beta * b
            zb = AreaSp *  ( fy - 0.85 * fcp )  + AreaS * Es * EpslonC
            zc = - AreaS * Es * EpslonC * D
            lstAns.append('一元二次方程式==> ' + Format(za, 2,' X2 + ') + Format(zb, 2,' X + ') + Format(zc, 2) + ' = 0')
            # WkRng.Cells[21, 1] = '一元二次方程式為 ' + Format(za, 2,' X2 + ') + Format(zb, 2,' X + ') + Format(zc, 2) + ' = 0'
            x = Quad(za, zb, zc)
            a = x * beta
            FS = EpslonC * Es *  ( D - x )  / x
            if FS > fy:
                FS = fy
            T = AreaS * FS
            cc = 0.85 * fcp * b * a
            CS = AreaSp *  ( fy - 0.85 * fcp )
            Mn = cc *  ( D - 0.5 * a )  + CS *  ( D - dp )
            Mn = Mn / 100000
            Mu = 0.9 * Mn
            lstAns.append('====> 壓力破壞, 壓力鋼筋已經降伏 <=====')
            # WkRng.Cells[14, 2] = '\'====> 壓力破壞, 壓力鋼筋已經降伏 <====='
        Esp = EpslonC *  ( Xb - dp )  / Xb
        Ess = EpslonC *  ( D - Xb )  / Xb
    else:
        # if 平衡破壞

        Icase = 0
        x = Xb
        fsp = Es * EpslonC *  ( x - dp )  / x
        if fsp > fy:
            fsp = fy
        AreaSb = 0.85 * beta * b * D * EpslonC /  ( EpslonC + EpslonY )  * fcp / fy + AreaSp *  ( fsp / fy - 0.85 * fcp / fy )
        Rb = 0.85 * beta * fcp / fy * EpslonC /  ( EpslonC + EpslonY )  + rhop *  ( fsp / fy - 0.85 * fcp / fy )
        rmax = 0.75 * 0.85 * beta * fcp / fy * EpslonC /  ( EpslonC + EpslonY )  + rhop *  ( fsp / fy - 0.85 * fcp / fy )
        if abs(AreaSb - AreaS) < 0.01:
            Icase = 1
        if Icase == 0:
            za = 0.85 * fcp * beta * b
            zb = AreaSp * Es * EpslonC - AreaS * fy - 0.85 * fcp * AreaSp
            zc = - AreaSp * Es * EpslonC * dp
            x = Quad(za, zb, zc)
            fsp = Es * EpslonC *  ( x - dp )  / x
            if fsp > fy:
                fsp = fy
            AreaSb = 0.85 * beta * b * D * EpslonC /  ( EpslonC + EpslonY )  * fcp / fy + AreaSp *  ( fsp / fy - 0.85 * fcp / fy )
            Rb = 0.85 * beta * fcp / fy * EpslonC /  ( EpslonC + EpslonY )  + rhop *  ( fsp / fy - 0.85 * fcp / fy )
            rmax = 0.75 * 0.85 * beta * fcp / fy * EpslonC /  ( EpslonC + EpslonY )  + rhop *  ( fsp / fy - 0.85 * fcp / fy )
            if AreaS < AreaSb:
                Icase = 2
                lstAns.append('一元二次方程式==> ' + Format(za, 2,' X2 + ') + Format(zb, 2,' X + ') + Format(zc, 2) + ' = 0')
                # WkRng.Cells[21, 1] = '一元二次方程式為 ' + Format(za, 2,' X2 + ') + Format(zb, 2,' X + ') + Format(zc, 2) + ' = 0'

        if Icase == 0:
            za = 0.85 * fcp * beta * b
            zb = AreaS * Es * EpslonC + AreaSp *  ( Es * EpslonC - 0.85 * fcp )
            zc = - Es * EpslonC *  ( AreaSp * dp + AreaS * D )
            x = Quad(za, zb, zc)
            fsp = Es * EpslonC *  ( x - dp )  / x
            if fsp > fy:
                fsp = fy
            AreaSb = 0.85 * beta * b * D * EpslonC /  ( EpslonC + EpslonY )  * fcp / fy + AreaSp *  ( fsp / fy - 0.85 * fcp / fy )
            Rb = 0.85 * beta * fcp / fy * EpslonC /  ( EpslonC + EpslonY )  + rhop *  ( fsp / fy - 0.85 * fcp / fy )
            rmin = 0.75 * 0.85 * beta * fcp / fy * EpslonC /  ( EpslonC + EpslonY )  + rhop *  ( fsp / fy - 0.85 * fcp / fy )
            if AreaS > AreaSb:
                Icase = 3
                lstAns.append('一元二次方程式==> ' + Format(za, 2,' X2 + ') + Format(zb, 2,' X + ') + Format(zc, 2) + ' = 0')
                # WkRng.Cells[21, 1] = '一元二次方程式為 ' + Format(za, 2,' X2 + ') + Format(zb, 2,' X + ') + Format(zc, 2) + ' = 0'
        Esp = EpslonC *  ( x - dp )  / x
        Ess = EpslonC *  ( D - x )  / x
        a = beta * x
        cc = 0.85 * fcp * b * a
        select_variable_1 = True

        if ( Icase == 1):
            CS = AreaSp *  ( fsp - 0.85 * fcp )
            T = AreaS * fy
            FS = fy
            lstAns.append('====> 平衡破壞, 壓力鋼筋尚未降伏 <=====')
            # WkRng.Cells[14, 2] = '\'====> 平衡破壞, 壓力鋼筋尚未降伏 <====='
        elif ( Icase == 2):
            CS = AreaSp *  ( fsp - 0.85 * fcp )
            T = AreaS * fy
            FS = fy
            lstAns.append('====> 拉力破壞, 壓力鋼筋尚未降伏 <=====')
            # WkRng.Cells[14, 2] = '\'====> 拉力破壞, 壓力鋼筋尚未降伏 <====='
        elif ( Icase == 3):
            CS = AreaSp *  ( fsp - 0.85 * fcp )
            FS = Es * EpslonC *  ( D - x )  / x
            if FS > fy:
                FS = fy
            T = AreaS * FS
            lstAns.append('====> 壓力破壞, 壓力鋼筋尚未降伏 <=====')
            # WkRng.Cells[14, 2] = '\'====> 壓力破壞, 壓力鋼筋尚未降伏 <====='

        Mn = cc *  ( D - 0.5 * a )  + CS *  ( D - dp )
        Mn = Mn / 100000
        Mu = 0.9 * Mn
    lstAns.append('拉力鋼筋比 r = ' + Format(rho, 4,'   壓力鋼筋比 rp = ') + Format(rhop, 4))
    lstAns.append('平衡鋼筋量 Asb =  ' + Format(AreaSb, 2,' cm2'))
    lstAns.append('平衡鋼筋比 rb =  ' + Format(Rb, 4,''))
    lstAns.append('---------------------------------------')
    lstAns.append('中性軸位置 X = ' + Format(x, 3,' cm'))
    lstAns.append('等值矩形應力方塊深度 a = ' + Format(a, 3,' cm  Beta1 = ') + Format(beta, 3))
    lstAns.append('拉力鋼筋應力 fs= ' + Format(FS, 2,' kg/cm2   拉力筋應變量 = ') + Format(Ess, 6))
    lstAns.append('壓力鋼筋應力 fs\'= ' + Format(fsp, 2,' kg/cm2   壓力筋應變量 = ') + Format(Esp, 6))
    lstAns.append('拉力鋼筋拉力 T  = ' + Format(T, 2,' Kg'))
    lstAns.append('混凝土壓力 Cc = ' + Format(cc, 2,' kg'))
    lstAns.append('壓力鋼筋壓力 Cs = ' + Format(CS, 2,' kg'))
    lstAns.append('合 壓 力 C = ' + Format(cc + CS, 2,' kg'))
    lstAns.append('設計彎矩 Mu = ' + Format(Mu, 3,' t-m'))
    lstAns.append('標稱彎矩 Mn = ' + Format(Mn, 3,' t-m'))

    dicInfo={}
    dicInfo['b'] =  b  # 雙筋梁梁寬 b cm		
    dicInfo['fcp'] =  fcp   # 混凝土抗壓強度 fc' kg/cm2		
    dicInfo['d'] =  D  # 雙筋梁拉力筋有效深度 d  cm	
    dicInfo['fy'] =  fy   # 鋼筋降伏強度 fy kg/cm2		
    dicInfo['dp']  =  dp  # 雙筋梁壓力筋有效深度 d'  cm		
    dicInfo['Es'] =  Es   # 鋼筋彈性模數 Es Kg/cm2	
    dicInfo['h'] =  h  # 雙筋梁實際深度 h cm
    dicInfo['Wc'] = WperMeter # 混凝土梁單位重 Kg/m		
    dicInfo['AreaS'] =  AreaS  # 拉力鋼筋 As	
    dicInfo['rho'] =  rho  # 鋼筋比	
    dicInfo['AreaSp'] =  AreaSp  # 壓力鋼筋 As'
    dicInfo['rhop'] =  rhop  # 鋼筋比
    dicInfo['EpslonY'] =  EpslonY  # 鋼筋應變量
    dicInfo['beta'] =  beta  # Beta
    dicInfo['Xb'] =  Xb  # 中性軸位置 Xb cm		
    dicInfo['beta_Xb'] =  beta*Xb  # 等值矩形應力方塊深度 a cm		
    dicInfo['Rb'] =  Rb  # 平衡鋼筋比 ρb		
    dicInfo['AreaSb'] =  AreaSb  # 平衡鋼筋量 Asb cm2	
    dicInfo['rmin'] =  rmin  # 最少抗拉鋼筋比			
    dicInfo['AreaSy'] =  AreaSy  # 抗壓鋼筋降伏的最低抗拉鋼筋量 cm2				
    dicInfo['rmax'] =  rmax  # 最大抗拉鋼筋比	   	
    dicInfo['x'] =  x  # 中性軸位置 X cm		
    dicInfo['a'] =  a  # 等值壓力塊深度 a cm			
    dicInfo['Esp'] =  Esp  # 壓力筋應變量			
    dicInfo['fsp'] =  fsp  # 壓力鋼筋 應力 fs' kg/cm2			
    dicInfo['Ess'] =  Ess  # 拉力筋應變量			
    dicInfo['FS'] =  FS  # 拉力鋼筋應 力 fs Kg/cm2					
    dicInfo['cc'] =  cc  # 混凝土壓力 Cc Kg	
    dicInfo['CS'] =  CS  # 壓力鋼筋壓力 Cs Kg/cm2		
    dicInfo['cc_CS'] =  cc + CS  # 合 壓 力 C Kg	
    dicInfo['T'] =  T  # 拉力鋼筋拉力 T Kg	
    dicInfo['Mn'] =  Mn  # 標稱彎矩 Mn t-m	
    dicInfo['Mu'] =  Mu  # 設計彎矩 Mu t-m	
    dicInfo['Mn_T'] =   Mn*100000/T # 力矩臂距
    # WkRng.Cells[10, 4] = Rb
    # WkRng.Cells[10, 8] = AreaSb
    # WkRng.Cells[11, 8] = AreaSy
    # WkRng.Cells[11, 4] = rmin
    # WkRng.Cells[12, 4] = rmax
    # if rho > rmax:
    #     WkRng.Cells[12, 5] = '抗拉鋼筋用量超過規範規定最大量'
    # else:
    #     WkRng.Cells[12, 5] = '抗拉鋼筋用量 未 超過規範規定最大量'
    # WkRng.Cells[15, 3] = x
    # WkRng.Cells[15, 8] = a
    # WkRng.Cells[16, 3] = Esp
    # WkRng.Cells[16, 8] = fsp
    # WkRng.Cells[17, 3] = Ess
    # WkRng.Cells[17, 8] = FS
    # WkRng.Cells[18, 3] = cc
    # WkRng.Cells[18, 8] = CS
    # WkRng.Cells[19, 3] = cc + CS
    # WkRng.Cells[19, 8] = T
    # WkRng.Cells[19, 5] = Format(Mn * 100000 / T, 2,' cm')
    # WkRng.Cells[20, 3] = Mn
    # WkRng.Cells[20, 7] = Mu
    # cmdPrint.Enabled = True

    return lstAns, dicInfo

def A003_Func(RequiredItem, fcp, fy, Be, Bw, D, T, Es,
              WperCubMeter, h, TName='', optype=2, NumAs=0,
              BarName='D25', NumAs2=0, BarName2="D25", layer=1, ic=4,
              StirrupName='D13'):
    db = dic[BarName][0]
    Adb = dic[BarName][1]
    ds = dic[StirrupName][0]
    db2 = dic[BarName2][0]
    Adb2 = dic[BarName2][1]
    if layer == 2:
        D1=h-ic-ds-db/2
        D2=h-ic-ds-db-2.5-db2/2
        D=(D1*NumAs+D2*NumAs2)/(NumAs+NumAs2)
        Dt = D1
        AreaS = NumAs*Adb + NumAs2*Adb2
    elif layer == 1:
        Dt=D
        AreaS = NumAs*Adb

    # inilizi


    # click
    esplonC = 0.003
    Xb = 0.0
    Asb = 0.0
    AsMax = 0.0
    AsMin = 0.0
    beta = 0.0
    a = 0.0
    Mn = 0.0
    C1 = 0.0
    C2 = 0.0
    cc = 0.0
    zz = 0.0
    WperMeter = 0.0
    vbCr = '\n'
    Msg = '因缺少下列要項.....' + vbCr + vbCr
    MsgLen = len(Msg)
    if ( RequiredItem & 4 )  == 0:
        Msg = Msg + 'T,L形梁有效寬度bE' + vbCr
    if ( RequiredItem & 8 )  == 0:
        Msg = Msg + '梁腹寬度bW' + vbCr
    if ( RequiredItem & 16 )  == 0:
        Msg = Msg + '拉力鋼筋有效深度d' + vbCr
    if ( RequiredItem & 32 )  == 0:
        Msg = Msg + 'T,L形梁翼版厚度t cm' + vbCr
    if ( RequiredItem & 1 )  == 0:
        Msg = Msg + '混凝土抗壓強度fc\'' + vbCr
    if ( RequiredItem & 2 )  == 0:
        Msg = Msg + '鋼筋降伏應力fy' + vbCr
    if ( RequiredItem & 64 )  == 0:
        Msg = Msg + '拉力鋼筋用量 As ' + vbCr
    if len(Msg) > MsgLen:
        Msg = Msg + vbCr
        Msg = Msg + '而無法進行 Ｔ形梁斷面分析'
        return Msg
    if ( RequiredItem & 128 )  == 0:
        Es = 2040000
    if ( RequiredItem & 256 )  != 256:
        WperCubMeter = 2400
    #
    if fcp <= 280:
        beta = 0.85
    else:
        beta = 0.85 - int(( fcp - 280 )  / 50) * 0.05
        if beta < 0.65:
            beta = 0.65
    #
    # AreaS = 82 ' for testing some special cases
    lstAns = []
    Cells = {}

    if (2 == optype):
        lstAns.append('=========>  雙翼Ｔ形梁  <=========')
        if len(TName) == 0:
            Cells[1, 1] = '雙翼Ｔ形梁斷面分析'
        else:
            Cells[1, 1] = '[ ' + TName + ' ] ' + '雙翼Ｔ形梁斷面分析'
    elif (1 == optype):
        lstAns.append('=========>  單翼L形梁  <=========')
        if len(TName) == 0:
            Cells[1, 1] = '單翼L形梁斷面分析'
        else:
            Cells[1, 1] = '[ ' + TName + ' ] ' + '單翼L形梁斷面分析'
    elif (0 == optype):
        lstAns.append('=========>  獨立Ｔ形梁  <=========')
        if len(TName) == 0:
            Cells[1, 1] = '獨立Ｔ形梁斷面分析'
        else:
            Cells[1, 1] = '[ ' + TName + ' ] ' + '獨立Ｔ形梁斷面分析'
        if T < 0.5 * Bw or Be <= 4 * Bw:
            Msg = '獨立T形梁的板厚應大於腹寬的一半, 有效翼版寬度應小於腹寬的四倍(與規範值不符)'
            return Msg
    #
    if (RequiredItem & 256) == 0:
      h = D + 4
      RequiredItem = RequiredItem or 512
    elif h <= D:
      h = D + 4
      RequiredItem = RequiredItem or 512
    # '{:07.3f}'.format(3.1415926)
    esplonY = fy / Es
    WperMeter = WperCubMeter *  ( Be * T +  ( h - T )  * Bw )  / 10000
    lstAns.append('Beta = ' + Format(beta,3))
    lstAns.append('鋼筋降伏應變量 = ' + Format(esplonY,5))
    lstAns.append('T,L形梁有效寬度bE = ' + Format(Be,2)+' cm')
    lstAns.append('梁腹寬度bW = ' + Format(Bw,2)+' cm')
    lstAns.append('T,L形梁翼版厚度t = ' + Format(T,2)+' cm')
    lstAns.append('拉力鋼筋有效深度d =' + Format(D,2)+' cm')
    lstAns.append('T形梁深度h = ' + Format(h,2)+' cm')
    lstAns.append('混凝土每立方公尺重量(公斤) = ' + Format(WperCubMeter,2)+' kg/m3')
    lstAns.append('混凝土梁每公尺重量 = ' + Format(WperMeter,2)+'kg')
    lstAns.append('混凝土抗壓強度 fc\'= ' + Format(fcp,2)+' cm2')
    lstAns.append('鋼筋降伏應力 fy = '+ Format(fy,2)+' cm2')
    lstAns.append('拉力鋼筋量 As = ' + Format(AreaS,2)+' cm2')
    lstAns.append('拉力鋼筋量 有效深度d = ' + Format(D,2)+' cm')
    Cells[2, 4] = Be
    Cells[2, 8] = fcp
    Cells[3, 4] = Bw
    Cells[3, 8] = Es
    Cells[4, 4] = T
    Cells[4, 8] = fy
    Cells[5, 4] = D
    Cells[5, 8] = WperMeter
    Cells[6, 4] = h
    Cells[6, 8] = WperCubMeter
    Cells[7, 4] = AreaS
    Cells[7, 8] = beta
    Cells[8, 4] = esplonY
    # Start to calculate Asb, Asmax, Asmin and weight per meter
    Xb = D * esplonC /  ( esplonC + esplonY )
    a = beta * Xb
    if a <= T:
        C1 = 0.85 * fcp *  ( Be - Bw )  * a
        C2 = 0.85 * fcp * a * Bw
    else:
        C1 = 0.85 * fcp *  ( Be - Bw )  * T
        C2 = 0.85 * fcp * a * Bw
    cc = C1 + C2
    Asb = cc / fy
    AsMax = 0.75 * Asb
    AsMin = 0.8 * Sqr(fcp) / fy
    if AsMin < 14 / fy:
        AsMin = 14 / fy
    AsMin = AsMin * Bw * D
    #
    a = AreaS * fy / 0.85 / fcp / Be
    lstAns.append('寬度為有效寬度(' + Format(Be, 2, ' cm') + '的矩形梁的等值應力方塊深度 a = ' + Format(a, 2,' cm'))
    Cells[13, 5] = a
    Cells[13, 7] = T
    if a <= T:
        AsMin = 0.8 * (fcp)**(1/2) / fy
        if AsMin < 14 / fy:
            AsMin = 14 / fy
        AsMin = AsMin * Be * D
        Asb = 0.85 * beta * fcp / fy * Be * D * esplonC /  ( esplonC + esplonY )
        AsMax = 0.75 * Asb
        C1 = 0.85 * fcp * beta * Xb * Be
        lstAns.append('平衡破壞時,中性軸距壓力面外緣的深度 Xb = ' + Format(Xb, 3, ' cm'))
        Cells[9, 5] = Xb
        Cells[9, 8] = C1
        Cells[10, 5] = Asb
        Cells[10, 8] = 0
        Cells[11, 5] = AsMin
        Cells[11, 8] = Asb * fy
        Cells[12, 5] = AsMax
        lstAns.append('平衡破壞時,Cc=' + Format(C1, 4, ' kg'))
        lstAns.append('平衡破壞時,T=' + Format(Asb * fy, 4, ' kg'))
        lstAns.append('平衡拉力鋼筋量 Asb = ' + Format(Asb, 3, ' cm2'))
        lstAns.append('規範規定 最小鋼筋量 = ' + Format(AsMin, 3, ' cm2'))
        lstAns.append('規範規定 最大鋼筋量 = ' + Format(AsMax, 3, ' cm2'))
        lstAns.append('- - - - - - - - - - - - - - - - - - - - - ')
        lstAns.append('======== > 視同矩形梁 < ========')
        #
        Mn = AreaS * fy *  ( D - 0.5 * a )
        cc = 0.85 * fcp * Be * a
        lstAns.append('中性軸距壓力面外緣深度 X (cm) = ' + Format(a / beta, 2))
        lstAns.append('           等值壓力方塊深度 a = ' + Format(a, 2 , ' cm'))
        lstAns.append('混凝土總壓力 Cc = ' + Format(cc, 2, ' Kg'))
        lstAns.append('拉力鋼筋承受拉力 = ' + Format(AreaS * fy, 2,' Kg'))
        lstAns.append('標稱彎矩 Mn = ' + Format(Mn,2,' kg-cm  或  ') + Format(Mn / 100000, 2,' t-m'))
        lstAns.append('設計彎矩 Mu= ' + Format(Mn * 0.9, 2,' kg-cm  或  ') + Format(Mn * 0.9 / 100000, 2,' t-m'))
        Cells[13, 6] = '≦'
        Cells[14, 1] = '\'======== > 視同矩形梁 < ========'
        Cells[15, 5] = a / beta
        Cells[15, 8] = a
        Cells[16, 5] = 0
        Cells[16, 8] = 0
        Cells[17, 5] = cc / 1000
        Cells[17, 8] = AreaS * fy / 1000
        Cells[18, 5] = Mn / 100000
        Cells[18, 8] = Mn * 0.9 / 100000
        Cells[19, 1] = ''
    else:
        lstAns.append('平衡破壞時,中性軸距壓力面外緣的深度 Xb = ' + Format(Xb, 3,' cm'))
        Cells[9, 5] = Xb
        Cells[9, 8] = C1
        Cells[10, 5] = Asb
        Cells[10, 8] = C2
        Cells[11, 5] = AsMin
        Cells[11, 8] = Asb * fy
        Cells[12, 5] = AsMax
        lstAns.append('平衡破壞時,C1=' + Format(C1, 4,' kg'))
        lstAns.append('平衡破壞時,C2=' + Format(C2, 4,' kg'))
        lstAns.append('平衡破壞時,T=' + Format(Asb * fy, 4,' kg'))
        lstAns.append('平衡拉力鋼筋量 Asb = ' + Format(Asb, 3,' cm2'))
        lstAns.append('規範規定 最小鋼筋量 = ' + Format(AsMin, 3,' cm2'))
        lstAns.append('規範規定 最大鋼筋量 = ' + Format(AsMax, 3,' cm2'))
        lstAns.append('- - - - - - - - - - - - - - - - - - - - - ')
        #
        lstAns.append('======== > 應以Ｔ形梁分析之 < ========')
        Cells[13, 6] = '＞'
        Cells[14, 1] = '\'======== > 應以Ｔ形梁分析之 < ========'
        a = ( AreaS * fy - 0.85 * fcp *  ( Be - Bw )  * T )  /  ( 0.85 * fcp * Bw )
        C1 = 0.85 * fcp *  ( Be - Bw )  * T
        AsMax = AsMax + C1 / fy
        C2 = 0.85 * fcp * Bw * a
        cc = C1 + C2
        Mn = C1 *  ( D - 0.5 * T )  + C2 *  ( D - 0.5 * a )
        lstAns.append('中性軸距壓力面外緣深度 X (cm) = ' + Format(a / beta, 2))
        lstAns.append('           等值壓力方塊深度 a = ' + Format(a, 2,' cm'))
        lstAns.append('混凝土兩翼壓力 C1 = ' + Format(C1, 2,' Kg'))
        lstAns.append('混凝土梁腹壓力 C2= ' + Format(C2, 2,' Kg '))
        lstAns.append('混凝土總壓力 Cc = ' + Format(cc, 2,' Kg'))
        lstAns.append('拉力鋼筋承受拉力 = ' + Format(AreaS * fy, 2 ,'Kg'))
        lstAns.append('標稱彎矩 Mn = ' + Format(Mn / 100000, 2,' t-m'))
        lstAns.append('設計彎矩 Mu= ' + Format(Mn * 0.9 / 100000, 2,' t-m'))
        
        Cells[15, 5] = a / beta
        Cells[15, 8] = a
        Cells[16, 5] = C1 / 1000
        Cells[16, 8] = C2 / 1000
        Cells[17, 5] = cc / 1000
        Cells[17, 8] = AreaS * fy / 1000
        Cells[18, 5] = Mn / 100000
        Cells[18, 8] = Mn * 0.9 / 100000
    select_variable_1 = True
    if (select_variable_1 == AreaS < Asb):
        Msg = '拉力破壞 '
    elif (select_variable_1 == AreaS > Asb):
        Msg = '壓力破壞 '
    else:
        Msg = '平衡破壞 '
    select_variable_2 = True
    if (select_variable_2 == AreaS < AsMin):
        Msg = Msg + ', 但鋼筋用量小於規範的最小量'
    elif (select_variable_2 == AreaS > AsMax):
        Msg = Msg + ', 但鋼筋用量大於規範的最大量'
    else:
        Msg = Msg + ', 鋼筋用量符合規範'
    Cells[19, 1] = Msg
    lstAns.append(Msg)
    
    dicInfo={}    
    dicInfo['Be'] = Cells[2, 4]
    dicInfo['fcp'] = Cells[2, 8]
    dicInfo['Bw'] = Cells[3, 4]
    dicInfo['Es'] = Cells[3, 8]
    dicInfo['T'] = Cells[4, 4]    
    dicInfo['fy'] = Cells[4, 8]
    dicInfo['D'] = Cells[5, 4]
    dicInfo['WperMeter'] = Cells[5, 8]
    dicInfo['h'] = Cells[6, 4]
    dicInfo['WperCubMeter'] = Cells[6, 8]
    dicInfo['AreaS'] = Cells[7, 4]
    dicInfo['beta'] = Cells[7, 8]
    dicInfo['esplonY'] = Cells[8, 4]    
    dicInfo['Xb'] = Cells[9, 5]
    dicInfo['C1'] = Cells[9, 8]
    dicInfo['Asb'] = Cells[10, 5]
    dicInfo['C2'] = Cells[10, 8]
    dicInfo['AsMin'] = Cells[11, 5]
    dicInfo['Asb_fy'] = Cells[11, 8]
    dicInfo['AsMax'] = Cells[12, 5]
    dicInfo['a'] = Cells[13, 5]
    dicInfo['op_a_T2'] = Cells[13, 6]
    dicInfo['T2'] = Cells[13, 7]
    dicInfo['MidTille'] = Cells[14, 1]    
    dicInfo[ 'X' ] = Cells[15, 5] 
    dicInfo[ 'a2' ] = Cells[15, 8] 
    dicInfo[ 'C1_1000' ] = Cells[16, 5] 
    dicInfo[ 'C2_1000' ] = Cells[16, 8] 
    dicInfo[ 'cc_1000' ] = Cells[17, 5] 
    dicInfo[ 'AreaS_fy_1000' ] = Cells[17, 8] 
    dicInfo[ 'Mn' ] = Cells[18, 5] 
    dicInfo[ 'Mu' ] = Cells[18, 8] 
    dicInfo[ 'Ans' ] = Cells[19, 1]
    return lstAns, dicInfo

def D001_Func(b, BarName, dagg=2, Mu=0, StirrupName="D13", Wc=2400,
              h=0, Es=2040000, fy=4200, fcp=280, ic=4, D=0):


    results = []
    db = dic[BarName][0]
    Adb = dic[BarName][1]
    ds = dic[StirrupName][0]
    Ads = dic[StirrupName][1]

    if D == 0 :
        D = h-ic-ds-db/2
    if h == 0:
       h=D+6.5
    WperCubMeter = Wc
    if Wc != -1:
        Ec=4270* (Wc*1000)**(1.5)*math.sqrt(fcp)
    else:
        Ec=15000*math.sqrt(fcp)
    if fy == 4200:
        EpslonY = 0.002
    else:
        EpslonY = fy / Es
    EpslonC = 0.003
    if fcp <= 280:
        beta = 0.85
    elif fcp < 560 :
        beta = 0.85 - (0.2/280)*(fcp-280)
    else:
        beta = 0.65

    WperMeter = WperCubMeter * b * h / 10000
    m=fy/(0.85*fcp)

    Rn=Mu*10**5/(0.9*b*D**2)
    if (1-2*m*Rn/fy)<0:
        return '1-2*m*Rn/fy  <  0'

    R_req=1/m*(1-(1-2*m*Rn/fy)**(1/2))

    As_req=R_req*b*D

    Rmax = 0.85 * beta * fcp / fy * EpslonC / (EpslonC + 0.004)
    Rmin = max(14 / fy, 0.8*math.sqrt(fcp)/fy)
    Asmin = Rmin * b * D
    Asmax = Rmax * b * D
    if As_req < Asmin:
          str1='鋼筋用量不合乎規範值  (鋼筋量小於最小鋼筋量)'
    elif As_req > Asmax:
          str1='鋼筋用量符合最小鋼筋量，但鋼筋量大於最大鋼筋量需"雙筋梁設計"'
    else:
          str1='鋼筋用量符合最小鋼筋量，且鋼筋量小於最大鋼筋量可"單筋梁設計"'
    N=As_req/Adb
    Sbn=(b-2*ic-2*ds-N*db)/(N-1)
    Sbn_min=max(2.5,db,1.33*dagg)
    layer=1
    if Sbn<Sbn_min:
        str2='Sbn<Sbn,min(鋼筋淨間距)不符合，需雙排排設計'
        layer=2
        N=math.ceil(N)
        if N%2==0:
            N1=int(N/2)
            N2=int(N/2)
        else:
            N1=math.ceil(N/2)
            N2=int(N/2)
    else:
        N=math.ceil(N)
        str2='Sbn>Sbn,min(鋼筋淨間距)符合'



    if layer == 2:
        D1=h-ic-ds-db/2
        D2=h-ic-ds-db-2.5-db/2
        D=(D1*N1+D2*N1)/(N1+N2)
        Dt = D1
        As = N1*Adb + N2*Adb
        str3 = f"設計第一層拉力鋼筋為 #{BarName} X {N1} 第二層拉力鋼筋為#{BarName} X {N2} 拉力鋼筋量 As= {As:.2f} cm\u00B2"

    elif layer == 1:
        Dt=D
        As = N*Adb
        str3= f"設計拉力鋼筋為 #{BarName} X {N} 拉力鋼筋量 As= {As:.2f} cm\u00B2"
        N1=N
    x = As*fy/(0.85*fcp*b*beta)
    a = beta*x

    EpslonS = 0.003 * (D - x) / x
    Epslon_t = 0.003 * (Dt - x) / x
    cc=ic+ds
    fs=2/3*fy

    Sb_max=min(38*2800/fs-2.5*cc,30*2800/fs)

    if N <=1:
        return 'N = 1'
    Sb=(b-2*ic-2*ds-db)/(N-1)

    if Sb<Sb_max:
        str4="Sb<Sb_max，裂紋控制符合規範"
    else:
        str4="Sb<Sb_max，裂紋控制不符合規範"


    if Epslon_t <= EpslonY:
        phi = 0.65
        str5 = "εs < εy 壓力斷面"
    elif Epslon_t < 0.005:
        phi = 0.65 + (0.9-0.65) / 0.003 * (Epslon_t-0.002)
        str5 = "εy < εs < 0.005   過度斷面"
    else :
        phi = 0.9
        str5 = "εs > 0.005 拉力斷面"

    Cc = 0.85 * fcp * b * beta * x

    Mn = Cc * (D-a/2)

    phiMn = phi * Mn

    if phiMn>Mu:
        str6="φMn > Mu, 設計彎曲強度符合規範"
    else:
        str6="φMn < Mu, 設計彎曲強度不符合規範"
    
    #輸出文字
    results.append(f"矩形梁寬度 (cm) b = {b:.2f}")
    results.append(f"矩形梁有效深度 (cm) d = {D:.2f}")
    results.append(f"矩形梁有效深度 (cm) dt = {Dt:.2f}")
    results.append(f"矩形梁實際深度 (cm) h= {h:.2f}")
    results.append(f"矩形梁每公尺重量 (Kg/m) wc= {WperMeter} (以每立方公尺2400 Kg計)")
    results.append(f"混凝土抗壓強度 (Kg/cm\u00B2) f′c= {fcp}")
    results.append(f"混凝土抗壓強度乘數 β1 = {beta:.2f}")
    results.append(f"鋼筋降伏強度 (Kg/cm\u00B2) fy= {fy:}")
    results.append(f"鋼筋彈性模數 (Kg/cm\u00B2) Es= {Es:}")
    results.append("-----------------------計算-----------------------")
    results.append(f"m= {m:.4f}")
    results.append(f"Rn= {Rn:.4f}")
    results.append(f"需求鋼筋比 ρ,req= {R_req:.4f}")
    results.append(f"最大鋼筋比 ρ,max= {Rmax:.4f}")
    results.append(f"需求鋼筋量 As,req= {As_req:.3f} cm\u00B2")
    results.append(f"最小鋼筋量 As,min= {Asmin:.3f} cm\u00B2")
    results.append(f"最大鋼筋量 As,max= {Asmax:.3f} cm\u00B2")
    results.append(str1)
    results.append(f"N = {N:.3f}")
    results.append(f"Sbn = {Sbn:.3f}")
    results.append(f"Sbn_min = {Sbn_min:.3f}")
    results.append(f"實際鋼筋量 As= {As:.3f} cm\u00B2")
    results.append(str2)
    results.append(str3)
    results.append(f"Sb = {Sb:.3f}")
    results.append(f"Sb_max = {Sb_max:.3f}")
    results.append(str4)
    results.append(f"x = {x:.3f}")
    results.append(f"a = {a:.3f}")
    results.append(f"x,0.004 = {D*3/7:.3f}")
    results.append(f"x,0.005 = {D*3/8:.3f}")
    results.append(f"εs = {EpslonS:.3f}")
    results.append(f"φ = {phi:.3f}")
    results.append(str5)
    results.append(f"矩形梁彎矩強度 Mn = {Mn / 100000:.3f} tf-m")
    results.append(f"矩形梁設計彎矩強度 φMn = {phiMn / 100000:.3f} tf-m")
    results.append(str6)
    dicInfo={}
    dicInfo['NumAs'] = N1
    dicInfo['EpslonS'] = EpslonS
    dicInfo['NumAs2'] = N2
    dicInfo['layer'] = layer
    dicInfo['dd'] = D
    
    dicInfo['b'] = b # 矩形梁梁寬 (cm) b	
    dicInfo['fcp'] = fcp # 混凝土抗壓強度(kg/cm2)fc'	
    dicInfo['h'] = h # 矩形梁實際梁深 (cm) h	
    dicInfo['fy'] = fy # 鋼筋降伏強度 (Kg/cm2) fy	
    dicInfo['ic'] = ic # 鋼筋保護層厚度 cm
    dicInfo['Es'] = Es # 鋼筋彈性模數 Kg/cm2	
    dicInfo['Mu'] = Mu # 標稱彎矩  Mn (t-m)	    
    dicInfo['Mn'] = Mn # 設計彎矩  Mu (t-m)    	
    dicInfo['D'] = D # 矩形梁有效梁深 (cm) d	    		
    dicInfo['WperMeter'] = WperMeter # 斷面尺寸固定,設計鋼筋量			
    dicInfo['beta'] = beta # β	
    dicInfo['a']  =  a #  等值壓力塊的深度a cm	
    dicInfo['rmin'] = Rmin # 拉力破壞的最小鋼筋比ρmin	
    dicInfo['Asmin'] = Asmin # 最小鋼筋量	
    dicInfo['rmax'] = Rmax # 拉力破壞的最大鋼筋比ρmax		
    dicInfo['Asmax'] = Asmax # 最大鋼筋量	
    dicInfo['m'] = m # 材料強度m
    dicInfo['Rn']  =  Rn # Rn kg/cm2	
    dicInfo['R_req'] = R_req #需要的鋼筋比ρ	
    dicInfo['AreaS'] =  As# 需要的鋼筋量 As cm2	  
    
    return results, dicInfo

def D002_Func(b, D, dp, h, Mn, Mu, fcp, fy, Es, Wc, BarAsi = 5, BarAsPi=5, Doption=1023):
    if Mn==0:
        Mn=Mu/0.9
    Mnmax = 0.0

    Mn1 = 0.0

    Mn2 = 0.0

    # i = Integer()
    select_variable_0 = True
    if (select_variable_0 and ( ( Doption and 2 )  == 2 )  and  ( ( Doption and 8 )  == 8 )  ):
        if h < D + 4:
            Msg = '梁的實際深度 h(' + Format(h, 2,' cm) 小於有效深度d(') + Format(D, 2,' cm) 加 4 公分, 接受嗎?')
            # if MsgBox(Msg, vbOKCancel, '') == vbCancel:
            #     return  Msg
    elif (select_variable_0 and ( ( Doption and 2 )  == 2 )  and  ( ( Doption and 8 )  == 0 )  ):
        h = D + 4
        Msg = '未指定梁的深度, 設定為有效深度 加4公分 = ' + Format(h, 2,' cm 接受嗎?')
        # if MsgBox(Msg, vbOKCancel, '') == vbCancel:
        #     return
        # else:
        #     Doption = Doption or 8
    select_variable_1 = True
    if (select_variable_1 and ( Doption and 16 )  == 16 and  ( Doption and 32 )  == 0):
        Mu = 0.9 * Mn
        Doption = Doption or 32
    elif (select_variable_1 and ( Doption and 16 )  == 0 and  ( Doption and 32 )  == 32):
        Mn = Mu / 0.9
        Doption = Doption or 16
    elif (select_variable_1 and ( Doption and 16 )  == 16 and  ( Doption and 32 )  == 32):
        if abs(Mn * 0.9 - Mu) > 0.1:
            Msg = '設計彎矩 Mu (' + Format(Mu, 2,' t-m) 不等於 標稱彎矩 Mn(') + Format(Mn, 2,' t-m) 的 0.9 倍, 不合理')
            return Msg
    # --------------------
    Msg = '因缺少下列要項......' + vbCr + vbCr
    MsgLen = len(Msg)
    if ( Doption and 1 )  == 0:
        Msg = Msg + '雙筋梁梁寬b' + vbCr
    if ( Doption and 2 )  == 0:
        Msg = Msg + '雙筋梁拉力筋有效深度 d' + vbCr
    if ( Doption and 4 )  == 0:
        Msg = Msg + '雙筋梁壓力筋有效深度 d\'' + vbCr
    if ( Doption and 16 )  == 0 and  ( Doption and 32 )  == 0:
        Msg = Msg + '標稱彎矩 Mn 或設計彎矩 Mu' + vbCr
    if ( Doption and 64 )  == 0:
        Msg = Msg + '混凝土抗壓強度 fc\'' + vbCr
    if ( Doption and 128 )  == 0:
        Msg = Msg + '鋼筋降伏強度 fy' + vbCr
    if ( Doption and 256 )  == 0:
        Msg = Msg + '鋼筋彈性模數 Es ' + vbCr
    if len(Msg) > MsgLen:
        Msg = Msg + vbCr
        # MsgBox(Msg, vbCritical, '雙筋矩形梁斷面設計')
        return Msg
    # LstAns.Clear()
    LstAns=[]
    m = fy / 0.85 / fcp
    EpslonY = fy / Es
    EpslonC = 0.003
    #
    if fcp <= 280:
        beta = 0.85
    else:
        beta = 0.85 - int(( fcp - 280 )  / 50) * 0.05
        if beta < 0.65:
            beta = 0.65
    #
    Rb = 0.85 * beta * fcp / fy *  ( EpslonC /  ( EpslonC + EpslonY ) )
    rmax = 0.75 * Rb
    rmin = 0.8 * Sqr(fcp) / fy
    if rmin < 14 / fy:
        rmin = 14 / fy
    Mnmax = rmax * b * D * D * fy *  ( 1 - 0.5 * rmax * m )
    LstAns.append('矩形樑寬度 b = ' + Format(b, 2,' cm'))
    LstAns.append('矩形樑拉力筋有效深度 d = ' + Format(D, 2,' cm'))
    LstAns.append('壓力筋有效深度度 dp = ' + Format(dp, 2,' cm'))
    LstAns.append('矩形樑實際深度 h = ' + Format(h, 2,' cm'))
    LstAns.append('雙筋樑之標稱彎距 Mn = ' + Format(Mn, 2,' t-m'))
    LstAns.append('雙筋樑之設計彎距 Mu = ' + Format(Mu, 2,' t-m'))
    LstAns.append('混凝土極限強度 fcp = ' + Format(fcp, 2,' kg/cm2'))
    LstAns.append('鋼筋極限強度 fy = ' + Format(fy, 2,' kg/cm2'))
    LstAns.append('鋼筋彈性模數 Es = ' + Format(Es, 2,' kg/cm2'))
    LstAns.append('混凝土單位重 = ' + Format(Wc, 2,' kg/m3'))
    LstAns.append(' - - - - - - - - - - - - - - - - - - - - - - - - - ')
    # if len(Trim(txtName.Text)) > 0:
    #     WkRng.Cells[1, 1] = '[ ' + Trim(txtName.Text) + ' ] ' + '雙筋梁斷面設計'
    # else:
    #     WkRng.Cells[1, 1] = '雙筋梁斷面設計'
    # WkRng.Cells[2, 4] = b
    # WkRng.Cells[2, 8] = fcp
    # WkRng.Cells[3, 4] = D
    # WkRng.Cells[3, 8] = fy
    # WkRng.Cells[4, 4] = dp
    # WkRng.Cells[4, 8] = Es
    # WkRng.Cells[5, 4] = h
    # WkRng.Cells[5, 8] = Wc * h * b / 10000
    # WkRng.Cells[6, 4] = Mn
    # WkRng.Cells[6, 8] = Mu
    # WkRng.Cells[7, 4] = beta
    # WkRng.Cells[7, 8] = m
    # WkRng.Cells[8, 4] = EpslonY
    # #WkRng.Cells(8, 8) = Xb * Beta
    # WkRng.Cells[9, 4] = rmax
    # WkRng.Cells[9, 8] = rmin
    # WkRng.Cells[10, 4] = rmax * b * D
    # WkRng.Cells[10, 8] = Mnmax / 100000
    dicInfo={}
    dicInfo['b'] = b # 雙筋梁梁寬 b cm				
    dicInfo['fcp'] = fcp # 混凝土抗壓強度 fc' kg/cm2			
    dicInfo['D'] = D # 雙筋梁拉力筋有效深度 d  cm			
    dicInfo['fy'] = fy # 鋼筋降伏強度 fy kg/cm2			
    dicInfo['dp']  = dp # 雙筋梁壓力筋有效深度 d'  cm				
    dicInfo['Es'] = Es # 鋼筋彈性模數 Es Kg/cm2			
    dicInfo['h'] = h # 雙筋梁實際深度 h cm		
    dicInfo['Wc'] = Wc # 混凝土梁單位重 Kg/m		
    dicInfo['Mn'] = Mn # 標稱彎矩 Mn t-m			
    dicInfo['Mu'] = Mu # 設計彎矩 Mu t-m		
    dicInfo['beta'] =  beta  # Beta
    dicInfo['m'] =  m  # m		
    dicInfo['EpslonY'] =  EpslonY  # 鋼筋極限應變量		
    #dicInfo['beta_Xb'] = beta*Xb # 等值矩形應力方塊深度 a cm
    dicInfo['rmax'] =  rmax  # 最大抗拉鋼筋比
    dicInfo['rmin'] =  rmin  # 最少抗拉鋼筋比
    dicInfo['rmax_b_D'] =  rmax * b * D  # 規範允許單筋梁最大鋼筋量 cm2		
    dicInfo['Mnmax'] =  Mnmax / 100000 # 規範允許單筋梁最大標稱彎矩 Mn,max t-m		
    
    for i in range(1, 4):
        stri = '_'+str(i)
        rmax = 0.75 * Rb
        select_variable_2 = True
        if (select_variable_2 and i == 1):
            LstAns.append('===>情況一, 鋼筋比取單筋矩形樑之最大允許鋼筋比<===')
            rho = rmax
            # WkRng1 = ws.Range('A12')
        elif (select_variable_2 and i == 2):
            LstAns.append('===>情況二, 鋼筋比取單筋矩形樑之最大允許鋼筋比之3/4<===')
            #     rmax = 0.75 * Rb
            rho = 0.75 * rmax
            # WkRng1 = ws.Range('A22')
        elif (select_variable_2 and i == 3):
            LstAns.append('===>情況三, 鋼筋比取單筋矩形樑之最大允許鋼筋比之一半<===')
            #     rmax = 0.75 * Rb
            rho = 0.5 * rmax
            # WkRng1 = ws.Range('A32')
        LstAns.append('Beta = ' + Format(beta, 3))
        LstAns.append('m = ' + Format(m, 3))
        LstAns.append('鋼筋極限應變量 = ' + Format(EpslonY, 5))
        LstAns.append('平衡破壞鋼筋比 = ' + Format(Rb, 4,''))
        LstAns.append('規範允許單筋梁最大鋼筋比 = ' + Format(rmax, 4))
        LstAns.append('規範允許單筋梁最大鋼筋量 = ' + Format(rmax * b * D, 4))
        LstAns.append('規範允許最小鋼筋比 = ' + Format(rmin, 4))
        LstAns.append('規範允許單筋梁最大標稱彎矩 Mn,max = ' + Format(Mnmax / 100000, 2,' t-m'))

        if Mn * 100000 < Mnmax:
            Msg = '標稱彎矩 Mn(' + Format(Mn, 2,' t-m)小於 規範允許單筋梁最大標稱彎矩(') + Format(Mnmax / 100000, 2,' t-m), 採用單筋梁設計即可!!')
            # MsgBox(Msg, vbCritical, '雙筋矩形梁斷面設計')
            # return Msg
        Xb = ( rho * D * fy )  /  ( 0.85 * fcp * beta )
        Esp = ( Xb - dp )  * EpslonC / Xb
        if Esp >= EpslonY:
            fsp = fy
        else:
            fsp = Esp * Es
        LstAns.append('中性軸位置 = ' + Format(Xb, 3,' cm'))
        LstAns.append('等值應力方塊深度 a = ' + Format(Xb * beta, 3,' cm'))
        LstAns.append('鋼筋極限應變量 = ' + Format(EpslonY, 5))
        LstAns.append('壓力筋應變量 = ' + Format(Esp, 5))
        LstAns.append('壓力筋應力 = ' + Format(fsp, 3,' kg/cm2'))
        Mn1 = rho * b * D * D * fy *  ( 1 - 0.5 * rho * m )
        Mn2 = Mn * 100000 - Mn1
        LstAns.append('拉力筋抵抗彎矩 Mn1 = ' + Format(Mn1 / 100000, 2,' t-m'))
        LstAns.append('壓力筋抵抗彎矩 Mn2  = ' + Format(Mn2 / 100000, 2,' t-m'))
        
        
        dicInfo['Xb' + stri] =  Xb # 中性軸位置  cm		
        dicInfo['Rb' + stri] =  Rb # 平衡鋼筋比 ρb		
        dicInfo['Esp' + stri] =  Esp  # 壓力筋應變量 		
        dicInfo['fsp' + stri] =  fsp  # 壓力筋應力 kg/cm2		
        dicInfo['Mn1' + stri] =  Mn1 / 100000 # 拉力筋抵抗彎矩 Mn1 t-m		
        dicInfo['Mn2' + stri] =  Mn2 / 100000 # 壓力筋抵抗彎矩 Mn2 t-m		
        
        # WkRng1.Cells[1, 4] = Xb
        # WkRng1.Cells[1, 8] = Rb
        # WkRng1.Cells[2, 4] = Esp
        # WkRng1.Cells[2, 8] = fsp
        # WkRng1.Cells[3, 4] = Mn1 / 100000
        # WkRng1.Cells[3, 8] = Mn2 / 100000
        Areas1 = rho * b * D
        # AreaS1 = rmax * b * d
        Areas2 = Mn2 / fy /  ( D - dp )
        AreaSp = Mn2 /  ( fsp - 0.85 * fcp )  /  ( D - dp )
        AreaST = Areas1 + Areas2
        ArrangeBar(AreaST, AreaSp,BarAsi,BarAsPi,b,D)
        rho = AreaST / b / D
        rhop = AreaSp / b / D
        rmax = rmax + rhop * fsp / fy


        if rho >= rmin and rho <= rmax:
            LstAns.append('需要的拉力鋼筋量' + Format(AreaST, 2,' cm2   鋼筋比 = ') + Format(rho, 4))
            LstAns.append('設計的拉力鋼筋 #' + Format(fun_BarNo(BarAsi)) + '(' + fun_BarName(BarAsi) + ')X' + Format(NumOfBarAs, 0) + Format(SpaceAs, 2,' cm'))
            LstAns.append('      面積=' + Format(AreaSelectedAs, 2,' cm2   鋼筋比 = ') + Format(RhoSelectedAs, 4))
            LstAns.append('需要的壓力鋼筋量' + Format(AreaSp, 2,' cm2   鋼筋比 = ') + Format(rhop, 4))
            LstAns.append('設計的壓力鋼筋 #' + Format(fun_BarNo(BarAsPi)) + '(' + fun_BarName(BarAsPi) + ')X' + Format(NumOfBarAsP, 0) + Format(SpaceAsp, 2,' cm'))
            LstAns.append('       面積=' + Format(AreaSelectedAsp, 2,' cm2   鋼筋比 = ') + Format(RhoSelectedAsp, 4))
            LstAns.append('修正的最大拉力鋼筋比' + Format(rmax, 4))
            LstAns.append('修正的最小拉力鋼筋比' + Format(rmin, 4))
            # WkRng1.Cells[4, 4] = AreaST
            # WkRng1.Cells[4, 6] = rho
            # WkRng1.Cells[5, 3] = '#' + Format(BarNo(BarAsi)) + '(' + BarName(BarAsi) + ')X' + Format(NumOfBarAs)
            # WkRng1.Cells[5, 4] = Format(AreaSelectedAs, 2,' cm2')
            # WkRng1.Cells[5, 6] = RhoSelectedAs
            # WkRng1.Cells[5, 8] = SpaceAs
            # WkRng1.Cells[6, 4] = AreaSp
            # WkRng1.Cells[6, 6] = rhop
            # WkRng1.Cells[7, 3] = '#' + Format(BarNo(BarAsPi)) + '(' + BarName(BarAsPi) + ')X' + Format(NumOfBarAsP)
            # WkRng1.Cells[7, 4] = Format(AreaSelectedAsp, 2,' cm2')
            # WkRng1.Cells[7, 6] = RhoSelectedAsp
            # WkRng1.Cells[7, 8] = SpaceAsp
            # WkRng1.Cells[8, 4] = rmax
            # WkRng1.Cells[8, 8] = rmin
            dicInfo['AreaST' + stri] =  AreaST  # 需要的拉力鋼筋量 cm2			
            dicInfo['rho' + stri] =  rho  # 鋼筋比 	            
            dicInfo['AreaSelectedAs' + stri] =  Format(AreaSelectedAs, 2,' cm2')  # 設計的拉力鋼筋    	 		
            dicInfo['RhoSelectedAs' + stri] =  RhoSelectedAs  # 鋼筋比          
            dicInfo['SpaceAs' + stri] =  SpaceAs   # 鋼筋間距  cm		
            
            dicInfo['AreaSp' + stri] =  AreaSp  # 需要的壓力鋼筋量 cm2				
            dicInfo['rhop' + stri] =  rhop  # 鋼筋比 	            
            dicInfo['AreaSelectedAsp' + stri] =  Format(AreaSelectedAsp, 2,' cm2') # 設計的壓力鋼筋	    	 		
            dicInfo['RhoSelectedAsp' + stri] =  RhoSelectedAsp  # 鋼筋比          
            dicInfo['SpaceAsp' + stri] =  SpaceAsp   # 鋼筋間距  cm
            dicInfo['rmax' + stri] =  rmax  # 修正的最大拉力鋼筋比		
            dicInfo['rmin' + stri] =  rmin  # 修正的最小拉力鋼筋比		
        else:
            LstAns.append('需要的拉力鋼筋比' + Format(rho, 4))
            LstAns.append('修正的最大拉力鋼筋比' + Format(rmax, 4))
            LstAns.append('修正的最小拉力鋼筋比' + Format(rmin, 4))
            Msg = '需要的拉力鋼筋比不在有效範圍內'
            # MsgBox(Msg, vbCritical, '雙筋矩形梁斷面設計')
            return LstAns ,Msg
        LstAns.append(' - - - - - - - - - - - - - - - - - - - - - - - - - - - -')
    return LstAns, dicInfo
    # cmdOK.Enabled = False
    # cmdPrint.Enabled = True

def D003_Func(isTDesign, fcp, fy, Be, Bw, D, T, Mu, Mn, Es, h,
              WperCubMeter, optype, BarAsi=5, BarAsPi=5, dp=6,
              Alpha=1.0, TName=''):
    # isTDesign bool
    # Dim fcp As Double   ' bit 0   1   混凝土抗壓強度
    # Dim fy As Double    ' bit 1   2   鋼筋降伏應力
    # Dim Be As Double    ' bit 2   4   有效樑寬
    # Dim Bw As Double    ' bit 3   8   腹寬
    # Dim D As Double     ' bit 4   16  拉力筋有效樑深  d
    # Dim T As Double     ' bit 5   32  翼版厚度  T
    # Dim Mu As Double    ' bit 6   64   設計彎矩 Mu
    # Dim Mn As Double    ' bit 7  128   標稱彎矩 Mn
    # Dim Es As Double    ' bit 8  256   鋼筋彈性模數 Es
    # Dim h As Double     ' bit 9  512   T形樑實際寬度
    # Dim WperCubMeter As Double ' bit 10 1024  混凝土單位重 kg/m3
    # Dim Alpha As Double  ' bit 11  2048 抗拉鋼筋量為規範規定最大鋼筋量的倍數(<=1.0)
    # optype 雙翼T型梁:2  單翼T型梁:1 獨立T型梁:0
    # dp=d'
    # T=hf
    InMask = 1024 + 256 + 2048
    # WperMeter = 0.0
    #
    #  處理 h 與 d 的關係
    select_variable_0 = True

    if (select_variable_0 and ( ( InMask and 16 )  == 16 )  and  ( ( InMask and 512 )  == 0 ) ):
        h = D + 4
        InMask = InMask or 512
    elif (select_variable_0 and ( ( InMask and 16 )  == 0 )  and  ( ( InMask and 512 )  == 512 ) ):
        D = h - 4
        InMask = InMask or 16

    #  處理 Mn 與 Mu 的關係
    select_variable_1 = True
    if (select_variable_1 and ( ( InMask and 64 )  == 64 )  and  ( ( InMask and 128 )  == 128 ) ):
        if abs(Mn * 0.9 - Mu) > 0.1:
            # Msg = '標稱彎矩Mn(' + Format(Mn, 2,' t-m)的0.9倍不恰等於設計彎矩Mu(') + Format(Mu,2, ' t-m)') + vbCr
            # Msg = Msg + '選是(Y)以標稱彎矩Mn為準,  選否(N)以設計彎矩Mu為準' + vbCr
            if isTDesign:
                Mu = Mn * 0.9
            else:
                Mn = Mu / 0.9
    elif (select_variable_1 and ( ( InMask and 64 )  == 64 )  and  ( ( InMask and 128 )  == 0 ) ):
        Mn = Mu / 0.9
        InMask = InMask or 128
    elif (select_variable_1 and ( ( InMask and 64 )  == 0 )  and  ( ( InMask and 128 )  == 128 ) ):
        Mu = Mn * 0.9
        InMask = InMask or 64
    #
    Msg = '因缺少下列要項.....' + vbCr + vbCr
    MsgLen = len(Msg)
    if ( InMask and 1 )  == 0:
        Msg = Msg + '混凝土抗壓強度fc\'' + vbCr
    if ( InMask and 2 )  == 0:
        Msg = Msg + '鋼筋降伏應力fy' + vbCr
    if ( InMask and 4 )  == 0:
        Msg = Msg + 'Ｔ形梁有效寬度 bE' + vbCr
    if ( ( InMask and 8 )  == 0 ) :
        Msg = Msg + 'Ｔ形梁梁腹寬度bw' + vbCr
    if ( ( InMask and 16 )  == 0 ) :
        Msg = Msg + '拉力鋼筋的有效深度 d' + vbCr
    if ( ( InMask and 32 )  == 0 ) :
        Msg = Msg + 'Ｔ形梁梁翼厚度t' + vbCr
    if ( ( InMask and 64 )  == 0 )  and  ( ( InMask and 128 )  == 0 ) :
        Msg = Msg + 'Ｔ形梁承受的標稱彎矩 Mn 或設計彎矩 Mu' + vbCr
    if ( ( InMask and 256 )  == 0 ) :
        Msg = Msg + '鋼筋彈性模數 Es' + vbCr
    if ( ( InMask and 1024 )  == 0 ) :
        Msg = Msg + '混凝土單位重' + vbCr
    if ( ( InMask and 2048 )  == 0 ) :
        Msg = Msg + '抗拉鋼筋量為規範規定最大鋼筋量的倍數' + vbCr
    if len(Msg) > MsgLen:
        Msg = Msg + vbCr
        Msg = Msg + '而無法進行Ｔ形梁斷面設計'
        # MsgBox(Msg, vbCritical, 'Ｔ形梁斷面設計')
        return Msg
    #

    if fcp <= 280:
        beta = 0.85
    else:
        # Fix Error
        beta = 0.85 - int(( fcp - 280 )  / 50) * 0.05
        if beta < 0.65:
            beta = 0.65
    WperMeter = WperCubMeter *  ( Be * T +  ( h - T )  * Bw )  / 10000
    #
    Cells={}
    select_variable_2 = True
    # if (2 == optype):
    #     if Len(Trim(TName)) == 0:
    #         WkRng.Cells[1, 1] = '雙翼Ｔ形梁斷面設計'
    #     else:
    #         WkRng.Cells[1, 1] = '[ ' + (TName) + ' ] ' + '雙翼Ｔ形梁斷面設計'
    # elif (1 == optype):
    #     if Len(Trim(TName)) == 0:
    #         WkRng.Cells[1, 1] = '單翼Ｔ形梁斷面設計'
    #     else:
    #         WkRng.Cells[1, 1] = '[ ' + (TName) + ' ] ' + '單翼Ｔ形梁斷面設計'
    # elif (0 == optype):
    #     if Len(Trim(TName)) == 0:
    #         WkRng.Cells[1, 1] = '獨立Ｔ形梁斷面設計'
    #     else:
    #         WkRng.Cells[1, 1] = '[ ' + (TName) + ' ] ' + '獨立Ｔ形梁斷面設計'
    #     if T < 0.5 * Bw or Be <= 4 * Bw:
    #         Msg = '獨立T形梁的板厚應大於腹寬的一半, 有效翼版寬度應小於腹寬的四倍(與規範值不符)'
    #         MsgBox(Msg, vbCritical, 'Ｔ形梁斷面設計')
    #         return
    if 0 == optype and (T < 0.5 * Bw or Be <= 4 * Bw):
        Msg = '獨立T形梁的板厚應大於腹寬的一半, 有效翼版寬度應小於腹寬的四倍(與規範值不符)'
        return Msg
    #
    LstAns=[]
    esplonY = fy / Es
    m = fy / 0.85 / fcp
    Cells[12, 8] = esplonY
    Cells[8, 4] = m
    # LstAns.Clear()
    LstAns.append('Ｔ(L)   形  梁  斷  面  設  計')
    LstAns.append('鋼筋極限降伏應變 = ' + Format(esplonY,5 ))
    LstAns.append('Ｔ形梁梁翼有效寬度 be  = ' + Format(Be, 2,' cm'))
    LstAns.append('Ｔ形梁梁腹寬度 bw  = ' + Format(Bw,2 ,' cm'))
    LstAns.append('Ｔ形梁梁翼厚度 t  = ' + Format(T,2 ,' cm'))
    LstAns.append('拉力鋼筋有效深度d = ' + Format(D,2, ' cm'))
    LstAns.append('T形梁深度h = ' + Format(h,2 ,' cm'))
    LstAns.append('設計彎距 Mu = ' + Format(Mu,2 ,' t-m'))
    LstAns.append('標稱彎距 Mn = ' + Format(Mn,2 ,' t-m'))
    LstAns.append('混凝土抗壓強度fcp = ' + Format(fcp,2 ,' kg/cm2'))
    LstAns.append('Beta1 = ' + Format(beta,2 ))
    LstAns.append('鋼筋降伏應力fy = ' + Format(fy,2 ,' kg/cm2'))
    LstAns.append('材料強度比 m = ' + Format(m, 2))
    LstAns.append('鋼筋彈性模數 Es = ' + Format(Es,2 ,' Kg/cm2'))
    LstAns.append('混凝土單位重 = ' + Format(WperCubMeter,2 ,' kg/m3'))
    LstAns.append('Ｔ形梁單位重 = ' + Format(WperMeter,2 ,' kg/m'))
    LstAns.append('- - - - - - - - - - - - - - - - - - - - - - ')
    # select_variable_3 = True
    if (2 == optype):
        LstAns.append('=========>  雙翼Ｔ形梁  <=========')
        # if Len(Trim(TName.Text)) == 0:
        #     WkRng.Cells[1, 1] = '雙翼Ｔ形梁斷面設計'
        # else:
        #     WkRng.Cells[1, 1] = '[ ' + Trim(TName.Text) + ' ] ' + '雙翼Ｔ形梁斷面設計'
    elif (1 == optype):
        LstAns.append('=========>  單翼L形梁  <=========')
        # if Len(Trim(TName.Text)) == 0:
        #     WkRng.Cells[1, 1] = '單翼L形梁斷面設計'
        # else:
        #     WkRng.Cells[1, 1] = '[ ' + Trim(TName.Text) + ' ] ' + '單翼L形梁斷面設計'
    elif (0 == optype):
        LstAns.append('=========>  獨立Ｔ形梁  <=========')
        # if Len(Trim(TName.Text)) == 0:
        #     WkRng.Cells[1, 1] = '獨立Ｔ形梁斷面設計'
        # else:
        #     WkRng.Cells[1, 1] = '[ ' + Trim(TName.Text) + ' ] ' + '獨立Ｔ形梁斷面設計'
        if T < 0.5 * Bw or Be <= 4 * Bw:
            Msg = '獨立T形梁的板厚應大於腹寬的一半, 有效翼版寬度應小於腹寬的四倍(與規範值不符)'
            # MsgBox(Msg, vbCritical, 'Ｔ形梁斷面設計')
            return Msg
    Cells[2, 4] = Be
    Cells[2, 8] = fcp
    Cells[3, 4] = Bw
    Cells[3, 8] = beta
    Cells[4, 4] = T
    Cells[4, 8] = fy
    Cells[5, 4] = h
    Cells[5, 8] = Es
    Cells[6, 4] = Mn
    Cells[6, 8] = WperMeter
    Cells[7, 4] = Mu
    Cells[7, 8] = WperCubMeter
    Cells[8, 8] = D
    #
    #'  依據劉淋賢先生 鋼筋混凝土學 5-19頁方法設計
    Mc = 0.85 * fcp * T * Be *  ( D - 0.5 * T )
    LstAns.append('判斷彎矩 Mc (t-m) = ' + Format(Mc / 100000, 2))
    Cells[9, 4] = Mc / 100000
    esplonC=0.003
    Rb = 0.85 * beta *  ( esplonC /  ( esplonC + esplonY ) )  *  ( fcp / fy )
    AsMin = 0.8 * Sqr(fcp) / fy
    if AsMin < 14 / fy:
        AsMin = 14 / fy
    AsMin = AsMin * Be * D
    select_variable_4 = True
    if (select_variable_4 and (Mn * 100000 <= Mc)):
        Rn = Mn * 100000 / Be / D / D
        if ( 1 - 2 * m * Rn / fy )  < 0:
            Msg = '需增大斷面積才能承受指定的彎矩'
            # MsgBox(Msg, vbCritical, 'Ｔ形梁斷面設計')
            return Msg
        rho = ( 1 - Sqr(1 - 2 * m * Rn / fy) )  / m
        AreaS = rho * Be * D
        ArrangeBar(AreaS, 0, BarAsi, BarAsPi, Bw, D, Be)
        #   AreaS1 = AreaSelectedAs
        AsMax = Be * D * 0.75 * Rb
        Cells[12, 4] = Rb * Be * D
        Cells[12, 8] = Rb
        Cells[13, 4] = AsMin
        Cells[13, 8] = AsMax
        a = AreaS * fy /  ( 0.85 * fcp * Be )
        C1 = 0.85 * fcp * Be * a
        LstAns.append('===== As ===> ' + Format(AreaS, 2,' cm2'))
        LstAns.append('視同梁寬為 ' + Format(Be, 2,' cm 的矩形梁設計之'))
        LstAns.append('中性軸距壓力面外緣深度 X = ' + Format(a / beta, 2,' cm'))
        LstAns.append('等值壓力方塊深度 a = ' + Format(a, 2,' cm'))
        LstAns.append('Rn = ' + Format(Rn, 3) + '  鋼筋比 = ' + Format(rho,5))
        LstAns.append('拉力鋼筋用量 = ' + Format(AreaSelectedAs, 2,' cm2'))
        LstAns.append('混凝土梁壓力 C = ' + Format(C1, 1,' Kg'))
        LstAns.append('拉力鋼筋承受拉力 = ' + Format(AreaS * fy, 2,' Kg'))
        LstAns.append('= = = = = = = = = = = = = = = =')
        #   lstAns.append "設計的拉力鋼筋 #" & Format(BarNo(BarAsi)) & "(" & BarName(BarAsi) & _")X" & Format(NumOfBarAs, "#0  @") & Format(SpaceAs, "#0.00 cm")
        LstAns.append('設計的拉力鋼筋 #' + Format(fun_BarNo(BarAsi)) + '(' + fun_BarName(BarAsi) + ')X' + Format(NumOfBarAs, 0))
        LstAns.append('      面積=' + Format(AreaSelectedAs, 2,' cm2   鋼筋比 = ') + Format(RhoSelectedAs, 4))
        Cells[9, 8] = 0
        Cells[10, 4] = a / beta
        Cells[10, 8] = a
        Cells[11, 4] = Rn
        Cells[11, 5] = '視同梁寬為 ' + Format(Be, 2,' cm 的矩形梁設計之')
        Cells[14, 4] = C1 / 1000
        Cells[15, 4] = 0
        Cells[16, 4] = 0
        Cells[17, 4] = C1 / 1000
        Cells[14, 8] = Mn
        Cells[15, 8] = 0
        Cells[16, 8] = 0
        Cells[17, 8] = Mn
        Cells[18, 4] = AreaS * fy / 1000
        Cells[18, 7] = 0
        Cells[18, 8] = 0
        Cells[19, 4] = AreaS
        Cells[19, 6] = AreaS / Bw / D
        Cells[20, 4] = AreaSelectedAs
        Cells[20, 6] = RhoSelectedAs
        # Cells[20, 7] = '#' + Format(BarNo(BarAsi),0) + '(' + BarName(BarAsi) + ')X' + Format(NumOfBarAs, 0) + Format(SpaceAs, 2, " cm")
        Cells[21, 4] = 0
        Cells[21, 6] = 0
        # #   WkRng.Cells(21, 7) = "無需壓力鋼筋"
        Cells[21, 7] = ''
        Cells[22, 4] = 0
        Cells[22, 6] = 0
        Cells[22, 7] = ''
    elif (select_variable_4 and (Mn * 100000 > Mc)):
        LstAns.append('視同Ｔ形梁設計之')
        #  M1:梁翼(扣掉bw寬)負擔的彎矩及所需鋼筋量(Asf)
        C1 = 0.85 * fcp *  ( Be - Bw )  * T
        M1 = C1 *  ( D - 0.5 * T )
        Asf = C1 / fy
        rhosf = Asf / Bw / D
        #  M2:矩形梁負擔的彎矩
        M2 = Mn * 100000 - M1
        Rn = M2 / Bw / D / D
        if ( 1 - 2 * m * Rn / fy )  < 0:
            Msg = '需增大斷面積才能承受指定的彎矩'
            # MsgBox(Msg, vbCritical, 'Ｔ形梁斷面設計')
            return Msg
        rho = ( 1 - Sqr(1 - 2 * m * Rn / fy) )  / m
        rhoMax = 0.75 *  ( Rb + rhosf )
        AsMax = 0.75 *  ( Asf + Rb * Bw * D )
        AsMin = 0.8 * Sqr(fcp) / fy
        if AsMin < 14 / fy:
            AsMin = 14 / fy
        AsMin = AsMin * Bw * D
        Cells[12, 4] = Asf + Rb * Bw * D
        Cells[12, 8] = Rb + rhosf
        Cells[13, 4] = AsMin
        Cells[13, 8] = AsMax
        rho1 = Alpha * rhoMax - rhosf
        
        if rho1 >= rho:
            Cells[11, 5] = '視同Ｔ形梁設計之(不需壓力鋼筋)'
            AreaSp = 0
            AreaS = Asf + rho * Bw * D
            xx0 = 2 * M2 /  ( 0.85 * fcp * Bw )
            xx1 = - 2 * D
            xx2 = 1
            a = Eq2(xx2, xx1, xx0, 0.1)
            C2 = 0.85 * fcp * Bw * a
            cc = C1 + C2
            rho1 = AreaS / Bw / D
            LstAns.append('中性軸距壓力面外緣深度 X = ' + Format(a / beta,2,' cm'))
            LstAns.append('等值壓力方塊深度 a = ' + Format(a, 2,' cm'))
            LstAns.append('Rn = ' + Format(Rn, 4) + '  鋼筋比 = ' + Format(rho1, 5))
            LstAns.append('拉力鋼筋用量 = ' + Format(AreaS, 2,' cm2'))
            LstAns.append('梁翼混凝土壓力 C1 = ' + Format(C1, 2,' Kg  彎矩 M1=') + Format(M1 / 100000, 2,' t-m'))
            LstAns.append('梁腰混凝土壓力 C2 = ' + Format(C2,2,' Kg  彎矩 M2=') + Format(M2 / 100000,  2,' t-m'))
            LstAns.append('混凝土合壓力 Cc = ' + Format(cc,2 ,' Kg'))
            LstAns.append('拉力鋼筋承受拉力 = ' + Format(AreaS * fy, 2,' Kg'))
            LstAns.append('======= As ====> ' + Format(AreaS, 2,' cm2  彎矩 Mn=') + Format(Mn, 2,' t-m'))
            # ArrangeBar(AreaS, AreaSp)
            ArrangeBar(AreaS, AreaSp, BarAsi, BarAsPi, Bw, D, Be)
            LstAns.append('= = = = = = = = = = = = = = = =')
            #   lstAns.append "設計的拉力鋼筋 #" & Format(BarNo(BarAsi)) & "(" & BarName(BarAsi) & _")X" & Format(NumOfBarAs, "#0  @") & Format(SpaceAs, "#0.00 cm")
            LstAns.append('設計的拉力鋼筋 #' + Format(fun_BarNo(BarAsi)) + '(' + fun_BarName(BarAsi) + ')X' + Format(NumOfBarAs, 0))
            LstAns.append('      面積=' + Format(AreaSelectedAs, 2,' cm2   鋼筋比 = ') + Format(RhoSelectedAs, 5))
            Cells[10, 4] = a / beta
            Cells[10, 8] = a
            Cells[11, 4] = Rn
            Cells[14, 4] = C1 / 1000
            Cells[15, 4] = C2 / 1000
            Cells[16, 4] = 0
            Cells[17, 4] = cc / 1000
            Cells[14, 8] = M1 / 100000
            Cells[15, 8] = M2 / 100000
            Cells[16, 8] = 0
            Cells[17, 8] = Mn
            Cells[18, 4] = AreaS * fy / 1000
            Cells[18, 7] = 0
            Cells[18, 8] = 0
            Cells[19, 4] = AreaS
            Cells[19, 6] = AreaS / Bw / D
            Cells[20, 4] = AreaSelectedAs
            Cells[20, 6] = RhoSelectedAs
            #   WkRng.Cells(20, 7) = "#" & Format(BarNo(BarAsi)) & "(" & BarName(BarAsi) & _")X" & Format(NumOfBarAs, "#0  @") & Format(SpaceAs, "#0.00 cm")
            #   Cells[20, 7] = '#' + Format(BarNo(BarAsi),0) + '(' + BarName(BarAsi) + ')X' + Format(NumOfBarAs, 0) + Format(SpaceAs, 2," cm")
            Cells[21, 4] = AreaSp
            Cells[21, 6] = 0
            # #   WkRng.Cells(21, 7) = "無需壓力鋼筋"
            Cells[21, 7] = ''
            Cells[22, 4] = 0
            Cells[22, 6] = 0
            #Cells[22, 7] = ''
        else:
            Cells[11, 5] = '視同Ｔ形梁設計之(需壓力鋼筋)'
            # while 1:
            #     dp = 6
            #     Msg = '本Ｔ形梁需要壓力鋼筋,請輸入壓力鋼筋的有效深度'
            #     dp = Val(InputBox(Msg, 'Ｔ形梁斷面設計', dp))
            #     if dp > 0:
            #         break
            Mn1 = rho1 * fy * Bw * D * D *  ( 1 - 0.5 * rho1 * m )
            a = rho1 * Bw * D * fy / 0.85 / fcp / Bw
            x1 = a / beta
            esplonsp = ( x1 - dp )  * esplonC / x1
            fsp = fy
            if esplonsp < esplonY:
                fsp = esplonsp * Es
            As2 = ( M2 - Mn1 )  / fy /  ( D - dp )
            AreaSp = As2 * fy / fsp
            AreaS = Asf + rho1 * Bw * D + As2
            CS = AreaSp * fsp
            C2 = 0.85 * fcp * Bw * a
            cc = C1 + C2
            rhoMax = 0.75 *  ( Rb + rhosf )  + As2 /  ( Bw * D )
            AsMax = 0.75 *  ( Asf + Rb * Bw * D )  + As2
            Cells[12, 4] = Asf + Rb * Bw * D + As2
            Cells[12, 8] = Rb + rhosf + As2 / Bw / D
            Cells[13, 4] = AsMin
            Cells[13, 8] = AsMax
            Cells[9, 8] = dp
            LstAns.append('===== As ====> ' + Format(AreaS, 2,' cm2'))
            LstAns.append('===== As\'====> ' + Format(AreaSp,2, ' cm2'))
            LstAns.append('中性軸距壓力面外緣深度 X = ' + Format(a / beta,2, ' cm'))
            LstAns.append('等值壓力方塊深度 a = ' + Format(a, 2,' cm'))
            LstAns.append('壓力鋼筋的應變量 = ' + Format(esplonsp, 5))
            LstAns.append('壓力鋼筋應力 = ' + Format(fsp, 2,' kg/cm2'))
            LstAns.append('拉力鋼筋用量 = ' + Format(AreaS, 2,' cm2'))
            LstAns.append('梁翼混凝土壓力 C1 = ' + Format(C1,2 ,' Kg  彎矩 M1=') + Format(M1 / 100000, 2,' t-m'))
            LstAns.append('梁腰混凝土壓力 C2 = ' + Format(C2,2 ,' Kg  彎矩 M2=') + Format(Mn1 / 100000, 2,' t-m'))
            LstAns.append('混凝土合壓力 Cc = ' + Format(cc, 2,' Kg'))
            LstAns.append('壓力鋼筋的壓力 Cs = ' + Format(CS, 2,'  Kg  彎矩 MS=') + Format(( M2 - Mn1 )  / 100000,2 ,' t-m'))
            LstAns.append('拉力鋼筋承受拉力  = ' + Format(AreaS * fy, 2,' Kg 彎矩 Mn=') + Format(Mn,2 ,' t-m'))
            # ArrangeBar(AreaS, AreaSp)
            ArrangeBar(AreaS, AreaSp, BarAsi, BarAsPi, Bw, D, Be)
            LstAns.append('= = = = = = = = = = = = = = = =')
            #   lstAns.append "設計的拉力鋼筋 #" & Format(BarNo(BarAsi)) & "(" & BarName(BarAsi) & _")X" & Format(NumOfBarAs, "#0  @") & Format(SpaceAs, "#0.00 cm")
            LstAns.append('設計的拉力鋼筋 #' + Format(fun_BarNo(BarAsi)) + '(' + fun_BarName(BarAsi) + ')X' + Format(NumOfBarAs, 0))
            LstAns.append('      面積=' + Format(AreaSelectedAs,2 ,' cm2   鋼筋比 = ') + Format(RhoSelectedAs, 4))
            #   lstAns.append "設計的壓力鋼筋 #" & Format(BarNo(BarAsPi)) & "(" & BarName(BarAsPi) & _")X" & Format(NumOfBarAsP, "#0  @") & Format(SpaceAsp, "#0.00 cm")
            LstAns.append('設計的壓力鋼筋 #' + Format(fun_BarNo(BarAsPi)) + '(' + fun_BarName(BarAsPi) + ')X' + Format(NumOfBarAsP, 0))
            LstAns.append('       面積=' + Format(AreaSelectedAsp,2 , ' cm2   鋼筋比 = ') + Format(RhoSelectedAsp, ))
            Cells[10, 4] = a / beta
            Cells[10, 8] = a
            Cells[15, 4] = Rn
            Cells[15, 8] = rho
            Cells[14, 4] = C1 / 1000
            Cells[15, 4] = C2 / 1000
            Cells[16, 4] = CS / 1000
            Cells[17, 4] = cc / 1000
            Cells[14, 8] = M1 / 100000
            Cells[15, 8] = Mn1 / 100000
            Cells[16, 8] = ( M2 - Mn1 )  / 100000
            Cells[17, 8] = Mn
            Cells[18, 4] = AreaS * fy / 1000
            Cells[18, 7] = esplonsp
            Cells[18, 8] = fsp
            Cells[19, 4] = AreaS
            Cells[19, 6] = AreaS / Bw / D
            Cells[20, 4] = AreaSelectedAs
            Cells[20, 6] = RhoSelectedAs
            #   WkRng.Cells(20, 7) = "#" & Format(BarNo(BarAsi)) & "(" & BarName(BarAsi) & _")X" & Format(NumOfBarAs, "#0  @") & Format(SpaceAs, "#0.00 cm")
            #   Cells[20, 7] = '#' + Format(BarNo(BarAsi)) + '(' + BarName(BarAsi) + ')X' + Format(NumOfBarAs, 0)
            Cells[21, 4] = AreaSp
            Cells[21, 6] = AreaSp / Bw / D
            Cells[21, 7] = ''
            Cells[22, 4] = AreaSelectedAsp
            Cells[22, 6] = RhoSelectedAsp
            #    WkRng.Cells(22, 7) = "#" & Format(BarNo(BarAsPi)) & "(" & BarName(BarAsPi) & _")X" & Format(NumOfBarAsP, "#0  @") & Format(SpaceAsp, "#0.00 cm")
            #    Cells[22, 7] = '#' + Format(BarNo(BarAsPi)) + '(' + BarName(BarAsPi) + ')X' + Format(NumOfBarAsP, 0)
    
    LstAns.append('本T形梁在拉力破壞情況下, 最小鋼筋量 (cm2) = ' + Format(AsMin,3))
    LstAns.append('本T形梁在拉力破壞情況下, 最大鋼筋量 (cm2) = ' + Format(AsMax,3))
    select_variable_5 = True
    if (select_variable_5 and AreaS < AsMin):
        LstAns.append('鋼筋用量小於規範的最小量')
    elif (select_variable_5 and AreaS > AsMax):
        LstAns.append('鋼筋用量大於規範的最大量')
    else:
        LstAns.append('鋼筋用量符合規範')
    
    xx=a / beta
    Epslons = (D-xx)/xx*0.003
    dicInfo={}
    dicInfo['NumAs'] = NumOfBarAs
    dicInfo['NumOfBarAsP'] = NumOfBarAsP
    dicInfo['EpslonS'] = Epslons
    
    dicInfo['Be']=Cells[2, 4] # T形梁有效寬度bE cm		
    dicInfo['fcp']=Cells[2, 8] # 混凝土抗壓強度 fc' kg/cm2		
    dicInfo['Bw']=Cells[3, 4] # 梁腹寬度bW cm		
    dicInfo['beta']=Cells[3, 8] # Beta1		
    dicInfo['T']=Cells[4, 4] # T形梁翼版厚度 t cm		
    dicInfo['fy']=Cells[4, 8] # 鋼筋降伏應力 fy kg/cm2		
    dicInfo['h']=Cells[5, 4] # T形梁深度 h cm		
    dicInfo['Es']=Cells[5, 8] # 鋼筋彈性模數 Es kg/cm2		
    dicInfo['Mn']=Cells[6, 4] # 標稱彎矩 Mn  t-m		
    dicInfo['WperMeter']=Cells[6, 8] # Ｔ形梁單位重 kg/m		
    dicInfo['Mu']=Cells[7, 4] # 設計彎矩  Mu  t-m		
    dicInfo['WperCubMeter']=Cells[7, 8] # 混凝土單位重 kg/m3		
    dicInfo['m']=Cells[8, 4] # 材料強度比 m		
    dicInfo['D']=Cells[8, 8] # 拉力鋼筋有效深度d cm		
    dicInfo['Mcn']=Cells[9, 4] # 判斷標稱彎矩 Mcn  t-m		
    dicInfo['dp']=Cells[9, 8] # 壓力鋼筋有效深度d' cm		
    dicInfo['X']=Cells[10, 4] # 中性軸距壓力面外緣深度 X cm 
    dicInfo['a']=Cells[10, 8] # 等值壓力方塊深度 a	
    dicInfo['Rn']= Cells.get((11,4),'')#Cells[11, 4] # Rn 
    dicInfo['Asb']=Cells[12, 4] # 平衡鋼筋量Asb cm2	      
    dicInfo['Rb']=Cells[12, 8] # 平衡鋼筋比		
    dicInfo['AsMin']=Cells[13, 4] # 規範允許最小鋼筋量As,min Cm2		
    dicInfo['AsMax']=Cells[13, 8] # 規範允許最大鋼筋量As,max Cm2		      
    dicInfo['C1']=Cells[14, 4] # 梁翼混凝土壓力 C1 t		
    dicInfo['Mc1']=Cells[14, 8] # 梁翼承擔標稱彎矩Mc1  t-m		
    dicInfo['C2']=Cells[15, 4] # 梁腰混凝土壓力C2 t		
    dicInfo['Mc2']=Cells[15, 8] # 梁腰承擔標稱彎矩Mc2  t-m		
    dicInfo['CS']=Cells[16, 4] # 壓力鋼筋的壓力 t		
    dicInfo['Mcs']=Cells[16, 8] # 壓力筋承擔標稱彎矩Mcs  t-m		
    dicInfo['cc']=Cells[17, 4] # 混凝土梁壓力 Cc t		
    dicInfo['Mt']=Cells[17, 8] # 拉力筋承擔標稱彎矩Mt  t-m		
    dicInfo['AreaS_fy']=Cells[18, 4] # 拉力鋼筋承受拉力T t	
    # 拉力鋼筋	
    dicInfo['AreaS']=Cells[19, 4] # 需用量 cm2	
    dicInfo['AreaS_Bw_D']=Cells[19, 6]# 鋼筋比  
    dicInfo['AreaSelectedAs']=Cells[20, 4] # 使用量 cm2	
    dicInfo['RhoSelectedAs']=Cells[20, 6] # 鋼筋比 
    # 壓力鋼筋
    dicInfo['AreaSp']=Cells[21, 4] # 需用量 cm2	
    dicInfo['AreaSp_Bw_D']=Cells[21, 6] # 鋼筋比 
    dicInfo['AreaSelectedAsp']=Cells[22, 4] # 使用量 cm2
    dicInfo['RhoSelectedAsp']=Cells[22, 6] # 鋼筋比 
    return LstAns , dicInfo
    # cmdPrint.Enabled = True



# # Example usage
#calculate_beam_strength(b=30, D=0, h=60, Es=2040000, fcp=280, fy=4200, Wc=2400,BarName="D22", StirrupName="D10",BarNo=4,ic=4,BarNo2=4,BarName2="D22",layer=2)