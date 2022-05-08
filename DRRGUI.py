# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DRRGUI.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1085, 852)
        self.gridLayoutWidget = QtWidgets.QWidget(Form)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(36, 0, 1033, 915))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        self.gridLayoutWidget.setFont(font)
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.Space2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.Space2.setMinimumSize(QtCore.QSize(130, 0))
        self.Space2.setMaximumSize(QtCore.QSize(130, 16777215))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        self.Space2.setFont(font)
        self.Space2.setText("")
        self.Space2.setObjectName("Space2")
        self.gridLayout.addWidget(self.Space2, 7, 2, 1, 1)
        self.Src2Det = QtWidgets.QLabel(self.gridLayoutWidget)
        self.Src2Det.setMinimumSize(QtCore.QSize(130, 0))
        self.Src2Det.setMaximumSize(QtCore.QSize(130, 16777215))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        self.Src2Det.setFont(font)
        self.Src2Det.setStyleSheet("QLabel{\n"
"    background-color: rgb(255, 240, 184);\n"
"    border-style: outset;\n"
"    border-radius: 10px;\n"
"}")
        self.Src2Det.setAlignment(QtCore.Qt.AlignCenter)
        self.Src2Det.setObjectName("Src2Det")
        self.gridLayout.addWidget(self.Src2Det, 4, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.PixSize = QtWidgets.QLabel(self.gridLayoutWidget)
        self.PixSize.setMinimumSize(QtCore.QSize(130, 0))
        self.PixSize.setMaximumSize(QtCore.QSize(130, 16777215))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        self.PixSize.setFont(font)
        self.PixSize.setStyleSheet("QLabel{\n"
"    background-color: rgb(255, 240, 184);\n"
"    border-style: outset;\n"
"    border-radius: 10px;\n"
"}")
        self.PixSize.setAlignment(QtCore.Qt.AlignCenter)
        self.PixSize.setObjectName("PixSize")
        self.gridLayout.addWidget(self.PixSize, 2, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.Src2Iso = QtWidgets.QLabel(self.gridLayoutWidget)
        self.Src2Iso.setMinimumSize(QtCore.QSize(130, 0))
        self.Src2Iso.setMaximumSize(QtCore.QSize(130, 16777215))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        self.Src2Iso.setFont(font)
        self.Src2Iso.setStyleSheet("QLabel{\n"
"    background-color: rgb(255, 240, 184);\n"
"    border-style: outset;\n"
"    border-radius: 10px;\n"
"}")
        self.Src2Iso.setAlignment(QtCore.Qt.AlignCenter)
        self.Src2Iso.setObjectName("Src2Iso")
        self.gridLayout.addWidget(self.Src2Iso, 5, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.Input = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.Input.setMinimumSize(QtCore.QSize(156, 0))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(-1)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.Input.setFont(font)
        self.Input.setStyleSheet("QPushButton#Input {\n"
"    background-color: lightgrey;\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 10px;\n"
"    border-color: beige;\n"
"    font: bold 14px;\n"
"    min-width: 10em;\n"
"    padding: 6px;\n"
"}\n"
"")
        self.Input.setObjectName("Input")
        self.gridLayout.addWidget(self.Input, 0, 0, 1, 6)
        self.TodoInput = QtWidgets.QTextEdit(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.TodoInput.sizePolicy().hasHeightForWidth())
        self.TodoInput.setSizePolicy(sizePolicy)
        self.TodoInput.setMinimumSize(QtCore.QSize(200, 40))
        self.TodoInput.setMaximumSize(QtCore.QSize(200, 40))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        self.TodoInput.setFont(font)
        self.TodoInput.setStyleSheet("QTextEdit{\n"
"    background-color: rgb(255, 240, 184);\n"
"    border-style: outset;\n"
"    border-width: 1px;\n"
"    border-radius: 10px;\n"
"}")
        self.TodoInput.setObjectName("TodoInput")
        self.gridLayout.addWidget(self.TodoInput, 6, 1, 1, 1, QtCore.Qt.AlignHCenter)
        self.SenSize = QtWidgets.QLabel(self.gridLayoutWidget)
        self.SenSize.setMinimumSize(QtCore.QSize(130, 0))
        self.SenSize.setMaximumSize(QtCore.QSize(130, 16777215))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        self.SenSize.setFont(font)
        self.SenSize.setStyleSheet("QLabel{\n"
"    background-color: rgb(255, 240, 184);\n"
"    border-style: outset;\n"
"    border-radius: 10px;\n"
"}")
        self.SenSize.setAlignment(QtCore.Qt.AlignCenter)
        self.SenSize.setObjectName("SenSize")
        self.gridLayout.addWidget(self.SenSize, 3, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.TraditionalDRRDisplay = QtWidgets.QLabel(self.gridLayoutWidget)
        self.TraditionalDRRDisplay.setMinimumSize(QtCore.QSize(512, 512))
        self.TraditionalDRRDisplay.setMaximumSize(QtCore.QSize(512, 512))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        self.TraditionalDRRDisplay.setFont(font)
        self.TraditionalDRRDisplay.setStyleSheet("QLabel {\n"
"    background-color: beige;\n"
"    border-style: outset;\n"
"    border-width: 1px;\n"
"    border-radius: 10px;\n"
"}")
        self.TraditionalDRRDisplay.setAlignment(QtCore.Qt.AlignCenter)
        self.TraditionalDRRDisplay.setObjectName("TraditionalDRRDisplay")
        self.gridLayout.addWidget(self.TraditionalDRRDisplay, 8, 3, 1, 3, QtCore.Qt.AlignVCenter)
        self.TraditionalDRR = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.TraditionalDRR.setMinimumSize(QtCore.QSize(156, 0))
        self.TraditionalDRR.setMaximumSize(QtCore.QSize(100, 16777215))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(-1)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.TraditionalDRR.setFont(font)
        self.TraditionalDRR.setStyleSheet("QComboBox {\n"
"    background-color: lightgrey;\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 10px;\n"
"    border-color: beige;\n"
"    font: bold 14px;\n"
"    min-width: 10em;\n"
"    padding: 6px;\n"
"}")
        self.TraditionalDRR.setObjectName("TraditionalDRR")
        self.TraditionalDRR.addItem("")
        self.TraditionalDRR.addItem("")
        self.gridLayout.addWidget(self.TraditionalDRR, 7, 4, 1, 1)
        self.Spectrum = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.Spectrum.setMinimumSize(QtCore.QSize(156, 0))
        self.Spectrum.setMaximumSize(QtCore.QSize(200, 16777215))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(-1)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.Spectrum.setFont(font)
        self.Spectrum.setStyleSheet("QComboBox {\n"
"    background-color: lightgrey;\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 10px;\n"
"    border-color: beige;\n"
"    font: bold 14px;\n"
"    min-width: 10em;\n"
"    padding: 6px;\n"
"}")
        self.Spectrum.setObjectName("Spectrum")
        self.Spectrum.addItem("")
        self.Spectrum.addItem("")
        self.Spectrum.addItem("")
        self.gridLayout.addWidget(self.Spectrum, 7, 1, 1, 1, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.PixSizeInput = QtWidgets.QTextEdit(self.gridLayoutWidget)
        self.PixSizeInput.setMinimumSize(QtCore.QSize(200, 40))
        self.PixSizeInput.setMaximumSize(QtCore.QSize(200, 40))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        self.PixSizeInput.setFont(font)
        self.PixSizeInput.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.PixSizeInput.setStyleSheet("QTextEdit{\n"
"    background-color: rgb(255, 240, 184);\n"
"    border-style: outset;\n"
"    border-width: 1px;\n"
"    border-radius: 10px;\n"
"}")
        self.PixSizeInput.setObjectName("PixSizeInput")
        self.gridLayout.addWidget(self.PixSizeInput, 2, 1, 1, 1, QtCore.Qt.AlignHCenter)
        self.SenSizeInput = QtWidgets.QTextEdit(self.gridLayoutWidget)
        self.SenSizeInput.setMinimumSize(QtCore.QSize(200, 40))
        self.SenSizeInput.setMaximumSize(QtCore.QSize(200, 40))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        self.SenSizeInput.setFont(font)
        self.SenSizeInput.setStyleSheet("QTextEdit{\n"
"    background-color: rgb(255, 240, 184);\n"
"    border-style: outset;\n"
"    border-width: 1px;\n"
"    border-radius: 10px;\n"
"}")
        self.SenSizeInput.setObjectName("SenSizeInput")
        self.gridLayout.addWidget(self.SenSizeInput, 3, 1, 1, 1, QtCore.Qt.AlignHCenter)
        self.DeepDRRDisplay = QtWidgets.QLabel(self.gridLayoutWidget)
        self.DeepDRRDisplay.setEnabled(True)
        self.DeepDRRDisplay.setMinimumSize(QtCore.QSize(512, 512))
        self.DeepDRRDisplay.setMaximumSize(QtCore.QSize(512, 512))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        self.DeepDRRDisplay.setFont(font)
        self.DeepDRRDisplay.setStyleSheet("QLabel {\n"
"    background-color: beige;\n"
"    border-style: outset;\n"
"    border-width: 1px;\n"
"    border-radius: 10px;\n"
"}")
        self.DeepDRRDisplay.setTextFormat(QtCore.Qt.AutoText)
        self.DeepDRRDisplay.setAlignment(QtCore.Qt.AlignCenter)
        self.DeepDRRDisplay.setObjectName("DeepDRRDisplay")
        self.gridLayout.addWidget(self.DeepDRRDisplay, 8, 0, 1, 3, QtCore.Qt.AlignHCenter)
        self.Src2DetInput = QtWidgets.QTextEdit(self.gridLayoutWidget)
        self.Src2DetInput.setMinimumSize(QtCore.QSize(200, 40))
        self.Src2DetInput.setMaximumSize(QtCore.QSize(200, 40))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        self.Src2DetInput.setFont(font)
        self.Src2DetInput.setStyleSheet("QTextEdit{\n"
"    background-color: rgb(255, 240, 184);\n"
"    border-style: outset;\n"
"    border-width: 1px;\n"
"    border-radius: 10px;\n"
"}")
        self.Src2DetInput.setObjectName("Src2DetInput")
        self.gridLayout.addWidget(self.Src2DetInput, 4, 1, 1, 1, QtCore.Qt.AlignHCenter)
        self.Todo = QtWidgets.QLabel(self.gridLayoutWidget)
        self.Todo.setMinimumSize(QtCore.QSize(130, 0))
        self.Todo.setMaximumSize(QtCore.QSize(130, 16777215))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        self.Todo.setFont(font)
        self.Todo.setStyleSheet("QLabel{\n"
"    background-color: rgb(255, 240, 184);\n"
"    border-style: outset;\n"
"    border-radius: 10px;\n"
"}")
        self.Todo.setAlignment(QtCore.Qt.AlignCenter)
        self.Todo.setObjectName("Todo")
        self.gridLayout.addWidget(self.Todo, 6, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.Src2IsoInput = QtWidgets.QTextEdit(self.gridLayoutWidget)
        self.Src2IsoInput.setMinimumSize(QtCore.QSize(200, 40))
        self.Src2IsoInput.setMaximumSize(QtCore.QSize(200, 40))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        self.Src2IsoInput.setFont(font)
        self.Src2IsoInput.setStyleSheet("QTextEdit{\n"
"    background-color: rgb(255, 240, 184);\n"
"    border-style: outset;\n"
"    border-width: 1px;\n"
"    border-radius: 10px;\n"
"}")
        self.Src2IsoInput.setObjectName("Src2IsoInput")
        self.gridLayout.addWidget(self.Src2IsoInput, 5, 1, 1, 1, QtCore.Qt.AlignHCenter)
        self.Slicer3D = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.Slicer3D.setMinimumSize(QtCore.QSize(156, 0))
        self.Slicer3D.setMaximumSize(QtCore.QSize(130, 16777215))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(-1)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.Slicer3D.setFont(font)
        self.Slicer3D.setStyleSheet("QPushButton {\n"
"    background-color: silver;\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 10px;\n"
"    border-color: beige;\n"
"    font: bold 14px;\n"
"    min-width: 10em;\n"
"    padding: 6px;\n"
"}")
        self.Slicer3D.setObjectName("Slicer3D")
        self.gridLayout.addWidget(self.Slicer3D, 1, 0, 1, 1)
        self.DRRShow = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.DRRShow.sizePolicy().hasHeightForWidth())
        self.DRRShow.setSizePolicy(sizePolicy)
        self.DRRShow.setMinimumSize(QtCore.QSize(156, 0))
        self.DRRShow.setMaximumSize(QtCore.QSize(160, 16777215))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(-1)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.DRRShow.setFont(font)
        self.DRRShow.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.DRRShow.setStyleSheet("QPushButton {\n"
"    background-color: silver;\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 10px;\n"
"    border-color: beige;\n"
"    font: bold 14px;\n"
"    min-width: 10em;\n"
"    padding: 6px;\n"
"}")
        self.DRRShow.setObjectName("DRRShow")
        self.gridLayout.addWidget(self.DRRShow, 7, 0, 1, 1)
        self.DRRShow_2 = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.DRRShow_2.sizePolicy().hasHeightForWidth())
        self.DRRShow_2.setSizePolicy(sizePolicy)
        self.DRRShow_2.setMinimumSize(QtCore.QSize(156, 0))
        self.DRRShow_2.setMaximumSize(QtCore.QSize(200, 16777215))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(-1)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.DRRShow_2.setFont(font)
        self.DRRShow_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.DRRShow_2.setStyleSheet("QPushButton {\n"
"    background-color: silver;\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 10px;\n"
"    border-color: beige;\n"
"    font: bold 14px;\n"
"    min-width: 10em;\n"
"    padding: 6px;\n"
"}")
        self.DRRShow_2.setObjectName("DRRShow_2")
        self.gridLayout.addWidget(self.DRRShow_2, 7, 3, 1, 1)
        self.CTInfoLabel = QtWidgets.QLabel(self.gridLayoutWidget)
        self.CTInfoLabel.setMinimumSize(QtCore.QSize(130, 40))
        self.CTInfoLabel.setMaximumSize(QtCore.QSize(130, 40))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        self.CTInfoLabel.setFont(font)
        self.CTInfoLabel.setStyleSheet("QLabel{\n"
"    background-color: rgb(255, 240, 184);\n"
"    border-style: outset;\n"
"    border-radius: 10px;\n"
"}")
        self.CTInfoLabel.setObjectName("CTInfoLabel")
        self.gridLayout.addWidget(self.CTInfoLabel, 3, 2, 1, 1)
        self.CTInfo = QtWidgets.QTextBrowser(self.gridLayoutWidget)
        self.CTInfo.setMinimumSize(QtCore.QSize(0, 40))
        self.CTInfo.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        self.CTInfo.setFont(font)
        self.CTInfo.setStyleSheet("QTextEdit{\n"
"    background-color: rgb(255, 240, 184);\n"
"    border-style: outset;\n"
"    border-width: 1px;\n"
"    border-radius: 10px;\n"
"}")
        self.CTInfo.setObjectName("CTInfo")
        self.gridLayout.addWidget(self.CTInfo, 3, 3, 1, 3)
        self.ErrInfoLabel = QtWidgets.QLabel(self.gridLayoutWidget)
        self.ErrInfoLabel.setMinimumSize(QtCore.QSize(130, 40))
        self.ErrInfoLabel.setMaximumSize(QtCore.QSize(130, 40))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        self.ErrInfoLabel.setFont(font)
        self.ErrInfoLabel.setStyleSheet("QLabel{\n"
"    background-color: rgb(255, 240, 184);\n"
"    border-style: outset;\n"
"    border-radius: 10px;\n"
"}")
        self.ErrInfoLabel.setObjectName("ErrInfoLabel")
        self.gridLayout.addWidget(self.ErrInfoLabel, 5, 2, 1, 1)
        self.ErrInfo = QtWidgets.QTextBrowser(self.gridLayoutWidget)
        self.ErrInfo.setMinimumSize(QtCore.QSize(0, 0))
        self.ErrInfo.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        self.ErrInfo.setFont(font)
        self.ErrInfo.setStyleSheet("QTextEdit{\n"
"    background-color: rgb(255, 240, 184);\n"
"    border-style: outset;\n"
"    border-width: 1px;\n"
"    border-radius: 10px;\n"
"}")
        self.ErrInfo.setObjectName("ErrInfo")
        self.gridLayout.addWidget(self.ErrInfo, 4, 3, 3, 3)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.Src2Det.setText(_translate("Form", "src2det"))
        self.PixSize.setText(_translate("Form", "Pixel_Size"))
        self.Src2Iso.setText(_translate("Form", "src2iso"))
        self.Input.setText(_translate("Form", "请选择输入文件"))
        self.SenSize.setText(_translate("Form", "Sensor_Size"))
        self.TraditionalDRRDisplay.setText(_translate("Form", "TraditionalDRR"))
        self.TraditionalDRR.setItemText(0, _translate("Form", "光线追踪"))
        self.TraditionalDRR.setItemText(1, _translate("Form", "Sidon"))
        self.Spectrum.setItemText(0, _translate("Form", "60KV_35AL"))
        self.Spectrum.setItemText(1, _translate("Form", "90KV_40AL"))
        self.Spectrum.setItemText(2, _translate("Form", "120KV_45KL"))
        self.DeepDRRDisplay.setText(_translate("Form", "DeepDRR"))
        self.Todo.setText(_translate("Form", "todo"))
        self.Slicer3D.setText(_translate("Form", "3DSlicer"))
        self.DRRShow.setText(_translate("Form", "DeepDRR"))
        self.DRRShow_2.setText(_translate("Form", "TradiDRR"))
        self.CTInfoLabel.setText(_translate("Form", " CT Size Info:"))
        self.ErrInfoLabel.setText(_translate("Form", "Error Info"))

