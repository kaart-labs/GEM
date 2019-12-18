import os
import sys
import sys, random
import string
from PySide2.QtWidgets import QApplication
from PySide2 import QtCore, QtGui, QtWidgets
import PyQt5
from PyQt5 import QtGui,QtCore
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5 import QtGui, QtCore, uic
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QLabel, QGridLayout, QWidget
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtCore import QSize
################################################
__author__ = "Chris Gousset"
__copyright__ = "N/A"
__credits__ = ["Louis Morales","Zack LaVergne"]
__license__ = "N/A"
__version__ = "2.0"
__maintainer__ = "Chris Gousset"
__email__ = "chris.gousset@kaart.com"
__status__ = "Development"

################################################        
try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s
try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

###############################################
class CONFIRMPOPUP (QMainWindow ):
    def __init__(self):
        QMainWindow.__init__(self)
        #self.setWindowFlags(QtCore.Qt.Window | QtCore.Qt.CustomizeWindowHint | Qt.WindowStaysOnTopHint)
        self.setGeometry(900,100,300,80)
        self.setWindowTitle("CONFIRMATION")
        self.POPHOME()

    def POPHOME(self):
        self.LABEL = QtWidgets.QLabel(self)
        self.LABEL.setText("Are you sure you want to remove this Editor?")
        self.LABEL.resize(300,20)
        self.LABEL.move(13,5)
        
        self.CONFIRM = QPushButton(self)
        self.CONFIRM.setText("CONFIRM")
        self.CONFIRM.resize(150,25)
        self.CONFIRM.move(5,30)
        self.CONFIRM.clicked.connect(self.CONFIRMED_clicked)

        self.CANCEL = QPushButton(self)
        self.CANCEL .setText("CANCEL")
        self.CANCEL .resize(150,25)
        self.CANCEL .move(145,30)
        self.CANCEL.clicked.connect(self.CANCEL_clicked)
        self.show()

    def CONFIRMED_clicked(self):
        if one.GOREMOVEALL == False:
           one.REMOVE_GO()
        if one.GOREMOVEALL == True:
            one.REMOVEALL_GO()
        self.close()
    def CANCEL_clicked(self):
        self.close()
        


class TABMOD(QAbstractTableModel):
    def __init__(self, ARRAY,headers =[], parent=None,):
        QAbstractTableModel.__init__(self, parent)
        self.arraydata=ARRAY
        self.headers = headers
        self.thumbSize=64
    def resizePixmap(self, mult):
        self.thumbSize=self.thumbSize*mult
        self.reset()
    def flags(self, index):
        return Qt.ItemIsEnabled | Qt.ItemIsSelectable | Qt.ItemIsEditable
    def rowCount(self, parent):
        return 50      
    def columnCount(self, parent):
        return 4
    def data ( self , index , role ):
        row = index.row()
        column = index.column()
        value = self.arraydata[row][column]
        if role == QtCore.Qt.DisplayRole: 
            row = index.row()
            column = index.column()
            if column == 0:
                try:
                    value = self.arraydata[row][column]
                    self.dataChanged.emit(index,index)
                    return str(value)
                except:
                 pass
            if column == 1:
                try:
                    value = self.arraydata[row][column]
                    self.dataChanged.emit(index,index)
                    return str(value)
                except:
                 pass 
        if role == QtCore.Qt.DecorationRole:
            row = index.row()
            column = index.column()

            if column == 2:
                pix=(QtGui.QPixmap(15, 15))
                value = self.arraydata[row][column]
                pix.fill(value)
                self.dataChanged.emit(index,index)
                icon = QtGui.QIcon(pix) 
                return icon
            if column == 3:
                pix=(QtGui.QPixmap(15, 15))
                value = self.arraydata[row][column]
                pix.fill(value)
                self.dataChanged.emit(index,index)
                icon = QtGui.QIcon(pix) 
                return icon

    def setData(self, index, value):
        if role == QtCore.Qt.DisplayRole: 
            row = index.row()
            column = index.column()
            if column == 0:
              try:  
                value = self.arraydata[row][column]
                self.dataChanged.emit(index,index)
                return str(value)
              except:      
                pass    
            if column == 1:
               try:
                value = self.arraydata[row][column]
                self.dataChanged.emit(index,index)
                return str(value)
               except:
                 pass 
        if role == QtCore.Qt.DecorationRole:
            row = index.row()
            column = index.column()
 

            if column == 2:
                pix=(QtGui.QPixmap(15, 15))
                value = self.arraydata[row][column]
                pix.fill(value)
                self.dataChanged.emit(index,index)
                icon = QtGui.QIcon(pix) 
                return icon
            if column == 3:
                pix=(QtGui.QPixmap(15, 15))
                value = self.arraydata[row][column]
                pix.fill(value)
                self.dataChanged.emit(index,index)
                icon = QtGui.QIcon(pix) 
                return icon

    def headerData(self,section,orientation,role):
        if role == QtCore.Qt.DisplayRole:
            if orientation == QtCore.Qt.Horizontal:
                if section < len (self.headers):
                    return self.headers[section]
#####################################################     
Model = TABMOD
clear=  QtGui.QColor(0,0,0,0)
red   = QtGui.QColor(255,0,0)

class EDITORINFO(object):
        def __init__ (self):
            self.NAME = ''
            self.UID = ''
            self.LINECOLORTEXT = ""
            self.NODECOLORTEXT = ""
            self.LINECOLORUI = ""
            self.NODECOLORUI = ""
            self.ICONSIZE= 10
            self.LINEWIDTH = 5
            self.ICONSHAPE = ""
###############################################
            
class MAINWindow (QMainWindow ):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setGeometry(650,300,580,420)
        self.setWindowTitle("Q.A. PAINTSTYLE GENERATOR")
        self.MWHOME(self)

    def MWHOME(self, MAINWindow):
        MAINWindow.setObjectName(_fromUtf8("MAINWindow"))
        self.GOREMOVEALL = False
        self.TEAMNAMETEXT = ""
        self.SETUPENTRYBLOCK = ""
        self.SETTINGBLOCK = ""
        self.NODEENTRYBLOCK = ""
        self.WAYENTRYBLOCK = ""
        self.MASTEROUTPUTBLOCK = ""
        self.WHITE = "#FFFFFF"
        self.EDITORNODECOLORUI = "#FFFFFF"
        self.TEAMLINECOLORTEXT = "#47D608"
        self.TEAMNODECOLORTEXT = "orange"
        self.TEAMLINECOLORUI = "#47D608"
        self.TEAMNODECOLORUI = "#ffaa00"
        self.LINEWIDTH  = 5
        self.ICONSIZE = 10
        self.TEAMICONSHAPE = "Circle"
        self.FOLDER = os.getcwd()
        self.NRSELECT = ''
        self.usercount = 0
        self.tempcount = 1
        self.TEMPUSERS = {}
        for j in range(100):  
            self.TEMPUSERS[str(j)] = 0
        self.ADDUSERS=[]
        self.filters = ''
        self.select_filters = 'MAPCSS (*.mapcss)'
        self.directory = os.getcwd()
        self.SELTEXT= ''
        
