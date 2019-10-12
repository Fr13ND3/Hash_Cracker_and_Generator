# Coded By Zed-Team
# Channel telegram : @Arch_TM

from os import system
import datetime
try:
    from PyQt5 import QtCore, QtGui, QtWidgets
except ModuleNotFoundError:
    print("Oh! This Error Module Not Found ! Please Enter pip install PyQt5")
    system('pip install pyqt5')
import requests
try :
    from bs4 import BeautifulSoup
except:
    print("Oh! This Error Module Not Found ! Please Enter pip install bs4")
    system('pip install bs4')
try:
    import hashlib
except:
    print("Oh! This Error Module Not Found ! Please Enter pip install hashlib")
    system('pip install hashlib')

class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        mainWindow.setObjectName("mainWindow")
        mainWindow.resize(536, 411)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("D:/x2ico.1.2.3.9/x2ico/Icons/2394490_0.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        mainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(mainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tab_hash_cracker = QtWidgets.QTabWidget(self.centralwidget)
        self.tab_hash_cracker.setGeometry(QtCore.QRect(10, 10, 521, 391))
        self.tab_hash_cracker.setObjectName("tab_hash_cracker")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.groupBox = QtWidgets.QGroupBox(self.tab)
        self.groupBox.setGeometry(QtCore.QRect(20, 130, 151, 211))
        self.groupBox.setObjectName("groupBox")
        self.c_md5 = QtWidgets.QCheckBox(self.groupBox)
        self.c_md5.setGeometry(QtCore.QRect(20, 40, 81, 20))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.c_md5.setFont(font)
        self.c_md5.setChecked(True)
        self.c_md5.setObjectName("c_md5")
        self.checkBox_5 = QtWidgets.QCheckBox(self.groupBox)
        self.checkBox_5.setGeometry(QtCore.QRect(20, 160, 81, 20))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.checkBox_5.setFont(font)
        self.checkBox_5.setObjectName("checkBox_5")
        self.checkBox_3 = QtWidgets.QCheckBox(self.groupBox)
        self.checkBox_3.setGeometry(QtCore.QRect(20, 100, 81, 20))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.checkBox_3.setFont(font)
        self.checkBox_3.setObjectName("checkBox_3")
        self.checkBox_2 = QtWidgets.QCheckBox(self.groupBox)
        self.checkBox_2.setGeometry(QtCore.QRect(20, 70, 81, 20))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.checkBox_2.setFont(font)
        self.checkBox_2.setObjectName("checkBox_2")
        self.checkBox_4 = QtWidgets.QCheckBox(self.groupBox)
        self.checkBox_4.setGeometry(QtCore.QRect(20, 130, 81, 20))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.checkBox_4.setFont(font)
        self.checkBox_4.setObjectName("checkBox_4")
        self.lineEdit = QtWidgets.QLineEdit(self.tab)
        self.lineEdit.setGeometry(QtCore.QRect(20, 20, 481, 21))
        self.lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit.setObjectName("lineEdit")
        self.textEdit = QtWidgets.QTextEdit(self.tab)
        self.textEdit.setGeometry(QtCore.QRect(200, 60, 301, 281))
        self.textEdit.setObjectName("textEdit")
        self.start_crack_hash = QtWidgets.QPushButton(self.tab)
        self.start_crack_hash.setGeometry(QtCore.QRect(22, 70, 161, 28))
        self.start_crack_hash.setObjectName("start_crack_hash")
        self.tab_hash_cracker.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_2.setGeometry(QtCore.QRect(10, 20, 481, 22))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.conver_pass_to_hash = QtWidgets.QPushButton(self.tab_2)
        self.conver_pass_to_hash.setGeometry(QtCore.QRect(10, 60, 151, 28))
        self.conver_pass_to_hash.setObjectName("conver_pass_to_hash")
        self.groupBox_2 = QtWidgets.QGroupBox(self.tab_2)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 110, 151, 201))
        self.groupBox_2.setObjectName("groupBox_2")
        self.checkBox = QtWidgets.QCheckBox(self.groupBox_2)
        self.checkBox.setGeometry(QtCore.QRect(20, 30, 81, 20))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.checkBox.setFont(font)
        self.checkBox.setObjectName("checkBox")
        self.checkBox_6 = QtWidgets.QCheckBox(self.groupBox_2)
        self.checkBox_6.setGeometry(QtCore.QRect(20, 60, 81, 20))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.checkBox_6.setFont(font)
        self.checkBox_6.setObjectName("checkBox_6")
        self.checkBox_7 = QtWidgets.QCheckBox(self.groupBox_2)
        self.checkBox_7.setGeometry(QtCore.QRect(20, 90, 81, 20))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.checkBox_7.setFont(font)
        self.checkBox_7.setObjectName("checkBox_7")
        self.checkBox_8 = QtWidgets.QCheckBox(self.groupBox_2)
        self.checkBox_8.setGeometry(QtCore.QRect(20, 120, 81, 20))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.checkBox_8.setFont(font)
        self.checkBox_8.setObjectName("checkBox_8")
        self.checkBox_9 = QtWidgets.QCheckBox(self.groupBox_2)
        self.checkBox_9.setGeometry(QtCore.QRect(20, 150, 81, 20))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.checkBox_9.setFont(font)
        self.checkBox_9.setObjectName("checkBox_9")
        self.textEdit_2 = QtWidgets.QTextEdit(self.tab_2)
        self.textEdit_2.setGeometry(QtCore.QRect(190, 60, 301, 251))
        self.textEdit_2.setObjectName("textEdit_2")
        self.tab_hash_cracker.addTab(self.tab_2, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.tab_4)
        self.lineEdit_3.setGeometry(QtCore.QRect(129, 30, 241, 22))
        self.lineEdit_3.setMinimumSize(QtCore.QSize(200, 0))
        self.lineEdit_3.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_6 = QtWidgets.QLabel(self.tab_4)
        self.label_6.setGeometry(QtCore.QRect(20, 33, 103, 16))
        self.label_6.setObjectName("label_6")
        self.textEdit_3 = QtWidgets.QTextEdit(self.tab_4)
        self.textEdit_3.setGeometry(QtCore.QRect(20, 67, 471, 281))
        self.textEdit_3.setObjectName("textEdit_3")
        self.unhash_combo = QtWidgets.QPushButton(self.tab_4)
        self.unhash_combo.setGeometry(QtCore.QRect(380, 27, 121, 28))
        self.unhash_combo.setObjectName("unhash_combo")
        self.tab_hash_cracker.addTab(self.tab_4, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.label = QtWidgets.QLabel(self.tab_3)
        self.label.setGeometry(QtCore.QRect(150, 40, 251, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.tab_3)
        self.label_2.setGeometry(QtCore.QRect(110, 100, 501, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.tab_3)
        self.label_3.setGeometry(QtCore.QRect(40, 250, 501, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.tab_3)
        self.label_4.setGeometry(QtCore.QRect(70, 200, 401, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.tab_3)
        self.label_5.setGeometry(QtCore.QRect(90, 150, 401, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.tab_hash_cracker.addTab(self.tab_3, "")
        mainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(mainWindow)
        self.statusbar.setObjectName("statusbar")
        mainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(mainWindow)
        self.tab_hash_cracker.setCurrentIndex(2)
        self.start_crack_hash.clicked.connect(self.tab_crack_hash)
        self.conver_pass_to_hash.clicked.connect(self.tab_generator_hash)
        self.unhash_combo.clicked.connect(self.tab_unhash_combo)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)
    def tab_generator_hash(self):
        u_hash = self.lineEdit_2.text()
        if u_hash == "":self.textEdit_2.append("Please Enter Your Hash")
        u_hash = u_hash.split(',')
        if self.checkBox.isChecked():
            for i in u_hash:
                self.textEdit_2.append(f'Your Password : {i}')
                i = hashlib.md5(i.encode()).hexdigest()
                self.textEdit_2.append(f'Converted => {i}')
                self.textEdit_2.append('Status : Finished')
                self.textEdit_2.append('-------------------')
        elif self.checkBox_6.isChecked():
            for i in u_hash:
                self.textEdit_2.append(f'Your Password : {i}')
                i = hashlib.sha1(i.encode()).hexdigest()
                self.textEdit_2.append(f'Converted => {i}')
                self.textEdit_2.append('Status : Finished')
                self.textEdit_2.append('-------------------')
        elif self.checkBox_7.isChecked():
            for i in u_hash:
                self.textEdit_2.append(f'Your Password : {i}')
                i = hashlib.sha256(i.encode()).hexdigest()
                self.textEdit_2.append(f'Converted => {i}')
                self.textEdit_2.append('Status : Finished')
                self.textEdit_2.append('-------------------')
        elif self.checkBox_8.isChecked():
            for i in u_hash:
                self.textEdit_2.append(f'Your Password : {i}')
                i = hashlib.sha384(i.encode()).hexdigest()
                self.textEdit_2.append(f'Converted => {i}')
                self.textEdit_2.append('Status : Finished')
                self.textEdit_2.append('-------------------')
        elif self.checkBox_9.isChecked():
            for i in u_hash:
                self.textEdit_2.append(f'Your Password : {i}')
                i = hashlib.sha512(i.encode()).hexdigest()
                self.textEdit_2.append(f'Converted => {i}')
                self.textEdit_2.append('Status : Finished')
                self.textEdit_2.append('-------------------')
    def tab_crack_hash(self):
        u_hash = str(self.lineEdit.text())
        req = requests.get(f'https://hashtoolkit.com/reverse-hash/?hash={u_hash}')
        soup = BeautifulSoup(req.text,'html.parser')
        res = str(soup.find_all('span'))
        value = res.split('"')
        time = datetime.datetime.now().strftime('%H:%M:%S')
        if self.c_md5.isChecked():
            req = requests.get(f'https://hashtoolkit.com/reverse-md5-hash/{u_hash}')
            if req.status_code == 200:
                soup = BeautifulSoup(req.text,'html.parser')
                
                res = str(soup.find_all('span'))
                value = res.split('"')
                try:
                    hash_cracked = value[39]
                    hash_cracked = hash_cracked[21:]
                    if hash_cracked == "earch text-right":
                        self.textEdit.append("I'm Not Crack Your Hash")
                        self.textEdit.append("------------")
                    else:
                        self.textEdit.append(f"Hash : {self.lineEdit.text()}")
                        self.textEdit.append(f"Your Hash Cracked => {hash_cracked}")
                        self.textEdit.append(f"Time : {time}")
                        self.textEdit.append(f"Type Hash : {value[23]}")
                        self.textEdit.append("------------")
                except:
                    self.textEdit.append("I'm Not Crack Your Hash")
                    self.textEdit.append("------------")
            else:
                self.textEdit.append("oops ! Please Check Your Internet")      
        elif self.checkBox_2.isChecked():
            req = requests.get(f'https://hashtoolkit.com/reverse-sha1-hash/{u_hash}')
            if req.status_code == 200:
                soup = BeautifulSoup(req.text,'html.parser')
                
                res = str(soup.find_all('span'))
                value = res.split('"')
                try:
                    hash_cracked = value[39]
                    hash_cracked = hash_cracked[21:]
                    if hash_cracked == "earch text-right":
                        self.textEdit.append("I'm Not Crack Your Hash")
                        self.textEdit.append("------------")
                    else:
                        self.textEdit.append(f"Hash : {self.lineEdit.text()}")
                        self.textEdit.append(f"Your Hash Cracked => {hash_cracked}")
                        self.textEdit.append(f"Time : {time}")
                        self.textEdit.append(f"Type Hash : SHA1")
                        self.textEdit.append("------------")
                except:
                    self.textEdit.append("I'm Not Crack Your Hash")
                    self.textEdit.append("------------")
            else:
                self.textEdit.append("oops ! Please Check Your Internet")      
        elif self.checkBox_3.isChecked():
            req = requests.get(f'https://hashtoolkit.com/reverse-sha256-hash/{u_hash}')
            if req.status_code == 200:
                soup = BeautifulSoup(req.text,'html.parser')
                
                res = str(soup.find_all('span'))
                value = res.split('"')
                try:
                    hash_cracked = value[39]
                    hash_cracked = hash_cracked[21:]
                    if hash_cracked == "earch text-right":
                        self.textEdit.append("I'm Not Crack Your Hash")
                        self.textEdit.append("------------")
                    else:
                        self.textEdit.append(f"Hash : {self.lineEdit.text()}")
                        self.textEdit.append(f"Your Hash Cracked => {hash_cracked}")
                        self.textEdit.append(f"Time : {time}")
                        self.textEdit.append(f"Type Hash : SHA256")
                        self.textEdit.append("------------")
                except:
                    self.textEdit.append("I'm Not Crack Your Hash")
                    self.textEdit.append("------------")
            else:
                self.textEdit.append("oops ! Please Check Your Internet")      
        elif self.checkBox_4.isChecked():
            req = requests.get(f'https://hashtoolkit.com/reverse-sha384-hash/{u_hash}')
            if req.status_code == 200:
                soup = BeautifulSoup(req.text,'html.parser')
                
                res = str(soup.find_all('span'))
                value = res.split('"')
                try:
                    hash_cracked = value[39]
                    hash_cracked = hash_cracked[21:]
                    if hash_cracked == "earch text-right":
                        self.textEdit.append("I'm Not Crack Your Hash")
                        self.textEdit.append("------------")
                    else:
                        self.textEdit.append(f"Hash : {self.lineEdit.text()}")
                        self.textEdit.append(f"Your Hash Cracked => {hash_cracked}")
                        self.textEdit.append(f"Time : {time}")
                        self.textEdit.append(f"Type Hash : SHA384")
                        self.textEdit.append("------------")
                except:
                    self.textEdit.append("I'm Not Crack Your Hash")
                    self.textEdit.append("------------")
            else:
                self.textEdit.append("oops ! Please Check Your Internet")              
        elif self.checkBox_5.isChecked():
            req = requests.get(f'https://hashtoolkit.com/reverse-sha512-hash/{u_hash}')
            if req.status_code == 200:
                soup = BeautifulSoup(req.text,'html.parser')
                
                res = str(soup.find_all('span'))
                value = res.split('"')
                try:
                    hash_cracked = value[39]
                    hash_cracked = hash_cracked[21:]
                    if hash_cracked == "earch text-right":
                        self.textEdit.append("I'm Not Crack Your Hash")
                        self.textEdit.append("------------")
                    else:
                        self.textEdit.append(f"Hash : {self.lineEdit.text()}")
                        self.textEdit.append(f"Your Hash Cracked => {hash_cracked}")
                        self.textEdit.append(f"Time : {time}")
                        self.textEdit.append(f"Type Hash : SHA512")
                        self.textEdit.append("------------")
                except:
                    self.textEdit.append("I'm Not Crack Your Hash")
                    self.textEdit.append("------------")
            else:
                self.textEdit.append("oops ! Please Check Your Internet")      
        else:
            self.textEdit.append("Please select one of the options")  
    def tab_unhash_combo(self):

        try:
            with open('newcombo.txt','x'):
                pass
        except Exception:
            pass
        self.textEdit_3.append("*** Unhasher Combo Coded By Zed-Team ***")
        self.textEdit_3.append("  *** Channel Telegram : @Arch_TM ***")


        address_combo = self.lineEdit_3.text()
        self.textEdit_3.append("Good! Please Wait...")
        self.textEdit_3.append('-----------------------------------')
        try:
            with open(address_combo) as rf:
                s = ""
                for i in rf.readlines():
                    s += i
                mlist = s.split('\n')
                for x in mlist:
                    list0 = "".join(x)
                    line_combo = list0.split(':')
                    Hash = line_combo[1]
                    try:
                        req = requests.get(f'https://hashtoolkit.com/reverse-hash/?hash={Hash}')
                    except Exception as e:
                        print(e)
                    if req.status_code == 200:
                        soup = BeautifulSoup(req.text,'html.parser')
                        try:
                            cracked = str(soup.find('span',attrs={'title':'decrypted md5 hash'}))
                            cracked = cracked[33:]
                            o = cracked.split('</span>')
                            cracked = "".join(o[0])
                            
                            
                            with open('newcombo.txt','a') as af:
                                if cracked == "":
                                    pass
                                else:
                                    app.processEvents()
                                    af.write(f'{line_combo[0]}:{cracked}\n')
                                    self.textEdit_3.append(f"{line_combo[0]}:{cracked}")
                        except Exception as er:
                            print(er)
                            
                    else:
                        print("Please Check Ineternet")
        except Exception as error:
            print(error)

        print("Done! Enjoy ...")

    def retranslateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("mainWindow", "Hash Cracker And Generator"))
        self.groupBox.setTitle(_translate("mainWindow", "Type Hash"))
        self.c_md5.setText(_translate("mainWindow", "MD5"))
        self.checkBox_5.setText(_translate("mainWindow", "SHA512"))
        self.checkBox_3.setText(_translate("mainWindow", "SHA256"))
        self.checkBox_2.setText(_translate("mainWindow", "SHA1"))
        self.checkBox_4.setText(_translate("mainWindow", "SHA356"))
        self.lineEdit.setText(_translate("mainWindow", "Enter Your Hash"))
        self.textEdit.setHtml(_translate("mainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">*************** Result ***************</p></body></html>"))
        self.start_crack_hash.setText(_translate("mainWindow", "Start Crack"))
        self.tab_hash_cracker.setTabText(self.tab_hash_cracker.indexOf(self.tab), _translate("mainWindow", "Hash Cracker"))
        self.lineEdit_2.setText(_translate("mainWindow", "Please Enter Password with (,) example : 123,abc,abc123"))
        self.conver_pass_to_hash.setText(_translate("mainWindow", "Convert"))
        self.groupBox_2.setTitle(_translate("mainWindow", "GroupBox"))
        self.checkBox.setText(_translate("mainWindow", "MD5"))
        self.checkBox_6.setText(_translate("mainWindow", "SHA1"))
        self.checkBox_7.setText(_translate("mainWindow", "SHA256"))
        self.checkBox_8.setText(_translate("mainWindow", "SHA356"))
        self.checkBox_9.setText(_translate("mainWindow", "SHA512"))
        self.textEdit_2.setHtml(_translate("mainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">*************** Result ***************</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.tab_hash_cracker.setTabText(self.tab_hash_cracker.indexOf(self.tab_2), _translate("mainWindow", "Hash Generator"))
        self.lineEdit_3.setText(_translate("mainWindow", "combo.txt"))
        self.label_6.setText(_translate("mainWindow", "Address Combo : "))
        self.unhash_combo.setText(_translate("mainWindow", "Start Crack"))
        self.tab_hash_cracker.setTabText(self.tab_hash_cracker.indexOf(self.tab_4), _translate("mainWindow", "unhasher combo"))
        self.label.setText(_translate("mainWindow", "PROGRAMER : Zed-Team"))
        self.label_2.setText(_translate("mainWindow", "GitHub :  https://github.com/zed-team "))
        self.label_3.setText(_translate("mainWindow", "Instagram :  https://www.instagram.com/insta_cra3ked/"))
        self.label_4.setText(_translate("mainWindow", "Telegram Id Programer : https://t.me/Cra3ked"))
        self.label_5.setText(_translate("mainWindow", "Telegram Channel : https://t.me/Arch_TM"))
        self.tab_hash_cracker.setTabText(self.tab_hash_cracker.indexOf(self.tab_3), _translate("mainWindow", "About Programer"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = QtWidgets.QMainWindow()
    ui = Ui_mainWindow()
    ui.setupUi(mainWindow)
    mainWindow.show()
    app.processEvents()
    sys.exit(app.exec_())
