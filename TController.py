from PyQt6 import QtWidgets, QtGui, QtCore
#from UI import Ui_MainWindow
import TView as vw
import TModel as TM
import TDraw as TD

def strToFloat(S,defaultValue = 0):
    Ans = float(defaultValue)
    try:
       Ans = float(S)
    except:
        pass
    return Ans
def strToInt(S,defaultValue = 0):
    Ans = int(defaultValue)
    try:
       Ans = int(S)
    except:
        pass
    return Ans
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

class Menu_controller(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__() # in python3, super(Class, self).xxx = super().xxx
        self.ui = vw.Ui_Menu_MainWindow()
        self.ui.setupUi(self)
        self.setup_control()
        
    def setup_control(self):
        self.clicked_counter = 0
        self.ui.btn_A001.clicked.connect(self.btn_A001Clicked)
        self.ui.btn_A002.clicked.connect(self.btn_A002Clicked)
        self.ui.btn_A003.clicked.connect(self.btn_A003Clicked)
        self.ui.btn_D001.clicked.connect(self.btn_D001Clicked)
        self.ui.btn_D002.clicked.connect(self.btn_D002Clicked)
        self.ui.btn_D003.clicked.connect(self.btn_D003Clicked)
        
    def btn_A001Clicked(self):
        self.window_A001 = A001_controller()     
        self.window_A001.show()
     
    def btn_A002Clicked(self):
        self.window_A002 = A002_controller()     
        self.window_A002.show()
        
    def btn_A003Clicked(self):
        self.window_A003 = A003_controller()     
        self.window_A003.show()
        
    def btn_D001Clicked(self):
        self.window_D001 = D001_controller()     
        self.window_D001.show()
     
    def btn_D002Clicked(self):
        self.window_D002 = D002_controller()     
        self.window_D002.show()
        
    def btn_D003Clicked(self):
        self.window_D003 = D003_controller()     
        self.window_D003.show()

class A001_controller(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__() # in python3, super(Class, self).xxx = super().xxx
        self.ui = vw.Ui_A001_MainWindow()        
        self.ui.setupUi(self)
        self.setup_control()

    def setup_control(self):
        self.dicInfo = {}
        self.clicked_counter = 0
        self.ui.btn_Enter.clicked.connect(self.Enter_clicked)
        self.ui.btn_plt.clicked.connect(self.Plt_clicked)
        self.ui.btn_Cancel.clicked.connect(self.Cancel_clicked)
        self.InitForm()

    def Enter_clicked(self):
        try:
            self.clicked_counter += 1
            print(f"\r\nYou clicked {self.clicked_counter} times.")            
           
            # region 取得 User 輸入
            b = strToFloat(self.ui.txb_b.text())
            D = strToFloat(self.ui.txb_d.text())
            h = strToFloat(self.ui.txb_h.text())
            Es = strToFloat(self.ui.txb_Es.text())
            fcp = strToFloat(self.ui.txb_fcp.text())
            fy = strToFloat(self.ui.txb_fy.text())
            Wc = strToFloat(self.ui.txb_WperCubMeter.text())
            BarAsi =self.ui.cbx_BarAsi.currentIndex()
            BarName = self.ui.cbx_BarAsi.currentText()
            NumAs = strToInt(self.ui.txb_NumAs.text())
            # 2023.06.26 ui增加 BarName2 NumAs2 StirrupName layer ic
            BarName2 = self.ui.cbx_BarAsi_2.currentText()
            NumAs2 = strToInt(self.ui.txb_NumAs_2.text())
            StirrupName = self.ui.cbx_StirrupAsi.currentText()
            layer = strToInt(self.ui.txb_layer.text())
            ic = strToInt(self.ui.txb_ic.text())
            print('b',b)
            print('D',D)
            print('h',h)
            print('Es',Es)
            print('fcp',fcp)
            print('fy',fy)
            print('Wc',Wc)
            print('BarAsi',BarAsi)
            print('BarName',BarName)
            print('NumAs',NumAs)
            print('BarName2',BarName2)
            print('NumAs2',NumAs2)
            print('layer',layer)
            print('ic',ic)
            print('StirrupName',StirrupName)       
            
            if(self.CheckValue(b , 'b') == False): return 
            if(self.CheckValue(D , 'D') == False): return 
            if(self.CheckValue(h , 'h') == False): return 
            if(self.CheckValue(Es , 'Es') == False): return 
            if(self.CheckValue(fcp, 'fc') == False): return 
            if(self.CheckValue(fy , 'fy') == False): return 
            if(self.CheckValue(Wc , 'Wc') == False): return 
            if(self.CheckValue(NumAs , 'NumAs') == False): return 
            if(self.CheckValue(NumAs2 , 'NumAs2') == False): return 
            if(self.CheckValue(layer , 'layer') == False): return 
            if(self.CheckValue(ic , 'ic') == False): return 
            # endregion 
            
            # region 建立圖表所需字典
            self.dicInfo['BarAsi']=BarAsi
            self.dicInfo['BarName']=BarName
            self.dicInfo['NumAs']=NumAs
            self.dicInfo['BarName2']=BarName2
            self.dicInfo['NumAs2']=NumAs2
            self.dicInfo['layer']=layer
            self.dicInfo['ic']=ic
            self.dicInfo['StirrupName']=StirrupName        
            # endregion
            
            # region show Tab1      
            self.ui.listWidget.clear()
            # 接收不固定回傳值   
            Ans = TM.A001_Func(b, NumAs, BarName, StirrupName=StirrupName, Wc=Wc, h=h, Es=Es, fy=fy, fcp=fcp, ic=ic, D=D, layer=layer, NumAs2=NumAs2, BarName2=BarName2)
            # print('Ans')
            # print(Ans,'\n')
            if isinstance(Ans,tuple):
                for ans in Ans:
                    # print(ans,'\r\n')
                    if isinstance(ans, list):  
                        self.ui.listWidget.addItems(ans)  # 使用 addItems 建立選單
                    elif isinstance(ans, str): 
                        self.ui.listWidget.addItem(ans)
                    elif isinstance(ans, dict):       
                        self.dicInfo.update(ans)  
            elif isinstance(Ans,str):
                self.ui.listWidget.addItem(Ans)
            elif isinstance(Ans,list):
                self.ui.listWidget.addItems(Ans)
            #endregion
            
            # region show Tab2           
            self.ui.label_b.setText( Format(self.dicInfo['b'], 2))
            self.ui.label_h.setText( Format(self.dicInfo['h'], 2))           
            self.ui.label_WperMeter.setText( Format(self.dicInfo['WperMeter'], 2))
            self.ui.label_D.setText( Format(self.dicInfo['D'], 2))
            self.ui.label_fcp.setText( Format(self.dicInfo['fcp'], 2))
            self.ui.label_Wc.setText( Format(self.dicInfo['Wc'], 2))
            self.ui.label_fy.setText( Format(self.dicInfo['fy'], 2))
            self.ui.label_Es.setText( Format(self.dicInfo['Es'], 2))
            self.ui.label_beta.setText( Format(self.dicInfo['beta'], 2))
            self.ui.label_xb.setText( Format(self.dicInfo['xb'], 2))
            self.ui.label_xb_beta.setText( Format(self.dicInfo['xb_beta'], 2))
            self.ui.label_Rb.setText( Format(self.dicInfo['Rb'], 5))
            self.ui.label_Rb_bD.setText( Format(self.dicInfo['Rb_bD'], 2))
            self.ui.label_rmin.setText( Format(self.dicInfo['rmin'], 5))
            self.ui.label_Asmin.setText( Format(self.dicInfo['Asmin'], 2))
            self.ui.label_rmax.setText( Format(self.dicInfo['rmax'], 5))
            self.ui.label_Asmax.setText( Format(self.dicInfo['Asmax'], 2))
            self.ui.label_AreaS.setText( Format(self.dicInfo['AreaS'], 3))
            self.ui.label_R.setText( Format(self.dicInfo['R'], 5))
            self.ui.label_barinfo.setText( str(self.dicInfo['barinfo']))            
            # endregion

            print('Button Success')
        except:
            print('Button Error')
    
    def Plt_clicked(self):
        try:
            print('dicInfo')
            dicInfo = self.dicInfo
            print(dicInfo)
            D = dicInfo['D']
            b = dicInfo['b']
            h = dicInfo['h']
            BarAsi = dicInfo['BarAsi']
            NumAs = dicInfo['NumAs']
            Es = dicInfo['Es']
            fy = dicInfo['fy']
            EpslonS = dicInfo['EpslonS']            
            ic = dicInfo['ic']
            layer = dicInfo['layer']
            NumAs2 = dicInfo['NumAs2']            
            print('D',D)
            print('b',b)            
            print('h',h)
            print('BarAsi',BarAsi)
            print('NumAs',NumAs)
            print('Es',Es)            
            print('fy',fy) 
            print('ic',ic)
            print('layer',layer)
            print('NumAs2',NumAs2)            
             
            TD.func_beam(dd=D, b=b, h=h, EpslonS=EpslonS, BarAsi=BarAsi, NumAs=NumAs, Es=Es, fy=fy, ic=ic, layer=layer, NumAs2=NumAs2)
            
        except:
            print('Plt Error')
    
    def button_clicked(self):
        self.clicked_counter += 1
        print(f"You clicked {self.clicked_counter} times.")

    def CheckValue(self,cValue,Mcontent):
        if cValue <0:
            self.showBox(Mcontent+'值小於0')
            return False
        else:
            return True
    
    def showBox(self,MContent,MTitle = '提示'):
        self.mbox = QtWidgets.QMessageBox(self)
        self.mbox.information(self,MTitle,MContent)

    def InitForm(self):
        self.ib = self.ui.txb_b.text()
        self.iD = self.ui.txb_d.text()
        self.ih = self.ui.txb_h.text()
        self.iEs = self.ui.txb_Es.text()
        self.ifcp = self.ui.txb_fcp.text()
        self.ify = self.ui.txb_fy.text()
        self.iWc = self.ui.txb_WperCubMeter.text()
        self.iNumAs = self.ui.txb_NumAs.text()
        self.iNumAs2 = self.ui.txb_NumAs_2.text()
        self.ilayer = self.ui.txb_layer.text()
        self.iic = self.ui.txb_ic.text()
    
    def Cancel_clicked(self):
        try:     
            self.ui.txb_b.setText( self.ib )
            self.ui.txb_d.setText( self.iD )
            self.ui.txb_h.setText( self.ih )
            self.ui.txb_Es.setText( self.iEs )
            self.ui.txb_fcp.setText( self.ifcp )
            self.ui.txb_fy.setText( self.ify )
            self.ui.txb_WperCubMeter.setText( self.iWc )
            self.ui.txb_NumAs.setText( self.iNumAs )
            self.ui.txb_NumAs_2.setText( self.iNumAs2 )
            self.ui.txb_layer.setText( self.ilayer )
            self.ui.txb_ic.setText( self.iic )

        except:
            print('Cancel Button Error')

class A002_controller(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__() # in python3, super(Class, self).xxx = super().xxx
        self.ui = vw.Ui_A002_MainWindow()
        self.ui.setupUi(self)
        self.setup_control()

    def setup_control(self):
        self.dicInfo = {}
        self.clicked_counter = 0
        self.ui.btn_Enter.clicked.connect(self.Enter_clicked)
        self.ui.btn_Cancel.clicked.connect(self.Cancel_clicked)
        self.InitForm()

    def Enter_clicked(self):
        try:
            self.clicked_counter += 1
            print(f"\r\nYou clicked {self.clicked_counter} times.")
            # region 取得 User 輸入
            b = strToFloat(self.ui.txb_b.text())
            D = strToFloat(self.ui.txb_d.text())
            DP = strToFloat(self.ui.txb_dp.text())
            h = strToFloat(self.ui.txb_h.text())
            Es = strToFloat(self.ui.txb_Es.text())
            fcp = strToFloat(self.ui.txb_fcp.text())
            fy = strToFloat(self.ui.txb_fy.text())
            Wc = strToFloat(self.ui.txb_WperCubMeter.text())
            BarAsi =self.ui.cbx_BarAsi.currentIndex()
            BarName = self.ui.cbx_BarAsi.currentText()
            NumAs = strToInt(self.ui.txb_NumAs.text())
            BarAsPi =self.ui.cbx_BarAsPi.currentIndex()
            BarPName = self.ui.cbx_BarAsPi.currentText()
            NumAsP = strToInt(self.ui.txb_NumAsP.text())

            print('b',b)
            print('D',D)
            print('DP',DP)
            print('h',h)
            print('Es',Es)
            print('fcp',fcp)
            print('fy',fy)
            print('Wc',Wc)
            print('BarAsi',BarAsi)
            print('BarName',BarName)
            print('NumAs',NumAs)
            print('BarAsPi',BarAsPi)
            print('BarPName',BarPName)
            print('NumAsP',NumAsP)
            
            if(self.CheckValue(b , 'b') == False): return
            if(self.CheckValue(D , 'D') == False): return
            if(self.CheckValue(DP , 'DP') == False): return
            if(self.CheckValue(h , 'h') == False): return
            if(self.CheckValue(Es , 'Es') == False): return
            if(self.CheckValue(fcp, 'fc') == False): return
            if(self.CheckValue(fy , 'fy') == False): return
            if(self.CheckValue(Wc , 'Wc') == False): return
            if(self.CheckValue(NumAs , 'NumAs') == False): return
            if(self.CheckValue(NumAsP , 'NumAsP') == False): return
            # endregion
            
            # region show Tab1   
            self.ui.listWidget.clear()
            # 接收不固定回傳值             
            Ans = TM.A002_Func(Doption=1023, b=b, D=D, dp=DP, h=h, fcp=fcp, fy=fy, Es=Es, Wc=Wc, NumOfBarAs=NumAs, NumOfBarAsP=NumAsP, BarAsPi=BarAsPi, BarAsi=BarAsi)
            # print('Ans',Ans,'\n')
            if isinstance(Ans,tuple):
                for ans in Ans:
                    # print(ans,'\r\n')
                    if isinstance(ans, list):  
                        self.ui.listWidget.addItems(ans)  # 使用 addItems 建立選單
                    elif isinstance(ans, str): 
                        self.ui.listWidget.addItem(ans)
                    elif isinstance(ans, dict):       
                        self.dicInfo.update(ans)  
            elif isinstance(Ans,str):
                self.ui.listWidget.addItem(Ans)
            elif isinstance(Ans,list):
                self.ui.listWidget.addItems(Ans)
            #endregion
                 
            # region show Tab2            
            self.ui.label_b.setText( Format( self.dicInfo['b'], 2))
            self.ui.label_fcp.setText( Format( self.dicInfo['fcp'], 0))
            self.ui.label_d.setText( Format( self.dicInfo['d'], 2))  
            self.ui.label_fy.setText( Format( self.dicInfo['fy'], 0)) 
            self.ui.label_dp.setText( Format( self.dicInfo['dp'], 2)) 
            self.ui.label_Es.setText( Format( self.dicInfo['Es'], 0))  
            self.ui.label_h.setText( Format( self.dicInfo['h'], 2))  
            self.ui.label_Wc.setText( str( self.dicInfo['Wc']))
            self.ui.label_AreaS.setText( Format( self.dicInfo['AreaS'], 2)) 
            self.ui.label_rho.setText( Format( self.dicInfo['rho'], 4)) 
            self.ui.label_AreaSp.setText( Format( self.dicInfo['AreaSp'], 2)) 
            self.ui.label_rhop.setText( Format( self.dicInfo['rhop'], 4)) 
            self.ui.label_EpslonY.setText( Format( self.dicInfo['EpslonY'], 5)) 
            self.ui.label_beta.setText( Format( self.dicInfo['beta'], 2)) 
            self.ui.label_Xb.setText( Format( self.dicInfo['Xb'], 2)) 
            self.ui.label_beta_Xb.setText( Format( self.dicInfo['beta_Xb'], 2)) 
            self.ui.label_Rb.setText( Format( self.dicInfo['Rb'], 4)) 
            self.ui.label_AreaSb.setText( Format( self.dicInfo['AreaSb'], 2)) 
            self.ui.label_rmin.setText( Format( self.dicInfo['rmin'], 4)) 
            self.ui.label_AreaSy.setText( Format( self.dicInfo['AreaSy'], 2)) 
            self.ui.label_rmax.setText( Format( self.dicInfo['rmax'], 4)) 
            self.ui.label_x.setText( Format( self.dicInfo['x'], 2)) 
            self.ui.label_a.setText( Format( self.dicInfo['a'], 2)) 
            self.ui.label_Esp.setText( Format( self.dicInfo['Esp'], 6)) 
            self.ui.label_fsp.setText( Format( self.dicInfo['fsp'], 2)) 
            self.ui.label_Ess.setText( Format( self.dicInfo['Ess'], 6)) 
            self.ui.label_FS.setText( Format( self.dicInfo['FS'], 2)) 
            self.ui.label_cc.setText( Format( self.dicInfo['cc'], 2)) 
            self.ui.label_CS.setText( Format( self.dicInfo['CS'], 2)) 
            self.ui.label_cc_CS.setText( Format( self.dicInfo['cc_CS'], 2)) 
            self.ui.label_T.setText( Format( self.dicInfo['T'], 0)) 
            self.ui.label_Mn.setText( Format( self.dicInfo['Mn'], 2))  
            self.ui.label_Mu.setText( Format( self.dicInfo['Mu'], 2))
            self.ui.label_Mn_T.setText( Format( self.dicInfo['Mn_T'], 2)) 
            # endregion
            
            print('Button Success')
        except:
            print('Button Error')
            pass

    def CheckValue(self,cValue,Mcontent):
        if cValue <0:
            self.showBox(Mcontent+'值小於0')
            return False
        else:
            return True
    
    def showBox(self,MContent,MTitle = '提示'):
        self.mbox = QtWidgets.QMessageBox(self)
        self.mbox.information(self,MTitle,MContent)

    def InitForm(self):
        self.ib = self.ui.txb_b.text()
        self.iD = self.ui.txb_d.text()
        self.iDP = self.ui.txb_dp.text()
        self.ih = self.ui.txb_h.text()
        self.iEs = self.ui.txb_Es.text()
        self.ifcp = self.ui.txb_fcp.text()
        self.ify = self.ui.txb_fy.text()
        self.iWc = self.ui.txb_WperCubMeter.text()      
        self.iNumAs = self.ui.txb_NumAs.text()
        self.iNumAsP = self.ui.txb_NumAsP.text()
    
    def Cancel_clicked(self):
        try:     
            self.ui.txb_b.setText( self.ib )
            self.ui.txb_d.setText( self.iD )
            self.ui.txb_dp.setText( self.iDP )
            self.ui.txb_h.setText( self.ih )
            self.ui.txb_Es.setText( self.iEs )
            self.ui.txb_fcp.setText( self.ifcp )
            self.ui.txb_fy.setText( self.ify )
            self.ui.txb_WperCubMeter.setText( self.iWc )
            self.ui.txb_NumAs.setText( self.iNumAs )
            self.ui.txb_NumAsP.setText( self.iNumAsP )

        except:
            print('Cancel Button Error')

class A003_controller(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__() # in python3, super(Class, self).xxx = super().xxx
        self.ui = vw.Ui_A003_MainWindow()
        self.ui.setupUi(self)
        self.setup_control()

    def setup_control(self):
        self.dicInfo = {}
        self.clicked_counter = 0
        self.ui.btn_Enter.clicked.connect(self.Enter_clicked)
        self.ui.btn_Cancel.clicked.connect(self.Cancel_clicked)
        self.InitForm()

    def Enter_clicked(self):
        try:
            self.clicked_counter += 1
            print(f"\r\nYou clicked {self.clicked_counter} times.")
            # region 取得 User 輸入
            bE = strToFloat(self.ui.txb_bE.text())
            bW = strToFloat(self.ui.txb_bW.text())
            D = strToFloat(self.ui.txb_d.text())
            h = strToFloat(self.ui.txb_h.text())
            t = strToFloat(self.ui.txb_t.text())
            Es = strToFloat(self.ui.txb_Es.text())
            fcp = strToFloat(self.ui.txb_fcp.text())
            fy = strToFloat(self.ui.txb_fy.text())
            Wc = strToFloat(self.ui.txb_WperCubMeter.text())
            BarAsi =self.ui.cbx_BarAsi.currentIndex()
            BarName = self.ui.cbx_BarAsi.currentText()
            NumAs = strToInt(self.ui.txb_NumAs.text())
            TName = self.ui.txb_Tname.text()
            optype = 2
            if self.ui.rbn_optype_0.isChecked()==True:
                optype = 0
            elif self.ui.rbn_optype_1.isChecked()==True:
                optype = 1
            elif self.ui.rbn_optype_2.isChecked()==True:
                optype = 2                
            
            BarName2 = self.ui.cbx_BarAsi_2.currentText()
            NumAs2 = strToInt(self.ui.txb_NumAs_2.text())
            StirrupName = self.ui.cbx_StirrupAsi.currentText()
            layer = strToInt(self.ui.txb_layer.text())
            ic = strToInt(self.ui.txb_ic.text())
            
            print('bE',bE)
            print('bW',bW)
            print('D',D)
            print('h',h)
            print('t',t)
            print('Es',Es)
            print('fcp',fcp)
            print('fy',fy)
            print('Wc',Wc)
            print('BarAsi',BarAsi)
            print('BarName',BarName)
            print('NumAs',NumAs)
            print('TName',TName)
            print(optype)
            print('BarName2',BarName2)
            print('NumAs2',NumAs2)
            print('layer',layer)
            print('ic',ic)
            print('StirrupName',StirrupName) 
            
            if(self.CheckValue(bE , 'bE') == False): return
            if(self.CheckValue(bW , 'bW') == False): return
            if(self.CheckValue(D , 'D') == False): return
            if(self.CheckValue(h , 'h') == False): return
            if(self.CheckValue(t , 't') == False): return
            if(self.CheckValue(Es , 'Es') == False): return
            if(self.CheckValue(fcp, 'fc') == False): return
            if(self.CheckValue(fy , 'fy') == False): return
            if(self.CheckValue(Wc , 'Wc') == False): return
            if(self.CheckValue(NumAs , 'NumAs') == False): return
            # endregion

            # region show Tab1   
            self.ui.listWidget.clear()
            # 接收不固定回傳值             
            Ans = TM.A003_Func(RequiredItem=1023, fcp=fcp, fy=fy, Be=bE, Bw=bW, D=D, T=t, Es=Es, WperCubMeter=Wc, h=h, TName=TName, optype=optype, NumAs=NumAs, BarName=BarName, NumAs2=NumAs2, BarName2=BarName2, layer=layer, ic=ic, StirrupName=StirrupName)
            # print('Ans',Ans,'\n')
            if isinstance(Ans,tuple):
                for ans in Ans:
                    # print(ans,'\r\n')
                    if isinstance(ans, list):  
                        self.ui.listWidget.addItems(ans)  # 使用 addItems 建立選單
                    elif isinstance(ans, str): 
                        self.ui.listWidget.addItem(ans)
                    elif isinstance(ans, dict):       
                        self.dicInfo.update(ans)  
            elif isinstance(Ans,str):
                self.ui.listWidget.addItem(Ans)
            elif isinstance(Ans,list):
                self.ui.listWidget.addItems(Ans)
            #endregion

            # region show Tab2 
            self.ui.label_Be.setText( Format(self.dicInfo['Be'], 2))
            self.ui.label_fcp.setText( Format(self.dicInfo['fcp'], 2))           
            self.ui.label_Bw.setText( Format(self.dicInfo['Bw'], 2))
            self.ui.label_Es.setText( Format(self.dicInfo['Es'], 2))
            self.ui.label_T.setText( Format(self.dicInfo['T'], 2))
            self.ui.label_fy.setText( Format(self.dicInfo['fy'], 2))
            self.ui.label_D.setText( Format(self.dicInfo['D'], 2))
            self.ui.label_WperMeter.setText( Format(self.dicInfo['WperMeter'], 2))
            self.ui.label_h.setText( Format(self.dicInfo['h'], 2))
            self.ui.label_WperCubMeter.setText( Format(self.dicInfo['WperCubMeter'], 2))
            self.ui.label_AreaS.setText( Format(self.dicInfo['AreaS'], 3))
            self.ui.label_beta.setText( Format(self.dicInfo['beta'], 2))
            self.ui.label_esplonY.setText( Format(self.dicInfo['esplonY'], 6))
            self.ui.label_Xb.setText( Format(self.dicInfo['Xb'], 3))
            self.ui.label_C1.setText( Format(self.dicInfo['C1'], 2))
            self.ui.label_Asb.setText( Format(self.dicInfo['Asb'], 3))
            self.ui.label_C2.setText( Format(self.dicInfo['C2'], 2))
            self.ui.label_AsMin.setText( Format(self.dicInfo['AsMin'], 3))
            self.ui.label_Asb_fy.setText( Format(self.dicInfo['Asb_fy'], 2))
            self.ui.label_AsMax.setText( Format(self.dicInfo['AsMax'], 3))
            self.ui.label_a.setText( Format(self.dicInfo['a'], 3))            
            self.ui.label_op_a_T2.setText( str(self.dicInfo['op_a_T2']))            
            self.ui.label_T2.setText( Format(self.dicInfo['T2'], 2))
            self.ui.label_MidTille.setText( str(self.dicInfo['MidTille']))
            self.ui.label_X.setText( Format(self.dicInfo['X'], 3))
            self.ui.label_a2.setText( Format(self.dicInfo['a2'], 3))
            self.ui.label_C1_1000.setText( Format(self.dicInfo['C1_1000'], 3))
            self.ui.label_C2_1000.setText( Format(self.dicInfo['C2_1000'], 3))
            self.ui.label_cc_1000.setText( Format(self.dicInfo['cc_1000'], 3))
            self.ui.label_AreaS_fy_1000.setText( Format(self.dicInfo['AreaS_fy_1000'], 3))
            self.ui.label_Mn.setText( Format(self.dicInfo['Mn'], 3))
            self.ui.label_Mu.setText( Format(self.dicInfo['Mu'], 3))
            self.ui.label_Ans.setText( str(self.dicInfo['Ans']))        
            # endregion
            
            print('Button Success')
        except:
            print('Button Error')
            pass

    def CheckValue(self,cValue,Mcontent):
        if cValue <0:
            self.showBox(Mcontent+'值小於0')
            return False
        else:
            return True
    
    def showBox(self,MContent,MTitle = '提示'):
        self.mbox = QtWidgets.QMessageBox(self)
        self.mbox.information(self,MTitle,MContent)

    def InitForm(self):
        self.ibE = self.ui.txb_bE.text()
        self.ibW = self.ui.txb_bW.text()
        self.iD = self.ui.txb_d.text()
        self.ih = self.ui.txb_h.text()
        self.it = self.ui.txb_t.text()
        self.iEs = self.ui.txb_Es.text()
        self.ifcp = self.ui.txb_fcp.text()
        self.ify = self.ui.txb_fy.text()
        self.iWc = self.ui.txb_WperCubMeter.text()
        self.iNumAs = self.ui.txb_NumAs.text()
        self.iTName = self.ui.txb_Tname.text()
        self.iNumAs2 = self.ui.txb_NumAs_2.text()
        self.ilayer = self.ui.txb_layer.text()
        self.iic = self.ui.txb_ic.text()
    
    def Cancel_clicked(self):
        try:     
            self.ui.txb_bE.setText( self.ibE )
            self.ui.txb_bW.setText( self.ibW )
            self.ui.txb_d.setText( self.iD )
            self.ui.txb_h.setText( self.ih )
            self.ui.txb_t.setText( self.it )
            self.ui.txb_Es.setText( self.iEs )
            self.ui.txb_fcp.setText( self.ifcp )
            self.ui.txb_fy.setText( self.ify )
            self.ui.txb_WperCubMeter.setText( self.iWc )
            self.ui.txb_NumAs.setText( self.iNumAs )
            self.ui.txb_Tname.setText( self.iTName )
            self.ui.txb_NumAs_2.setText( self.iNumAs2 )
            self.ui.txb_layer.setText( self.ilayer )
            self.ui.txb_ic.setText( self.iic )
            
        except:
            print('Cancel Button Error')

class D001_controller(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__() # in python3, super(Class, self).xxx = super().xxx
        self.ui = vw.Ui_D001_MainWindow()
        self.ui.setupUi(self)
        self.setup_control()

    def setup_control(self):   
        self.dicInfo = {}    
        self.clicked_counter = 0 
        self.ui.btn_Enter.clicked.connect(self.Enter_clicked)
        self.ui.btn_plt.clicked.connect(self.Plt_clicked)
        self.ui.btn_Cancel.clicked.connect(self.Cancel_clicked)
        self.InitForm()

    def Enter_clicked(self):
        try:
            self.clicked_counter += 1
            print(f"\r\nYou clicked {self.clicked_counter} times.")
            
            # region 取得 User 輸入           
            b = strToFloat(self.ui.txb_b.text())
            D = strToFloat(self.ui.txb_d.text())
            h = strToFloat(self.ui.txb_h.text())
            ic = strToFloat(self.ui.txb_ic.text())            
            fcp = strToFloat(self.ui.txb_fcp.text())
            Wc = strToFloat(self.ui.txb_WperCubMeter.text())           
            Es = strToFloat(self.ui.txb_Es.text())           
            fy = strToFloat(self.ui.txb_fy.text())
            dagg = strToFloat(self.ui.txb_dagg.text())
            Mn = strToFloat(self.ui.txb_Mn.text())
            Mu = strToFloat(self.ui.txb_Mu.text())
            BarAsi =self.ui.cbx_BarAsi.currentIndex()
            BarName = self.ui.cbx_BarAsi.currentText()
            StirrupName = self.ui.cbx_StirrupAsi.currentText()
            print('b',b)
            print('D',D)
            print('h',h)
            print('Es',Es)
            print('fcp',fcp)
            print('fy',fy)
            print('ic',ic)
            print('Mn',Mn)
            print('Mu',Mu)
            print('BarAsi',BarAsi)
            print('BarName',BarName)
            print('Wc',Wc)
            print('dagg',dagg)
            print('StirrupName',StirrupName)
            # 2023.06.26 UI新增 dagg 、 StirrupName 、 Wc 、 ic
            # dagg 最大粒徑大小    
            
            if(self.CheckValue(b , 'b') == False): return
            if(self.CheckValue(D , 'D') == False): return
            if(self.CheckValue(h , 'h') == False): return
            if(self.CheckValue(ic , 'ic') == False): return
            if(self.CheckValue(fcp, 'fc') == False): return
            if(self.CheckValue(Wc , 'Wc') == False): return
            if(self.CheckValue(Es , 'Es') == False): return
            if(self.CheckValue(fy , 'fy') == False): return
            if(self.CheckValue(dagg , 'dagg') == False): return
            if(self.CheckValue(Mn , 'Mn') == False): return
            if(self.CheckValue(Mu , 'Mu') == False): return
            
            
            #endregion
            
            # region 建立圖表所需字典
            self.dicInfo['BarAsi']=BarAsi
            self.dicInfo['BarName']=BarName        
            self.dicInfo['ic']=ic
            self.dicInfo['StirrupName']=StirrupName            
            # endregion
                                    
            # region show Tab1         
            self.ui.listWidget.clear()
            # 接收不固定回傳值             
            Ans = TM.D001_Func(b=b, BarName=BarName, dagg=dagg, Mu=Mu, StirrupName=StirrupName, Wc=Wc, h=h, Es=Es, fy=fy, fcp=fcp, ic=ic, D=D)
            # print('Ans',Ans,'\n')
            if isinstance(Ans,tuple):
                for ans in Ans:
                    # print(ans,'\r\n')
                    if isinstance(ans, list):  
                        self.ui.listWidget.addItems(ans)  # 使用 addItems 建立選單
                    elif isinstance(ans, str): 
                        self.ui.listWidget.addItem(ans)
                    elif isinstance(ans, dict):       
                        self.dicInfo.update(ans)  
            elif isinstance(Ans,str):
                self.ui.listWidget.addItem(Ans) 
            elif isinstance(Ans,list):
                self.ui.listWidget.addItems(Ans)           
            #endregion
 
            # region show Tab2
            self.ui.label_b.setText( Format(self.dicInfo['b'], 3))
            self.ui.label_fcp.setText( Format(self.dicInfo['fcp'], 2))
            self.ui.label_h.setText( Format(self.dicInfo['h'], 2))  
            self.ui.label_fy.setText( Format(self.dicInfo['fy'], 0))   
            self.ui.label_ic.setText( Format(self.dicInfo['ic'], 2))   
            self.ui.label_Es.setText( Format(self.dicInfo['Es'], 0))
            self.ui.label_Mn.setText( Format(self.dicInfo['Mn'], 2))  
            self.ui.label_Mu.setText( Format(self.dicInfo['Mu'], 2))  
            self.ui.label_D.setText( Format(self.dicInfo['D'], 2))     
            self.ui.label_WperMeter.setText( Format(self.dicInfo['WperMeter'], 2))
            self.ui.label_a.setText( Format(self.dicInfo['a'], 3)) 
            self.ui.label_beta.setText( Format(self.dicInfo['beta'], 2)) 
            self.ui.label_rmin.setText( Format(self.dicInfo['rmin'], 5))
            self.ui.label_rmax.setText( Format(self.dicInfo['rmax'], 5))
            self.ui.label_Asmax.setText( Format(self.dicInfo['Asmax'], 2))
            self.ui.label_m.setText( Format(self.dicInfo['m'], 4)) 
            self.ui.label_Rn.setText( Format(self.dicInfo['Rn'], 2)) 
            self.ui.label_R_req.setText( Format(self.dicInfo['R_req'], 5)) 
            self.ui.label_AreaS.setText( Format(self.dicInfo['AreaS'], 2)) 
            self.ui.label_Asmin.setText( Format(self.dicInfo['Asmin'], 2))
            
            # endregion
           
            print('Button Success') 
        except:
            print('Button Error')
            
    def Plt_clicked(self):
        try:
            print('dicInfo')
            dicInfo = self.dicInfo
            print(dicInfo)
            D = dicInfo['D']
            b = dicInfo['b']
            h = dicInfo['h']
            BarAsi = dicInfo['BarAsi']
            NumAs = dicInfo['NumAs']
            Es = dicInfo['Es']
            fy = dicInfo['fy']
            EpslonS = dicInfo['EpslonS']            
            ic = dicInfo['ic']
            layer = dicInfo['layer']
            NumAs2 = dicInfo['NumAs2']            
            print('D',D)
            print('b',b)            
            print('h',h)
            print('BarAsi',BarAsi)
            print('NumAs',NumAs)
            print('Es',Es)            
            print('fy',fy) 
            print('EpslonS',EpslonS)
            print('ic',ic)
            print('layer',layer)
            print('NumAs2',NumAs2)            
             
            TD.func_beam(dd=D, b=b, h=h, BarAsi=BarAsi, NumAs=NumAs, Es=Es, fy=fy, EpslonS=EpslonS, NumAs2=NumAs2, layer=layer)

        except:
            print('Button Error')
    
    def CheckValue(self,cValue,Mcontent):
        if cValue <0:
            self.showBox(Mcontent+'值小於0')
            return False
        else:
            return True
    
    def showBox(self,MContent,MTitle = '提示'):
        self.mbox = QtWidgets.QMessageBox(self)
        self.mbox.information(self,MTitle,MContent)

    def InitForm(self):
        self.ib = self.ui.txb_b.text()
        self.iD = self.ui.txb_d.text()
        self.ih = self.ui.txb_h.text()
        self.iic = self.ui.txb_ic.text()
        self.ifcp = self.ui.txb_fcp.text()
        self.iWc = self.ui.txb_WperCubMeter.text()
        self.iEs = self.ui.txb_Es.text()
        self.ify = self.ui.txb_fy.text()
        self.idagg = self.ui.txb_dagg.text()
        self.iMn = self.ui.txb_Mn.text()
        self.iMu = self.ui.txb_Mu.text()
    
    def Cancel_clicked(self):
        try:     
            self.ui.txb_b.setText(self.ib )
            self.ui.txb_d.setText(self.iD )
            self.ui.txb_h.setText(self.ih )
            self.ui.txb_ic.setText(self.iic )
            self.ui.txb_fcp.setText(self.ifcp )
            self.ui.txb_WperCubMeter.setText(self.iWc )
            self.ui.txb_Es.setText(self.iEs )
            self.ui.txb_fy.setText(self.ify )
            self.ui.txb_dagg.setText(self.idagg )
            self.ui.txb_Mn.setText(self.iMn )
            self.ui.txb_Mu.setText(self.iMu )
            
        except:
            print('Cancel Button Error')

class D002_controller(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__() # in python3, super(Class, self).xxx = super().xxx
        self.ui = vw.Ui_D002_MainWindow()
        self.ui.setupUi(self)
        self.setup_control()

    def setup_control(self):
        self.dicInfo = {}
        self.clicked_counter = 0
        self.ui.btn_Enter.clicked.connect(self.Enter_clicked)
        self.ui.btn_Cancel.clicked.connect(self.Cancel_clicked)
        self.InitForm()

    def Enter_clicked(self):
        try:
            self.clicked_counter += 1
            print(f"\r\nYou clicked {self.clicked_counter} times.")            
            # region 取得 User 輸入
            b = strToFloat(self.ui.txb_b.text())
            D = strToFloat(self.ui.txb_d.text())
            DP = strToFloat(self.ui.txb_dp.text())
            h = strToFloat(self.ui.txb_h.text())
            Es = strToFloat(self.ui.txb_Es.text())
            fcp = strToFloat(self.ui.txb_fcp.text())
            fy = strToFloat(self.ui.txb_fy.text())
            Wc = strToFloat(self.ui.txb_WperCubMeter.text())
            Mn = strToFloat(self.ui.txb_Mn.text())
            Mu = strToFloat(self.ui.txb_Mu.text())
            BarAsi =self.ui.cbx_BarAsi.currentIndex()
            BarName = self.ui.cbx_BarAsi.currentText()
            NumAs = strToInt(self.ui.txb_NumAs.text())
            BarAsPi =self.ui.cbx_BarAsPi.currentIndex()
            BarPName = self.ui.cbx_BarAsPi.currentText()
            NumAsP = strToInt(self.ui.txb_NumAsP.text())
            print('b',b)
            print('D',D)
            print('DP',DP)
            print('h',h)
            print('Es',Es)
            print('fcp',fcp)
            print('fy',fy)
            print('Wc',Wc)
            print('Mn',Mn)
            print('Mu',Mu)
            print('BarAsi',BarAsi)
            print('BarName',BarName)
            print('NumAs',NumAs)
            print('BarAsPi',BarAsPi)
            print('BarPName',BarPName)
            print('NumAsP',NumAsP)
            
            if(self.CheckValue(b , 'b') == False): return
            if(self.CheckValue(D , 'D') == False): return
            if(self.CheckValue(DP , 'DP') == False): return
            if(self.CheckValue(h , 'h') == False): return
            if(self.CheckValue(Es , 'Es') == False): return
            if(self.CheckValue(fcp, 'fc') == False): return
            if(self.CheckValue(fy , 'fy') == False): return
            if(self.CheckValue(Wc , 'Wc') == False): return
            if(self.CheckValue(Mn , 'Mn') == False): return
            if(self.CheckValue(Mu , 'Mu') == False): return
            if(self.CheckValue(NumAs , 'NumAs') == False): return
            if(self.CheckValue(NumAsP , 'NumAsP') == False): return
            # endregion

            # region show Tab1   
            self.ui.listWidget.clear()
            # 接收不固定回傳值             
            Ans = TM.D002_Func(b=b, D=D, dp=DP, h=h, Mn=Mn, Mu=Mu, fcp=fcp, fy=fy, Es=Es, Wc=Wc, BarAsi=BarAsi, BarAsPi=BarAsPi)
            # print('Ans',Ans,'\n')
            if isinstance(Ans,tuple):
                for ans in Ans:
                    # print(ans,'\r\n')
                    if isinstance(ans, list):  
                        self.ui.listWidget.addItems(ans)  # 使用 addItems 建立選單
                    elif isinstance(ans, str): 
                        self.ui.listWidget.addItem(ans)
                    elif isinstance(ans, dict):       
                        self.dicInfo.update(ans)  
            elif isinstance(Ans,str):
                self.ui.listWidget.addItem(Ans)
            elif isinstance(Ans,list):
                self.ui.listWidget.addItems(Ans)
             #endregion
            
            # region show Tab2        
            self.ui.label_b.setText( Format( self.dicInfo['b'], 2))
            self.ui.label_fcp.setText( Format( self.dicInfo['fcp'], 0))
            self.ui.label_D.setText( Format( self.dicInfo['D'], 2))  
            self.ui.label_fy.setText( Format( self.dicInfo['fy'], 0)) 
            self.ui.label_dp.setText( Format( self.dicInfo['dp'], 2)) 
            self.ui.label_Es.setText( Format( self.dicInfo['Es'], 0))  
            self.ui.label_h.setText( Format( self.dicInfo['h'], 2))  
            self.ui.label_Wc.setText( Format( self.dicInfo['Wc'], 2))
            self.ui.label_Mn.setText( Format( self.dicInfo['Mn'], 2))  
            self.ui.label_Mu.setText( Format( self.dicInfo['Mu'], 2))
            self.ui.label_beta.setText( Format( self.dicInfo['beta'], 3))
            self.ui.label_m.setText( Format( self.dicInfo['m'], 3))  
            self.ui.label_EpslonY.setText( Format( self.dicInfo['EpslonY'], 6)) 
            self.ui.label_rmax.setText( Format( self.dicInfo['rmax'], 4))
            self.ui.label_rmin.setText( Format( self.dicInfo['rmin'], 2)) 
            self.ui.label_rmax_b_D.setText( Format( self.dicInfo['rmax_b_D'], 2)) 
            self.ui.label_Mnmax.setText( Format( self.dicInfo['Mnmax'], 2))
            
            self.ui.label_Xb_1.setText( Format( self.dicInfo['Xb_1'], 2)) 
            self.ui.label_Rb_1.setText( Format( self.dicInfo['Rb_1'], 4)) 
            self.ui.label_Esp_1.setText( Format( self.dicInfo['Esp_1'], 6))            
            self.ui.label_fsp_1.setText( Format( self.dicInfo['fsp_1'], 2)) 
            self.ui.label_Mn1_1.setText( Format( self.dicInfo['Mn1_1'], 2)) 
            self.ui.label_Mn2_1.setText( Format( self.dicInfo['Mn2_1'], 2)) 
            self.ui.label_AreaST_1.setText( Format( self.dicInfo['AreaST_1'], 2))             
            self.ui.label_rho_1.setText( Format( self.dicInfo['rho_1'], 5)) 
            self.ui.label_AreaSelectedAs_1.setText(str( self.dicInfo['AreaSelectedAs_1']))
            self.ui.label_RhoSelectedAs_1.setText( Format( self.dicInfo['RhoSelectedAs_1'], 5)) 
            self.ui.label_SpaceAs_1.setText( Format( self.dicInfo['SpaceAs_1'], 2)) 
            self.ui.label_AreaSp_1.setText( Format( self.dicInfo['AreaSp_1'], 2))             
            self.ui.label_rhop_1.setText( Format( self.dicInfo['rhop_1'], 5)) 
            self.ui.label_AreaSelectedAsp_1.setText(str( self.dicInfo['AreaSelectedAsp_1']))
            self.ui.label_RhoSelectedAsp_1.setText( Format( self.dicInfo['RhoSelectedAsp_1'], 5)) 
            self.ui.label_SpaceAsp_1.setText( Format( self.dicInfo['SpaceAsp_1'], 2)) 
            self.ui.label_rmax_1.setText( Format( self.dicInfo['rmax_1'], 4)) 
            self.ui.label_rmin_1.setText( Format( self.dicInfo['rmin_1'], 4)) 
            
            self.ui.label_Xb_2.setText( Format( self.dicInfo['Xb_2'], 2)) 
            self.ui.label_Rb_2.setText( Format( self.dicInfo['Rb_2'], 4)) 
            self.ui.label_Esp_2.setText( Format( self.dicInfo['Esp_2'], 6))            
            self.ui.label_fsp_2.setText( Format( self.dicInfo['fsp_2'], 2)) 
            self.ui.label_Mn1_2.setText( Format( self.dicInfo['Mn1_2'], 2)) 
            self.ui.label_Mn2_2.setText( Format( self.dicInfo['Mn2_2'], 2)) 
            self.ui.label_AreaST_2.setText( Format( self.dicInfo['AreaST_2'], 2))             
            self.ui.label_rho_2.setText( Format( self.dicInfo['rho_2'], 5)) 
            self.ui.label_AreaSelectedAs_2.setText( str( self.dicInfo['AreaSelectedAs_2']))
            self.ui.label_RhoSelectedAs_2.setText( Format( self.dicInfo['RhoSelectedAs_2'], 5)) 
            self.ui.label_SpaceAs_2.setText( Format( self.dicInfo['SpaceAs_2'], 2)) 
            self.ui.label_AreaSp_2.setText( Format( self.dicInfo['AreaSp_2'], 2))             
            self.ui.label_rhop_2.setText( Format( self.dicInfo['rhop_2'], 5)) 
            self.ui.label_AreaSelectedAsp_2.setText( str( self.dicInfo['AreaSelectedAsp_2']))
            self.ui.label_RhoSelectedAsp_2.setText( Format( self.dicInfo['RhoSelectedAsp_2'], 5)) 
            self.ui.label_SpaceAsp_2.setText( Format( self.dicInfo['SpaceAsp_2'], 2)) 
            self.ui.label_rmax_2.setText( Format( self.dicInfo['rmax_2'], 4)) 
            self.ui.label_rmin_2.setText( Format( self.dicInfo['rmin_2'], 4)) 
            
            self.ui.label_Xb_3.setText( Format( self.dicInfo['Xb_3'], 2)) 
            self.ui.label_Rb_3.setText( Format( self.dicInfo['Rb_3'], 4)) 
            self.ui.label_Esp_3.setText( Format( self.dicInfo['Esp_3'], 6))            
            self.ui.label_fsp_3.setText( Format( self.dicInfo['fsp_3'], 2)) 
            self.ui.label_Mn1_3.setText( Format( self.dicInfo['Mn1_3'], 2)) 
            self.ui.label_Mn2_3.setText( Format( self.dicInfo['Mn2_3'], 2)) 
            self.ui.label_AreaST_3.setText( Format( self.dicInfo['AreaST_3'], 2))             
            self.ui.label_rho_3.setText( Format( self.dicInfo['rho_3'], 5)) 
            self.ui.label_AreaSelectedAs_3.setText( str( self.dicInfo['AreaSelectedAs_3']))
            self.ui.label_RhoSelectedAs_3.setText( Format( self.dicInfo['RhoSelectedAs_3'], 5)) 
            self.ui.label_SpaceAs_3.setText( Format( self.dicInfo['SpaceAs_3'], 2)) 
            self.ui.label_AreaSp_3.setText( Format( self.dicInfo['AreaSp_3'], 2))             
            self.ui.label_rhop_3.setText( Format( self.dicInfo['rhop_3'], 5)) 
            self.ui.label_AreaSelectedAsp_3.setText( str( self.dicInfo['AreaSelectedAsp_3']))
            self.ui.label_RhoSelectedAsp_3.setText( Format( self.dicInfo['RhoSelectedAsp_3'], 5)) 
            self.ui.label_SpaceAsp_3.setText( Format( self.dicInfo['SpaceAsp_3'], 2)) 
            self.ui.label_rmax_3.setText( Format( self.dicInfo['rmax_3'], 4)) 
            self.ui.label_rmin_3.setText( Format( self.dicInfo['rmin_3'], 4)) 
            
            # endregion

            print('Button Success')
        except:
            print('Button Error')
            pass

    def CheckValue(self,cValue,Mcontent):
        if cValue <0:
            self.showBox(Mcontent+'值小於0')
            return False
        else:
            return True
    
    def showBox(self,MContent,MTitle = '提示'):
        self.mbox = QtWidgets.QMessageBox(self)
        self.mbox.information(self,MTitle,MContent)

    def InitForm(self):
        self.ib = self.ui.txb_b.text()
        self.iD = self.ui.txb_d.text()
        self.iDP = self.ui.txb_dp.text()
        self.ih = self.ui.txb_h.text()
        self.iEs = self.ui.txb_Es.text()
        self.ifcp = self.ui.txb_fcp.text()
        self.ify = self.ui.txb_fy.text()
        self.iWc = self.ui.txb_WperCubMeter.text()
        self.iMn = self.ui.txb_Mn.text()
        self.iMu = self.ui.txb_Mu.text()
        self.iNumAs = self.ui.txb_NumAs.text()
        self.iNumAsP = self.ui.txb_NumAsP.text()
    
    def Cancel_clicked(self):
        try:     
            self.ui.txb_b.setText(self.ib )
            self.ui.txb_d.setText(self.iD )
            self.ui.txb_dp.setText(self.iDP )
            self.ui.txb_h.setText(self.ih )
            self.ui.txb_Es.setText(self.iEs )
            self.ui.txb_fcp.setText(self.ifcp )
            self.ui.txb_fy.setText(self.ify )
            self.ui.txb_WperCubMeter.setText(self.iWc )
            self.ui.txb_Mn.setText(self.iMn )
            self.ui.txb_Mu.setText(self.iMu )
            self.ui.txb_NumAs.setText(self.iNumAs )
            self.ui.txb_NumAsP.setText(self.iNumAsP )
            
        except:
            print('Cancel Button Error')

class D003_controller(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__() # in python3, super(Class, self).xxx = super().xxx
        self.ui = vw.Ui_D003_MainWindow()
        self.ui.setupUi(self)
        self.setup_control()

    def setup_control(self):
        self.dicInfo = {}
        self.clicked_counter = 0
        self.ui.btn_Enter.clicked.connect(self.Enter_clicked)        
        self.ui.btn_Cancel.clicked.connect(self.Cancel_clicked)
        self.InitForm()

    def Enter_clicked(self):
        try:
            self.clicked_counter += 1
            print(f"\r\nYou clicked {self.clicked_counter} times.")
            # region 取得 User 輸入
            bE = strToFloat(self.ui.txb_bE.text())
            bW = strToFloat(self.ui.txb_bW.text())
            D = strToFloat(self.ui.txb_d.text())
            h = strToFloat(self.ui.txb_h.text())
            t = strToFloat(self.ui.txb_t.text())
            Es = strToFloat(self.ui.txb_Es.text())
            fcp = strToFloat(self.ui.txb_fcp.text())
            fy = strToFloat(self.ui.txb_fy.text())
            Wc = strToFloat(self.ui.txb_WperCubMeter.text())
            Mn = strToFloat(self.ui.txb_Mn.text())
            Mu = strToFloat(self.ui.txb_Mu.text())
            BarAsi =self.ui.cbx_BarAsi.currentIndex()
            BarName = self.ui.cbx_BarAsi.currentText()
            BarAsPi =self.ui.cbx_BarAsPi.currentIndex()
            BarPName = self.ui.cbx_BarAsPi.currentText()
            TName = self.ui.txb_Tname.text()
            Alpha = strToFloat(self.ui.txb_Alpha.text())            
            optype = 2
            if self.ui.rbn_optype_0.isChecked()==True:
                optype = 0
            elif self.ui.rbn_optype_1.isChecked()==True:
                optype = 1
            elif self.ui.rbn_optype_2.isChecked()==True:
                optype = 2
                
            # 2023.06.26 UI新增
            dp = strToFloat(self.ui.txb_dp.text())
            isTDesign = self.ui.cbx_isTDesign.isChecked()
            
            print('bE',bE)
            print('bW',bW)
            print('D',D)
            print('h',h)
            print('t',t)
            print('Es',Es)
            print('fcp',fcp)
            print('fy',fy)
            print('Wc',Wc)
            print('Mn',Mn)
            print('Mu',Mu)
            print('BarAsi',BarAsi)
            print('BarName',BarName)
            print('BarAsPi',BarAsPi)
            print('BarPName',BarPName)
            print('TName',TName)
            print('Alpha',Alpha)
            print('optype',optype)
            print('dp', dp)
            print('isTDesign', isTDesign)
            
            if(self.CheckValue(bE,'bE') == False): return
            if(self.CheckValue(bW,'bW') == False): return
            if(self.CheckValue(D,'D') == False): return
            if(self.CheckValue(h,'h') == False): return
            if(self.CheckValue(t,'t') == False): return
            if(self.CheckValue(Es,'Es') == False): return
            if(self.CheckValue(fcp,'fcp') == False): return
            if(self.CheckValue(fy,'fy') == False): return
            if(self.CheckValue(Wc,'Wc') == False): return
            if(self.CheckValue(Mn,'Mn') == False): return
            if(self.CheckValue(Mu,'Mu') == False): return
            if(self.CheckValue(Alpha,'Alpha') == False): return
            # endregion

            # region show Tab1   
            self.ui.listWidget.clear()
            # 接收不固定回傳值             
            Ans = TM.D003_Func(isTDesign=isTDesign, fcp=fcp, fy=fy, Be=bE, Bw=bW, D=D, T=t, Mu=Mu, Mn=Mn, Es=Es, h=h, WperCubMeter=Wc, optype=optype, BarAsi=BarAsi, BarAsPi=BarAsPi, Alpha=Alpha, TName=TName)
            # print('Ans',Ans,'\n')
            if isinstance(Ans,tuple):
                for ans in Ans:
                    # print(ans,'\r\n')
                    if isinstance(ans, list):  
                        self.ui.listWidget.addItems(ans)  # 使用 addItems 建立選單
                    elif isinstance(ans, str): 
                        self.ui.listWidget.addItem(ans)
                    elif isinstance(ans, dict):       
                        self.dicInfo.update(ans)  
            elif isinstance(Ans,str):
                self.ui.listWidget.addItem(Ans)
            elif isinstance(Ans,list):
                self.ui.listWidget.addItems(Ans)
            #endregion

            # region show Tab2 
            self.ui.label_Be.setText( Format(self.dicInfo['Be'], 2))
            self.ui.label_fcp.setText( Format(self.dicInfo['fcp'], 2))           
            self.ui.label_Bw.setText( Format(self.dicInfo['Bw'], 2))
            self.ui.label_beta.setText( Format(self.dicInfo['beta'], 2))
            self.ui.label_T.setText( Format(self.dicInfo['T'], 2))
            self.ui.label_fy.setText( Format(self.dicInfo['fy'], 2))
            self.ui.label_h.setText( Format(self.dicInfo['h'], 2))
            self.ui.label_Es.setText( Format(self.dicInfo['Es'], 2))
            self.ui.label_Mn.setText( Format(self.dicInfo['Mn'], 3))
            self.ui.label_WperMeter.setText( Format(self.dicInfo['WperMeter'], 2))
            self.ui.label_Mu.setText( Format(self.dicInfo['Mu'], 3))
            self.ui.label_WperCubMeter.setText( Format(self.dicInfo['WperCubMeter'], 2))
            self.ui.label_m.setText( Format(self.dicInfo['m'], 3))
            self.ui.label_d.setText( Format(self.dicInfo['D'], 2))   
            self.ui.label_Mcn.setText( Format(self.dicInfo['Mcn'], 3))
            self.ui.label_dp.setText( Format(self.dicInfo['dp'], 3))
            self.ui.label_X.setText( Format(self.dicInfo['X'], 3))
            self.ui.label_a.setText( Format(self.dicInfo['a'], 3))
            #print(self.dicInfo.get('Rn','Rn errer'))
           
            self.ui.label_Asb.setText( Format(self.dicInfo['Asb'], 3))
            self.ui.label_Rb.setText( Format(self.dicInfo['Rb'], 3))
            self.ui.label_AsMin.setText( Format(self.dicInfo['AsMin'], 3))
            self.ui.label_AsMax.setText( Format(self.dicInfo['AsMax'], 3))
            self.ui.label_C1.setText( Format(self.dicInfo['C1'], 3))
            self.ui.label_Mc1.setText( Format(self.dicInfo['Mc1'], 3))
            self.ui.label_C2.setText( Format(self.dicInfo['C2'], 3))
            self.ui.label_Mc2.setText( Format(self.dicInfo['Mc2'], 3))
            self.ui.label_CS.setText( Format(self.dicInfo['CS'], 3))
            self.ui.label_Mcs.setText( Format(self.dicInfo['Mcs'], 3))
            self.ui.label_cc.setText( Format(self.dicInfo['cc'], 3))
            self.ui.label_Mt.setText( Format(self.dicInfo['Mt'], 3))
            self.ui.label_AreaS_fy.setText( Format(self.dicInfo['AreaS_fy'], 3))
            self.ui.label_AreaS.setText( Format(self.dicInfo['AreaS'], 3))
            self.ui.label_AreaS_Bw_D.setText( Format(self.dicInfo['AreaS_Bw_D'], 3))
            self.ui.label_AreaSelectedAs.setText( Format(self.dicInfo['AreaSelectedAs'], 3))
            self.ui.label_RhoSelectedAs.setText( Format(self.dicInfo['RhoSelectedAs'], 3))
            self.ui.label_AreaSp.setText( Format(self.dicInfo['AreaSp'], 3))
            self.ui.label_AreaSp_Bw_D.setText( Format(self.dicInfo['AreaSp_Bw_D'], 3))
            self.ui.label_AreaSelectedAsp.setText( Format(self.dicInfo['AreaSelectedAsp'], 3))
            self.ui.label_RhoSelectedAsp.setText( Format(self.dicInfo['RhoSelectedAsp'], 3))
            self.ui.label_Rn.setText(self.dicInfo['Rn'])   
            # endregion
            
            print('Button Success')
            # Ans, dicInfo = TM.D003_Func(isTDesign=True, fcp=280, fy=4200, Be=120, Bw=40, D=53, T=12, Mu=100, Mn=90, Es=2040000, h=60, WperCubMeter=2400, optype=2, BarAsi=5, BarAsPi=5, Alpha=1, TName='TName')
            # TD.funcT_beam(dd=D, be=bE, bw=bW, h=h, hf=t, fy=fy, Es=Es, BarAsi=BarAsi, BarAsPi=BarAsPi, NumAs=dicInfo['NumAs'], NumOfBarAsP=dicInfo['NumOfBarAsP'], EpslonS=dicInfo['EpslonS'])
        except:
            print(6)
            print('Button Error')
            pass

    def CheckValue(self,cValue,Mcontent):
        if cValue <0:
            self.showBox(Mcontent+'值小於0')
            return False
        else:
            return True
    
    def showBox(self,MContent,MTitle = '提示'):
        self.mbox = QtWidgets.QMessageBox(self)
        self.mbox.information(self,MTitle,MContent)
    
    def InitForm(self):
        self.ibE = self.ui.txb_bE.text()
        self.ibW = self.ui.txb_bW.text()
        self.iD = self.ui.txb_d.text()
        self.ih = self.ui.txb_h.text()
        self.it = self.ui.txb_t.text()
        self.iEs = self.ui.txb_Es.text()
        self.ifcp = self.ui.txb_fcp.text()
        self.ify = self.ui.txb_fy.text()
        self.iWc = self.ui.txb_WperCubMeter.text()
        self.iMn = self.ui.txb_Mn.text()
        self.iMu = self.ui.txb_Mu.text()
        self.iAlpha = self.ui.txb_Alpha.text()
        self.idp = self.ui.txb_dp.text()        
        self.iTName = self.ui.txb_Tname.text()
    
    def Cancel_clicked(self):
        try:
            self.ui.txb_bE.setText(self.ibE)
            self.ui.txb_bW.setText(self.ibW)
            self.ui.txb_d.setText(self.iD)
            self.ui.txb_h.setText(self.ih)
            self.ui.txb_t.setText(self.it)
            self.ui.txb_Es.setText(self.iEs)
            self.ui.txb_fcp.setText(self.ifcp)
            self.ui.txb_fy.setText(self.ify)
            self.ui.txb_WperCubMeter.setText(self.iWc)
            self.ui.txb_Mn.setText(self.iMn)
            self.ui.txb_Mu.setText(self.iMu)
            self.ui.txb_Alpha.setText(self.iAlpha)
            self.ui.txb_dp.setText(self.idp)        
            self.ui.txb_Tname.setText(self.iTName)
            
        except:
            print('Cancel Button Error')
            
        