################################TABLE BUTTONS#######################################
        
        self.TABLE = QtWidgets.QTableView(self)
        self.TABLE.resize(300,330)
        self.TABLE.move(255,10)

        self.REMOVE = QtWidgets.QPushButton(self)
        self.REMOVE.setText("REMOVE")
        self.REMOVE.resize(110,25)
        self.REMOVE.move(250,347)
        self.REMOVE.clicked.connect(self.REMOVE_clicked)

        self.REMOVEALL = QPushButton(self)
        self.REMOVEALL.setText("REMOVE ALL")
        self.REMOVEALL.resize(110,25)
        self.REMOVEALL.move(350,347)
        self.REMOVEALL.clicked.connect(self.REMOVEALL_clicked)

        self.EXPORT = QPushButton(self)
        self.EXPORT.setText("EXPORT")
        self.EXPORT.resize(110,25)
        self.EXPORT.move(250,372)
        self.EXPORT.clicked.connect(self.EXPORT_clicked)
        
        self.IMPORT = QPushButton(self)
        self.IMPORT.setText("IMPORT")
        self.IMPORT.resize(110,25)
        self.IMPORT.move(350,372)
        self.IMPORT.clicked.connect(self.IMPORT_clicked)
        
######################################TEAM SETTINGS#####################################
        self.groupBox = QtWidgets.QGroupBox(self)

        self.groupBox.setGeometry(QtCore.QRect(5, 10, 245, 40))

        self.TEAMNAMELABEL = QtWidgets.QLabel(self.groupBox)
        self.TEAMNAMELABEL.setText("Team Name")
        self.TEAMNAMELABEL.resize(250,20)
        self.TEAMNAMELABEL.move(10,8)

        self.TEAMNAME= QtWidgets.QLineEdit(self.groupBox)
        self.TEAMNAME.resize(130,20)
        self.TEAMNAME.move(105,8)
######################################HIGHLIGHT SETTINGS#####################################
        self.groupBox3 = QtWidgets.QGroupBox(self)
        self.groupBox3.setGeometry(QtCore.QRect(5, 55, 245, 120))


        self.NOTUPLOADEDLABEL = QtWidgets.QLabel(self.groupBox3)
        self.NOTUPLOADEDLABEL.setText("Highlight non-uploaded additions")
        self.NOTUPLOADEDLABEL.resize(250,20)
        self.NOTUPLOADEDLABEL.move(10,5)



        self.TEAMLINECOLOR= QPushButton(self.groupBox3)
        self.TEAMLINECOLOR.setText("LINE COLOR")
        self.TEAMLINECOLOR.resize(110,25)
        self.TEAMLINECOLOR.move(3,30)
        self.TEAMLINECOLOR.clicked.connect(self.TEAMLINECOLOR_clicked)

        self.TEAMLINECOLORICON = QtWidgets.QLabel(self.groupBox3)
        self.TEAMLINECOLORICON.move(110,37)
        self.pix=(QtGui.QPixmap(15, 15))
        self.pix.fill(QColor(self.WHITE))
        self.TEAMLINECOLORICON.setPixmap(self.pix) 

        self.LINEWIDTHLABEL = QtWidgets.QLabel(self.groupBox3)
        self.LINEWIDTHLABEL.setText("Line Width")
        self.LINEWIDTHLABEL.resize(250,20)
        self.LINEWIDTHLABEL.move(130,34)
        
        self.TEAMLINEWIDTHSPIN = QtWidgets.QSpinBox(self.groupBox3)
        self.TEAMLINEWIDTHSPIN.setRange(1, 20)
        self.TEAMLINEWIDTHSPIN.setValue(self.LINEWIDTH)
        self.TEAMLINEWIDTHSPIN.move(200,34)        
        
        self.TEAMNODECOLOR= QPushButton(self.groupBox3)
        self.TEAMNODECOLOR.setText("NODE COLOR")
        self.TEAMNODECOLOR.resize(110,25)
        self.TEAMNODECOLOR.move(3,55)
        self.TEAMNODECOLOR.clicked.connect(self.TEAMNODECOLOR_clicked)

        self.TEAMNODECOLORICON = QtWidgets.QLabel(self.groupBox3)
        self.TEAMNODECOLORICON.move(110,62)
        self.pix=(QtGui.QPixmap(15, 15))
        self.pix.fill(QColor(self.WHITE))
        self.TEAMNODECOLORICON.setPixmap(self.pix)
 
        self.ICONSIZELABEL = QtWidgets.QLabel(self.groupBox3)
        self.ICONSIZELABEL.setText("Node Size")
        self.ICONSIZELABEL .resize(250,20)
        self.ICONSIZELABEL.move(130,59)
        
        self.TEAMICONSIZESPIN = QtWidgets.QSpinBox(self.groupBox3)
        self.TEAMICONSIZESPIN.setRange(10, 50)
        self.TEAMICONSIZESPIN.setValue(self.ICONSIZE)
        self.TEAMICONSIZESPIN.move(200,60)

        self.ICONSHAPELABEL = QtWidgets.QLabel(self.groupBox3)
        self.ICONSHAPELABEL.setText("Node Shape  -")
        self.ICONSHAPELABEL .resize(250,20)
        self.ICONSHAPELABEL.move(10,84)
        
        self.TEAMICONSHAPEBOX = QtWidgets.QComboBox(self.groupBox3)
        self.TEAMICONSHAPEBOX.resize(138,20)        
        self.TEAMICONSHAPEBOX.addItem("Circle")
        self.TEAMICONSHAPEBOX.addItem("Triangle")
        self.TEAMICONSHAPEBOX.addItem("Square")
        self.TEAMICONSHAPEBOX.addItem("Pentagon")
        self.TEAMICONSHAPEBOX.addItem("Hexagon")
        self.TEAMICONSHAPEBOX.addItem("Heptagon")
        self.TEAMICONSHAPEBOX.addItem("Octagon")
        self.TEAMICONSHAPEBOX.addItem("Nonagon")
        self.TEAMICONSHAPEBOX.addItem("Decagon")
        self.TEAMICONSHAPEBOX.move(105, 85)
