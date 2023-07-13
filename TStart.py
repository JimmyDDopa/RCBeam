from PyQt6 import QtWidgets
import TController as TC
#from TController import MainWindow_controller



if __name__ == '__main__':
    import sys
    try:
        app = QtWidgets.QApplication(sys.argv)

        MenuWindow = TC.Menu_controller()     
        MenuWindow.show()
        
        # window = TC.A001_controller()     
        # window.show()
        
        # window2 = TC.A002_controller()
        # window2.show()
        
        # window3 = TC.A003_controller()
        # window3.show()
        
        # windowD = TC.D001_controller()
        # windowD.show()
        
        # windowD2 = TC.D002_controller()
        # windowD2.show()
        
        # windowD3 = TC.D003_controller()
        # windowD3.show()
        
        sys.exit(app.exec())
    except :
        print('Close Exe')
        
    