## ##############################EDITOR SETTINGS######################################

        self.groupBox2 = QtWidgets.QGroupBox(self)
        self.groupBox2.setGeometry(QtCore.QRect(5, 180, 245, 220))


        self.EDITSETTINGSLABEL = QtWidgets.QLabel(self.groupBox2)
        self.EDITSETTINGSLABEL.setText("Editor Settings:")
        self.EDITSETTINGSLABEL.resize(250,20)
        self.EDITSETTINGSLABEL.move(10,5)
        
        self.EDITNAMELABEL = QtWidgets.QLabel(self.groupBox2)
        self.EDITNAMELABEL.setText("Editor Name")
        self.EDITNAMELABEL.resize(250,20)
        self.EDITNAMELABEL.move(10,25)

        self.EDITORNAME= QtWidgets.QLineEdit(self.groupBox2)
        self.EDITORNAME.resize(130,20)
        self.EDITORNAME.move(105,25)
        
        self.EDITIDLABEL = QtWidgets.QLabel(self.groupBox2)
        self.EDITIDLABEL.setText("Editor User ID")
        self.EDITIDLABEL.resize(250,20)
        self.EDITIDLABEL.move(10,50)        

        self.EDITORID= QtWidgets.QLineEdit(self.groupBox2)
        self.EDITORID.resize(130,20)
        self.EDITORID.move(105,50)

        self.ADD = QPushButton(self.groupBox2)
        self.ADD.setText("ADD")
        self.ADD.resize(80,25)
        self.ADD.move(5,75)
        self.ADD.clicked.connect(self.ADD_clicked)

        self.CLEAR = QPushButton(self.groupBox2)
        self.CLEAR.setText("CLEAR")
        self.CLEAR.resize(80,25)
        self.CLEAR.move(83,75)
        self.CLEAR.clicked.connect(self.CLEAR_clicked)
        
        self.EDIT = QPushButton(self.groupBox2)
        self.EDIT.setText("EDIT")
        self.EDIT.resize(80,25)
        self.EDIT.move(160,75)
        self.EDIT.clicked.connect(self.EDIT_clicked)
     


        self.EDITORLINECOLOR= QPushButton(self.groupBox2)
        self.EDITORLINECOLOR.setText("LINE COLOR")
        self.EDITORLINECOLOR.resize(110,25)
        self.EDITORLINECOLOR.move(5,105)
        self.EDITORLINECOLOR.clicked.connect(self.EDITORLINECOLOR_clicked)

        self.EDITORLINECOLORICON = QtWidgets.QLabel(self.groupBox2)
        self.EDITORLINECOLORICON.move(115,112)
        self.pix=(QtGui.QPixmap(15, 15))
        self.pix.fill(QColor(self.WHITE))
        self.EDITORLINECOLORICON.setPixmap(self.pix)
        
        self.EDITORLINEWIDTHLABEL = QtWidgets.QLabel(self.groupBox2)
        self.EDITORLINEWIDTHLABEL.setText("Line Width")
        self.EDITORLINEWIDTHLABEL.resize(75,20)
        self.EDITORLINEWIDTHLABEL.move(135,110)
        
        self.EDITORLINEWIDTHSPIN = QtWidgets.QSpinBox(self.groupBox2)
        self.EDITORLINEWIDTHSPIN.setRange(1, 20)
        self.EDITORLINEWIDTHSPIN.setValue(self.LINEWIDTH)
        self.EDITORLINEWIDTHSPIN.move(200,110) 
        


        self.EDITORNODECOLOR= QPushButton(self.groupBox2)
        self.EDITORNODECOLOR.setText("NODE COLOR")
        self.EDITORNODECOLOR.resize(110,25)
        self.EDITORNODECOLOR.move(5,134)
        self.EDITORNODECOLOR.clicked.connect(self.EDITORNODECOLOR_clicked)

        self.EDITORNODECOLORICON = QtWidgets.QLabel(self.groupBox2)
        self.EDITORNODECOLORICON.move(115,141)
        self.pix=(QtGui.QPixmap(15, 15))
        self.pix.fill(QColor(self.WHITE))
        self.EDITORNODECOLORICON.setPixmap(self.pix)

        
        self.EDITORNODESIZELABEL =QtWidgets.QLabel(self.groupBox2)
        self.EDITORNODESIZELABEL.setText("Node Size")
        self.EDITORNODESIZELABEL.resize(75,20)
        self.EDITORNODESIZELABEL.move(135,137)

        self.EDITORNODESIZESPIN = QtWidgets.QSpinBox(self.groupBox2)
        self.EDITORNODESIZESPIN.setRange(10, 50)
        self.EDITORNODESIZESPIN.setValue(10)
        self.EDITORNODESIZESPIN.move(200,137)



        self.TOGGLELABEL = QtWidgets.QLabel(self.groupBox2)
        self.TOGGLELABEL.setText("Toggle UID in Style Settings menu")
        self.TOGGLELABEL.resize(250,15)
        self.TOGGLELABEL .move(12,165)
        
        self.TOGGLECHECK = QtWidgets.QCheckBox(self.groupBox2)
        self.TOGGLECHECK.move(220,165)

        self.EDITORICONSHAPELABEL = QtWidgets.QLabel(self.groupBox2)
        self.EDITORICONSHAPELABEL.setText("Node Shape  -")
        self.EDITORICONSHAPELABEL.resize(250,20)
        self.EDITORICONSHAPELABEL.move(12,190)
        
        self.EDITORICONSHAPEBOX = QtWidgets.QComboBox(self.groupBox2)
        self.EDITORICONSHAPEBOX.resize(135,20)
        self.EDITORICONSHAPEBOX.addItem("Circle")
        self.EDITORICONSHAPEBOX.addItem("Triangle")
        self.EDITORICONSHAPEBOX.addItem("Square")
        self.EDITORICONSHAPEBOX.addItem("Pentagon")
        self.EDITORICONSHAPEBOX.addItem("Hexagon")
        self.EDITORICONSHAPEBOX.addItem("Heptagon")
        self.EDITORICONSHAPEBOX.addItem("Octagon")
        self.EDITORICONSHAPEBOX.addItem("Nonagon")
        self.EDITORICONSHAPEBOX.addItem("Decagon")
        self.EDITORICONSHAPEBOX.move(105, 190)
        
#################################################################################        
        self.retranslateUi(MAINWindow)
#################################################################################
    def retranslateUi(self,MAINWindow):
        self.headers = ["NAME", "USER ID","LINE COLOR","NODE COLOR"]
        self.rowcount = 50
        self.colcount = 4
        self.array =[[str(''),str(''),QtGui.QColor(clear),QtGui.QColor(clear)] for j in range(self.rowcount)]
        self.tablemodel=Model(self.array,self.headers,self)
        self.TABLE.setModel(self.tablemodel)
        self.TABLE.resizeRowsToContents()
        self.TABLE.resizeColumnsToContents()
#####################################################################################EDITOR FUNCTIONS#########################################################
        

    def EDITORLINECOLOR_clicked(self):
        color = QtWidgets.QColorDialog.getColor()
        clr = color.name()
        colr = ""
        for i in clr:
            colr+= str(i)
        if colr =="#000000":
                pass
        else:    
            if self.NRSELECT != '':
                self.TEMPUSERS[str(self.NRSELECT)].LINECOLORTEXT = colr
                self.TEMPUSERS[str(self.NRSELECT)].LINECOLORUI = color
                self.pix.fill(QColor(self.TEMPUSERS[str(self.NRSELECT)].LINECOLORUI))
                self.EDITORLINECOLORICON.setPixmap(self.pix)
                self.array[self.NRSELECT][2]=QtGui.QColor(self.TEMPUSERS[str(self.NRSELECT)].LINECOLORUI)
            else:
                self.TEMPLINECOLORTEXT = colr
                self.TEMPLINECOLORUI = color
                self.pix.fill(QColor(self.TEMPLINECOLORUI))
                self.EDITORLINECOLORICON.setPixmap(self.pix)
                self.EDITORLINECOLORICON.repaint()
          

    def EDITORNODECOLOR_clicked(self):
        color = QtWidgets.QColorDialog.getColor()
        clr = color.name()
        colr = ""
        for i in clr:
            colr+= str(i)
        if colr =="#000000":
                pass
        else:
            if self.NRSELECT != '':
                self.TEMPUSERS[str(self.NRSELECT)].NODECOLORTEXT = colr
                self.TEMPUSERS[str(self.NRSELECT)].NODECOLORUI = color
                self.pix.fill(QColor(self.TEMPUSERS[str(self.NRSELECT)].NODECOLORUI))
                self.EDITORNODECOLORICON.setPixmap(self.pix)
                self.array[self.NRSELECT][3]=QtGui.QColor(self.TEMPUSERS[str(self.NRSELECT)].NODECOLORUI)
            else:
                self.TEMPNODECOLORTEXT = colr
                self.TEMPNODECOLORUI = color
                self.pix.fill(QColor(self.TEMPNODECOLORUI))
                self.EDITORNODECOLORICON.setPixmap(self.pix)
                self.EDITORNODECOLORICON.repaint()
##################################################################################TEAM FUNCTIONS###############################################################

    def TEAMLINECOLOR_clicked(self):
            color = QtWidgets.QColorDialog.getColor()
            
            clr = color.name()
            colr = ""
            for i in clr:
                colr+= str(i)
            if colr =="#000000":
                pass
            else:
                self.TEAMLINECOLORTEXT = colr
                self.TEAMLINECOLORUI = color
                self.pix.fill(QColor(self.TEAMLINECOLORUI))
                self.TEAMLINECOLORICON.setPixmap(self.pix)
    
    def TEAMNODECOLOR_clicked(self):
        color = QtWidgets.QColorDialog.getColor()
        clr = color.name()
        colr = ""
        for i in clr:
            colr+= str(i)
        if colr =="#000000":
            pass
        else:
            self.TEAMNODECOLORTEXT = colr 
            self.TEAMNODECOLORUI = color
            self.pix.fill(QColor(self.TEAMNODECOLORUI))
            self.TEAMNODECOLORICON.setPixmap(self.pix)



        
    def ADD_clicked(self):
     try:
        if self.NRSELECT == '':
         if self.EDITORNAME.text() != "":
            ENAME = self.EDITORNAME.text()
            EUID = self.EDITORID.text()
            ECLASS = EDITORINFO()
            ECLASS.NAME = ENAME
            ECLASS.UID = EUID
            self.TEMPUSERS[str(self.usercount)] = ECLASS
            self.TEMPUSERS[str(self.usercount)].LINECOLORTEXT = self.TEMPLINECOLORTEXT 
            self.TEMPUSERS[str(self.usercount)].LINECOLORUI =  self.TEMPLINECOLORUI
            self.TEMPUSERS[str(self.usercount)].NODECOLORTEXT = self.TEMPNODECOLORTEXT 
            self.TEMPUSERS[str(self.usercount)].NODECOLORUI =  self.TEMPNODECOLORUI
            self.array[self.usercount][0]=str(ECLASS.NAME)
            self.array[self.usercount][1]=str(ECLASS.UID)
            self.array[self.usercount][2]=(QColor(ECLASS.LINECOLORUI))
            self.array[self.usercount][3]=(QColor(ECLASS.NODECOLORUI))
            self.ADDUSERS.append (ECLASS)
            self.EDITORNAME.setText('')
            self.EDITORID.setText('')
            self.EDITORNAME.repaint()
            self.EDITORID.repaint()
            self.usercount += 1
            self.pix.fill(QColor(self.WHITE ))
            self.EDITORNODECOLORICON.setPixmap(self.pix)
            self.EDITORLINECOLORICON.setPixmap(self.pix)
            self.EDITORNODECOLORICON.repaint()
            self.EDITORLINECOLORICON.repaint()
            
        if self.NRSELECT != '':
           if self.EDITORNAME.text() != "":
            ENAME = self.EDITORNAME.text()
            EUID = self.EDITORID.text()
            self.TEMPUSERS[str(self.NRSELECT)].NAME = ENAME
            self.TEMPUSERS[str(self.NRSELECT)].UID = EUID
            self.TEMPUSERS[str(self.NRSELECT)].ICONSHAPE = self.EDITORICONSHAPEBOX.currentText()
            
            self.TEMPUSERS[str(self.NRSELECT)].LINEWIDTH = str(self.EDITORLINEWIDTHSPIN.value())
            self.TEMPUSERS[str(self.NRSELECT)].ICONSIZE = str(self.EDITORNODESIZESPIN.value())
            self.array[self.NRSELECT][0]=str(self.TEMPUSERS[str(self.NRSELECT)].NAME)
            self.array[self.NRSELECT][1]=str(self.TEMPUSERS[str(self.NRSELECT)].UID)
            
            self.EDITORNAME.setText('')
            self.EDITORID.setText('')
            self.EDITORNAME.repaint()
            self.EDITORID.repaint()
            self.NRSELECT = ''
            self.ADD.setText("ADD")
            self.pix.fill(QColor(self.WHITE))
            self.EDITORNODECOLORICON.setPixmap(self.pix)
            self.EDITORLINECOLORICON.setPixmap(self.pix)
            self.EDITORLINECOLORICON.repaint()
            self.EDITORNODECOLORICON.repaint()    
     except:
         pass
        
    def GETTEAMSHAPETEXT(self):
        if self.TEAMICONSHAPE == "Circle":
            self.TEAMICONSHAPEBOX.setCurrentIndex(0)
        if self.TEAMICONSHAPE == "Triangle":
            self.TEAMICONSHAPEBOX.setCurrentIndex(1)
        if self.TEAMICONSHAPE == "Square":
            self.TEAMICONSHAPEBOX.setCurrentIndex(2)
        if self.TEAMICONSHAPE == "Pentagon":
            self.TEAMICONSHAPEBOX.setCurrentIndex(3)
        if self.TEAMICONSHAPE == "Hexagon":
            self.TEAMICONSHAPEBOX.setCurrentIndex(4)
        if self.TEAMICONSHAPE == "Heptagon":
            self.TEAMICONSHAPEBOX.setCurrentIndex(5)
        if self.TEAMICONSHAPE == "Octagon":
            self.TEAMICONSHAPEBOX.setCurrentIndex(6)
        if self.TEAMICONSHAPE == "Nonagon":
            self.TEAMICONSHAPEBOX.setCurrentIndex(7)
        if self.TEAMICONSHAPE == "Decagon":            
            self.TEAMICONSHAPEBOX.setCurrentIndex(8)
            
    def GETEDITORSHAPETEXT(self):
        if self.TEMPUSERS[str(self.NRSELECT)].ICONSHAPE == "Circle":
            self.EDITORICONSHAPEBOX.setCurrentIndex(0)
            self.EDITORICONSHAPEBOX.repaint()
        if self.TEMPUSERS[str(self.NRSELECT)].ICONSHAPE == "Triangle":
            self.EDITORICONSHAPEBOX.setCurrentIndex(1)
            self.EDITORICONSHAPEBOX.repaint()
        if self.TEMPUSERS[str(self.NRSELECT)].ICONSHAPE == "Square":
            self.EDITORICONSHAPEBOX.setCurrentIndex(2)
            self.EDITORICONSHAPEBOX.repaint()
        if self.TEMPUSERS[str(self.NRSELECT)].ICONSHAPE == "Pentagon":
            self.EDITORICONSHAPEBOX.setCurrentIndex(3)
            self.EDITORICONSHAPEBOX.repaint()
        if self.TEMPUSERS[str(self.NRSELECT)].ICONSHAPE == "Hexagon":
            self.EDITORICONSHAPEBOX.setCurrentIndex(4)
            self.EDITORICONSHAPEBOX.repaint()
        if self.TEMPUSERS[str(self.NRSELECT)].ICONSHAPE == "Heptagon":
            self.EDITORICONSHAPEBOX.setCurrentIndex(5)
            self.EDITORICONSHAPEBOX.repaint()
        if self.TEMPUSERS[str(self.NRSELECT)].ICONSHAPE == "Octagon":
            self.EDITORICONSHAPEBOX.setCurrentIndex(6)
            self.EDITORICONSHAPEBOX.repaint()
        if self.TEMPUSERS[str(self.NRSELECT)].ICONSHAPE == "Nonagon":
            self.EDITORICONSHAPEBOX.setCurrentIndex(7)
            self.EDITORICONSHAPEBOX.repaint()
        if self.TEMPUSERS[str(self.NRSELECT)].ICONSHAPE == "Decagon":            
            self.EDITORICONSHAPEBOX.setCurrentIndex(8)
            self.EDITORICONSHAPEBOX.repaint()

            
##############################################################EXPORT BLOCK###########################            
    def EXPORT_clicked(self):
        self.TITLEENTRYBLOCK = str(self.TEAMNAME.text())
        default_name = str(self.directory + ('/QAQC_%s.mapcss'%(self.TITLEENTRYBLOCK)))
        self.OUTFILE = ( QtWidgets.QFileDialog.getSaveFileName(self,directory =default_name))

        self.SETUPENTRYBLOCK = ""
        self.SETTINGBLOCK = ""
        self.NODEENTRYBLOCK = ""
        self.WAYENTRYBLOCK = ""
        self.MASTEROUTPUTBLOCK = ""
        
        self.LINEWIDTH = str(self.TEAMLINEWIDTHSPIN.value())
        self.ICONSIZE = str(self.TEAMICONSIZESPIN.value())
        self.SETTEAMICON()
        for i in self.ADDUSERS:
             if i.UID[-1] == " ":
                 i.UID = i.UID[:-1]
             if " " in i.UID:
                 self.SPACESETTINGENTRY(i.NAME,i.UID)
             else:    
                 self.SETTINGENTRY(i.NAME,i.UID)
             self.SETUPENTRY(i.NAME,i.UID)
             
             self.NODEENTRY(i.NAME,i.ICONSIZE,i.ICONSHAPE,i.NODECOLORTEXT)
             self.WAYDENTRY(i.NAME,i.LINECOLORTEXT,i.LINEWIDTH)
       
        self. MASTEROUTPUT()

        
    def SETTEAMICON(self):
        self.TEAMICONSHAPE = self.TEAMICONSHAPEBOX.currentText()


        
    def SETUPENTRY(self,name,uid):

        if self.TOGGLECHECK.isChecked():
            self.SETUPENTRYBLOCK +=("""setting::user_%s {
            type:boolean;
            label:tr("Turn User %s On/Off");
            default:true;
            }\n"""%(name,name))
            
        else:
            self.SETUPENTRYBLOCK +=("""setting::user_%s {
            type:boolean;
            label:tr("Turn User %s On/Off");
            default:true;
            }\n"""%(name,uid))

    def SPACESETTINGENTRY(self,name,uid):
        self.SETTINGBLOCK +=("""*[eval(JOSM_search("user:\\"%s\\""))][setting("user_%s")] {
  set .%s;
}\n"""%(uid,name,name))            
              
    def SETTINGENTRY(self,name,uid):
        self.SETTINGBLOCK +=("""*[eval(JOSM_search("user:%s"))][setting("user_%s")] {
  set .%s
}\n"""%(uid,name,name))
        
    def NODEENTRY(self,name,iconsize,iconshape,nodecolor):

        self.NODEENTRYBLOCK += ("""node.%s{
  symbol-size: %s;
  symbol-shape: %s;
  symbol-stroke-color: %s;
  symbol-stroke-width: 3px;
  symbol-fill-opacity: 0.5;
  z-index: -5;
}"""%(name,iconsize,iconshape,nodecolor))
            
        
    def WAYDENTRY(self,name,color,width):

        self.WAYENTRYBLOCK += ("""way.%s{
  z-index: -10;
  casing-color: %s;
  casing-width: %s;
  casing-opacity: 0.6;
  /*
  text: eval(concat("Highway type =", " ", tag("highway")));
  text-offset: -20;
  */
}"""%(name,color,width))
            
        
    def MASTEROUTPUT(self):

      path =(self.OUTFILE[0] )
      if path != '':
        with open (path,"w+") as OUT:
            OUT.writelines("""meta {
  title: "QC Style For %s Team";
  description: "Highlights features that were created/modified by users";
  watch-modified: true;
  version: "1.5";
  icon: "http://uncrate.com/p/2016/02/smart-kart.jpg";

}
/* Notes

1.0 Added styles -- provided by Jenn -- and users -- Ian -- 3/11/2019

1.1 Configured styles -- Louis -- 3/13/2019

1.2 Configured style colors and highlighting -- Ian -- 3/15/2019

1.3 Simplified user lines -- Louis -- 3/18/2019

1.4 Adjusted user, style lines and appearances -- 3/20/2019

1.5 Alphabetized users, added new users, added tips, simplified node highlight & node modified overlays -- Louis,Ian,AndrewP -- 5/15/2019

Tips:

A setting should be created for each separate user:

setting::user_aaron {
  type: boolean;
  label: tr("Turn User Aaron On/Off");
  default: false;
}

-- after :: comes your setting "class" which can be named as you will. Our example show user_aaron
-- Type: boolean; should always exist
-- label: tr("Anything you want to put here") -> This is what shows up under setting in JOSM
-- Default: false -> the setting will remain disabled on launch until a user enables it

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


at which point, it becomes necessary to create a selector statement for your user:

*[eval(JOSM_search("user:vespax"))][setting("user_aaron")] {
  set .aaron;
}

-- * denotes what you are selecting, in this case, every element type in OSM
-- [eval(JOSM_search("user:vespax"))] -> this is necessary and should be constructed as such.

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In order to construct time stamps, you can use the following:


String: "[eval(JOSM_search("timestamp:2016-02-20/"))]" can be modified in several ways
"timestamp:2016-02-20/" -- Shows all edits edited after date
"timestamp:2016-02-20/2016-02-22" -- Shows all edits after 02-20 but before 02-22
"timestamp:2016-02/ Day and Month can be removed to widen the range of edits shown, example here shows all edits starting in FEB2016.

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

So, a timestamped search would look like this:

*[eval(JOSM_search("user:IndianaJones737"))][eval(JOSM_search("timestamp:2016-03-14/2016-03-15"))] {
  casing-width: 10;
  casing-color: green;
  casing-opacity: 0.2;
}

-- set .aaron; -> this is setting the class for this statement. This allows us to call it out later on. Classes
can be set like that or as so -> set aaron;

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

way.aaron, & node.aaron,

-- This shows that we are looking for all ways/nodes which meet the "aaron" class. The comma here denotes
that there is another selector we would like to call out after "aaron"

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


{
  z-index: -10;
  casing-color: lime;
  casing-width: 10;
  casing-opacity: 0.3;
 
 
}

-- This is our code block which will style up whatever we called out as a selector

*/

/* Create Settings */


/* User Settings */

%s




/* Tracking Selectors -- Way and node style BEFORE they are uploaded */

node:modified::modified_layer {
    symbol-shape: %s;
    symbol-size: %s;
    symbol-stroke-color: %s;
    symbol-stroke-width: 3px;
    symbol-fill-opacity: 0.5;
    z-index: -5;
}

way:modified::modified_layer,
node:modified < way::modified_layer {
    width: 6;
    color: transparent;
    opacity: 0;
    casing-width: %s;
    casing-color: %s;
    casing-opacity: 0.7;
    z-index: -5;
}

/* QC Styles */


/* User specific styles */

%s


/* This is how you search for someone with a space in their name

*[eval(JOSM_search("user:\"Hector Vector\""))] {
  set .jman;
}

*/

/* Styling of ways and nodes once they belong to "history" for each individual user */


%s


%s


node:selected::selected_layer {
    symbol-shape: circle;
    symbol-size: 22;
    symbol-stroke-color: #DF2E08;
    symbol-stroke-width: 3px;
    symbol-fill-opacity: 0.5;
    z-index: -5;
}"""%(self.TITLEENTRYBLOCK,self.SETUPENTRYBLOCK,self.TEAMICONSHAPE,self.ICONSIZE,self.TEAMNODECOLORTEXT,self.LINEWIDTH,self.TEAMLINECOLORTEXT,self.SETTINGBLOCK,self.WAYENTRYBLOCK,self.NODEENTRYBLOCK))
 ##################################################################################################




################################
    def CLEAR_clicked(self):
     try:
        self.EDITORNAME.setText("")
        self.EDITORID.setText("")
        self.EDITORID.repaint()
        self.EDITORNAME.repaint()
        self.ADD.setText("ADD")
        self.ADD.repaint()
        self.SELTEXT = ''
        self.pix.fill(QColor(self.WHITE))
        self.EDITORNODECOLORICON.setPixmap(self.pix)
        self.EDITORLINECOLORICON.setPixmap(self.pix)
        self.EDITORNODECOLORICON.repaint()
        self.EDITORLINECOLORICON.repaint()
     except:
         pass

    def REMOVEALL_clicked(self):
             self.GOREMOVEALL = True
             self.dialog = CONFIRMPOPUP()
             self.dialog.LABEL.setText("Are you sure you want to remove all Editors?")
             self.dialog.LABEL.repaint()
             self.dialog.show()

        
    def REMOVEALL_GO(self):
     try:   
        self.usercount = 0
        self.ADDUSERS=[]       
        self.TEMPUSERS={}
        self.pix.fill(QColor(self.WHITE))
        self.TEAMNODECOLORICON.setPixmap(self.pix)
        self.TEAMLINECOLORICON.setPixmap(self.pix)
        self.TEAMLINEWIDTHSPIN.setValue(0)
        self.TEAMICONSIZESPIN.setValue(0)
        self.TEAMNAME.setText('')
        self.TEAMNAME.repaint()
        self.TEAMNODECOLORICON.repaint()
        self.TEAMLINECOLORICON.repaint()
        for i in range (0,50):
            self.array[i][0]=str('')
            self.array[i][1]=str('')
            self.array[i][2]=QtGui.QColor(clear)
            self.array[i][3]=QtGui.QColor(clear)
        self.GOREMOVEALL = False
     except:
         pass


    def REMOVE_GO(self):
        for ix in self.TABLE.selectedIndexes():
                column = ix.column()
                dat= ix.data()
                row = ix.row()
                if dat != None:
                    self.NRSELECT = row
                else:
                    self.NRSELECT = None

                    self.usercount -= 1
                try:
                     self.ADDUSERS.pop(int(self.NRSELECT))
                except:
                         pass
                
                try:
                     self.TEMPUSERS.pop(str(self.NRSELECT))
                except:
                     pass
                self.array[self.NRSELECT][0]=str('')
                self.array[self.NRSELECT][1]=str('')
                self.array[self.NRSELECT][2]=QtGui.QColor(clear)
                self.array[self.NRSELECT][3]=QtGui.QColor(clear)
             
    def REMOVE_clicked(self):
             self.dialog = CONFIRMPOPUP()
             self.dialog.show()

        
    def EDIT_clicked(self):
     try:
        self.ADD.setText("UPDATE")
                 
        for ix in self.TABLE.selectedIndexes():
                    column = ix.column()
                    dat= ix.data()
                    row = ix.row()
                    if dat != None:
                        self.NRSELECT = row
                    else:
                        self.NRSELECT = None
        self.EDITORNAME.setText(self.TEMPUSERS[str(self.NRSELECT)].NAME)
        self.EDITORID.setText(self.TEMPUSERS[str(self.NRSELECT)].UID)
        self.EDITORNAME.repaint()
        self.EDITORID.repaint()
        self.pix.fill(QColor(self.TEMPUSERS[str(self.NRSELECT)].NODECOLORUI))
        self.EDITORNODECOLORICON.setPixmap(self.pix)
        self.EDITORNODECOLORICON.repaint()
        self.pix.fill(QColor(self.TEMPUSERS[str(self.NRSELECT)].LINECOLORUI))
        self.EDITORLINECOLORICON.setPixmap(self.pix)
        self.EDITORLINECOLORICON.repaint()
        self.GETEDITORSHAPETEXT()
     except:
         pass
        
    def IMPORT_clicked(self):
     #try:
        INFILE = ( QtWidgets.QFileDialog.getOpenFileName(self,
             self.filters,self.directory,self.select_filters))
        INFILE = str(INFILE[0])
        global INKML
        #try:
        with open (INFILE, 'r+') as IN:
                INFILETEXT = IN.read()
                INFILETEXT = str(INFILETEXT)
                INFILETEXT= INFILETEXT.replace("""}
  z-index: -10;
  casing-color: #B108D6;
  casing-width: 7;
  casing-opacity: 0.6;
  z-index: -10;
  casing-color: #B108D6;
  casing-width: 5;
  casing-opacity: 0.6;
  /*
  text: eval(concat("Highway type =", " ", tag("highway")));
  text-offset: -20;
  */


}""","")
                INFILETEXT = INFILETEXT.split("""Team";""")
                TEAMNAMEBLOCK = INFILETEXT[0]
                TEAMNAMEBLOCK = TEAMNAMEBLOCK.split("For ")
                TEAMNAME= TEAMNAMEBLOCK[1]
                TEAMNAME = TEAMNAME.replace("\n","")
                TEAMNAME = TEAMNAME.replace(" ","")
                self.TEAMNAME.setText(TEAMNAME)
                INFILETEXT = INFILETEXT [1]
                INFILETEXT = INFILETEXT.split("/* User Settings */")
                INFILETEXT = INFILETEXT [1]
                INFILETEXT = INFILETEXT.split("/* Tracking Selectors -- Way and node style BEFORE they are uploaded */")
                EDITNAMEBLOCK = INFILETEXT [0]
                EDITNAMEBLOCK = EDITNAMEBLOCK.replace("setting::user_","")
                EDITNAMEBLOCK = EDITNAMEBLOCK.replace(" {\n","")
                EDITNAMEBLOCK = EDITNAMEBLOCK.replace("type:boolean;","")
                EDITNAMEBLOCK = EDITNAMEBLOCK.replace("""label:tr("Turn""","")
                EDITNAMEBLOCK = EDITNAMEBLOCK.replace(""");""","")
                EDITNAMEBLOCK = EDITNAMEBLOCK.replace("default:true;","")
                EDITNAMEBLOCK = EDITNAMEBLOCK.replace("}","")
                
                EDITNAMEBLOCK = EDITNAMEBLOCK.replace("  ","")

                EDITNAMEBLOCK = EDITNAMEBLOCK.replace("\n","")
                EDITNAMEBLOCK = EDITNAMEBLOCK.replace("User",":")
                EDITNAMEBLOCK = EDITNAMEBLOCK.replace('''On/Off"''',";")
                EDITNAMEBLOCK = EDITNAMEBLOCK.replace(" : ",":")
                EDITNAMEBLOCK = EDITNAMEBLOCK.split(";")


                SETUPBLOCK = INFILETEXT [1]
                SETUPBLOCK = SETUPBLOCK.split("/* QC Styles */")
                TEAMBLOCK = SETUPBLOCK[0]
                TEAMBLOCK  = TEAMBLOCK.replace("way:modified::modified_layer,","")
                TEAMBLOCK  = TEAMBLOCK.replace("node:modified < way::modified_layer {","")
                TEAMBLOCK  = TEAMBLOCK.replace("node:modified::modified_layer {","")
                TEAMBLOCK  = TEAMBLOCK.replace("    symbol-shape: ","")
                TEAMBLOCK  = TEAMBLOCK.replace("    symbol-size: ","")
                TEAMBLOCK  = TEAMBLOCK.replace("    symbol-stroke-color: ","")
                TEAMBLOCK  = TEAMBLOCK.replace("    symbol-stroke-width: ","")
                TEAMBLOCK  = TEAMBLOCK.replace("    symbol-fill-opacity: ","")
                TEAMBLOCK  = TEAMBLOCK.replace("    z-index: -5;","")
                TEAMBLOCK  = TEAMBLOCK.replace("    width: ","")
                TEAMBLOCK  = TEAMBLOCK.replace("    color: ","")
                TEAMBLOCK  = TEAMBLOCK.replace("    opacity: ","")
                TEAMBLOCK  = TEAMBLOCK.replace("    casing-width: ","")
                TEAMBLOCK  = TEAMBLOCK.replace("    casing-color: ","")
                TEAMBLOCK  = TEAMBLOCK.replace("    casing-opacity: ","")
                TEAMBLOCK  = TEAMBLOCK.replace("{","")
                TEAMBLOCK  = TEAMBLOCK.replace("}","")
                TEAMBLOCK  = TEAMBLOCK.replace("\n","")
                TEAMBLOCK  = TEAMBLOCK.split(";")
                self.TEAMLINECOLORTEXT = TEAMBLOCK[9]
                self.TEAMNODECOLORTEXT = TEAMBLOCK[2] 
                self.TEAMLINECOLORUI =QtGui.QColor(TEAMBLOCK[9])
                self.TEAMNODECOLORUI =QtGui.QColor(TEAMBLOCK[2]) 
                self.LINEWIDTH  = TEAMBLOCK[8]
                self.ICONSIZE = TEAMBLOCK[1]
                self.ICONSHAPE= TEAMBLOCK[0]
                SETTINGSBLOCK = SETUPBLOCK[1]
                SETTINGSBLOCK = SETTINGSBLOCK.split("""/* Styling of ways and nodes once they belong to "history" for each individual user */""")
                SETTINGSBLOCK = SETTINGSBLOCK[1]
                SETTINGSBLOCK = SETTINGSBLOCK.split("node.")
                NODESETTINGSBLOCK = str(SETTINGSBLOCK[0])

                WAYSETTINGSBLOCK = SETTINGSBLOCK[1:]
                EDITWAYSETTINGS = []
                for i in WAYSETTINGSBLOCK:
                     i=i.replace("\n","")
                     i=i.replace("node:modified::modified_layer {","")
                     i=i.replace("node:selected::selected_layer","")
                     i=i.replace("symbol-shape: ","")
                     i=i.replace("symbol-size: ",";")
                     i=i.replace("symbol-stroke-color: ","")
                     i=i.replace("symbol-stroke-width: ","")
                     i=i.replace("symbol-fill-opacity: ","")
                     i=i.replace("z-index: -5;","")
                     i=i.replace("way:modified::modified_layer,","")
                     i=i.replace("node:modified < way::modified_layer {","")
                     i=i.replace("width: ","")
                     i=i.replace("way:modified::modified_layer,","")
                     i=i.replace("node:modified < way::modified_layer {","")
                     i=i.replace("width: ","")
                     i=i.replace("color: transparent;","")
                     i=i.replace("opacity: ","")
                     i=i.replace("casing-width: ","")
                     i=i.replace("  casing-color: ","")
                     i=i.replace("casing-opacity:","")
                     i=i.replace("z-index: -5;","")
                     i=i.replace("}","")
                     i=i.replace("\n","")
                     i=i.replace(" ","")
                     i=i.split("{")
                     i= str (i[1])
                     EDITWAYSETTINGS.append(i)

                NODESETTINGSBLOCK = NODESETTINGSBLOCK.split("}way.")
                EDITNODESETTINGSBLOCK = []
                for i in NODESETTINGSBLOCK:
                         i=i. replace ("  z-index: -10;","")
                         i=i. replace ("  casing-color: ",";")
                         i=i. replace ("  casing-width: ","")
                         i=i. replace ("  casing-opacity: ","")
                         i=i. replace ("""  text: eval(concat("Highway type =", " ", tag("highway")));""","")
                         i=i. replace ("  text-offset: -20;","")
                         i=i. replace ("  text-offset: -20;","")
                         i=i.replace("z-index: -5;","")
                         i=i. replace ("  /*","")
                         i=i. replace ("  */","")
                         i=i. replace ("}","")
                         i=i. replace ("{","")
                         i=i. replace ("\n","")
                         EDITNODESETTINGSBLOCK.append(i)
                FINISHEDSETTINGSBLOCK = []         
                for a,b,c in zip(EDITNAMEBLOCK,EDITWAYSETTINGS,EDITNODESETTINGSBLOCK):
                    a+=b
                    a+=c
                    a=a.replace(":",";") 
                    FINISHEDSETTINGSBLOCK.append(a)
                for i in FINISHEDSETTINGSBLOCK:
                    i=i. replace  ("node;selected;;selected_layer","")
                    i = i.split(";")
                    CONSTRUCTOR = str(self.usercount)
                    CONSTRUCTOR = EDITORINFO()  
                    CONSTRUCTOR.NAME = i[0]
                    CONSTRUCTOR.UID  = i[1]
                    CONSTRUCTOR.LINECOLORUI = QtGui.QColor(i[8])
                    CONSTRUCTOR.NODECOLORUI = QtGui.QColor(i[4])
                    CONSTRUCTOR.LINECOLORTEXT = i[8]
                    CONSTRUCTOR.NODECOLORTEXT = i[4]
                    CONSTRUCTOR.ICONSIZE= i[2]
                    CONSTRUCTOR.LINEWIDTH = i[9]
                    CONSTRUCTOR.ICONSHAPE = i[3]                  
                    self.TEMPUSERS[str(self.usercount)] = CONSTRUCTOR
                    self.ADDUSERS.append (CONSTRUCTOR)
                    self.array[self.usercount][0]=(str(CONSTRUCTOR.NAME))
                    self.array[self.usercount][1]=(str(CONSTRUCTOR.UID))
                    self.array[self.usercount][2]=QtGui.QColor(CONSTRUCTOR.LINECOLORUI)
                    self.array[self.usercount][3]=QtGui.QColor(CONSTRUCTOR.NODECOLORUI)
                    self.pix.fill(QColor(self.TEAMNODECOLORUI))
                    self.TEAMNODECOLORICON.setPixmap(self.pix)
                    self.TEAMNODECOLORICON.repaint()
                    self.TEAMLINEWIDTHSPIN.setValue(int(self.LINEWIDTH))
                    self.TEAMICONSIZESPIN.setValue(int(self.ICONSIZE))
                    self.pix.fill(QColor(self.TEAMLINECOLORUI))
                    self.TEAMLINECOLORICON.setPixmap(self.pix)
                    self.TEAMLINECOLORICON.repaint()
                    self.usercount += 1
                    self.TABLE.resizeRowsToContents()
                    self.TABLE.resizeColumnsToContents()
                    self.GETTEAMSHAPETEXT()
     #except:
        #pass

        
def main(args):
        app = QtWidgets.QApplication(args)
        global one
        one =MAINWindow ()

        one.show()
        sys.exit(app.exec_())
        if self.EXIT == 1:
            sys.exit(0)
        sys._excepthook = sys.excepthook
        
def exception_hook(exctype, value, traceback):
    print(exctype, value, traceback)
    sys._excepthook(exctype, value, traceback) 
    sys.exit(1) 
sys.excepthook = exception_hook 
while  True:
    main(sys.argv) 
